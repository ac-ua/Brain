# -*- coding: utf-8 -*-
"""Build the narrated slide podcast: frames (Chrome headless) + voices (edge-tts) + ffmpeg.

Usage: python3 build.py [frames|audio|video|all]
Outputs in ./out : brain-podcast.mp4, brain-podcast.mp3, brain-podcast.srt, script.md
"""
import asyncio, os, re, subprocess, sys, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from episode import SLIDES, TITLE  # noqa

FFMPEG = os.path.expanduser("~/.local/bin/ffmpeg")
CHROME = os.path.expanduser("~/Library/Caches/ms-playwright/chromium_headless_shell-1248/chrome-headless-shell-mac-arm64/chrome-headless-shell")
VOICES = {"V": "fr-FR-VivienneMultilingualNeural", "R": "fr-FR-RemyMultilingualNeural"}
RATE = "+4%"
# Spoken-only respellings (subtitles keep the real spelling). Verified by transcribing a test clip.
PRONOUNCE = {"UnifyApps": "Iou-ni-faï Apps"}

def spoken(text):
    for k, v in PRONOUNCE.items():
        text = text.replace(k, v)
    return text
GAP_LINE, GAP_SLIDE = 0.35, 0.9
W, H = 1920, 1080

BUILD = HERE / "build"; OUT = HERE / "out"
FR = BUILD / "frames"; AU = BUILD / "audio"
for d in (FR, AU, OUT, BUILD / "html"): d.mkdir(parents=True, exist_ok=True)

