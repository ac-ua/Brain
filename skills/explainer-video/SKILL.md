---
name: explainer-video
description: Make a narrated explainer video in podcast mode with visuals — two stock voices (host + expert) over progressive-reveal slides, delivered as MP4 with subtitles, MP3, SRT and script. Use when Aurélien asks for an explainer video, a podcast with visuals, "fais-moi un podcast", "une vidéo explicative", "explique-moi X en podcast", an account explainer or an onboarding explainer, personal or for work.
---

# explainer-video

Two voices talk a listener through a topic while slides reveal step by step in sync. Reference episode: "Le Brain"
(French, 14:33) in `tools/explainer-video/`. Lessons from past episodes: [`references/lessons.md`](references/lessons.md).

```
scripts/
  build.py              frames (headless Chromium) → voices (edge-tts) → check → assembly (ffmpeg)
  episode_template.py   copy per episode: metadata, voices, pronunciation dictionary, slides and script
  theme.css             default 1920×1080 theme (cover, stats, layers, tree, matrix, flow, timeline, recap…)
```

## Where it runs
| Material | Session | Episode source and outputs |
|---|---|---|
| Personal topic | cloud session (`perso-general`) or any Mac | personal Drive, Notion, or a project repo |
| Client or pro material | **local session on the work Mac** | **work Drive only**; never moved to personal storage |

Nothing personal goes into a pro episode (no other domains, no personal names or projects). Only generic lessons
come back to the brain, through the Brain Inbox.

Publishing, posting or sending an episode to anyone always needs Aurélien.

## Setup
- `ffmpeg` on PATH (or `FFMPEG=/path/to/ffmpeg`).
- `pip install edge-tts playwright && playwright install chromium-headless-shell` (or `CHROME=/path/to/chromium`).
  On macOS use `chrome-headless-shell`: headless Google Chrome hangs.
- edge-tts needs a direct WebSocket to Microsoft's speech service; where a proxy blocks it, build frames and video
  there and generate the audio on another machine.

## Modes
| Mode | When | How |
|---|---|---|
| **Slides** (default) | explain a topic, a plan, a change | progressive-reveal slides (§3) |
| **Document** | walk through a doc, a blueprint, a guide ("explique-moi ce doc") | the document as HTML or page images in a `.doc-wrap`; `scroll=[…]` moves it to the passage being discussed, `data-pointer` rings the paragraph or box |
| **Diagram / app screens** | "show which box we're talking about" | screenshots or the diagram as the slide body; `data-pointer="n"` puts a ring + cursor on the box at step n |
| **Live app recording** | a real click-through of a running app | not this skill: on the work Mac use the team plugin's `demo-studio`; personal apps: `video-edit` over a screen recording |

## 1. Brief
Ask once, then go: topic and sources · listener (Aurélien, a client team, a new hire) · language (FR/EN) · **target
length** (10–15 min default; say the number back, then plan the chapters to it: ~150 spoken words a minute) · depth
(overview or detailed: "3:35 was too shallow" was a real complaint) · what the listener must be able to do or explain
afterwards · the questions Aurélien raised that the episode must answer. Read the sources; take facts only from them,
mark gaps `TODO(Aurélien)` in the script rather than inventing.

**No source files (a game, a product, a public topic)?** Research on the web, keep each fact with its source, and
cross-check rules, numbers and names against a second source before they go into the script. Visuals: download the
real images (screenshots, product shots, cards, maps) into `<out>/img/` and embed them; never hot-link.

## 2. Script (two voices, chapters)
- **Host** (`V`, Vivienne / Ava) asks, reacts, sums up. **Expert** (`R`, Rémy / Andrew) explains.
- Cover → one chapter per question the listener has → recap (3–5 sentences to remember).
- One expert line = one idea = one reveal step. 1–3 sentences per line, written for the ear (numbers and file names
  as they should sound).
- Share the chapter plan and script (as `script.md` or in chat) for a quick read before audio, when time allows:
  audio is the slow part to redo.
