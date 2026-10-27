#!/usr/bin/env python3
"""Build a planned GPX route from a list of waypoints: trail routing (BRouter, OpenStreetMap paths) or straight
great-circle legs (ice, tundra, sea ice, polar plateau), terrain altitude (Copernicus 90 m via Open-Meteo), stats per
leg, daily stages, and a GPX 1.1 file with Garmin symbols that Camp de Base, a watch or an inReach can read.

Usage:
  python3 route.py build PLAN.json [--out route.gpx] [--no-ele]
  python3 route.py stats ROUTE.gpx

PLAN.json:
{
  "name": "Vatnajökull crossing 2027",
  "kind": "planned",                       # planned | alternative | reconstructed
  "note": "Planned from the Notion route page, 2026-10-28",
  "default_mode": "straight",              # straight | trail
  "profile": "hiking-mountain",            # BRouter profile for trail legs (trekking, hiking-mountain, shortest)
  "step_km": 0.5,                          # point spacing on straight legs
  "waypoints": [
    {"name": "Start", "lat": 64.40, "lon": -16.80, "kind": "start"},
    {"name": "Depot 1", "lat": 64.45, "lon": -16.60, "kind": "depot", "mode": "trail", "via": [[64.42, -16.70]]},
    {"name": "End", "lat": 64.70, "lon": -16.20, "kind": "end"}
  ],
  "stages": {"km_per_day": 18, "rest_every": 6, "start_date": "2027-04-10"}     # or {"days": 12, ...}
}
A waypoint's "mode" and "via" apply to the leg that ends at it. Kinds: start end camp depot resupply pass summit
hut water danger crevasse airstrip photo waypoint.
"""
import argparse, datetime, json, math, sys, time, urllib.parse, urllib.request
import xml.etree.ElementTree as ET

R = 6371008.8
GPX_NS = "http://www.topografix.com/GPX/1/1"
SYM = {"start": "Flag, Green", "end": "Flag, Red", "camp": "Campground", "depot": "Flag, Blue",
       "resupply": "Shopping Center", "pass": "Summit", "summit": "Summit", "hut": "Lodge", "water": "Drinking Water",
       "danger": "Danger Area", "crevasse": "Danger Area", "airstrip": "Airport", "photo": "Scenic Area",
       "waypoint": "Waypoint"}


