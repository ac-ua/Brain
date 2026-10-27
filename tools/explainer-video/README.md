# explainer-video: reference episode

The skill now lives in [`skills/explainer-video/`](../../skills/explainer-video/SKILL.md) (method, generalised
scripts, lessons). This folder keeps the source of the "Le Brain" episode (French, 14:33, two voices, 16 slides) as a
worked example of a full episode.

| File | What |
|---|---|
| `episode.py` | slides (HTML with progressive reveal, `data-s` steps) and the two-voice script |
| `build.py` | the original one-off build, with the work Mac's paths hard-coded |
| `out/script.md`, `out/brain-podcast.srt` | script and subtitles of the published episode (MP4/MP3 not in the repo) |

To rebuild or adapt it, use the skill's builder, not `build.py` here: copy `episode.py`, add `NAME`, `SPEAKERS`
(`{"V": ("Vivienne", "fr-FR-VivienneMultilingualNeural"), "R": ("Rémy", "fr-FR-RemyMultilingualNeural")}`) and
`PRONOUNCE` (see `skills/explainer-video/scripts/episode_template.py`), then run
`python3 skills/explainer-video/scripts/build.py <episode>.py --out <folder>`.
