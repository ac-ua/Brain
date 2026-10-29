#!/usr/bin/env python3
"""Build the Brain artifact pages from src/: « Brain · Cockpit » (projects-cockpit.html) and « Brain · Plateforme des
apps » (platform.html).

Inlines the shared design system (skills/web-design-system: tokens.css, icons/icons.js, shell.js), the brand marks and
the app links, because an artifact page cannot load files from the repo. Run after any change, then republish.
Brand marks: brand/brain-mark.svg is the Brain's own; the others are copies of each app's mark (Camp de Base's comes
from the design system), refreshed by hand when an app changes its mark.
"""
import base64, json, pathlib
here = pathlib.Path(__file__).resolve().parent
ds = here.parent.parent / "skills" / "web-design-system"
APPS = {  # the apps the cockpit's side menu opens (Apps group); update when an app moves
    "campdebase": "https://base-camp.pages.dev",
    "sport": "https://sport-cw7.pages.dev",
    "finance": "https://claude.ai/artifact/BpPxLtgPLndNv2H6xnmzp5",
}

def data_uri(path, mime):
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()

MARKS = {
    "brain": data_uri(here / "brand" / "brain-mark.svg", "image/svg+xml"),
    "camp": data_uri(ds / "brand" / "mark.png", "image/png"),
    "sport": data_uri(here / "brand" / "sport-mark.svg", "image/svg+xml"),
    "finance": data_uri(here / "brand" / "finance-mark.svg", "image/svg+xml"),
}
COMMON = {
    "/*@DS_TOKENS@*/": (ds / "tokens.css").read_text(),
    "/*@DS_ICONS@*/": (ds / "icons" / "icons.js").read_text(),
    "/*@DS_SHELL@*/": (ds / "shell.js").read_text(),
    "/*@BRAND_MARK@*/": MARKS["brain"],
    "/*@APP_LINKS@*/{}": json.dumps(APPS),
    "/*@MARKS@*/{}": json.dumps(MARKS),
}
for src_name, out_name in (("cockpit.html", "projects-cockpit.html"), ("platform.html", "platform.html")):
    src = (here / "src" / src_name).read_text()
    for key, val in COMMON.items():
        n = src.count(key)
        assert n <= 1, (src_name, key)
        if n:
            src = src.replace(key, val)
    assert "/*@" not in src, (src_name, "unreplaced placeholder")
    (here / out_name).write_text(src)
    print(out_name, len(src), "bytes")
