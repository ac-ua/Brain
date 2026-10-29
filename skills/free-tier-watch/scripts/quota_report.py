#!/usr/bin/env python3
"""Weekly free-tier check: how close each service is to its free limit, as a Markdown report.

Reads services.json (next to this folder). GitHub through `gh api` (repo-scoped endpoints only), Cloudflare through
its API when WATCH_CLOUDFLARE_API_TOKEN (read-only) is set, Supabase through the `usage-*` artifact that each app's
nightly backup writes. Anything it cannot reach is listed as « not measured », never guessed. Standard library only.

Usage:  python3 quota_report.py [--json out.json] > report.md
"""
import argparse, io, json, math, os, re, subprocess, sys, urllib.request, zipfile
from datetime import datetime, timedelta, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
CONF = json.load(open(os.path.join(HERE, "..", "services.json")))
LIM, LEV = CONF["limits"], CONF["levels"]
NOW = datetime.now(timezone.utc)
MONTH0 = NOW.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
DAYS_IN_MONTH = ((MONTH0 + timedelta(days=32)).replace(day=1) - MONTH0).days
SKIP = ("[cf-pages-skip]", "[ci skip]", "[skip ci]")
MERGE = re.compile(r"\(#\d+\)$")   # squash-merge title; merge commits start with "Merge pull request"

rows, gaps = [], []          # rows: (service, what, used, limit, unit, note); gaps: what could not be measured


def gh(path, raw=False):
    r = subprocess.run(["gh", "api", "-H", "Accept: application/vnd.github+json", path], capture_output=True)
    if r.returncode:
        raise RuntimeError(r.stderr.decode(errors="replace").strip().splitlines()[-1][:160])
    return r.stdout if raw else json.loads(r.stdout or b"null")


def gh_pages(path, key):
    out, page = [], 1
    while True:
        sep = "&" if "?" in path else "?"
        d = gh(f"{path}{sep}per_page=100&page={page}")
        items = d[key] if key else d
        out += items
        if len(items) < 100 or page >= 10:
            return out
        page += 1


def add(service, what, used, limit, unit, note=""):
    rows.append((service, what, used, limit, unit, note))


def github():
    owner = CONF["github"]["owner"]
    minutes, artifacts_bytes, builds = 0, 0, 0
    since = MONTH0.strftime("%Y-%m-%dT%H:%M:%SZ")
    for r in CONF["github"]["repos"]:
        name, app = r["repo"], r["app"]
        try:
            meta = gh(f"repos/{owner}/{name}")
        except RuntimeError as e:
            gaps.append(f"GitHub `{owner}/{name}` ({app}): not reachable from this session ({e})")
            continue
        add("GitHub", f"{name}: repository size", meta["size"] * 1024, LIM["repo_soft_bytes"], "bytes",
            "public" if not meta["private"] else "private")
        try:
            runs = gh_pages(f"repos/{owner}/{name}/actions/runs?created=>={MONTH0:%Y-%m-%d}", "workflow_runs")
            m = 0
            if meta["private"]:
                for run in runs:
                    if run.get("status") != "completed":
                        continue
                    t = gh(f"repos/{owner}/{name}/actions/runs/{run['id']}/timing")
                    for os_name, b in (t.get("billable") or {}).items():
                        for j in b.get("job_runs", []):
                            m += math.ceil(j.get("duration_ms", 0) / 60000)
            minutes += m
            if runs:
                add("GitHub", f"{name}: Actions this month", m, None, "min",
                    f"{len(runs)} runs" + ("" if meta["private"] else ", public repo: free"))
            blocked(owner, name, app, runs)
            arts = gh_pages(f"repos/{owner}/{name}/actions/artifacts", "artifacts")
            artifacts_bytes += sum(a["size_in_bytes"] for a in arts if not a.get("expired"))
        except RuntimeError as e:
            gaps.append(f"GitHub Actions `{name}`: {e}")
            arts = []
        if r.get("pages"):
            try:
                cs = gh_pages(f"repos/{owner}/{name}/commits?sha={meta['default_branch']}&since={since}", None)
                titles = [c["commit"]["message"].split("\n")[0] for c in cs]
                n = sum(1 for t in titles if (MERGE.search(t) or t.startswith("Merge pull request"))
                        and not any(s in t.lower() for s in SKIP))
                builds += n
            except RuntimeError as e:
                gaps.append(f"Pages builds `{name}`: {e}")
        if r.get("usage_artifact"):
            supabase_usage(owner, name, app, r, arts)
    add("GitHub", "Actions minutes, all private repos (month)", minutes, LIM["actions_minutes_month"], "min",
        project(minutes, LIM["actions_minutes_month"]))
    add("GitHub", "Actions artifact storage", artifacts_bytes, LIM["actions_artifact_bytes"], "bytes")
    add("Cloudflare", "Pages production builds this month (estimate: merges to main without the marker)",
        builds, LIM["pages_builds_month"], "builds", project(builds, LIM["pages_builds_month"]))


