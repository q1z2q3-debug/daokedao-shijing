# -*- coding: utf-8 -*-
"""两图上下并置：svg -> png(920) -> PIL 竖排，输出 dist/pair-0NN.png。"""
import os, glob, re, cairosvg
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(ROOT, "assets", "fig")
DIST = os.path.join(ROOT, "dist")
os.makedirs(DIST, exist_ok=True)
PAPER = (247, 244, 238)
GAP = 20

bmap = {}
for f in glob.glob(os.path.join(FIG, "sj0*b-*.svg")):
    m = re.search(r"sj0(\d\d)b-", f)
    if m:
        bmap[m.group(1)] = f

for a in sorted(glob.glob(os.path.join(FIG, "sj0*a-*.svg"))):
    m = re.search(r"sj0(\d\d)a-", a)
    if not m:
        continue
    num = m.group(1)
    if not (21 <= int(num) <= 27):
        continue
    b = bmap.get(num)
    if not b:
        continue
    imgs = []
    for f in (a, b):
        tmp = "/tmp/pair_%s.png" % os.path.basename(f)[:-4]
        cairosvg.svg2png(url=f, write_to=tmp, output_width=920)
        imgs.append(Image.open(tmp).convert("RGB"))
    w = 920
    h = sum(i.height for i in imgs) + GAP
    canvas = Image.new("RGB", (w, h), PAPER)
    y = 0
    for i in imgs:
        canvas.paste(i, (0, y))
        y += i.height + GAP
    out = os.path.join(DIST, "pair-0%s.png" % num)
    canvas.save(out)
    print("pair-0%s" % num, canvas.size)