CSS = r"""
:root{--bg:#0f1d1c;--bg2:#152826;--fg:#e8efec;--mut:#94a9a3;--line:#2a4440;--acc:#7cc2b8;--acc2:#b9e3dc;--warm:#f0a07c;--ok:#9fd49f;--no:#f08c7c}
*{box-sizing:border-box}
html,body{margin:0;width:1920px;height:1080px;background:var(--bg);color:var(--fg);font-family:"Source Sans 3",Helvetica,Arial,sans-serif;overflow:hidden}
body{background:radial-gradient(1400px 900px at 85% -10%,#1d3a36 0%,transparent 60%),var(--bg)}
.frame{position:absolute;inset:0;padding:70px 110px}
.kicker{font-family:"JetBrains Mono",Menlo,monospace;font-size:24px;letter-spacing:.14em;text-transform:uppercase;color:var(--acc)}
h2{font-family:"Fraunces",Georgia,serif;font-weight:600;font-size:66px;margin:10px 0 40px;line-height:1.1}
.foot{position:absolute;left:110px;right:110px;bottom:40px;display:flex;justify-content:space-between;font-family:"JetBrains Mono",Menlo,monospace;font-size:18px;color:var(--mut)}
.prog{position:absolute;left:0;bottom:0;height:6px;background:var(--acc)}
.cover{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;padding:0 160px;background:
 repeating-radial-gradient(circle at 78% 60%,transparent 0 38px,rgba(124,194,184,.07) 39px 40px)}
.cover-k{font-family:"JetBrains Mono",Menlo,monospace;font-size:26px;letter-spacing:.14em;text-transform:uppercase;color:var(--acc)}
.cover-t{font-family:"Fraunces",Georgia,serif;font-size:210px;margin:10px 0 10px;font-weight:650;line-height:1}
.cover-s{font-size:44px;max-width:1300px;color:var(--acc2)}
.cover-v{margin-top:60px;font-size:30px;color:var(--mut)}
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:28px}
.stat{background:var(--bg2);border:1px solid var(--line);border-radius:14px;padding:30px 34px;display:flex;flex-direction:column;gap:10px}
.stat b{font-family:"Fraunces",Georgia,serif;font-size:76px;color:var(--acc);line-height:1}
.stat span{font-size:30px;line-height:1.3}
.stat.warn{border-color:var(--warm)} .stat.warn b{color:var(--warm)}
.punch{margin-top:46px;font-family:"Fraunces",Georgia,serif;font-size:46px;color:var(--acc2)}
.layers{display:grid;grid-template-columns:1fr 380px;gap:34px;align-items:stretch}
.stack{display:flex;flex-direction:column;gap:18px}
.layer,.side{border-radius:14px;padding:24px 32px;border:2px solid var(--line);background:var(--bg2);display:flex;flex-direction:column;gap:6px}
.layer em,.side em,.step em,.card em,.ph em,.fcol em,.fmid em{font-style:normal;font-family:"JetBrains Mono",Menlo,monospace;font-size:21px;letter-spacing:.08em;text-transform:uppercase;color:var(--acc)}
.layer strong,.side strong{font-size:40px;font-family:"Fraunces",Georgia,serif;font-weight:600}
.layer span,.side span{font-size:27px;color:var(--mut)}
.l-know{border-color:var(--acc)} .l-harn{border-color:#5f9fd0} .l-run{border-style:dashed}
.side{justify-content:center;border-color:var(--warm)} .side em{color:var(--warm)}
.chips{margin-top:34px;display:flex;gap:16px;align-items:center;flex-wrap:wrap}
.chips span{font-family:"JetBrains Mono",Menlo,monospace;font-size:28px;padding:8px 18px;border-radius:8px;background:#1f3b37;color:var(--acc2)}
.chips i{font-style:normal;font-size:28px;color:var(--mut);margin-left:10px}
.tree{font-family:"JetBrains Mono",Menlo,monospace;font-size:29px;line-height:1.45;white-space:pre;background:var(--bg2);border:1px solid var(--line);border-radius:14px;padding:26px 36px}
.tree b{color:var(--acc);font-weight:500} .tree i{color:var(--mut);font-style:normal}
.note{margin-top:28px;font-size:32px;padding:18px 28px;border-left:5px solid var(--acc);background:#16302c;border-radius:0 10px 10px 0}
.note.warn{border-color:var(--warm);background:#33241c}
.two{display:grid;grid-template-columns:1fr 1fr;gap:40px}
.card{background:var(--bg2);border:1px solid var(--line);border-radius:14px;padding:28px 34px}
.card.mono{font-family:"JetBrains Mono",Menlo,monospace;font-size:27px;line-height:1.5;white-space:pre}
.card.mono b{color:var(--acc);font-weight:500} .card.mono i{color:var(--mut);font-style:normal}
.col{display:flex;flex-direction:column;gap:24px}
.kpi{background:var(--bg2);border:1px solid var(--line);border-radius:14px;padding:26px 32px;display:flex;flex-direction:column;gap:8px}
.kpi b{font-family:"Fraunces",Georgia,serif;font-size:58px;color:var(--acc);line-height:1}
.kpi span{font-size:30px;line-height:1.3}
.kpi.warn{border-color:var(--warm)} .kpi.warn b{color:var(--warm)}
.matrix table{border-collapse:collapse;width:100%;font-size:27px}
.matrix th,.matrix td{border:1px solid var(--line);padding:14px 14px;text-align:left}
.matrix th{color:var(--acc2);font-weight:600;background:#14302c}
.matrix td{color:var(--fg)}
.flow{display:flex;align-items:stretch;gap:12px}
.step{flex:1;background:var(--bg2);border:1px solid var(--line);border-radius:14px;padding:24px 22px;display:flex;flex-direction:column;gap:8px}
.step strong{font-family:"Fraunces",Georgia,serif;font-size:36px;font-weight:600;line-height:1.1}
.step span{font-size:26px;color:var(--mut)}
.step.hot{border-color:var(--acc);border-width:2px}
.arrow{align-self:center;font-size:52px;color:var(--acc)}
.loop{display:flex;flex-direction:column;gap:22px}
.row{display:grid;grid-template-columns:330px 300px 330px 1fr;gap:20px;align-items:center}
.row .b{background:var(--bg2);border:1px solid var(--line);border-radius:12px;padding:18px 22px;font-size:31px;text-align:center}
.row .b.k{border-color:var(--acc)} .row .b.h{border-color:var(--warm);color:#ffd7c4} .row .b.g{border-color:#5f9fd0}
.row .a{font-size:28px;color:var(--acc);text-align:center}
.row .ex{font-size:27px;color:var(--mut);font-style:italic}
.files{display:grid;grid-template-columns:1fr 0.8fr 1fr;gap:34px;align-items:start}
.fcol,.fmid{background:var(--bg2);border:1px solid var(--line);border-radius:14px;padding:28px;display:flex;flex-direction:column;gap:14px}
.fmid{border-style:dashed;margin-top:60px}
.files .b{font-family:"Fraunces",Georgia,serif;font-size:40px}
.files span{font-size:28px;color:var(--mut)}
.outs{display:flex;flex-direction:column;gap:10px;margin-top:10px}
.outs .b{font-family:"Source Sans 3",Helvetica,sans-serif;font-size:28px;border:1px solid var(--acc);border-radius:10px;padding:10px 16px}
.oneway{margin-top:40px;display:flex;gap:30px;font-size:34px}
.oneway .no{color:var(--no)} .oneway .yes{color:var(--ok)}
.grid4{display:grid;grid-template-columns:repeat(4,1fr);gap:26px}
.grid4 .card ul{list-style:none;padding:0;margin:16px 0 0;display:flex;flex-direction:column;gap:12px;font-size:30px}
.grid4 li.y::before{content:"✓  ";color:var(--ok)} .grid4 li.n::before{content:"✕  ";color:var(--no)}
.grid4 .card.dash{border-style:dashed}
.mail{background:var(--bg2);border:1px solid var(--line);border-radius:12px;padding:22px 26px;font-size:32px;display:flex;justify-content:space-between;align-items:center}
.tag{font-family:"JetBrains Mono",Menlo,monospace;font-size:21px;padding:4px 12px;border-radius:6px;background:#1f3b37;color:var(--acc2)}
.banner{font-family:"Fraunces",Georgia,serif;font-size:42px;color:var(--acc2);margin-bottom:36px}
.rules{display:flex;flex-direction:column;gap:26px;font-size:38px}
.rules>div{display:flex;align-items:center;gap:26px}
.ic{width:66px;height:66px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:34px;flex:none;border:2px solid}
.ic.n{color:var(--no)} .ic.q{color:var(--warm)} .ic.y{color:var(--ok)} .ic.k{color:var(--acc)}
.timeline{display:flex;flex-direction:column;gap:18px}
.ph{display:grid;grid-template-columns:330px 1fr;grid-template-rows:auto auto;column-gap:30px;background:var(--bg2);border:1px solid var(--line);border-radius:12px;padding:18px 26px}
.ph em{grid-row:1/3;align-self:center}
.ph strong{font-family:"Fraunces",Georgia,serif;font-size:34px;font-weight:600}
.ph span{font-size:26px;color:var(--mut)}
.ph.hot{border-color:var(--acc);border-width:2px}
.recap{display:flex;flex-direction:column;gap:26px}
.recap>div{font-family:"Fraunces",Georgia,serif;font-size:46px;display:flex;gap:30px;align-items:baseline}
.recap b{font-family:"JetBrains Mono",Menlo,monospace;color:var(--acc);font-size:40px;width:50px}
"""

FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,650&family=Source+Sans+3:wght@400;600&family=JetBrains+Mono:wght@400;500&display=swap">'

def max_step(si):
    return max(l[1] for l in SLIDES[si]["lines"])

def step_css(k):
    rules = []
    for n in range(k + 1, 12):
        rules.append('[data-s="%d"]{visibility:hidden}' % n)
    on = ",".join('[data-on="%d"]' % n for n in range(1, k + 1))
    if on:
        rules.append(on + "{background:#2b5a53 !important;color:#ffffff !important;font-weight:600}")
    dim = ",".join('[data-dim="%d"]' % n for n in range(1, k + 1))
    if dim:
        rules.append(dim + "{opacity:.28}")
    return "\n".join(rules)

def frame_html(si, k):
    s = SLIDES[si]
    total = len(SLIDES)
    head = ""
    if s["title"]:
        head = '<div class="kicker">%s</div><h2>%s</h2>' % (s["kicker"], s["title"])
    prog = '<div class="prog" style="width:%.1f%%"></div>' % (100.0 * (si + 1) / total)
    foot = '<div class="foot"><span>Le Brain · podcast</span><span>%d / %d</span></div>' % (si, total - 1) if si else ""
    return ('<!doctype html><html><head><meta charset="utf-8">%s<style>%s\n%s</style></head><body>'
            '<div class="frame">%s%s</div>%s%s</body></html>') % (FONTS, CSS, step_css(k), head, s["body"], foot, prog)

def frames():
    prof = BUILD / "chrome-profile"
    for si in range(len(SLIDES)):
        for k in range(max_step(si) + 1):
            png = FR / ("s%02d_%d.png" % (si, k))
            if png.exists():
                continue
            html = BUILD / "html" / ("s%02d_%d.html" % (si, k))
            html.write_text(frame_html(si, k), encoding="utf-8")
            subprocess.run([CHROME, "--disable-gpu", "--hide-scrollbars",
                            "--user-data-dir=%s" % prof, "--force-device-scale-factor=1",
                            "--window-size=%d,%d" % (W, H), "--virtual-time-budget=4000",
                            "--screenshot=%s" % png, html.as_uri()],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=90)
            print("frame", png.name, png.exists())

async def tts_one(sem, text, voice, path):
    import edge_tts
    async with sem:
        for attempt in range(10):
            try:
                await edge_tts.Communicate(text, voice, rate=RATE).save(str(path))
                if path.stat().st_size > 2000:
                    return
                path.unlink()
            except Exception as e:  # network hiccups
                print("retry", path.name, e)
                if path.exists(): path.unlink()
                await asyncio.sleep(2 + attempt * 3)
        raise RuntimeError("TTS failed for %s" % path)

