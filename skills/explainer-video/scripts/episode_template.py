# -*- coding: utf-8 -*-
"""Episode template: copy it next to your outputs, rename it (the file name is the default output name), fill it.

Slides are HTML bodies styled by theme.css. Reveal steps, synced to the script:
  data-s="n"    element appears at step n (hidden before)
  data-on="n"   element is highlighted from step n
  data-dim="n"  element is dimmed from step n
Each script line is (speaker key, step, text): the slide shows step `step` while that line is spoken.
Step 0 is the slide with nothing revealed. Lines are spoken in order; one MP3 clip per line.

Build: python3 build.py <this file> [--out DIR] [frames|audio|check|video|all]
"""

NAME = "my-explainer"                      # output file names: NAME.mp4, NAME.mp3, NAME.srt
TITLE = "Titre de l'épisode"
FOOTER = "Titre court · podcast"           # bottom-left of every slide but the cover
LANG = "fr"                                # "fr" or "en": subtitle language tag and subtitle punctuation

# Stock voices only (edge-tts). Host asks, expert explains.
#   French : fr-FR-VivienneMultilingualNeural (host) · fr-FR-RemyMultilingualNeural (expert)
#   English: en-US-AvaMultilingualNeural (host)      · en-US-AndrewMultilingualNeural (expert)
SPEAKERS = {
    "V": ("Vivienne", "fr-FR-VivienneMultilingualNeural"),
    "R": ("Rémy", "fr-FR-RemyMultilingualNeural"),
}
RATE = "+4%"

# Spoken-only respellings: applied to the voice, never to subtitles or script.md.
# Verify each new entry by listening to (or transcribing) a test clip.
PRONOUNCE = {
    "UnifyApps": "Iou-ni-faï Apps",
}

EXTRA_CSS = ""                             # optional rules added after theme.css

SLIDES = []


def slide(kicker, title, body, lines):
    SLIDES.append({"kicker": kicker, "title": title, "body": body, "lines": lines})


# 0 ─ Cover (empty title → no header, no footer)
slide("", "", """
<div class="cover">
  <div class="cover-k">Podcast · date</div>
  <h1 class="cover-t">Sujet</h1>
  <div class="cover-s">La promesse de l'épisode, en une phrase</div>
  <div class="cover-v">avec Vivienne &amp; Rémy</div>
</div>""", [
    ("V", 0, "Bonjour et bienvenue. Aujourd'hui, on explique le sujet, simplement."),
    ("R", 0, "Et à la fin, vous saurez exactement comment ça marche, et pourquoi."),
])

# 1 ─ A chapter with progressive reveal
slide("Chapitre 1", "Le point de départ", """
<div class="stats">
  <div class="stat" data-s="1"><b>3</b><span>premier constat</span></div>
  <div class="stat" data-s="2"><b>12</b><span>deuxième constat</span></div>
  <div class="stat warn" data-s="3"><b>!</b><span>le point d'attention</span></div>
</div>
<div class="punch" data-s="4">La phrase à retenir du chapitre.</div>
""", [
    ("V", 0, "Commençons par le constat. C'était quoi, la situation ?"),
    ("R", 1, "Premier constat, en une phrase."),
    ("R", 2, "Deuxième constat, avec un chiffre."),
    ("R", 3, "Et un point d'attention, à traiter tout de suite."),
    ("V", 4, "Donc, la phrase à retenir."),
])

# Last ─ Recap: five sentences, one per step
slide("Pour finir", "À retenir", """
<div class="recap">
  <div data-s="1"><b>1</b>Première idée.</div>
  <div data-s="2"><b>2</b>Deuxième idée.</div>
</div>
""", [
    ("V", 0, "Pour conclure, les idées à retenir ?"),
    ("R", 1, "Un : première idée."),
    ("R", 2, "Deux : deuxième idée."),
    ("V", 2, "Merci. À très vite."),
])