def blocked(owner, name, app, runs):
    """GitHub refuses to start jobs when the minutes are used up or billing fails: runs end in seconds, no runner."""
    done = [r for r in runs if r.get("status") == "completed"]
    if not done:
        return
    last = max(done, key=lambda r: r["created_at"])
    secs = (datetime.fromisoformat(last["updated_at"].replace("Z", "+00:00"))
            - datetime.fromisoformat(last["run_started_at"].replace("Z", "+00:00"))).total_seconds()
    if last.get("conclusion") != "failure" or secs > 20:
        return
    jobs = gh(f"repos/{owner}/{name}/actions/runs/{last['id']}/jobs").get("jobs", [])
    msg = ""
    for j in jobs[:1]:
        for an in gh(f"repos/{owner}/{name}/check-runs/{j['id']}/annotations"):
            if "not started" in an.get("message", ""):
                msg = an["message"]
    if msg:
        failed = sum(1 for r in done if r.get("conclusion") == "failure")
        add("GitHub", f"{name}: Actions BLOCKED, jobs are refused ({failed} failed runs this month, last "
            f"{last['created_at'][:10]} « {last['name']} »)", 1, 1, "blocked", msg[:140])


def supabase_usage(owner, name, app, r, arts):
    usage = sorted((a for a in arts if a["name"].startswith(r["usage_artifact"]) and not a.get("expired")),
                   key=lambda a: a["created_at"], reverse=True)
    if usage:
        try:
            z = zipfile.ZipFile(io.BytesIO(gh(f"repos/{owner}/{name}/actions/artifacts/{usage[0]['id']}/zip", raw=True)))
            u = json.loads(z.read("usage.json"))
            add("Supabase", f"{app}: database", u["db_bytes"], LIM["supabase_db_bytes"], "bytes", f"measured {u['at'][:10]}")
            add("Supabase", f"{app}: file storage", u["storage_bytes"], LIM["supabase_storage_bytes"], "bytes",
                f"{u['storage_objects']} files")
            return
        except Exception as e:  # noqa: BLE001 — any failure becomes a gap, never a guess
            gaps.append(f"Supabase {app}: usage artifact unreadable ({e})")
    backups = sorted((a for a in arts if r.get("backup_artifact") and a["name"].startswith(r["backup_artifact"])
                      and not a.get("expired")), key=lambda a: a["created_at"], reverse=True)
    if backups:
        add("Supabase", f"{app}: last backup artifact (compressed, lower bound of the database)",
            backups[0]["size_in_bytes"], LIM["supabase_db_bytes"], "bytes", backups[0]["created_at"][:10])
    else:
        gaps.append(f"Supabase {app}: no usage artifact yet (its nightly backup must write usage.json, "
                    f"see skills/free-tier-watch)")
    gaps.append(f"Supabase {app}: egress (5 GB) and monthly active users are only in the dashboard (Organization › Usage)")


def cf(path, body=None):
    req = urllib.request.Request("https://api.cloudflare.com/client/v4/" + path,
                                 data=json.dumps(body).encode() if body else None,
                                 headers={"Authorization": "Bearer " + os.environ["WATCH_CLOUDFLARE_API_TOKEN"],
                                          "Content-Type": "application/json"})
    d = json.load(urllib.request.urlopen(req, timeout=30))
    if d.get("errors"):
        raise RuntimeError(str(d["errors"])[:160])
    return d


def cloudflare():
    if not os.environ.get("WATCH_CLOUDFLARE_API_TOKEN"):
        gaps.append("Cloudflare: WATCH_CLOUDFLARE_API_TOKEN is not set in this environment (read-only token, "
                    "see skills/free-tier-watch › Setup): D1, Workers, R2 and KV not measured")
        return
    try:
        acc = os.environ.get("WATCH_CLOUDFLARE_ACCOUNT_ID") or cf("accounts")["result"][0]["id"]
    except Exception as e:  # noqa: BLE001
        gaps.append(f"Cloudflare: account not readable ({e})")
        return
    step(lambda: d1(acc), "D1")
    step(lambda: workers(acc), "Workers requests")
    step(lambda: r2(acc), "R2")
    step(lambda: pages(acc), "Pages deployments")


def step(fn, label):
    try:
        fn()
    except Exception as e:  # noqa: BLE001
        gaps.append(f"Cloudflare {label}: {e}")


def d1(acc):
    dbs = cf(f"accounts/{acc}/d1/database?per_page=100")["result"]
    total = 0
    for db in dbs:
        size = cf(f"accounts/{acc}/d1/database/{db['uuid']}")["result"].get("file_size", 0)
        total += size
        add("Cloudflare", f"D1 `{db['name']}`", size, None, "bytes")
    add("Cloudflare", "D1 storage, all databases", total, LIM["d1_bytes_total"], "bytes")


