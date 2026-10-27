#!/usr/bin/env python3
"""Build ledger for a personal project: every feature, screen, data store, deploy piece, decision and open item.

Usage: ledger.py --ledger docs/build-ledger.json <command> [options]
Commands: init, add, decide, open-item, close-item, change, guide, show, check
"""
import argparse, json, re, sys
from datetime import datetime
from pathlib import Path

KINDS = ["feature", "screen", "data", "backup", "deploy", "integration", "secret-ref", "metric", "artifact", "other"]


def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def load(path):
    p = Path(path)
    if not p.exists():
        sys.exit(f"no ledger at {p}; run init first")
    return json.loads(p.read_text())


def save(path, data):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n")


def cmd_init(a):
    if Path(a.ledger).exists() and not a.force:
        sys.exit(f"{a.ledger} exists (use --force to overwrite)")
    save(a.ledger, {
        "build": {"project": a.project, "tag": a.tag, "owner": a.owner, "use_cases": a.use_case or [], "created": now()},
        "guide": {"path": "docs/config-guide/guide.html", "url": None, "version": "v0", "updated": None},
        "assets": [], "decisions": [], "open_items": [], "changes": [],
    })
    print(f"ledger created: {a.ledger}")


def cmd_add(a):
    d = load(a.ledger)
    fields = {k: v for k, v in {"kind": a.kind, "id": a.id, "name": a.name, "purpose": a.purpose,
                                "where": a.where, "status": a.status}.items() if v is not None}
    for asset in d["assets"]:
        if asset["id"] == a.id and asset["kind"] == a.kind:
            asset.update(fields, updated=now())
            print(f"updated {a.kind}:{a.id}")
            break
    else:
        d["assets"].append({**fields, "status": a.status or "live", "created": now(), "updated": now()})
        print(f"added {a.kind}:{a.id}")
    save(a.ledger, d)


def cmd_decide(a):
    d = load(a.ledger)
    d["decisions"].append({"date": now(), "what": a.what, "why": a.why, "by": a.by})
    save(a.ledger, d)


def cmd_open_item(a):
    d = load(a.ledger)
    d["open_items"].append({"date": now(), "what": a.what, "kind": a.kind, "owner": a.owner, "status": "open"})
    save(a.ledger, d)


def cmd_close_item(a):
    d = load(a.ledger)
    hits = [i for i in d["open_items"] if a.match.lower() in i["what"].lower() and i.get("status") == "open"]
    if len(hits) != 1:
        sys.exit(f"{len(hits)} open items match '{a.match}'; be more specific")
    hits[0].update(status="closed", closed=now(), resolution=a.resolution)
    save(a.ledger, d)


def cmd_change(a):
    d = load(a.ledger)
    d["changes"].append({"date": now(), "summary": a.summary})
    save(a.ledger, d)


def cmd_guide(a):
    d = load(a.ledger)
    d["guide"].update({k: v for k, v in {"version": a.version, "url": a.url, "path": a.path}.items() if v})
    d["guide"]["updated"] = now()
    save(a.ledger, d)


def cmd_show(a):
    d = load(a.ledger)
    b = d["build"]
    print(f"{b['project']} ({b['tag']}) · guide {d['guide']['version']}")
    for k in KINDS:
        items = [x for x in d["assets"] if x["kind"] == k]
        if items:
            print(f"\n{k} ({len(items)})")
            for x in items:
                print(f"  - {x['name']} [{x.get('status', '')}] {x.get('purpose', '')}")
    opened = [i for i in d["open_items"] if i.get("status") == "open"]
    print(f"\ndecisions: {len(d['decisions'])} · open items: {len(opened)} · changes: {len(d['changes'])}")


def cmd_check(a):
    d = load(a.ledger)
    text = re.sub(r"<[^>]+>", " ", Path(a.guide).read_text()).lower()
    missing = [x for x in d["assets"] if x["name"].lower() not in text]
    for x in missing:
        print(f"not in guide: {x['kind']}:{x['id']} — {x['name']}")
    print(f"{len(d['assets']) - len(missing)}/{len(d['assets'])} assets covered")
    sys.exit(1 if missing else 0)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--ledger", default="docs/build-ledger.json")
    s = p.add_subparsers(dest="cmd", required=True)

    i = s.add_parser("init"); i.add_argument("--project", required=True); i.add_argument("--tag", required=True)
    i.add_argument("--owner", default="Aurélien"); i.add_argument("--use-case", action="append")
    i.add_argument("--force", action="store_true")

    ad = s.add_parser("add"); ad.add_argument("--kind", required=True, choices=KINDS); ad.add_argument("--id", required=True)
    ad.add_argument("--name", required=True); ad.add_argument("--purpose"); ad.add_argument("--where")
    ad.add_argument("--status", choices=["live", "sample", "unfinished", "retired"])

    de = s.add_parser("decide"); de.add_argument("--what", required=True); de.add_argument("--why", required=True)
    de.add_argument("--by", default="Aurélien")

    oi = s.add_parser("open-item"); oi.add_argument("--what", required=True)
    oi.add_argument("--kind", default="todo", choices=["todo", "choice", "blocker", "risk"]); oi.add_argument("--owner", default="Aurélien")

    ci = s.add_parser("close-item"); ci.add_argument("--match", required=True); ci.add_argument("--resolution", required=True)

    ch = s.add_parser("change"); ch.add_argument("--summary", required=True)

    g = s.add_parser("guide"); g.add_argument("--version"); g.add_argument("--url"); g.add_argument("--path")

    s.add_parser("show")
    c = s.add_parser("check"); c.add_argument("--guide", default="docs/config-guide/guide.html")

    a = p.parse_args()
    globals()["cmd_" + a.cmd.replace("-", "_")](a)


if __name__ == "__main__":
    main()
