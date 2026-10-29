# explainer-video: lessons

From the episodes made so far: "Le Brain" (French, 14:33, 16 slides, the reference in `tools/explainer-video/`), a
28-minute French interview-prep podcast, and client explainers made on the work Mac.

## Script
- **Two roles, unequal.** The host asks short questions, reacts and sums up ("Donc, le problème…"); the expert does
  most of the talking. One expert line = one idea = one reveal step. Lines of 1–3 sentences.
- **Write for the ear.** Numbers in words where the voice stumbles ("deux mille vingt-sept"); file names spelled the
  way they should sound ("agents point M D", "intervals point i c u"); no parentheses, no lists read aloud.
- **Chapters.** Cover → one chapter per question the listener has → recap of 3–5 sentences. Each chapter ends on a
  takeaway the host repeats. 10–15 minutes is the default; longer (the 28-minute interview prep) suits one listener
  preparing for something, with a short recap per chapter.
- **The listener by name** ("Aurélien n'avait pas bien compris…") makes a personal explainer land; drop it for anything
  shared.
- **Facts only from the sources.** The script is checked against the source documents before any audio is generated:
  audio is the slow step to redo.

## Slides
- One slide per chapter, revealed in 3–6 steps; the slide never shows something the voice hasn't reached yet.
- Highlight (`data-on`) and dim (`data-dim`) work better than new slides for tables and matrices.
- Big type: nothing under ~26 px at 1920×1080; 3–6 items per slide. The footer shows the episode and `n / total`.
- Fonts come from Google Fonts; the 4 s virtual-time budget lets them load. Offline, the fallbacks (Georgia, Helvetica,
  Menlo) still render cleanly.
- Check 2–3 frames visually before generating audio.

## Voices
- Stock edge-tts voices: French `fr-FR-VivienneMultilingualNeural` (host) and `fr-FR-RemyMultilingualNeural` (expert);
  English `en-US-AvaMultilingualNeural` and `en-US-AndrewMultilingualNeural`. Rate `+4%`.
- Pronunciation dictionary (`PRONOUNCE`) is applied to the voice only; subtitles and `script.md` keep the real spelling.
  French: "UnifyApps" → "Iou-ni-faï Apps". Add an entry only after listening to a test clip; brand names and
  acronyms are the usual offenders.
- Some clips come back empty or cut mid-sentence (network hiccups, rate limiting). Normal speech is about 20 characters
  per second; the `check` step flags clips outside 11–30 chars/s or under 2 kB and regenerates them. Two parallel
  requests at most.
- edge-tts needs a direct WebSocket to Microsoft's speech service: it fails behind proxies that block WebSocket
  upgrades (some cloud sandboxes). Frames and assembly still run there; generate the audio elsewhere.

## Build
- On macOS, headless Google Chrome hangs on `--screenshot`: use Playwright's `chrome-headless-shell`
  (`pip install playwright && playwright install chromium-headless-shell`). On Linux, either works.
- Every step is idempotent (existing frames and clips are reused): fix one line, delete its clip, rebuild.
- Subtitles are timed per sentence, in proportion to its length within the clip; good enough for a podcast, not for
  karaoke. They are muxed as a soft track (`mov_text`) and also delivered as `.srt`.
- Audio is loudness-normalised (−16 LUFS) for the MP3 and the MP4.

## Delivery
- Deliver all four: MP4 (with subtitles), MP3 (to listen on the move), SRT, `script.md` (to read or quote).
- Personal episodes: outputs to the personal Drive or a Notion page; the episode source can live in a project repo.
  Pro episodes: everything stays in the work Drive, built on the work Mac.

## From the October 2026 audit (12+ episodes, pro and personal)
- **Say which box you mean.** On diagrams and app screens, listeners lose track without a pointer: `data-pointer`.
- **Length is a brief item, not an outcome.** A 3:35 episode on a solution change felt too shallow; ask the target
  and the depth up front.
- **Answer his questions.** An episode about a plan missed a point Aurélien had raised (cloud environments): list his
  questions and map each to a chapter before audio.
- **Real visuals win.** A game-strategy episode had to be re-rendered with real card and board images; download
  them into the episode folder, never link.
- **Check rules and facts from the web twice.** A wrong game rule slipped in from a single source.
- **Files over 30 MiB can't be sent in chat** (47 and 37.6 MB failures): `compress`.
- **Never the cloned voice for work**, even when the clone skill is on the machine.