def graphql(q, v):
    d = cf("graphql", {"query": q, "variables": v})
    return d["data"]["viewer"]["accounts"][0]


def workers(acc):
    d0 = (NOW - timedelta(days=7)).strftime("%Y-%m-%d")
    a = graphql("query($a:String!,$d:Date!){viewer{accounts(filter:{accountTag:$a}){workersInvocationsAdaptive("
                "limit:10000,filter:{date_geq:$d}){sum{requests} dimensions{date scriptName}}}}}", {"a": acc, "d": d0})
    per_day = {}
    for g in a["workersInvocationsAdaptive"]:
        per_day[g["dimensions"]["date"]] = per_day.get(g["dimensions"]["date"], 0) + g["sum"]["requests"]
    peak = max(per_day.values()) if per_day else 0
    add("Cloudflare", "Workers + Pages Functions requests, busiest day of the last 7", peak,
        LIM["workers_requests_day"], "requests", max(per_day, key=per_day.get) if per_day else "no traffic")


def r2(acc):
    t0 = (NOW - timedelta(days=2)).strftime("%Y-%m-%dT%H:%M:%SZ")
    a = graphql("query($a:String!,$t:Time!){viewer{accounts(filter:{accountTag:$a}){r2StorageAdaptiveGroups("
                "limit:100,filter:{datetime_geq:$t}){max{payloadSize metadataSize objectCount} dimensions{bucketName}}}}}",
                {"a": acc, "t": t0})
    sizes = {}
    for g in a["r2StorageAdaptiveGroups"]:
        b = g["dimensions"]["bucketName"]
        sizes[b] = max(sizes.get(b, 0), g["max"]["payloadSize"] + g["max"]["metadataSize"])
    add("Cloudflare", "R2 storage, all buckets", sum(sizes.values()), LIM["r2_bytes"], "bytes",
        ", ".join(sorted(sizes)) or "no bucket with data")


def pages(acc):
    for p in cf(f"accounts/{acc}/pages/projects")["result"]:
        deps = cf(f"accounts/{acc}/pages/projects/{p['name']}/deployments?per_page=25")["result"]
        month = [x for x in deps if x["created_on"] >= MONTH0.isoformat()[:10]]
        add("Cloudflare", f"Pages `{p['name']}` deployments this month (last 25 read)", len(month), None, "builds",
            "previews on" if any(x.get("environment") == "preview" for x in month) else "")


def project(used, limit):
    day = (NOW - MONTH0).total_seconds() / 86400
    if day < 1 or not used:
        return ""
    est = used / day * DAYS_IN_MONTH
    return f"month-end pace ≈ {est:,.0f}" + (" ⚠ over the limit" if est > limit else "")


def human(v, unit):
    if unit == "bytes":
        for u in ("B", "KB", "MB", "GB"):
            if v < 1000 or u == "GB":
                return f"{v:,.0f} {u}" if u == "B" else f"{v:,.1f} {u}"
            v /= 1000
    if unit == "blocked":
        return "yes"
    return f"{v:,} {unit}"


def level(used, limit):
    if not limit:
        return ""
    r = used / limit
    return "🔴 alert" if r >= LEV["alert"] else "🟠 watch" if r >= LEV["watch"] else "🟢 ok"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json")
    a = ap.parse_args()
    github()
    cloudflare()
    out = [f"# Free-tier check · {NOW:%Y-%m-%d}", "",
           f"Month {MONTH0:%B %Y}, day {NOW.day} of {DAYS_IN_MONTH}. Levels: watch ≥ {LEV['watch']:.0%}, alert ≥ {LEV['alert']:.0%}.", "",
           "| Level | Service | What | Used | Free limit | % | Note |", "|---|---|---|---|---|---|---|"]
    order = {"🔴 alert": 0, "🟠 watch": 1, "🟢 ok": 2, "": 3}
    for s, w, u, l, unit, n in sorted(rows, key=lambda x: (order[level(x[2], x[3])], x[0])):
        out.append(f"| {level(u, l)} | {s} | {w} | {human(u, unit)} | {human(l, unit) if l else '—'} | "
                   f"{(u / l):.0%} | {n} |" if l else f"| | {s} | {w} | {human(u, unit)} | — | | {n} |")
    out += ["", "## Not measured", ""] + [f"- {g}" for g in gaps] if gaps else []
    print("\n".join(out))
    if a.json:
        json.dump({"at": NOW.isoformat(), "rows": rows, "gaps": gaps}, open(a.json, "w"), indent=1, ensure_ascii=False)
    alerts = sum(1 for r in rows if level(r[2], r[3]) == "🔴 alert")
    sys.exit(2 if alerts else 0)


if __name__ == "__main__":
    main()
