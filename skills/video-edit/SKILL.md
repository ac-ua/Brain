---
name: video-edit
description: Edit raw clips into a short video — reel, recap, short film — with ffmpeg and whisper - inventory, transcript of what is said, script and storyboard for Aurélien's OK, low-res preview, voice-over (stock voice by default), subtitles, HD render, and delivery. A starting point for the video pipeline. Use for "fais un montage", "monte une vidéo à partir de ces clips", a reel for Instagram or TikTok, a run-club or expedition recap, a voice-over on footage, or describing and indexing a batch of videos.
---

# video-edit

Starting point of the video pipeline (Content domain): rough cuts and short edits here; finishing in DaVinci Resolve
by Aurélien when needed (FCPXML / OTIO export is the next step to add). Tool setup per machine:
[`references/tooling.md`](references/tooling.md). Narrated slides are `explainer-video`, not this skill.

## 1. Brief (ask once)
Purpose and platform (Instagram reel 9:16 ≤ 60–90 s, TikTok, YouTube 16:9), length, tone (documentary, funny,
epic), voice-over or not and which voice (**stock by default**; his cloned voice only if he asks in this request),
music, brand or colour inserts, who appears (consent for a public cut), deadline. Ask for the **full-quality
clips** (Drive or AirDrop originals), not chat-compressed ones (480p).

## 2. Inventory and transcript
```bash
ffprobe -v error -show_entries format=duration:stream=width,height,r_frame_rate -of csv=p=0 <clip>   # each clip
ffmpeg -i <clip> -vf "select='gt(scene,0.35)',scale=480:-2" -vsync vfr frames/<clip>_%03d.jpg        # key frames
```
Transcribe speech with whisper (`mlx-whisper` on Apple silicon, `faster-whisper` elsewhere), keep word timestamps.
Write `inventory.md`: clip, length, resolution, what happens, the good lines (with times), usable moments.

## 3. Script and storyboard (Aurélien's OK before rendering)
Beat by beat: time, clip and in/out points, what is said or shown, voice-over line, text on screen, music cue.
Mark jokes and pauses (a beat of silence before a punchline). Keep the target length.

## 4. Preview, then HD
- **Preview** in low res (540p, fast preset) for structure and timing; iterate on single beats, not the whole edit.
- **Voice-over**: stock edge-tts voice (see `explainer-video` voices) or the clone on request; offer both when he
  asks to compare. Check each clip's characters per second (~20/s) and regenerate outliers.
- **Subtitles**: from the transcript and the voice-over; burned in for social platforms, a soft track otherwise.
  Bleeped words: bleep the audio, keep or mask the word in subtitles as he asks.
- **HD render** from the originals: 1080×1920 (reel) or 1920×1080, H.264, AAC, `-movflags +faststart`, loudness
  −14 LUFS for social.
- Inserts (colour cards, logos) and crops: say what changed in each version (v2 → v5).

## 5. Deliver
Send each version as soon as it is ready (he asked for this). Under 29 MB for the chat, else a compressed copy as
well and the HD original in his personal Drive (`40_Content/Exports/`). Never publish: he posts himself.

## Batch description (many videos)
For indexing a large folder: stream one file at a time (never copy 200 GB), key frames + whisper transcript per
file, one line per clip in a catalog (date, place, people, what happens, good moments). Small batches until the
dedicated machine exists.

## Rules
- Footage of other people: consent before a public cut; cut a shot when in doubt.
- Personal footage stays in personal storage; nothing goes through the work Drive.
- Learnings for the pipeline (a filter, a setting, a pitfall) → `references/tooling.md` via the Brain Inbox.