def all_lines():
    for si, s in enumerate(SLIDES):
        for li, (spk, k, text) in enumerate(s["lines"]):
            yield si, li, spk, k, text

def audio():
    async def run():
        sem = asyncio.Semaphore(2)
        jobs = []
        for si, li, spk, k, text in all_lines():
            p = AU / ("l%02d_%02d.mp3" % (si, li))
            if not p.exists() or p.stat().st_size < 2000:
                jobs.append(tts_one(sem, spoken(text), VOICES[spk], p))
        await asyncio.gather(*jobs)
    asyncio.run(run())

def duration(path):
    r = subprocess.run([FFMPEG, "-hide_banner", "-i", str(path)], capture_output=True, text=True)
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", r.stderr)
    return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))

def fmt(t):
    h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return "%02d:%02d:%06.3f" % (h, m, s)

def video():
    sil = {}
    for g in (GAP_LINE, GAP_SLIDE):
        p = AU / ("sil_%d.wav" % int(g * 1000))
        subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono",
                        "-t", str(g), str(p)], check=True)
        sil[g] = p
    alist, ilist, cues, script = [], [], [], ["# %s\n" % TITLE]
    t = 0.0
    lines = list(all_lines())
    for idx, (si, li, spk, k, text) in enumerate(lines):
        mp3 = AU / ("l%02d_%02d.mp3" % (si, li))
        wav = AU / ("l%02d_%02d.wav" % (si, li))
        if not wav.exists():
            subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-i", str(mp3), "-ar", "24000", "-ac", "1", str(wav)], check=True)
        d = duration(wav)
        last_of_slide = idx + 1 == len(lines) or lines[idx + 1][0] != si
        gap = GAP_SLIDE if last_of_slide else GAP_LINE
        alist += ["file '%s'" % wav, "file '%s'" % sil[gap]]
        ilist += ["file '%s'" % (FR / ("s%02d_%d.png" % (si, k))), "duration %.3f" % (d + gap)]
        # subtitles: split into sentence chunks, time proportional to length
        parts = [p.strip() for p in re.split(r"(?<=[.?!:])\s+", text) if p.strip()]
        tot = sum(len(p) for p in parts); c = t
        for p in parts:
            dd = d * len(p) / tot
            cues.append((c, c + dd, ("Vivienne : " if spk == "V" else "Rémy : ") + p))
            c += dd
        if li == 0 and SLIDES[si]["title"]:
            script.append("\n## %s — %s\n" % (SLIDES[si]["kicker"], SLIDES[si]["title"]))
        script.append("**%s** — %s\n" % ("Vivienne" if spk == "V" else "Rémy", text))
        t += d + gap
    ilist.append("file '%s'" % (FR / ("s%02d_%d.png" % (lines[-1][0], lines[-1][3]))))
    (BUILD / "audio.txt").write_text("\n".join(alist) + "\n")
    (BUILD / "images.txt").write_text("ffconcat version 1.0\n" + "\n".join(ilist) + "\n")
    srt = OUT / "brain-podcast.srt"
    srt.write_text("\n".join("%d\n%s --> %s\n%s\n" % (i + 1, fmt(a).replace(".", ","), fmt(b).replace(".", ","), x)
                             for i, (a, b, x) in enumerate(cues)), encoding="utf-8")
    (OUT / "script.md").write_text("\n".join(script), encoding="utf-8")
    wav_all = BUILD / "voice.wav"
    subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(BUILD / "audio.txt"),
                    "-c", "copy", str(wav_all)], check=True)
    subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-i", str(wav_all), "-af", "loudnorm=I=-16:TP=-1.5",
                    "-ar", "44100", "-b:a", "128k", str(OUT / "brain-podcast.mp3")], check=True)
    subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(BUILD / "images.txt"),
                    "-i", str(OUT / "brain-podcast.mp3"), "-i", str(srt),
                    "-map", "0:v", "-map", "1:a", "-map", "2:s",
                    "-vf", "fps=24,format=yuv420p", "-c:v", "libx264", "-tune", "stillimage", "-crf", "22",
                    "-preset", "medium", "-c:a", "aac", "-b:a", "128k", "-c:s", "mov_text",
                    "-metadata:s:s:0", "language=fre", "-movflags", "+faststart", "-shortest",
                    str(OUT / "brain-podcast.mp4")], check=True)
    print("total %.1f s, %d lines, %d cues" % (t, len(lines), len(cues)))

if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "all"
    if what in ("frames", "all"): frames()
    if what in ("audio", "all"): audio()
    if what in ("video", "all"): video()
