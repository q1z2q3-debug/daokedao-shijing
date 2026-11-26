# -*- coding: utf-8 -*-
"""分片并置图：svg -> png(920) -> 上下并置，统一 920×1336，输出 dist/pair-0NN.png。
用法: python3 scripts/make_pair_shard.py 034 035 ..."""
import os, sys, glob, re, cairosvg
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(ROOT, "assets", "fig")
DIST = os.path.join(ROOT, "dist")
os.makedirs(DIST, exist_ok=True)
PAPER = (247, 244, 238)
GAP = 20
CW, CH = 920, 658

def make(num):
    a = [f for f in glob.glob(os.path.join(FIG, "sj" + num + "a-*.svg"))]
    b = [f for f in glob.glob(os.path.join(FIG, "sj" + num + "b-*.svg"))]
    if not a or not b:
        print("skip", num, a, b); return
    imgs = []
    for f in (a[0], b[0]):
        tmp = "/tmp/pair_%s.png" % os.path.basename(f)[:-4]
        cairosvg.svg2png(url=f, write_to=tmp, output_width=920)
        imgs.append(Image.open(tmp).convert("RGB").resize((CW, CH), Image.LANCZOS))
    canvas = Image.new("RGB", (CW, CH * 2 + GAP), PAPER)
    y = 0
    for i in imgs:
        canvas.paste(i, (0, y)); y += CH + GAP
    out = os.path.join(DIST, "pair-%s.png" % num)
    canvas.save(out)
    print("pair-%s" % num, canvas.size)

if __name__ == "__main__":
    for n in sys.argv[1:]:
        make(n)
