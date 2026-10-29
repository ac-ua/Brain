# -*- coding: utf-8 -*-
"""Build a narrated slide explainer: frames (headless Chromium) + voices (edge-tts) + assembly (ffmpeg).

Usage:
  python3 build.py EPISODE.py [--out DIR] [--max-mb N] [frames|audio|check|video|compress|all]

  EPISODE.py   episode module (copy episode_template.py): TITLE, NAME, SPEAKERS, SLIDES, optional PRONOUNCE,
               RATE, LANG, FOOTER, EXTRA_CSS.
  --out DIR    output folder (default: ./out next to the episode). Intermediate files go to DIR/build.
               Pro material: point it at the work Drive folder.

Steps are idempotent: existing frames and clips are reused; delete a file to redo it.
  frames  one PNG per slide step
  audio   one MP3 per script line (stock voices, pronunciation dictionary applied to the voice only)
  check   characters-per-second check on every clip; bad clips are deleted and regenerated (up to 3 rounds)
  video   NAME.mp4 (with soft subtitles), NAME.mp3, NAME.srt, script.md
  compress  NAME-small.mp4 under --max-mb (default 29 MB: chat and mail attachment limits), two-pass H.264
  all     frames, audio, check, video (and compress when the MP4 is over --max-mb)

Environment (all optional):
  FFMPEG   ffmpeg binary (default: ffmpeg on PATH)
  CHROME   Chromium binary able to take --screenshot. Default: Playwright's chrome-headless-shell (looked up in
           PLAYWRIGHT_BROWSERS_PATH, ~/.cache/ms-playwright, ~/Library/Caches/ms-playwright), then chromium /
           google-chrome on PATH. On macOS prefer chrome-headless-shell: headless Google Chrome can hang.
  TTS_CONCURRENCY  parallel TTS requests (default 2)
"""
import argparse, asyncio, glob, importlib.util, os, re, shutil, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
W, H = 1920, 1080
GAP_LINE, GAP_SLIDE = 0.35, 0.9
CPS_TARGET, CPS_MIN, CPS_MAX = 20.0, 11.0, 30.0   # characters per second of speech; outside → suspect clip
MIN_BYTES = 2000

FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;'
         '9..144,650&family=Source+Sans+3:wght@400;600&family=JetBrains+Mono:wght@400;500&display=swap">')
SUB_LANG = {"fr": "fre", "en": "eng", "es": "spa", "de": "ger", "it": "ita"}


# ── configuration ────────────────────────────────────────────────────────────
def find_ffmpeg():
    return os.environ.get("FFMPEG") or shutil.which("ffmpeg") or sys.exit("ffmpeg not found: install it or set FFMPEG")


def find_chrome():
    if os.environ.get("CHROME"):
        return os.environ["CHROME"]
    roots = [os.environ.get("PLAYWRIGHT_BROWSERS_PATH", ""), "~/.cache/ms-playwright", "~/Library/Caches/ms-playwright"]
    for root in filter(None, roots):
        hits = sorted(glob.glob(os.path.join(os.path.expanduser(root), "chromium_headless_shell-*", "*", "chrome-headless-shell")))
        if hits:
            return hits[-1]
    for name in ("chrome-headless-shell", "chromium", "chromium-browser", "google-chrome"):
        if shutil.which(name):
            return shutil.which(name)
    sys.exit("No Chromium found: `pip install playwright && playwright install chromium-headless-shell`, or set CHROME")


def load_episode(path):
    spec = importlib.util.spec_from_file_location("episode", path)
    ep = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ep)
    for attr in ("TITLE", "SLIDES", "SPEAKERS"):
        if not hasattr(ep, attr):
            sys.exit("%s: missing %s" % (path, attr))
    ep.NAME = getattr(ep, "NAME", Path(path).stem)
    ep.PRONOUNCE = getattr(ep, "PRONOUNCE", {})
    ep.RATE = getattr(ep, "RATE", "+4%")
    ep.LANG = getattr(ep, "LANG", "fr")
    ep.FOOTER = getattr(ep, "FOOTER", ep.TITLE)
    ep.EXTRA_CSS = getattr(ep, "EXTRA_CSS", "")
    return ep


