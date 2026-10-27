# explainer-video kit

Build kit of the "Le Brain" explainer podcast (14:34, French, two voices), kept as raw material for a future
`explainer-video` skill (Build Roadmap: "Explainer video / podcast skill"). Not a skill yet.

| File | What |
|---|---|
| `episode.py` | slides (HTML with progressive reveal, `data-s` steps) and the two-voice script |
| `build.py` | frames (headless Chrome), voices (edge-tts), assembly (ffmpeg): `python3 build.py [frames\|audio\|video\|all]` |
| `out/script.md`, `out/brain-podcast.srt` | script and subtitles of the published episode (MP4/MP3 not in the repo) |

Paths in `build.py` (ffmpeg, Playwright `chrome-headless-shell`) are the work Mac's; adapt them per machine.

Lessons to keep in the skill:
- Stock voices (`fr-FR-VivienneMultilingualNeural`, `fr-FR-RemyMultilingualNeural`); the cloned voice only on request.
- Pronunciation dictionary applied to the voice only (`PRONOUNCE`); subtitles keep the real spelling.
- Check every clip: characters per second ≈ 20; regenerate empty or truncated clips.
- On the work Mac, headless Google Chrome hangs: use Playwright's `chrome-headless-shell`.
