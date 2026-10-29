---
name: unifyapps-format
description: "Fallback for UnifyApps-branded decks when the team plugin's unifyapps-brand-deck is not installed. Use this skill whenever the user wants to create, edit, or build any PowerPoint presentation, slide deck, or .pptx file. This skill produces presentations that follow the UnifyApps brand design system — using the official Sand-Gold-Green earth-tone palette, Spectral serif typography, and the luxury 'quiet intelligence' aesthetic — so any request for slides, a deck, a pitch, a status update, a QBR, a product brief, or any kind of presentation should use this skill. Also triggers for requests like 'make me a deck', 'put together some slides', 'build a presentation', or 'create a PowerPoint'. If the user mentions anything about slides or decks, use this skill even if they don't say PowerPoint explicitly."
---

# UnifyApps Branded PowerPoint Skill

> **Fallback.** When the team plugin is installed (`unifyapps`, skill `unifyapps-brand-deck`, Playbook v4), use that
> skill for slides: it is the team's current brand system and wins over this one. Use this skill only where the
> plugin isn't installed (claude.ai chats, Cowork, another machine). Either way, write the storyline first with
> `case-for-change` and follow its deck lessons.

This skill produces on-brand presentations using UnifyApps' official design system. The base PowerPoint mechanics (PptxGenJS API, editing XML, QA workflow) all come from the core `pptx` skill — read it first:

- **Creating from scratch** → Read the pptx skill's `pptxgenjs.md`
- **Editing an existing file** → Read the pptx skill's `editing.md`
- **QA (required after every build)** → Follow the QA section in the pptx skill's `SKILL.md`

Everything in the core pptx skill still applies — the QA steps, visual inspection, layout and typography advice — **except** where this skill overrides it. The core override: do NOT invent colors or fonts. Use the brand tokens defined below, always.

---

## Brand Philosophy

UnifyApps is **the world's first luxury software company**. The brand aesthetic is calm, considered, and nature-inspired — drawn from the desert (sand), the sunset beach (gold), and the jungle (deep green). Every slide should feel like a great hotel lobby: spacious, unhurried, deeply resolved.

**Tagline:** *Intelligence that compounds.*
**Founding belief:** Other platforms shout. Ours exhales.
**Product positioning:** Agentic Automation for the Enterprise — the horizontal AI operating system a CIO standardizes on.

This philosophy should directly shape slide design: generous white space, restrained element count, warm earthy tones, nothing that crowds or raises the pulse.

---

## Brand Design System

### Color Palette

The palette is rooted in three families — **Sand** (the earth, negative space), **Gold** (the sun, accents and warmth), and **Green** (the jungle, depth and dark backgrounds). There is no purple, no bright blue, no neon.

**Sand — the canvas**

| Token | Hex | When to use |
|---|---|---|
| Sand Tint 2 | `F7F3ED` | Primary slide background (light slides) |
| Sand Tint 1 | `EDE6D7` | Card fills, secondary background washes |
| Sand | `E3D8C2` | Dividers, borders, subtle texture |
| Sand Shade 1 | `C3B9A8` | Secondary text on light backgrounds, captions |
| Sand Shade 2 | `9D9687` | Muted labels, footnotes, axis text |

**Gold — the accent**

| Token | Hex | When to use |
|---|---|---|
| Gold Tint 2 | `C4B58C` | Light gold fills, tinted cards on dark slides |
| Gold Tint 1 | `A19164` | Secondary gold accents, eyebrow text on dark |
| Gold | `847347` | Primary accent — headlines on dark, key CTAs, logo color |
| Gold Shade 1 | `6A5A32` | Darker gold for contrast on light backgrounds |
| Gold Shade 2 | `4C4123` | Deep gold for strong emphasis |

**Green — the depth**

| Token | Hex | When to use |
|---|---|---|
| Green Tint 2 | `828750` | Lighter green accents, chart fills |
| Green Tint 1 | `4E582D` | Secondary green, table header tints |
| Green | `0F2805` | Primary dark background (covers, section breaks, closing) |
| Green Shade 1 | `002000` | Darker green panels |
| Green Shade 2 | `001700` | Deepest background shade |

**Text**

| Token | Hex | When to use |
|---|---|---|
| Dark text | `1A1A14` | Body text on light/sand backgrounds |
| Light text | `F7F3ED` | All text on dark/green backgrounds |
| Muted text | `9D9687` | Captions, footnotes, source lines |

**What to avoid**
- No purple of any shade — not `3414A4`, not any violet or lavender
- No bright blue (`1E90FF`, `4472C4`, etc.)
- No neon green (`12D965`) — use the forest greens above
- No pure white (`FFFFFF`) as a primary background — Sand Tint 2 is the light-side canvas

### Typography

**One font family: Spectral.** An elegant, refined serif designed for screen-first environments. We use it — and only it — for everything. Total discipline in one family is, itself, the luxury.

- **Primary font:** Spectral → fallback to `Georgia` if unavailable
- **Do not use:** Poppins, Inter, Calibri, Segoe UI, or any sans-serif font

**Type scale**

| Role | Font | Size | Weight | Use for |
|---|---|---|---|---|
| Headline 1 | Spectral | 52–60pt | Light (300) | Hero/cover title |
| Headline 2 | Spectral | 36–40pt | Light (300) | Section break title |
| Headline 3 | Spectral | 28–32pt | Regular (400) | Major slide title |
| Subheadline | Spectral | 20–24pt | Light Italic | Supporting subtitle, section label |
| Eyebrow | Spectral | 9–10pt | Regular, letter-spaced | Section tags (e.g. "T H E  C U R R E N T  S T A T E  O F  A I") |
| Body | Spectral | 12–14pt | Regular (400) | Slide body text |
| Data/table | Spectral | 11–12pt | Medium (500) | Tables, metrics, labels |
| Caption | Spectral | 9–10pt | Light (300) | Footnotes, source lines |

