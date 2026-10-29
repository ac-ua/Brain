# web-design-system · feedback and changes

Every general piece of design feedback from Aurélien lands here (rule: `SKILL.md` › Feedback loop). Newest first.
Each line: date · app where it was said · the feedback in his words (short) · what changed in the system · apps that
still have to adopt it. When an app adopts a line, strike its name (`~~Sport~~`) and note its release.

Version = the latest line's version; an app records the version it runs in its own `docs/`.

| Version | Date | App | Feedback | What changed | Apps to adopt |
|---|---|---|---|---|---|
| v1.2 | 2026-10-29 | Camp de Base | Aurélien: "Camp de Base's look must not change; where the system differs from its current screens, the system follows Camp de Base." | v1.0's "one control height, 36 px" unification is void. From `camp.css`: buttons padding 8×13 with no fixed height and regular weight (`.btn`), chips regular weight (`.chip`), inputs padding 7×9 radius 7, meter fill green (`.meter`), error toast text white (`.toast.err`). Table headings, tabs, KPIs, panels, segmented control, chart palette (v1.1) and primary radius 2 already matched. | Camp de Base (nothing visible: the system now equals it), Sport data (its select and Retry button, next release), Element Logbook, Finance, website |
| v1.1 | 2026-10-29 | all | Aurélien: "Camp de Base is the only reference; chart palette re-derived from its expedition charts, no purple; button radius from its app screens; Camp de Base renames to ds- classes." | Reference = Camp de Base's app screens only, never the website. Series re-derived from its expedition charts: `--c1` accent `#0a6aa7`/`#6fb0e0`, `--c2` gear slate `#5b7f95`/`#7fa3ba`, `--c3` food orange `#d9480f`/`#ff7a3d`, `--c4` fuel amber `#e8a33d`/`#f0b44c` (`expeditions.js` load chart, `camp.css`), `--c5` good-weather green `#3f9b6b`/`#56b07f` (`simulation.js`), `--c6` deadline red `#b42318`/`#ff8a7a` (expedition calendar), `--c-other` rest grey `#adb5bd`/`#6b7a86` (`simulation.js`); purple (`--c4` `#7a4f9a`/`#b48ad6`) and `--c7` dropped. Primary button radius 2 px (`camp.css` `.btn.primary`, `index.html`), other buttons 8. Decided path: Camp de Base renames its classes to `ds-` and loads `ds.css`, no alias layer. | Camp de Base (rename to `ds-`, series), ~~Sport data~~ (v0.12, ac-ua/sport#24), Element Logbook, Finance (first UI), website (fonts and colours only) |
| v1.0 | 2026-10-29 | all | "Every app shares one design system; Camp de Base is the reference." | System extracted from Camp de Base: tokens (light, dark, context palettes), shell, `ds-` components, data-viz rules, faceted icon kit (73 icons, 16 glyphs). Unified Camp de Base's drift: one button radius (8 px, the primary was 2 px in `camp.css`), one control height (36 px), table heads 11 px `.08em`, status colours as tokens instead of hex (login error, calendar kinds, avatars, pins), unused fonts dropped (Saira Condensed, IBM Plex Sans), categorical series `--c1`…`--c7` (new dark purple `#b48ad6`). | Camp de Base (rename to `ds-` classes at a quiet release, or alias; superseded by v1.1: rename, no alias), ~~Sport data~~ (v0.12, ac-ua/sport#24), Element Logbook, Finance (first UI), website (fonts and colours only) |

## Icons proposed for the kit
Drawn by an app in its own `data/icons.app.json`, generic enough for every app; promote them to `icons/icons.json` at
the next kit change (copy the entry, keep the name).

| Date | App | Icons | Source |
|---|---|---|---|
| 2026-10-29 | Sport data | `stopwatch` (duration, moving time), `trend` (progress, form), `battery` (energy, charge), `sync` (sync, refresh), `heart` (heart rate, health), `power` (power, energy), `trophy` (records) | `ac-ua/sport` › `data/icons.app.json` |
