# Media tooling by machine

Found again in four sessions (Oct 2026); write here what works so the next session doesn't search.

## Work Mac (no admin rights, no Homebrew)
- **No admin**: Homebrew can't be installed. Use `uv` (user-level) for Python tools and static binaries in `~/bin`.
- **ffmpeg**: a static build in `~/bin/ffmpeg` (add `~/bin` to PATH), or the one inside an installed app
  (e.g. `/Applications/Shutter Encoder.app/Contents/Resources/Library/ffmpeg`). `FFMPEG=/path` for the scripts.
  TODO(Aurélien): confirm which path is current on the work Mac.
- **whisper**: `uv tool install mlx-whisper` (Apple silicon), model `mlx-community/whisper-large-v3-turbo`.
- **Headless browser** (for frames): Playwright's `chrome-headless-shell`, version matching the installed
  Playwright (`npx playwright install chromium-headless-shell`); headless Google Chrome hangs on `--screenshot`.
- **Voice clone** (`say-as-me`, local only, `~/voice-clone`): Fish S2 Pro for personal use. Slow (~1 min of
  compute per second of audio); stock voices first, clone only on request. Never for work material.
- Personal footage on the work Mac: Google Drive for desktop on the personal account; nothing via the work Drive.

## Cloud session (perso-general)
- ffmpeg on PATH (`/usr/bin/ffmpeg`), Chromium at `/opt/pw-browsers/` (headless shell:
  `/opt/pw-browsers/chromium_headless_shell-*/chrome-headless-shell-linux64/chrome-headless-shell`).
- `pip install faster-whisper edge-tts`. edge-tts may be blocked by the proxy (WebSocket): generate audio elsewhere.
- No access to his phone or Drive files unless shared through a connector; ask for uploads or Drive links.

## Getting files to his phone or iPad
- Small files (< 30 MiB): send them in the chat as soon as each is ready.
- Larger: his personal Google Drive (`40_Content/Exports/`), then open from the Drive app.
- USB debugging from the work Mac is blocked by device management: don't spend time on it.
