#!/usr/bin/env python3
"""Check a cloud session's environment against what a project needs, in one pass, without printing any secret.

Usage:
  python3 preflight.py scan [REPO]              list the variable names and hosts the code refers to (draft a manifest)
  python3 preflight.py check [MANIFEST]         check variables, hosts and tools (default: docs/environment.json)

Manifest (docs/environment.json in the project repo):
{
  "project": "base-camp",
  "variables": [
    {"name": "BASECAMP_SUPABASE_URL", "kind": "public", "match": "^https://wtsf\\\\w+\\\\.supabase\\\\.co$",
     "purpose": "scripts: Supabase project URL", "set_in": "environment variables"},
    {"name": "BASECAMP_SUPABASE_SERVICE_ROLE_KEY", "kind": "secret", "prefix": "sb_secret_",
     "purpose": "scripts: service key", "set_in": "environment variables", "optional": false}
  ],
  "forbidden": ["SUPABASE_SERVICE_ROLE_KEY"],          # must NOT be set here (another project's keys, unused power)
  "hosts": [
    {"url": "https://wtsf….supabase.co/rest/v1/", "expect": [200, 401], "why": "scripts"},
    {"url": "https://basecamp.example.com/api/health", "expect": [200], "why": "API with network secret"}
  ],
  "tools": ["python3", "node", "ffmpeg"]
}
Exit code 0 when everything passes, 1 otherwise. Values are never printed: only set/missing, length and prefix match.
"""
import json, os, re, shutil, ssl, sys, urllib.error, urllib.request
from pathlib import Path

SKIP_DIRS = {".git", "node_modules", "dist", "vendor", ".venv", "__pycache__", "artifacts"}
ENV_PATTERNS = [
    r"os\.environ\.get\(\s*['\"]([A-Z][A-Z0-9_]+)",
    r"os\.environ\[\s*['\"]([A-Z][A-Z0-9_]+)",
    r"os\.getenv\(\s*['\"]([A-Z][A-Z0-9_]+)",
    r"process\.env\.([A-Z][A-Z0-9_]+)",
    r"\benv\.([A-Z][A-Z0-9_]{2,})\b",
    r"\$\{?([A-Z][A-Z0-9_]*(?:URL|KEY|TOKEN|SECRET|ID))\}?",
]
HOST_RE = re.compile(r"https://([a-z0-9.-]+\.[a-z]{2,})")
COMMON_HOSTS = {"github.com", "www.w3.org", "fonts.googleapis.com", "fonts.gstatic.com", "cdn.jsdelivr.net",
                "unpkg.com", "cdnjs.cloudflare.com", "example.com"}


def scan(repo):
    names, hosts = {}, {}
    for p in Path(repo).rglob("*"):
        if not p.is_file() or set(p.parts) & SKIP_DIRS or p.suffix not in {
                ".py", ".js", ".mjs", ".ts", ".sh", ".toml", ".yml", ".yaml", ".md", ".json", ".sql"}:
            continue
        try:
            text = p.read_text(errors="ignore")
        except OSError:
            continue
        rel = str(p.relative_to(repo))
        for pat in ENV_PATTERNS:
            for m in re.finditer(pat, text):
                names.setdefault(m.group(1), set()).add(rel)
        if p.suffix in {".py", ".js", ".mjs", ".ts", ".sh", ".toml", ".yml", ".yaml"}:
            for m in HOST_RE.finditer(text):
                h = m.group(1)
                if h not in COMMON_HOSTS:
                    hosts.setdefault(h, set()).add(rel)
    print("Variables referenced by the code:")
    for n in sorted(names):
        print("  %-40s %s%s" % (n, "SET    " if os.environ.get(n) else "missing", "  ← " + ", ".join(sorted(names[n])[:3])))
    print("\nHosts referenced by the code (check which ones the session must reach):")
    for h in sorted(hosts):
        print("  %-45s ← %s" % (h, ", ".join(sorted(hosts[h])[:2])))
    print("\nDraft docs/environment.json from this list; keep only what a session really needs.")


def reach(url, timeout=12):
    ctx = ssl.create_default_context(cafile=os.environ.get("SSL_CERT_FILE") or os.environ.get("REQUESTS_CA_BUNDLE") or None)
    req = urllib.request.Request(url, method="GET", headers={"User-Agent": "preflight/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
            return r.status, ""
    except urllib.error.HTTPError as e:
        body = e.read(300).decode(errors="ignore")
        return e.code, body
    except Exception as e:  # DNS, TLS, proxy refusal, timeout
        return None, str(e)[:160]


def check(manifest):
    m = json.loads(Path(manifest).read_text())
    todo, ok = [], True
    print("Project: %s\n" % m.get("project", "?"))
    print("Variables")
    for v in m.get("variables", []):
        val, name = os.environ.get(v["name"], ""), v["name"]
        status = "ok"
        if not val:
            status = "missing" if not v.get("optional") else "missing (optional)"
        elif v.get("prefix") and not val.startswith(v["prefix"]):
            status = "WRONG TYPE (expected a value starting with %s)" % v["prefix"]
        elif v.get("match") and not re.search(v["match"], val):
            status = "WRONG VALUE (does not match the expected project)"
        print("  %-42s %-8s len=%-4s %s" % (name, v.get("kind", ""), len(val) if val else "-", status))
        if status != "ok" and not status.startswith("missing (optional)"):
            ok = False
            todo.append("%s %s — %s — set in: %s" % ("Set" if "missing" in status else "Fix", name,
                                                     v.get("purpose", ""), v.get("set_in", "environment variables")))
    for f in m.get("forbidden", []):
        if os.environ.get(f):
            ok = False
            print("  %-42s present but must not be set here" % f)
            todo.append("Remove %s from this environment (not this project's, or more power than needed)" % f)
    print("\nHosts")
    for h in m.get("hosts", []):
        code, err = reach(h["url"])
        expect = h.get("expect", [200])
        good = code in expect
        blocked = code == 403 and ("policy" in err.lower() or "not allowed" in err.lower() or "proxy" in err.lower())
        tunnel = code is None and "Tunnel connection failed" in err   # the session's proxy refused or DNS failed
        blocked = blocked or tunnel
        label = ("ok" if good else "BLOCKED by the network policy (or unknown host)" if blocked
                 else "HTTP %s %s" % (code, err[:80].replace("\n", " ")) if code else "unreachable: " + err)
        print("  %-60s %s" % (h["url"][:60], label))
        if not good:
            ok = False
            host = re.sub(r"^https?://([^/]+).*", r"\1", h["url"])
            if code in (401, 403) and not blocked:
                todo.append("Check the credential for %s (%s): HTTP %s" % (host, h.get("why", ""), code))
            else:
                todo.append("Allow host %s in the environment's network settings (%s)" % (host, h.get("why", "")))
    print("\nTools")
    for t in m.get("tools", []):
        where = shutil.which(t)
        print("  %-20s %s" % (t, where or "missing"))
        if not where:
            ok = False
            todo.append("Install %s (setup script or the repo's SessionStart hook)" % t)
    print("\n" + ("All good." if ok else "To fix (one pass, then start a NEW session: variables and hosts are read at start):"))
    for i, t in enumerate(dict.fromkeys(todo), 1):
        print("  %d. %s" % (i, t))
    return 0 if ok else 1


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in ("scan", "check"):
        sys.exit(__doc__)
    if sys.argv[1] == "scan":
        scan(sys.argv[2] if len(sys.argv) > 2 else ".")
    else:
        sys.exit(check(sys.argv[2] if len(sys.argv) > 2 else "docs/environment.json"))
