---
name: gpx-route
description: Create GPX routes to plan Aurélien's expeditions — from waypoints, a map, a route description or an operator's route map to a planned track (trail routing on OpenStreetMap paths, or straight great-circle legs on ice, tundra and polar plateau), terrain altitude, distance and climb per leg, daily stages with camps and rest days, Garmin symbols, ready for Camp de Base, a watch or an inReach. Also variants, and reconstructing a past route from loose evidence. Use for "fais-moi la trace GPX de…", "planifie l'itinéraire", "découpe en étapes", "trace prévue", "reconstitue la trace de 2019".
---

# gpx-route

Planning tool for the Expeditions domain. The route lives in **Camp de Base** (`ac-ua/Base-Camp`, Route tab: planned,
actual and alternative tracks, waypoints, stage planner, polar view); this skill makes the GPX that goes into it.
Script: `scripts/route.py` (no dependencies; BRouter for trails, Open-Meteo elevation for altitude).

## 1. Brief (ask once)
Expedition and mode of travel (ski with pulk, trek, packraft, bike), start and end, must-pass points (depots, huts,
passes, resupply, airstrips), what to avoid (crevasse zones, closed areas, rivers), terrain type per section,
daily distance or number of days, rest rhythm, start date, sources (Notion route page, operator map, guidebook,
earlier GPX). Several options → one main (`planned`) and the others as `alternative`.

## 2. Waypoints
Coordinates from the sources (guidebook, operator map, OSM, Aurélien's notes), each with a kind (`start end camp depot
resupply pass summit hut water danger crevasse airstrip photo waypoint`) and its source. Unknown or estimated
coordinates are marked in the waypoint's note ("estimated from the operator's map"). Show the list before building.

## 3. Build
Write `PLAN.json` (format in the script's header), then:
```bash
python3 <brain>/skills/gpx-route/scripts/route.py build PLAN.json --out <slug>.gpx
python3 <brain>/skills/gpx-route/scripts/route.py stats <slug>.gpx
```
| Terrain | Leg mode |
|---|---|
| Marked trails, huts, roads | `trail` (BRouter `hiking-mountain`; `trekking` for bike; add `via` points to force a pass) |
| Ice cap, sea ice, tundra, polar plateau, open fell | `straight` (great circle, works up to the Pole); add intermediate waypoints to follow the real line around obstacles |

Altitude comes from the terrain model (Copernicus 90 m), not from the routing. If the elevation service is rate
limited, the route is still written: import it with Camp de Base's "Use the terrain altitude" option.

Stages: `"stages": {"km_per_day": 20, "rest_every": 7, "start_date": "…"}` or `{"days": 12}` adds one camp per day
along the track. For polar travel, plan short first days and say the assumption (km/day grows as the pulk lightens).

## 4. Check, then hand over
- Read the per-leg table: distance and climb plausible for the mode of travel; compare with the source (operator's
  stated distance, guidebook times). Say the gap.
- Look at the track on a map (Camp de Base after import, or a quick artifact with the GPX) before calling it done.
- The GPX metadata says `PLANNED (not recorded)` or `RECONSTRUCTED`, with the sources: a planned track is never
  presented as done.
- Import: drag the GPX onto the expedition's Route tab (kind planned / alternative), or via the API
  (`POST /expeditions/{id}/routes`, see `ac-ua/Base-Camp` `docs/api.md`). Store the file in the repo
  (`data/routes/<slug>.gpx`) or the expedition's Drive folder.

## Reconstructing a past route
Same tool, different evidence: places and times Aurélien remembers, photos with GPS or timestamps, calendar events,
screenshots of maps. Ask the questions first (dates, where each night was, start and end times), mark the result
`reconstructed`, and keep what is estimated in the waypoint notes. Times between known points are spread by effort
(Naismith), not invented as recorded.

From a map screenshot:
- A compass button on a Google Maps screenshot means the map is rotated. Fit scale **and** rotation on two known
  points (the exact start and a named place: a pass, a village, a lake), never one point and "north up".
- Check the result on a topo map (the stars should sit on the valley, road or trail), then ask Aurélien for a rough
  sketch on Camp de Base's map to confirm the valley before importing.
- A corrected track that is already in the app is refreshed in place (update the route, waypoints, days); nothing is
  deleted without his OK.

## Rules
- Safety-critical choices (crevasse zones, sea-ice crossings, river fords) come from his sources and his
  operator, never from routing alone: say so on those legs.
- Route, day and gear details live in Camp de Base, not in Notion Memories.