Headlines stay elegant through **lighter weights** — use Light (300) and Regular (400) at large sizes. Reserve Semibold (600) only for strong emphasis within body or table content, not for primary headlines. Leading at 120%. Let space do the work of emphasis.

In PptxGenJS: `fontFace: "Spectral"` (or `"Georgia"` as fallback).

**Eyebrow style:** Letter-spaced small caps in muted gold or sand — used to label sections above the main headline. Example: `"T H E  C U R R E N T  S T A T E  O F  A I"`

### Chart & Data Visualization Defaults

**Series color order**
1. `847347` — Gold
2. `0F2805` — Deep Green
3. `C4B58C` — Gold Tint 2
4. `4E582D` — Green Tint 1
5. `A19164` — Gold Tint 1
6. `828750` — Green Tint 2

**Axis / grid defaults**
- Grid lines: `E3D8C2`
- Axis labels: `9D9687`
- Chart background: `F7F3ED`

**Always set `chartColors` explicitly:**
```javascript
slide.addChart(pres.ChartType.bar, data, {
  chartColors: ["847347", "0F2805", "C4B58C", "4E582D", "A19164", "828750"],
});
```

### Layout & Spacing Defaults

| Element | Value |
|---|---|
| Light slide background | `F7F3ED` (Sand Tint 2) |
| Dark slide background | `0F2805` (Deep Green) |
| Slide margins | 0.6" minimum on all sides |
| Card background (light) | `EDE6D7` fill, `E3D8C2` 1px border |
| Accent color | `847347` (Gold) |
| Content gaps | 0.4" between blocks |

**What to avoid**
- No purple or blue of any kind
- No pure white backgrounds
- No drop-shadows on text
- No decorative full-width header/footer bars
- No underlines under titles
- No busy, cluttered layouts — each slide breathes
- No more than 3–4 visual elements per slide (brand principle: "consider the meaning of every mark")

---

## Slide Structures

### Title / Cover Slide
- Background: `0F2805` (Deep Green, full bleed)
- Eyebrow (optional): Spectral Regular 9pt, letter-spaced, `A19164`
- Title: Spectral Light 52–60pt, `F7F3ED`
- Subtitle / tagline: Spectral Light Italic 20–24pt, `C4B58C`
- Optional: Gold horizontal rule (`847347`, 1pt) under the title

### Section Divider Slide
- Background: `0F2805` or `002000`
- Section number: Spectral Light 60pt, `C4B58C`
- Section title: Spectral Light 36pt, `F7F3ED`
- Thin rule: `847347`, 1pt, under the section number
- Keep it sparse — one strong element per slide

### Content Slide (light — primary)
- Background: `F7F3ED`
- Eyebrow: Spectral Regular 9pt, letter-spaced, `9D9687`
- Title: Spectral Regular 28–32pt, `0F2805`
- Body: Spectral Regular 12–14pt, `1A1A14`
- Accent rule: `847347`, 1pt, under the title
- Cards: `EDE6D7` fill with `E3D8C2` 1px border

### Content Slide (dark — high-impact moments)
- Background: `0F2805`
- Title: Spectral Light 28–32pt, `F7F3ED`
- Body: Spectral Regular 12pt, `C4B58C`
- Accent: `847347` gold left border on callout boxes

### Metrics / Stats Slide
- Background: `F7F3ED`
- Large stat number: Spectral Light 56–64pt, `0F2805`
- Eyebrow label: Spectral Regular 9pt, letter-spaced, `9D9687`
- Delta / context: Spectral Regular 11pt, `847347` for positive
- Cards: `EDE6D7` fill, `E3D8C2` border

### Chart Slide
- Background: `F7F3ED`
- Title: Spectral Regular 28pt, `0F2805`
- Chart legend labels: Spectral Regular 10pt, `9D9687`
- Source / footnote: Spectral Light 9pt, `9D9687`, bottom-left

### RAG / Status Table Slide
- Background: `F7F3ED`
- Header row: `0F2805` fill, `F7F3ED` text
- Alternating rows: `F7F3ED` / `EDE6D7`
- For RAG status: gold/green tones preferred; if red is truly needed, flag it (the brand has no approved red)

### Closing / Thank You Slide
- Same as Cover: `0F2805` full bleed
- Large text: Spectral Light 40–48pt, `F7F3ED`
- URL / contact: Spectral Light Italic 18pt, `C4B58C`
- Tagline: *Intelligence that compounds.* — Spectral Light Italic 20pt, `A19164`

---

## Key Messaging (for sales/product decks)

- **Positioning:** "The horizontal AI operating system for the enterprise — the open, assembly-first platform that does the hard part of Enterprise AI the models can't."
- **The 80/20:** "The model is the easy part. The other 80% — knowledge, governance, actionability, workflows, apps and agents — is what makes AI deliver in production."
- **Key stats:** 11,000+ capabilities · 950+ connectors · up to 10× faster, cheaper & easier to build and maintain
- **The motion:** Lighthouse → flywheel. One use case in weeks, each one reuses the last.

---

## Important Reminders

1. **Always QA** — convert slides to images and run visual inspection per the core pptx skill's QA section.
2. **Font fallback** — if Spectral is unavailable, use Georgia. Note this in your response.
3. **No purple, ever** — the single biggest brand violation risk. If you find yourself typing `3414A4` or any violet, stop.
4. **Vary layouts** — deep green for covers, section breaks, and closing; sand for content.
5. **Restraint over decoration** — every element must earn its place. When in doubt, remove it.
6. **Text overflow is the #1 defect** — check every text box in QA.
