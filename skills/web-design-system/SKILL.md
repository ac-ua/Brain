---
name: web-design-system
description: The one web design system shared by all of Aurélien's apps (Camp de Base, Sport data, Finance, Element Logbook, the website and every future app) — colour and type tokens with light and dark themes, layout, components, data-viz rules and the faceted icon kit, plus the loop that turns his design feedback into durable changes. Use for any UI, page, component, chart, icon or look-and-feel work on any of his apps, when he gives feedback on UI, UX, colours, layout or icons, and when starting a new app.
---

# web-design-system

Every app Aurélien uses should feel like the same product: same colours, type, shell, controls and icons. The
reference is **Camp de Base** (`ac-ua/Base-Camp`) and only Camp de Base (Aurélien's call, 2026-10-29): its app screens
(`web/camp.css`, the expeditions pages) decide every value, never his website. Its identity: Syne and Questrial, the
`#0a6aa7` button blue, the `#ebf4ff` ice band, the faceted mountain mark.

| File | What |
|---|---|
| [`tokens.css`](tokens.css) | tokens (light, dark, context palettes), base styles and the core `ds-` components; copy it as `web/ds.css` |
| [`icons/`](icons/) | `icons.json` (73 generic faceted icons), `glyphs.json` (16 UI glyphs), `build_icons.py` → `icons.js` |
| [`shell.js`](shell.js) | the app shell's behaviour (fold the side menu, phone drawer, theme switch, full screen for cards v1.6, the filter bar's phone toggle v1.7, the app switcher v1.9); copy it next to the pages |
| [`apps.json`](apps.json) | the registry of the apps (v1.9): name, address, kit icon, `data-ds-app` key, `/api/attention`; read by the app switcher, the Brain cockpit and the attention connector; copy it next to the pages |
| [`brand/`](brand/) | `mark.png` (Camp de Base's faceted mountain), `favicon.png`; every other app has its own mark (Brand marks) |
| [`FEEDBACK.md`](FEEDBACK.md) | change log of the system and which apps still have to adopt each change |

## Principles
1. **Calm and dense.** Pale cool background, white surfaces, thin `--line` borders, one shadow used only on hover and
   overlays. Information first: numbers big and in mono, labels small and uppercase.
2. **One accent.** `--accent` carries links, the primary action, the selected tab, focus marks. Status colours mean
   status only, never decoration.
3. **Selected = inverted.** A pressed chip, segment, sub-tab or stage turns `--ink` on `--bg`; a selected tab gets an
   accent underline; the current side link gets a surface and a 3 px accent bar.
4. **Same in dark.** Every colour is a token; nothing hard-coded except inside icons and photos. Both themes are
   checked before shipping.
5. **Phone first for field screens, desktop first for analysis**, but every page works on both (side menu becomes a
   drawer under 860 px; tables scroll in their frame; wide tables become cards under 700 px, except matrices).
6. **No emojis in the UI.** Icons come from the kit; controls use the plain glyphs.

## Tokens
Load the fonts once per page:
```html
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Syne:wght@700&family=Questrial&family=IBM+Plex+Mono:wght@400;500&display=swap">
```

| Token | Light | Dark | Use |
|---|---|---|---|
| `--bg` | `#f6f9fd` | `#0b1218` | page |
| `--surface` | `#ffffff` | `#121c24` | cards, panels, inputs |
| `--sunken` | `#ebf4ff` | `#0e1820` | side menu, table heads, tracks, hover rows |
| `--ink` | `#000000` | `#eef4f9` | text; inverted selection background |
| `--muted` | `#5b6b7a` | `#92a5b4` | secondary text, labels |
| `--line` | `#d6e1ec` | `#22323e` | borders, dividers, axes |
| `--accent` / `--accent-ink` | `#0a6aa7` / `#ffffff` | `#6fb0e0` / `#04121c` | links, primary, selection; text on accent |
| `--accent-soft` | `#e2eef8` | `#10283a` | selected rows, suggestion boxes, chart areas |
| `--focus` | `#1b68f6` | `#8cc0ff` | focus ring |
| `--ok` / `--ok-soft` | `#2b7a4b` / `#dff2e6` | `#6cc795` / `#12301f` | done, owned, healthy |
| `--warn` / `--warn-soft` | `#9a5b00` / `#fff1d6` | `#f0b44c` / `#33260f` | to check, missing, still due (not an error) |
| `--bad` / `--bad-soft` | `#b42318` / `#fde4e1` | `#ff8a7a` / `#3a1612` | errors, over budget, destructive |
| `--info` / `--info-soft` | `#1f5f99` / `#e0edf9` | `#7db6ef` / `#11263a` | in progress, ordered, sources |
| `--c1`…`--c6`, `--c-other` | `#0a6aa7 #5b7f95 #d9480f #e8a33d #3f9b6b #b42318`, `#adb5bd` | `#6fb0e0 #7fa3ba #ff7a3d #f0b44c #56b07f #ff8a7a`, `#6b7a86` | data series, in this order (Data viz) |
| `--c7`, `--c8` (v1.5) | `#1a8a96 #8b5e34` | `#4fc1c9 #c49a6c` | two more series, not status colours: ocean teal, desert earth (Data viz) |
| `--c9`…`--c12` (v1.8) | `#0e3e84 #6b7a1f #1a4f1c #4a4c48` | `#b4cdf7 #b5c25a #9fd49a #c4c6c2` | four more series for apps with up to twelve categories: deep ocean, olive, deep forest, granite (Data viz) |
| `--ci-ink`, `--ci-a`…`--ci-d` | `#0d1117`; `#5b8fc0 #3e5d75 #ffffff #9ea2ab` | `#05080b`; same fills | icon outline; sky, slate, snow, stone |
| `--shadow` | `0 1px 2px rgba(15,30,39,.06), 0 8px 24px rgba(15,30,39,.08)` | stronger black | hover, menus, dialogs |
| `--scrim` | `rgba(5,12,16,.45)` | same | behind drawers and dialogs |

**Type.** `--display` Syne 700 (titles, tabs, card titles, big dates); `--body` Questrial 400 (everything else; its
"600" is synthetic, use it only for small labels); `--mono` IBM Plex Mono 400/500 with tabular numbers for every
figure, date and unit. Body 15px/1.5. Scale: h1 `clamp(28px, 4.4vw, 40px)/1.05` (hero 32–58), h2 22, card title
18–19, section label (`h3`, `.ds-label`) 12 px uppercase `.1em` muted, small label 11 px uppercase `.08em`, KPI value
22 px mono 500 (hero figures 30–76), table 14, secondary 12–13. Never two display-font sizes in one card.

**Spacing** on a 2/4 px rhythm: 4 8 12 16 24 32 64 (`--s1`…`--s7`), plus 6, 10, 14, 18 inside components. Page gap
18, grid gaps 10–14, panel padding 16, card padding 14×16, page padding 24 top / 64 bottom.
**Radii:** 2 the primary button (Camp de Base's `.btn.primary`) · 4 tags · 6 small buttons, thumbs · 7 inputs · 8 buttons,
menu links · 10 panels, cards, tables · 12 dialogs,
big tiles · 18 hero · 999 pills, chips, segments. **Borders:** 1 px `--line`; dashed = empty, optional or "drop
here"; a 3–4 px left border carries a status or category colour. **Motion:** `.15s` hover (border, shadow,
`translateY(-1px)` on tiles), `.18s ease-out` drawers, `.3–.4s ease` folding headers; everything off under
`prefers-reduced-motion`.

## Layout
- **Shell (required in every app):** exactly Camp de Base's. A fixed left menu `.ds-side` (232 px, `--sunken`):
  brand at the top (the app's mark 34 px + app name in Syne 20 + owner in 12 px muted, then the fold button `«`),
  groups with an uppercase label, one link per section with its faceted icon (`.ico`, 20 px), a count or a "Soon"
  badge; current link `aria-current="page"` (surface + 3 px accent bar). At the bottom left (`.ds-side-foot`) the
  theme switch, then **Sign out** under it, full width (`.ds-signout`). Folded (`«` / `»`): icons only at 64 px,
  opening over the page on hover or keyboard focus, the choice kept per app (`<app>.side.mini`). Content in
  `.ds-app > main.ds-wrap.ds-main` (max 1320 px, 16 px gutters plus safe areas), starting with the page title row.
  Under 860 px: sticky top bar `.ds-mtop` (menu button + « **App** · Page ») and the menu as a drawer over a scrim;
  a link, the scrim or Escape closes it. Behaviour: `shell.js` (classes `ds-side-mini` / `ds-side-open` on `<body>`,
  or on a `[data-ds-shell]` root when the page lives inside another host, like a claude.ai dashboard):
  ```html
  <body data-ds-app="sport">            <!-- or <div data-ds-shell data-ds-app="sport"> inside a host -->
  <div class="ds-mtop"><button class="ds-icon-btn" data-ds-side-open aria-controls="side" aria-expanded="false"
    aria-label="Open the menu">(menu glyph)</button><span><b>App</b> · Page</span></div>
  <div class="ds-scrim" data-ds-scrim hidden></div>
  <nav class="ds-side" id="side" aria-label="App">
    <div class="ds-side-brand"><img src="mark.svg" alt=""><span><b>App</b><small>Aurélien Caye</small></span>
      <button class="ds-side-fold" data-ds-side-fold title="Fold or open the menu" aria-label="Fold or open the menu">
        <span class="ds-fold">«</span><span class="ds-unfold">»</span></button></div>
    <div class="ds-side-group"><span class="ds-side-h">Group</span>
      <a class="ds-side-link" aria-current="page" href="#"><span class="ico">(icon)</span>Section</a></div>
    <div class="ds-side-foot">
      <div class="ds-seg" role="group" aria-label="Theme"><button data-ds-theme="auto" aria-label="Automatic theme">…</button>
        <button data-ds-theme="light" aria-label="Light theme">…</button><button data-ds-theme="dark" aria-label="Dark theme">…</button></div>
      <a class="ds-signout" href="/logout">Sign out</a></div>
  </nav>
  <div class="ds-app"><main class="ds-wrap ds-main"><header class="ds-head">…</header>…</main></div>
  <script src="shell.js"></script>
  ```
- **App switcher (v1.9, required at the next release):** right under `.ds-side-brand`, `<div class="ds-apps"
  data-ds-apps></div>`; `shell.js` fills it from `apps.json` (copied next to the pages, or inlined as
  `<script type="application/json" id="ds-apps-data">` where the page cannot fetch, like a claude.ai artifact): a
  button with the current app (found by host, else by `data-ds-app` = `shell`), a menu with every app and, under a
  rule, the hub (Brain cockpit). Folded, only the icon shows; on phones it sits in the drawer. Moving between apps
  needs no new login (one Access application). Each item carries an empty `.ds-count[data-ds-apps-count="<key>"]`
  the page may fill (the cockpit puts the attention count there); a `ds-apps` event (`detail.apps`,
  `detail.current`) fires once it is drawn. A new app, a new address or a renamed app is a change to `apps.json`
  here, then every app re-copies it.
- **Page:** `.ds-head` = eyebrow (12 px uppercase accent: the app or the context) + h1 (the page's title) on the left, `.ds-facts` (label over mono value) on the
  right; then the filter bar (`.ds-filters`, v1.7) or tabs or a sticky toolbar (`.ds-sticky`: search, filters, chips, view switch); then content.
- **Grids:** `repeat(auto-fit|auto-fill, minmax(min(100%, N), 1fr))` with N = 170 (KPIs), 210–230 (tiles, forms),
  290 (cards), 320 (columns). Overview + side column: `minmax(0, 1fr) 300px`, one column under 900 px.
- **Breakpoints:** 600–640 (two KPIs per row, stacked rows), 700 (tables → cards, smaller maps), 860 (menu),
  900–1000 (side columns stack). Use `min-width: 0` on grid children so tables scroll in their frame, not the page.
- **Context palette:** a page about one context may retint the accent family and the icon fills with
  `<html data-palette="…">` (Camp de Base: polar, forest, mountain, desert, ocean). The side menu keeps the neutral
  palette. A palette defines light and dark values and passes the contrast check below.

## What every app must have
- [ ] The shell above: side menu with the app's mark and name, its sections with their icons, fold button (state kept),
      phone top bar and drawer.
- [ ] The app switcher (v1.9) under the brand, from the brain's `apps.json`.
- [ ] The theme switch (Auto · Light · Dark) at the bottom left of the side menu, set before the first paint.
- [ ] Sign out at the bottom left, under the theme switch (the app's own sign-out: Supabase, Cloudflare Access
      `/cdn-cgi/access/logout`…); hidden only where there is nothing to sign out of.
- [ ] Its own brand mark (below) in the side menu, the phone top bar's place and the favicon (32 and 180 px PNG + SVG).
- [ ] Empty, loading and error states on every screen (`.ds-empty`, `.ds-loading`, `.ds-note.ds-bad` + retry).

## Brand marks
Each app has its own mark, drawn in Camp de Base's faceted style: 100 × 100, 3 to 5 facets in the icon palette (sky
`#7397b3`, slate `#5a768b`, snow `#f3f3f0`, stone `#a9aaad`), a 5.2 dark outline (`#131313`), light from the
top-left. Camp de Base keeps the mountain (`brand/mark.png`), Sport data has the stopwatch, Finance a coin stack. The
mark lives in the app's repo, as `brand/<app>-mark.svg` or `brand/mark.svg` under the app's web root (`web/brand/…`,
`app/brand/…`; both names are fine, v1.5), and is also the favicon.

## Components (`tokens.css`)
| Component | Class | Rules |
|---|---|---|
| Button | `.ds-btn`, `.ds-btn.ds-btn--primary`, `--sm`, `--danger` | as Camp de Base's `.btn`: padding 8×13 (no fixed height), radius 8 (primary 2), 14 px regular; `--sm` 4×8, 12.5 px, radius 6. Modifiers are written with the base class (`.ds-btn.ds-btn--sm`), the weight of Camp de Base's `.btn.sm`. No rule on icons inside: a glyph in a button gets its size and stroke from the app. One primary per view |
| Icon button | `.ds-icon-btn` | 36×36, always with `aria-label` and `title` |
| Segmented / theme switch | `.ds-seg` + `aria-pressed` | pill; pressed = inverted. Theme: Auto · Light · Dark glyphs |
| Tabs / sub-tabs | `.ds-tabs` (buttons with `aria-selected`, or links with `aria-current="page"`, v1.5), `.ds-subtabs` | tabs in Syne 15 with a 3 px accent underline; link tabs for routes (same look); sub-tabs as pills, scroll sideways on phones |
| Filter chips | `.ds-chips > .ds-chip` (`aria-pressed`, optional `.num`) | 999 radius, 13 px; pressed = inverted |
| Filter bar (v1.7) | `.ds-filters` > `button.ds-btn.ds-filters-toggle[data-ds-filters-toggle]` (filter glyph, « Filters », `.ds-fcount`) + `.ds-filters-body` > `.ds-filter` (`.ds-filter-l` label + a `select.ds-input`, a `.ds-seg` or `.ds-chips`) … + `button.ds-btn.ds-btn--sm.ds-filters-reset` « Clear filters » | Camp de Base's toolbar (its « Filters » button with a count, « Clear filters »). Right under `.ds-head`, before the KPIs: the page's relevant filters only, **Period first**. Selects for long lists (period, sport, source), `.ds-seg` for 2–5 short choices. A filter away from its default gets `data-on` (accent border and soft fill on its field, accent label); the count and the reset show only then; the reset puts every filter of the page back. Under 700 px the controls fold behind the Filters button (`shell.js` toggles `aria-expanded` and `.ds-filters--open`) and stack full width, fields at 16 px. Filters are state, not text: keep them in the URL (hash or query) so a reload or a link keeps them; a shared filter (the period) keeps its value across pages. Every chart, KPI and table on the page follows them; a filter that leaves nothing shows the empty state (`.ds-empty--inline` « Nothing for these filters »), never a blank chart; KPI comparisons use the previous period of the same length. **Folded variant** (v1.7.1) `.ds-filters.ds-filters--fold`, Camp de Base's inventory toolbar: the Filters button sits in the main toolbar row (search, scope, sort, view) and shows on every screen; the controls wait on their own row (`.ds-filters-body`) until it is pressed and stay open while one is on; bare selects whose first option names them (« All activities », no label and no `data-on` highlight: the count carries it); « Clear filters » at the end of that row, shown with it; no panel on phones; the page's own empty state may stay (« No matching item · Change the search or remove a filter ») |
| Status pill | `.ds-pill.ds-ok|warn|bad|info` | dot + word; never colour alone; no tone = neutral (muted on sunken). A pill inherits the font (Camp de Base's `.pill`); inside a mono cell add `.ds-pill--body` (v1.5) |
| Tag, Soon badge | `.ds-tag`, `.ds-soon` | 11 px; source tags in info, gaps in warn |
| Panel, card, KPI | `.ds-panel`, `.ds-card`, `.ds-kpis > .ds-kpi (.k .v .s)` | radius 10; a whole clickable card is a `button` or `a` with `.ds-card` |
| Note | `.ds-note` (+ `.ds-warn`, `.ds-bad`) | explanation with a 3 px accent bar, 12 px below (Camp de Base's `.infobox`); a warning or error is a tinted box without border (`.warnbox`) |
| Meter, track | `.ds-meter > i`, `.ds-track > i` | 6 px progress (ok green as on Camp de Base, `.ds-over` = bad); 14 px stacked bar |
| Table | `.ds-table-wrap > table.ds-table` | sunken head (not sticky), 11 px uppercase; numbers right-aligned in mono (`.n`, tabular figures in the head too); group rows `tr.ds-grp` in Syne; subtotal and total rows `tr.ds-total` (sunken in light, lifted towards ink in dark (v1.5.1), bold, numbers stay mono, v1.5); clickable rows `tr[data-href]`; `table.ds-table.ds-table--matrix` for year matrices and comparisons (v1.5): never turned into cards, scrolls sideways in its frame with the first column kept in view (an app's card rules target `table.ds-table:not(.ds-table--matrix)`). Rules sit under `:where(.ds-table)`: they weigh what Camp de Base's bare `table`/`th`/`td` did, so an app's own table rules still win |
| Form | `.ds-form` (labels wrap inputs), `.ds-input`, `.ds-switch`, `.ds-search` | label 13 px muted above the field; fields 7×9, radius 7; a visible file input is compacted to the same height (v1.5.1); switch 34×20 (14 px travel, whole switch clickable, disabled at .4); `.missing` = warn |
| Dialog, sheet | `dialog.ds-dialog > .ds-dialog-body + .ds-dialog-foot`, `.ds-sheet` | dialog ≤ 640 px; detail views open as a right sheet (≤ 760 px), full screen on phones |
| Toast | `.ds-toast` (`.ds-err`) | bottom centre, inverted; errors in bad |
| Full screen (v1.6) | `button.ds-fs-btn[data-ds-fs]` in the card header (`.ds-fs-btn--over` on a map), card `.ds-full` (`[data-ds-fs-card]` or the closest `.ds-panel` / `.ds-card`) | every chart and map card has one (Camp de Base's map button): 32 px glyph button at the right of the title, `aria-label="Full screen"`, `aria-pressed`, both glyphs inside (`span.ds-fs-enter` `fullscreen`, `span.ds-fs-exit` `exit_fullscreen`, shown by `aria-pressed`). `shell.js` puts the card in full screen (v1.6.1, as in Camp de Base: a **map** card, its button `--over`, covers the whole window edge to edge, z 50, over the side menu, under toasts; **any other card** fills the content area, from the side menu's edge, and stays under the menu, never over it), asks the browser for full screen when allowed (refused in iframes and on iPhones: the card still fills the frame), exits on Esc, the button or the browser leaving full screen, then fires `ds-fullscreen` (`detail.on`, `detail.settled`) on the card twice (at once, then after 450 ms) and a window `resize`: **the app redraws its chart at the new size** (width and height; the drawing area is `.ds-chart` or `[data-ds-fs-grow]`, which takes the room left). Only classes and attributes change, so it also works inside a host page such as a claude.ai dashboard |
| Tooltip | `.ds-tip` for charts; native `title` elsewhere | inverted, mono 12 px |
| Help mark (v1.10) | `button.ds-help[data-ds-help="…"]` « ? » right after a chart card's title or a KPI label, `aria-label` = the same text, `title` for hover | 16 px circle, 10 px; a tap or click opens `.ds-help-pop` (inverted, 13 px body, ≤ 320 px) under it, Esc / tap elsewhere / scroll closes (`shell.js`). **Every chart and every KPI has one** (Aurélien, 2026-10-30): two or three short sentences for a beginner — what the figure is, how to read the chart (axes, colours, lines, what « good » looks like), jargon defined in the sentence. Apps keep the texts in one module keyed by id |
| Empty, loading, error | `.ds-empty` (dashed, title + one line + the action; inside a panel `.ds-empty.ds-empty--inline`: text only, body size, `strong` + `p` on one line, v1.5), `.ds-loading` ("Loading expeditions…" in place), `.ds-note.ds-bad` + retry | never a blank page; say what to do next |
| Login | `.ds-login` | full-screen surface: mark 84 px, app name, one line, one primary button, `.ds-err` line |

**Decided (v1.1):** Camp de Base renames its classes to the `ds-` names below and loads `ds.css`; no alias layer.
Camp de Base names → system names: `.side*` → `.ds-side*` (`.side-link.on` → `[aria-current=page]`), `.mtop` →
`.ds-mtop`, `.app` → `.ds-app`, `.wrap` → `.ds-wrap`, `main` → `.ds-main`, `.head/.eyebrow/.facts` → `.ds-head/…`,
`.btn.primary/.sm/.danger` → `.ds-btn--primary/--sm/--danger`, `.icon-btn` → `.ds-icon-btn`, `.theme`/`.seg` →
`.ds-seg`, `.tabs`/`.subtabs`/`.chips`/`.chip` → `ds-` same, `.pill.s-*` → `.ds-pill.ds-ok|warn|bad|info`, `.tag` →
`.ds-tag`, `.panel/.ecard/.kpis/.kpi` → `.ds-panel/.ds-card/.ds-kpis/.ds-kpi`, `.warnbox`/`.infobox` → `.ds-note`,
`.meter`/`.track` → `.ds-meter`/`.ds-track`, `.tw` + `table` → `.ds-table-wrap` + `.ds-table`, `.form` →
`.ds-form`, `dialog`/`.dlg` → `dialog.ds-dialog`/`.ds-dialog-body`, `.toast` → `.ds-toast`, `.rt-tip` → `.ds-tip`,
`.empty` → `.ds-empty`, `.login` → `.ds-login`, `.sc2-switch` → `.ds-switch`, `.legend` → `.ds-legend`,
`html[data-biome]` → `html[data-palette]`; also `.tools` → `.ds-toolbar`, `.cards`/`.cols` → `.ds-cards`/`.ds-cols`,
`.dlg-foot` → `.ds-dialog-foot`, `tr.grp` → `tr.ds-grp`, `.soon`/`.cnt` → `.ds-soon`/`.ds-count`, `.warnbox(.bad)` →
`.ds-note.ds-warn` (`.ds-bad`), `.tag.src|warn|ok` → `.ds-tag.ds-info|warn|ok`, `.meter.over` → `.ds-meter.ds-over`,
`.toast.err` → `.ds-toast.ds-err`, `.pill.s-<status>` → `.ds-pill.ds-<tone>`. Tokens keep the same names. Done in Camp de Base
on 2026-10-29 (v1.4), with no visible change.

## Dark mode
Default follows the device (`prefers-color-scheme`); `<html data-theme="light|dark">` forces one. The switch has three
states (Auto, Light, Dark) stored as `<app>.theme` in `localStorage`; Auto removes the attribute. Set it before the
first paint, in `<head>`:
```html
<script>try{const t=localStorage.getItem("APP.theme");if(t&&t!=="auto")document.documentElement.dataset.theme=t}catch{}</script>
```
Photos and product thumbs sit on white (`#fff`) in both themes; icon outlines stay dark in both (like the logo on a
dark background).

## Data viz
- **Every chart, diagram and map can go full screen** (v1.6, Full screen above): a `.ds-fs-btn` in its card header, and a
  drawing that reads its size when drawn and redraws on `ds-fullscreen`.
  Camp de Base's charts use their own "view larger" instead (a corner button on the chart; a copy of the chart fitted to
  the content area, texts kept legible, legend below; Esc or a click outside closes): same rule, never over the side menu.
- **Maps stay behind the shell** (v1.6.2): a map (`.ds-map`, a Leaflet container) and the card that holds it make their
  own stacking context (`isolation: isolate`, in `tokens.css`; Camp de Base's `.rt-map-wrap`, `.wm-wrap`), so Leaflet's
  layers (z 400–1000) and the map's overlays scroll under the side menu, the phone top bar and the drawer. An app whose
  map wrapper is not one of those classes adds `position: relative; z-index: 0; isolation: isolate` to it.
- Charts are hand-made SVG (no chart library by default) inside `.ds-chart`; axis text 11 px mono muted; axes and
  grid in `--line`; a chart scrolls sideways under its minimum width (640 px for time series).
- Series take `--c1`…`--c6` in order; "other" is `--c-other`. They are the hues of Camp de Base's expedition charts
  (v1.1): `--c1` accent blue (plan and main series), `--c2` slate (`--c-gear`), `--c3` orange (`--c-food`), `--c4`
  amber (`--c-fuel`) from the expedition load chart (`expeditions.js`, `camp.css`), `--c5` green (good weather,
  `simulation.js`), `--c6` red (deadlines on the expedition calendar), `--c-other` the rest grey (`simulation.js`).
  Dark variants are the same hues lightened just enough for contrast on `--surface`. **No purple**, and no hue Camp de
  Base doesn't use. **Seven or eight series** (v1.5): add `--c7` ocean teal and `--c8` desert earth (the hues of Camp
  de Base's ocean and desert palettes), each ≥ 3:1 on `--bg`, `--surface` and `--sunken` in both themes (light 3.7–5.6,
  dark 6.7–8.8). Where red would read as "bad" (wealth, allocations, budgets that are not over), skip `--c6` and use
  `--c7`, `--c8` instead. **Up to twelve series** (v1.8, Sport data's water and air sports): `--c9` deep ocean (Camp de
  Base's ocean slate), `--c10` olive (between its forest and desert palettes), `--c11` deep forest (its forest palette),
  `--c12` granite (its mountain palette), each ≥ 3:1 on `--bg`, `--surface` and `--sunken` (light 4.3–9.3, dark
  8.9–10.7) and at least ΔE 17 from every other series in both themes; take them after `--c8`, by meaning where one
  fits. Beyond twelve, reuse with a dash pattern or a label. Never red, never purple. Status bars use the
  status tokens (ok, info, warn, bad). The same thing has the same colour on every chart of an app; an app may map
  its own things onto the tokens by meaning (Sport: run `--c1`, swim `--c2`, ride `--c3`, strength `--c4`, hike `--c5`, pulling tires `--c8`, kitesurf `--c9`,
  paragliding `--c10`, dive `--c11`, surf `--c12`).
- Plan vs actual: plan = muted dashed (`5 4`); actual = solid 2–2.5 px accent line with an `--accent-soft` area;
  alternative = dotted (`1.5 5`). Today or the cursor = a 1.5 px `--ink` line; hover value in a `.ds-tip`.
- Bars: 6–14 px high, radius 3, on a `--sunken` track; legends with 10 px squares (radius 2). Big numbers above the
  chart, in mono, with the unit small and muted (`1 240 <small>km</small>`).
- Every chart and KPI carries a help mark (`.ds-help`, Components): what it shows and how to read it, for a non-specialist.
- Label directly when there are ≤ 4 series; otherwise a legend. Never rely on colour alone: add the value, a dash
  pattern or a label.

## Icons
Two kinds. **Faceted icons** (the kit) for things, sections, categories, statuses and weather. **Glyphs** (plain
24 px line drawings, stroke 2, `currentColor`) for controls: menu, close, search, filter, edit, prev/next, view,
full screen, theme.

Style of a faceted icon, drawn like the mountain mark:
- 24 × 24 grid; shapes kept inside 2–22; geometric facets with straight edges, rounded joins.
- **2 to 4 main facets**, filled with palette roles: `a` sky `#5b8fc0` (the lit, coloured face), `b` slate
  `#3e5d75` (shadow, depth), `c` snow `#ffffff` (the main body), `d` stone `#9ea2ab` (the side in shade). Small parts
  (wheels, windows) may add up to 7 in total; above that, simplify.
- **Light from the top-left:** faces towards top-left are snow or sky, faces towards bottom-right stone or slate.
- **Outline 1.3, always dark** (`--ci-ink`), in both themes; detail lines 1.3 with round caps: on a facet they are dark,
  free-standing they take the text colour.
- **Legible at 16 px:** one idea per icon, no text, no detail thinner than the outline gap; check the sheet at 16,
  24 and 48 px in both themes.
- A fixed `#rrggbb` fill only for a meaning colour (a red flag); `!#rrggbb` flat fills only for illustrations
  (Camp de Base's biome badges), never in UI rows.

Use: load `icons.js` on every page, write `:ci-name:` in any text (side links, labels, table cells, data) and it
renders as the icon (stripped from `<option>`, `<title>` and attributes); in code, through the global set with
`--global` (`SportIcons`, default `AppIcons`): `.svg("calendar")`, `.svgAt("start", x, y, 16)` inside an SVG
drawing, `.glyph("search")`. Sizes: 1.25 em inline, 20 px in
menus (`.ico`), 28 px in card headers. Icons are `aria-hidden`; the text next to them carries the meaning.

**The starter set** (`icons/icons.json`): navigation and sections (home, dashboard `tower`, calendar, map, document,
folder, book, team, partners, budget, accounts, content, cart, kit, weight, other), objects and actions (link, photo,
repair, visible, review, location, position, gps, checkpoint), markers (start, finish, milestone, deadline, hazard,
star), weather (`wx_fine` → `wx_good` → `wx_windy` → `wx_storm`, cloudy, snowcloud, storm, cold, hot, temperate,
night, seasons), travel (travel, flight, train, bus, car, taxi, boat, lodging, bed), sport and food (training, bike,
cycling, foot, trek, water, drink, meal, breakfast, lunch, dinner, snack, nutrition, rest, sleep, first_aid,
morale1–5). Camp de Base keeps its expedition icons (skis, sled, crevasse, biomes…) in its own repo.

**An app adds its own icons** in `data/icons.app.json` (same format, English `label`), drawn by the rules above,
and builds one file with the kit first:
```bash
python3 <brain>/skills/web-design-system/icons/build_icons.py \
  --src <brain>/skills/web-design-system/icons/icons.json --src data/icons.app.json \
  --global SportIcons --out web/icons.js --sheet /tmp/icons.html     # then the app's asset stamp, if any
```
App glyphs (plain UI controls the kit lacks) go the same way: `--glyphs <kit>/glyphs.json --glyphs data/glyphs.app.json`
(repeatable, later files add or override). `--check` validates only; `--emoji map.json` replaces leftover emojis while migrating. An icon that would be useful
to every app (not domain-specific) goes into the kit's `icons.json` through the feedback loop, not only the app's file.

## Accessibility
- Contrast AA everywhere: body and muted text ≥ 4.5:1 on `--bg`, `--surface` and `--sunken` (the tokens pass: muted
  4.9–5.5 light, 6.8–7.4 dark; each status on its soft ≥ 4.5). A new token or palette is checked before merging.
- Focus: `:focus-visible` 2 px `--focus` ring, offset 2; never `outline: none` without a replacement.
- Real elements: buttons for actions, links for navigation; state in `aria-pressed`, `aria-selected`,
  `aria-current`, `aria-expanded`; icon-only buttons have `aria-label`.
- Controls about 36–40 px high as on Camp de Base (44 px on field screens); chips and small buttons only in dense toolbars; inputs 16 px on
  phones (no zoom on focus); safe-area insets on fixed bars.
- Status and series never by colour alone; `prefers-reduced-motion` honoured.

## Feedback loop
Aurélien's feedback on UI, UX, colours, layout, icons or look and feel, in any app session, becomes a durable
improvement of this system, not only a local fix:
1. **General** (it would apply to every app: a token, a component, a spacing, an icon rule) → change this skill in
   `ac-ua/brain` through a PR from a cloud session (`tokens.css`, `SKILL.md`, `icons/`), add a line to
   [`FEEDBACK.md`](FEEDBACK.md) (date, app, feedback, what changed, apps to adopt), and fix the app in the same
   session by adopting the new version.
2. **App-specific** (its data, its domain icons, its own screens) → fix it in the app and note it in the app's repo
   (changelog or `docs/`), with a line saying why it is not general.
3. **Cannot push to `ac-ua/brain`** (work Mac) → a Brain Inbox row: Type `skill change`, Domain Brain, mentioning
   `web-design-system`, the app and the exact change.
When unsure, treat it as general and say so in the recap. An app that is behind `FEEDBACK.md` adopts the pending lines
at its next release (`release-webapp` UI check).

## How an app adopts it
- [ ] Copy `tokens.css` to `web/ds.css` (keep the header; note the system version from `FEEDBACK.md` in the app's
      `docs/`), load it first; load the three fonts; the app's own mark and favicon (Brand marks).
- [ ] Build `icons.js` from the kit (plus `data/icons.app.json` for domain icons) with the app's global name; load it
      on every page; no emojis left in the UI.
- [ ] Use the shell (side menu with fold, top bar and drawer on phones, theme switch with the pre-paint script, sign
      out; copy `shell.js` and `apps.json`, v1.9) and the `ds-` components;
      the app's CSS adds only what is specific, with its own prefix, and uses tokens only (no hex outside icons).
- [ ] Charts follow the data-viz rules; empty, loading and error states exist on every screen.
- [ ] Check both themes, 375 px and 1280 px wide, keyboard focus, contrast; record the adoption (version) in the
      app's ledger (`config-guide`) and in `FEEDBACK.md` when a pending line is closed.