def hav(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * R * math.asin(math.sqrt(min(1.0, h)))


def great_circle(a, b, step_m):
    """Points from a to b along the great circle, every ~step_m (works near the poles)."""
    d = hav(a, b)
    n = max(1, int(d // step_m))
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    delta = d / R
    out = []
    for i in range(1, n + 1):
        f = i / n
        if delta == 0:
            out.append([b[0], b[1], None]); continue
        A, B = math.sin((1 - f) * delta) / math.sin(delta), math.sin(f * delta) / math.sin(delta)
        x = A * math.cos(la1) * math.cos(lo1) + B * math.cos(la2) * math.cos(lo2)
        y = A * math.cos(la1) * math.sin(lo1) + B * math.cos(la2) * math.sin(lo2)
        z = A * math.sin(la1) + B * math.sin(la2)
        out.append([math.degrees(math.atan2(z, math.hypot(x, y))), math.degrees(math.atan2(y, x)), None])
    return out


def get_json(url, tries=3):
    for k in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "brain-gpx-route/1.0"})
            return json.load(urllib.request.urlopen(req, timeout=120))
        except Exception as ex:  # rate limit or network: back off
            if k == tries - 1:
                raise
            print("  retry:", str(ex)[:80], file=sys.stderr)
            time.sleep(5 * (k + 1))


def brouter(points, profile):
    ll = "|".join("%.6f,%.6f" % (p[1], p[0]) for p in points)
    g = get_json("https://brouter.de/brouter?" + urllib.parse.urlencode(
        {"lonlats": ll, "profile": profile, "alternativeidx": 0, "format": "geojson"}))
    return [[c[1], c[0], c[2] if len(c) > 2 else None] for c in g["features"][0]["geometry"]["coordinates"]]


def terrain(points):
    """Fill altitudes from Open-Meteo's elevation API (Copernicus DEM 90 m), 100 points per call, ≤ ~1,000 calls'
    worth of points sampled, the rest interpolated."""
    idx = list(range(0, len(points), max(1, len(points) // 1000))) + [len(points) - 1]
    idx = sorted(set(idx))
    ele = {}
    for i in range(0, len(idx), 100):
        chunk = idx[i:i + 100]
        q = urllib.parse.urlencode({"latitude": ",".join("%.5f" % points[j][0] for j in chunk),
                                    "longitude": ",".join("%.5f" % points[j][1] for j in chunk)})
        res = get_json("https://api.open-meteo.com/v1/elevation?" + q)["elevation"]
        ele.update(zip(chunk, res))
        time.sleep(0.3)
    known = sorted(ele)
    for a, b in zip(known, known[1:]):
        for j in range(a, b + 1):
            f = 0 if b == a else (j - a) / (b - a)
            points[j][2] = round(ele[a] + f * (ele[b] - ele[a]), 1)


def stats(points):
    dist, up, down, smooth = 0.0, 0.0, 0.0, None
    for a, b in zip(points, points[1:]):
        dist += hav(a, b)
    eles = [p[2] for p in points if p[2] is not None]
    for e in eles:  # 10 m hysteresis so GPS or DEM noise doesn't count as climbing
        if smooth is None:
            smooth = e
        elif e - smooth >= 10:
            up += e - smooth; smooth = e
        elif smooth - e >= 10:
            down += smooth - e; smooth = e
    return {"km": round(dist / 1000, 2), "ascent_m": round(up), "descent_m": round(down),
            "min_m": round(min(eles)) if eles else None, "max_m": round(max(eles)) if eles else None}


def stages(points, cfg):
    total = sum(hav(a, b) for a, b in zip(points, points[1:]))
    per = cfg.get("km_per_day", 0) * 1000 or total / max(1, cfg.get("days", 1))
    rest, start = cfg.get("rest_every", 0), cfg.get("start_date")
    date = datetime.date.fromisoformat(start) if start else None
    camps, run, target, day, walk = [], 0.0, per, 1, 0
    for a, b in zip(points, points[1:]):
        run += hav(a, b)
        if run >= target and total - run > per * 0.25:
            walk += 1
            camps.append({"name": "Camp %d" % walk, "lat": b[0], "lon": b[1], "kind": "camp",
                          "date": (date + datetime.timedelta(days=day - 1)).isoformat() if date else None,
                          "km": round(run / 1000, 1)})
            day += 1
            if rest and walk % rest == 0:
                day += 1  # rest day at that camp
            target += per
    return camps, day


def write_gpx(path, plan, points, wpts):
    ET.register_namespace("", GPX_NS)
    g = ET.Element("{%s}gpx" % GPX_NS, {"version": "1.1", "creator": "brain gpx-route"})
    md = ET.SubElement(g, "{%s}metadata" % GPX_NS)
    ET.SubElement(md, "{%s}name" % GPX_NS).text = plan["name"]
    ET.SubElement(md, "{%s}desc" % GPX_NS).text = "%s. %s" % (plan.get("kind", "planned").upper() + " (not recorded)"
                                                               if plan.get("kind", "planned") != "actual" else "ACTUAL",
                                                               plan.get("note", ""))
    for w in wpts:
        e = ET.SubElement(g, "{%s}wpt" % GPX_NS, {"lat": "%.6f" % w["lat"], "lon": "%.6f" % w["lon"]})
        if w.get("ele") is not None:
            ET.SubElement(e, "{%s}ele" % GPX_NS).text = "%.1f" % w["ele"]
        if w.get("date"):
            ET.SubElement(e, "{%s}time" % GPX_NS).text = w["date"] + "T00:00:00Z"
        ET.SubElement(e, "{%s}name" % GPX_NS).text = w["name"]
        if w.get("note"):
            ET.SubElement(e, "{%s}desc" % GPX_NS).text = w["note"]
        ET.SubElement(e, "{%s}sym" % GPX_NS).text = SYM.get(w.get("kind", "waypoint"), "Waypoint")
        ET.SubElement(e, "{%s}type" % GPX_NS).text = w.get("kind", "waypoint")
    trk = ET.SubElement(g, "{%s}trk" % GPX_NS)
    ET.SubElement(trk, "{%s}name" % GPX_NS).text = plan["name"]
    ET.SubElement(trk, "{%s}type" % GPX_NS).text = plan.get("kind", "planned")
    seg = ET.SubElement(trk, "{%s}trkseg" % GPX_NS)
    for p in points:
        e = ET.SubElement(seg, "{%s}trkpt" % GPX_NS, {"lat": "%.6f" % p[0], "lon": "%.6f" % p[1]})
        if p[2] is not None:
            ET.SubElement(e, "{%s}ele" % GPX_NS).text = "%.1f" % p[2]
    ET.indent(g)
    ET.ElementTree(g).write(path, encoding="utf-8", xml_declaration=True)


def read_gpx(path):
    root = ET.parse(path).getroot()
    pts = []
    for tag in ("trkpt", "rtept"):
        for e in root.iter("{%s}%s" % (GPX_NS, tag)):
            el = e.find("{%s}ele" % GPX_NS)
            pts.append([float(e.get("lat")), float(e.get("lon")), float(el.text) if el is not None else None])
    return pts


def build(plan_path, out, with_ele):
    plan = json.load(open(plan_path))
    wps, step = plan["waypoints"], plan.get("step_km", 0.5) * 1000
    points, legs = [[wps[0]["lat"], wps[0]["lon"], None]], []
    for a, b in zip(wps, wps[1:]):
        mode = b.get("mode", plan.get("default_mode", "straight"))
        via = [[v[0], v[1]] for v in b.get("via", [])]
        chain = [[a["lat"], a["lon"]]] + via + [[b["lat"], b["lon"]]]
        if mode == "trail":
            seg = brouter(chain, b.get("profile", plan.get("profile", "hiking-mountain")))[1:]
        else:
            seg = []
            for p, q in zip(chain, chain[1:]):
                seg += great_circle(p, q, step)
        start = len(points) - 1
        points += seg
        legs.append((a["name"], b["name"], mode, start, len(points) - 1))
    if with_ele:
        try:
            terrain(points)
        except Exception as ex:  # rate limit or blocked host: keep the route, say so
            print("  terrain altitude skipped (%s); rerun later or import with Camp de Base's terrain option"
                  % str(ex)[:60], file=sys.stderr)
    wpts = [dict(w) for w in wps]
    for w in wpts:  # altitude of each waypoint = nearest track point
        near = min(points, key=lambda p: hav(p, (w["lat"], w["lon"])))
        w.setdefault("ele", near[2])
    camps = []
    if plan.get("stages"):
        camps, days = stages(points, plan["stages"])
        wpts += camps
    write_gpx(out, plan, points, wpts)
    s = stats(points)
    print("%s → %s" % (plan["name"], out))
    print(("  total: %(km)s km, +%(ascent_m)s m / -%(descent_m)s m, altitude %(min_m)s–%(max_m)s m" if s["max_m"] is not None
           else "  total: %(km)s km (no altitude)") % s)
    for a, b, mode, i, j in legs:
        ls = stats(points[i:j + 1])
        print("  %-22s → %-22s %-8s %7.1f km  +%s m" % (a[:22], b[:22], mode, ls["km"], ls["ascent_m"]))
    if camps:
        print("  stages: %d camps, %d days with rests" % (len(camps), days))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build"); b.add_argument("plan"); b.add_argument("--out", default="route.gpx")
    b.add_argument("--no-ele", action="store_true")
    s = sub.add_parser("stats"); s.add_argument("gpx")
    a = ap.parse_args()
    if a.cmd == "build":
        build(a.plan, a.out, not a.no_ele)
    else:
        print(json.dumps(stats(read_gpx(a.gpx)), indent=1))
