# web-design-system · feedback and changes

Every general piece of design feedback from Aurélien lands here (rule: `SKILL.md` › Feedback loop). Newest first.
Each line: date · app where it was said · the feedback in his words (short) · what changed in the system · apps that
still have to adopt it. When an app adopts a line, strike its name (`~~Sport~~`) and note its release.

Version = the latest line's version; an app records the version it runs in its own `docs/`.

| Version | Date | App | Feedback | What changed | Apps to adopt |
|---|---|---|---|---|---|
| v1.0 | 2026-10-29 | all | "Every app shares one design system; Camp de Base is the reference." | System extracted from Camp de Base: tokens (light, dark, context palettes), shell, `ds-` components, data-viz rules, faceted icon kit (73 icons, 16 glyphs). Unified Camp de Base's drift: one button radius (8 px, the primary was 2 px in `camp.css`), one control height (36 px), table heads 11 px `.08em`, status colours as tokens instead of hex (login error, calendar kinds, avatars, pins), unused fonts dropped (Saira Condensed, IBM Plex Sans), categorical series `--c1`…`--c7` (new dark purple `#b48ad6`). | Camp de Base (rename to `ds-` classes at a quiet release, or alias), Sport data, Element Logbook, Finance (first UI), website (fonts and colours only) |