- **Before audio, check the script against the brief:** every question Aurélien raised is answered somewhere (list
  them with the chapter that answers each); the planned length is within ±20%; every fact traces to a source.

## 3. Slides (progressive reveal)
Copy `scripts/episode_template.py` to the output folder as `<name>.py` and fill it. Each slide is an HTML body using
the theme classes; reveal is driven by attributes:

| Attribute | Effect |
|---|---|
| `data-s="n"` | appears at step n |
| `data-on="n"` | highlighted from step n |
| `data-dim="n"` | dimmed from step n |
| `data-pointer="n m"` | ring + cursor at steps n and m only ("this box here") |
| slide `scroll=[0, 0, 420]` | document mode: the `.doc` scrolls to that offset (px) at each step |

Each script line is `(speaker, step, text)`: the slide shows that step while the line is spoken. The theme covers
most layouts; add `EXTRA_CSS` for the rest. Render frames first and look at 2–3 of them.

## 4. Voices (stock only)
| Language | Host | Expert |
|---|---|---|
| French | `fr-FR-VivienneMultilingualNeural` | `fr-FR-RemyMultilingualNeural` |
| English | `en-US-AvaMultilingualNeural` | `en-US-AndrewMultilingualNeural` |

Stock voices always. The cloned voice only if Aurélien explicitly asks for it in this request, and **never for work
material**, even if a voice-clone skill (`say-as-me`) is installed on the machine. "La voix synthétique" means the
stock voice; if a request is ambiguous between stock and clone, make the stock version and offer the other.

**Pronunciation dictionary** (`PRONOUNCE` in the episode): respellings applied to the voice only; subtitles and
script keep the real spelling. French: `"UnifyApps": "Iou-ni-faï Apps"`. Add entries after listening to a test clip.

## 5. Build and check
```bash
B=<brain>/skills/explainer-video/scripts
python3 $B/build.py <name>.py --out <output folder> frames   # look at a few PNGs in <out>/build/frames
python3 $B/build.py <name>.py --out <output folder> audio
python3 $B/build.py <name>.py --out <output folder> check    # per-clip chars/sec, regenerates bad clips
python3 $B/build.py <name>.py --out <output folder> video
python3 $B/build.py <name>.py --out <output folder> compress   # <name>-small.mp4 under --max-mb (default 29)
# or: … all   (compresses automatically when the MP4 is over --max-mb)
```
- **Per-clip check:** normal speech is about 20 characters per second. `check` flags clips outside 11–30 chars/s or
  under 2 kB (empty or truncated) and regenerates them, up to 3 rounds; a clip still failing needs its text fixed.
- Steps are idempotent: to change one line, edit it, delete its clip (`build/audio/lSS_LL.*`) and run `audio`,
  `check`, `video` again. To change a slide, delete its frames (`build/frames/sSS_*.png`) and run `frames`, `video`:
  the audio is reused, so a visual fix takes a minute, not a re-recording.
- "Corrige mais ne régénère pas la vidéo": fix the source (script, slide, document) and stop; rebuild only when asked.
- Listen to the start, one middle chapter and the end before delivering.

## 6. Deliver
In the output folder: `<name>.mp4` (H.264, subtitles as a soft track), `<name>.mp3` (−16 LUFS), `<name>.srt`,
`script.md`, and `<name>-small.mp4` when the MP4 is over 29 MB (the chat file limit is 30 MiB; mail is ~25 MB).
The `build/` folder is disposable. Say the real length and how it compares with the target.
- Personal: link or upload to the personal Drive or the relevant Notion page; record the episode in Notion
  (Memories or the project page) if it matters later.
- Pro: leave it in the work Drive folder; tell Aurélien where it is.
- A way of working learned on the way → Brain Inbox (`brain-inbox`).

## Done when
The four outputs exist, every clip passed `check`, frames match the script, and Aurélien knows where they are.
Nothing is published or sent without him.
