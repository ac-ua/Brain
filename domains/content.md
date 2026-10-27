# Domain: Content

Aurélien's personal content: short-form video first (TikTok, Instagram), expedition films, posts, the personal website,
explainers and podcasts. Notion context card: not migrated yet (Expeditions + Content migration).

## Where things live
| What | Where |
|---|---|
| Footage | personal Google Drive, ~200 GB. Target layout: `40_Content/Rushes/<year>-<event>`, `Projects`, `Exports` |
| Personal website | repo `ac-ua/website` (Astro, Cloudflare Pages), `aureliencaye.com` |
| Explainer / podcast kit | `tools/explainer-video/` in this repo |
| Content databases (planned) | Rushes catalog, Editorial calendar, Published posts — created at migration |

## How each capability applies
**content-studio — strategy first.** The first job is the content strategy: audiences, 3–5 pillars (expeditions,
training, the build-in-public of his tools…), formats, cadence (several posts a week, possibly one a day on TikTok),
and the Notion databases to run it. Aurélien publishes by hand at first.

**content-studio — production.** Scripts, hooks and captions are drafted freely. Video: the AI indexes footage,
picks moments, writes the script and produces a rough cut (FCPXML / OTIO); Aurélien finishes in DaVinci Resolve (free,
on Mac or iPad). Large-scale indexing waits for a real machine (Mac mini, open decision); until then, small test batches.
Narration: stock TTS voice; French TTS respells "UnifyApps" as "Iou-ni-faï Apps" (subtitles keep the spelling).
TTS clips can come back empty or truncated: check characters per second (~20 is normal) and regenerate outliers.

**builder — website.** Same release rules as any web app (`build-webapp`). The site still announces the South Pole
for November 2026; the expedition moved to November 2027 (fix at the next website change).

## Rules
- Nothing is published without Aurélien.
- The cloned voice is used only on his explicit request.
- Footage of other people: check consent before it goes into a public cut.

## TODO(Aurélien)
- Which accounts (TikTok, Instagram handles) and which first pillar to test.
- Where finished exports live and who uploads.