class Build:
    def __init__(self, ep, out):
        self.ep, self.out = ep, out
        self.build = out / "build"
        self.fr, self.au, self.html = self.build / "frames", self.build / "audio", self.build / "html"
        for d in (self.fr, self.au, self.html, out):
            d.mkdir(parents=True, exist_ok=True)
        self.css = (HERE / "theme.css").read_text(encoding="utf-8") + "\n" + ep.EXTRA_CSS

    # ── helpers ──
    def spoken(self, text):
        """Respell for the voice only; subtitles and script keep the real spelling."""
        for k, v in self.ep.PRONOUNCE.items():
            text = text.replace(k, v)
        return text

    def lines(self):
        for si, s in enumerate(self.ep.SLIDES):
            for li, (spk, k, text) in enumerate(s["lines"]):
                yield si, li, spk, k, text

    def clip(self, si, li):
        return self.au / ("l%02d_%02d.mp3" % (si, li))

    def duration(self, path):
        r = subprocess.run([find_ffmpeg(), "-hide_banner", "-i", str(path)], capture_output=True, text=True)
        m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", r.stderr)
        return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3)) if m else 0.0

    # ── frames ──
    def max_step(self, si):
        return max([l[1] for l in self.ep.SLIDES[si]["lines"]] + [0])

    def step_css(self, k, top, scroll=None):
        rules = ['[data-s="%d"]{visibility:hidden}' % n for n in range(k + 1, top + 2)]
        # pointer: ring + cursor on the element(s) under discussion, at that step only (data-pointer="2 3")
        rules.append('[data-pointer~="%d"]{outline:6px solid #e0a526;outline-offset:8px;border-radius:10px;position:relative}'
                     '[data-pointer~="%d"]::after{content:"";position:absolute;right:-34px;bottom:-34px;width:44px;height:44px;'
                     'background:url("data:image/svg+xml;utf8,<svg xmlns=%%27http://www.w3.org/2000/svg%%27 viewBox=%%270 0 24 24%%27>'
                     '<path d=%%27M3 2l7 19 2.6-7.4L20 11z%%27 fill=%%27%%23111%%27 stroke=%%27white%%27 stroke-width=%%271.5%%27/></svg>")'
                     ' no-repeat center/contain}' % (k, k))
        # document scroll: the slide's .doc moves to the offset of the current step (slide key "scroll": [px per step])
        if scroll:
            rules.append(".doc{transform:translateY(-%dpx)}" % scroll[min(k, len(scroll) - 1)])
        on = ",".join('[data-on="%d"]' % n for n in range(1, k + 1))
        if on:
            rules.append(on + "{background:#2b5a53 !important;color:#ffffff !important;font-weight:600}")
        dim = ",".join('[data-dim="%d"]' % n for n in range(1, k + 1))
        if dim:
            rules.append(dim + "{opacity:.28}")
        return "\n".join(rules)

    def frame_html(self, si, k):
        s, total = self.ep.SLIDES[si], len(self.ep.SLIDES)
        head = '<div class="kicker">%s</div><h2>%s</h2>' % (s["kicker"], s["title"]) if s["title"] else ""
        prog = '<div class="prog" style="width:%.1f%%"></div>' % (100.0 * (si + 1) / total)
        foot = ('<div class="foot"><span>%s</span><span>%d / %d</span></div>' % (self.ep.FOOTER, si, total - 1)) if si else ""
        return ('<!doctype html><html lang="%s"><head><meta charset="utf-8">%s<style>%s\n%s</style></head><body>'
                '<div class="frame">%s%s</div>%s%s</body></html>') % (
            self.ep.LANG, FONTS, self.css, self.step_css(k, self.max_step(si), s.get("scroll")), head, s["body"], foot, prog)

    def frames(self):
        chrome, prof = find_chrome(), self.build / "chrome-profile"
        for si in range(len(self.ep.SLIDES)):
            for k in range(self.max_step(si) + 1):
                png = self.fr / ("s%02d_%d.png" % (si, k))
                if png.exists():
                    continue
                html = self.html / ("s%02d_%d.html" % (si, k))
                html.write_text(self.frame_html(si, k), encoding="utf-8")
                subprocess.run([chrome, "--headless", "--disable-gpu", "--hide-scrollbars", "--no-sandbox",
                                "--user-data-dir=%s" % prof, "--force-device-scale-factor=1",
                                "--window-size=%d,%d" % (W, H), "--virtual-time-budget=4000",
                                "--screenshot=%s" % png, html.as_uri()],
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=90)
                print("frame", png.name, "ok" if png.exists() else "MISSING")

    # ── audio ──
    async def tts_one(self, sem, text, voice, path):
        import edge_tts
        async with sem:
            for attempt in range(10):
                try:
                    await edge_tts.Communicate(text, voice, rate=self.ep.RATE).save(str(path))
                    if path.stat().st_size > MIN_BYTES:
                        return
                    path.unlink()
                except Exception as e:  # network hiccups
                    print("retry", path.name, e)
                    if path.exists():
                        path.unlink()
                await asyncio.sleep(2 + attempt * 3)
            raise RuntimeError("TTS failed for %s" % path)

    def audio(self):
        async def run():
            sem = asyncio.Semaphore(int(os.environ.get("TTS_CONCURRENCY", "2")))
            jobs = []
            for si, li, spk, k, text in self.lines():
                p = self.clip(si, li)
                if not p.exists() or p.stat().st_size < MIN_BYTES:
                    jobs.append(self.tts_one(sem, self.spoken(text), self.ep.SPEAKERS[spk][1], p))
            await asyncio.gather(*jobs)
        asyncio.run(run())

    # ── check ──
    def check(self, rounds=3):
        """Flag empty or truncated clips (speech rate far from ~20 chars/s), delete them and regenerate."""
        for r in range(rounds):
            bad = []
            for si, li, spk, k, text in self.lines():
                p = self.clip(si, li)
                d = self.duration(p) if p.exists() else 0.0
                cps = len(self.spoken(text)) / d if d else float("inf")
                if not p.exists() or p.stat().st_size < MIN_BYTES or not (CPS_MIN <= cps <= CPS_MAX):
                    bad.append((p, cps))
            if not bad:
                print("check: all %d clips ok" % sum(1 for _ in self.lines()))
                return
            for p, cps in bad:
                print("check: %s %.1f chars/s → regenerate" % (p.name, cps))
                p.with_suffix(".wav").unlink(missing_ok=True)
                p.unlink(missing_ok=True)
            self.audio()
        sys.exit("check: clips still suspect after %d rounds; listen to them and fix the text" % rounds)

    # ── video ──
    def video(self):
        ff, ep = find_ffmpeg(), self.ep
        sil = {}
        for g in (GAP_LINE, GAP_SLIDE):
            p = self.au / ("sil_%d.wav" % int(g * 1000))
            subprocess.run([ff, "-y", "-loglevel", "error", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono",
                            "-t", str(g), str(p)], check=True)
            sil[g] = p
        alist, ilist, cues, script = [], [], [], ["# %s\n" % ep.TITLE]
        t, lines = 0.0, list(self.lines())
        for idx, (si, li, spk, k, text) in enumerate(lines):
            mp3, wav = self.clip(si, li), self.clip(si, li).with_suffix(".wav")
            if not wav.exists():
                subprocess.run([ff, "-y", "-loglevel", "error", "-i", str(mp3), "-ar", "24000", "-ac", "1", str(wav)], check=True)
            d = self.duration(wav)
            gap = GAP_SLIDE if idx + 1 == len(lines) or lines[idx + 1][0] != si else GAP_LINE
            alist += ["file '%s'" % wav, "file '%s'" % sil[gap]]
            ilist += ["file '%s'" % (self.fr / ("s%02d_%d.png" % (si, k))), "duration %.3f" % (d + gap)]
            # subtitles: sentence chunks, timed in proportion to their length; real spelling, speaker name first
            parts = [p.strip() for p in re.split(r"(?<=[.?!:])\s+", text) if p.strip()]
            tot, c, who = sum(len(p) for p in parts), t, ep.SPEAKERS[spk][0]
            for p in parts:
                dd = d * len(p) / tot
                cues.append((c, c + dd, "%s : %s" % (who, p) if ep.LANG == "fr" else "%s: %s" % (who, p)))
                c += dd
            if li == 0 and ep.SLIDES[si]["title"]:
                script.append("\n## %s — %s\n" % (ep.SLIDES[si]["kicker"], ep.SLIDES[si]["title"]))
            script.append("**%s** — %s\n" % (who, text))
            t += d + gap
        ilist.append("file '%s'" % (self.fr / ("s%02d_%d.png" % (lines[-1][0], lines[-1][3]))))
        (self.build / "audio.txt").write_text("\n".join(alist) + "\n")
        (self.build / "images.txt").write_text("ffconcat version 1.0\n" + "\n".join(ilist) + "\n")
        ts = lambda x: "%02d:%02d:%06.3f" % (x // 3600, x % 3600 // 60, x % 60)
        srt, mp3, mp4 = (self.out / (ep.NAME + ext) for ext in (".srt", ".mp3", ".mp4"))
        srt.write_text("\n".join("%d\n%s --> %s\n%s\n" % (i + 1, ts(a).replace(".", ","), ts(b).replace(".", ","), x)
                                 for i, (a, b, x) in enumerate(cues)), encoding="utf-8")
        (self.out / "script.md").write_text("\n".join(script), encoding="utf-8")
        voice = self.build / "voice.wav"
        subprocess.run([ff, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(self.build / "audio.txt"),
                        "-c", "copy", str(voice)], check=True)
        subprocess.run([ff, "-y", "-loglevel", "error", "-i", str(voice), "-af", "loudnorm=I=-16:TP=-1.5",
                        "-ar", "44100", "-b:a", "128k", str(mp3)], check=True)
        subprocess.run([ff, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(self.build / "images.txt"),
                        "-i", str(mp3), "-i", str(srt), "-map", "0:v", "-map", "1:a", "-map", "2:s",
                        "-vf", "fps=24,format=yuv420p", "-c:v", "libx264", "-tune", "stillimage", "-crf", "22",
                        "-preset", "medium", "-c:a", "aac", "-b:a", "128k", "-c:s", "mov_text",
                        "-metadata:s:s:0", "language=%s" % SUB_LANG.get(ep.LANG, "und"), "-movflags", "+faststart",
                        "-shortest", str(mp4)], check=True)
        print("%s: %d:%02d, %d lines, %d cues → %s" % (ep.NAME, t // 60, t % 60, len(lines), len(cues), self.out))


    # ── compress ──
    def compress(self, max_mb):
        ff, src = find_ffmpeg(), self.out / (self.ep.NAME + ".mp4")
        dst, d = self.out / (self.ep.NAME + "-small.mp4"), self.duration(src)
        if not d:
            sys.exit("compress: %s missing; run video first" % src.name)
        kbps = max(150, int(max_mb * 8192 * 0.95 / d) - 96)   # 5% margin, 96 kb/s for the audio
        log = str(self.build / "x264pass")
        for n in (1, 2):
            subprocess.run([ff, "-y", "-loglevel", "error", "-i", str(src), "-map", "0", "-c:v", "libx264", "-b:v", "%dk" % kbps,
                            "-pass", str(n), "-passlogfile", log, "-preset", "medium", "-vf", "scale=1280:-2",
                            "-c:a", "aac", "-b:a", "96k", "-c:s", "copy", "-movflags", "+faststart"]
                           + (["-f", "mp4", os.devnull] if n == 1 else [str(dst)]), check=True)
        print("compress: %s %.1f MB (%d kb/s video)" % (dst.name, dst.stat().st_size / 1048576, kbps))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("episode", type=Path)
    ap.add_argument("step", nargs="?", default="all", choices=["frames", "audio", "check", "video", "compress", "all"])
    ap.add_argument("--out", type=Path)
    ap.add_argument("--max-mb", type=float, default=29.0)
    a = ap.parse_args()
    ep = load_episode(a.episode.resolve())
    b = Build(ep, (a.out or a.episode.resolve().parent / "out").resolve())
    if a.step in ("frames", "all"): b.frames()
    if a.step in ("audio", "all"): b.audio()
    if a.step in ("check", "all"): b.check()
    if a.step in ("video", "all"): b.video()
    if a.step == "compress" or (a.step == "all" and (b.out / (ep.NAME + ".mp4")).stat().st_size > a.max_mb * 1048576):
        b.compress(a.max_mb)


if __name__ == "__main__":
    main()
