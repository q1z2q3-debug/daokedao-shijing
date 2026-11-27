# -*- coding: utf-8 -*-
"""靶场一：谐波器形。器形由「对称半轮廓 + 镜像」构造，闭合无自交。"""
import os, sys, math
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svgbrush import svg_open, stroke, text, INK, INK2, PAPER, RED, GREY
from fourier_shape import fd_smooth, fd_between, smooth_open, wobble

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "fig", "drill-fourier.svg")
W, H = 1140, 640
g = [svg_open(W, H), '<rect width="%d" height="%d" fill="%s"/>' % (W, H, PAPER)]

HALF_DING = [(0, -74), (-19, -74), (-39, -70), (-45, -56), (-47, -38), (-43, -18),
             (-37, 0), (-34, 18), (-31, 38), (-27, 52), (-21, 52), (-18, 34),
             (-16, 18), (-11, 12), (-7, 20), (-6, 40), (0, 46)]
HALF_DOU = [(0, -58), (-20, -57), (-34, -52), (-40, -44), (-32, -38), (-15, -36),
            (-9, -28), (-7, -8), (-8, 10), (-12, 18), (-20, 24), (-24, 30),
            (-18, 34), (0, 35)]
BOW = [(0, -74), (-14, -60), (-28, -40), (-34, -14), (-28, 12), (-15, 30), (0, 44)]


def mirror(half):
    h = np.asarray(half, float)
    return np.vstack([h, h[1:][::-1] * np.array([-1, 1])])


DING, DOU = mirror(HALF_DING), mirror(HALF_DOU)


def closed_stroke(pts, w=0.95, col=INK, n=220, gap=0.02):
    p = np.asarray(pts, float)
    k = max(3, int(len(p) * gap))
    p = np.vstack([p[-k:], p, p[:k]])
    return stroke(p, w, col=col, n=n)


def blk(P, cx, cy, s, k, is_open=False):
    base = np.asarray(P, float)
    pts = smooth_open(base, k) if is_open else fd_smooth(base, k)
    pts = np.stack([cx + pts[:, 0] * s, cy + pts[:, 1] * s], 1)
    if is_open:
        p0 = (cx + base[0][0] * s, cy + base[0][1] * s)
        p1 = (cx + base[-1][0] * s, cy + base[-1][1] * s)
        chord = np.array([p0, p1], float)
        return stroke(pts, 0.95, n=140) + stroke(chord, 0.5, col=INK2, n=30)
    return closed_stroke(pts)


g.append(text(44, 46, "谐 波 器 形", 22, INK, ls=8, weight=700))
g.append(text(44, 66, "器形 = 一组系数。阶数低得「势」，阶数高得「形」；六阶辨骨架，十二阶形备。耳与纹带归靶场二", 8.4, INK2, ls=1))
g.append('<line x1="44" y1="84" x2="1096" y2="84" stroke="%s" stroke-width="0.8"/>' % GREY)

KS = [3, 6, 12, 24, 48]
ROWS = [("鼎　三足显于六阶，腹线十二阶才圆", DING, 162, False),
        ("豆　校与圈足六阶立，盘沿十二阶得厚", DOU, 322, False),
        ("弓　开放曲线走低通：三阶存弧势，十二阶得屈曲", BOW, 482, True)]
for (label, P, cy, is_open) in ROWS:
    g.append(text(44, cy - 56, label, 7.8, RED, ls=0.4))
    for i, k in enumerate(KS):
        cx = 132 + i * 96
        g.append(blk(P, cx, cy, 0.58, k, is_open))
        g.append(text(cx, cy + 52, "k=%d" % k, 6.6, GREY, anchor='middle'))

# 右：同族形空间
g.append('<line x1="600" y1="96" x2="600" y2="556" stroke="%s" stroke-width="0.6"/>' % GREY)
g.append(text(626, 118, "同 族 形 空 间：鼎 ↔ 豆", 8.6, RED, ls=0.8))
for i, t in enumerate([0, 0.25, 0.5, 0.75, 1.0]):
    cx = 646 + i * 94
    pts = fd_between(np.asarray(DING, float), np.asarray(DOU, float), t, k=14)
    g.append(closed_stroke(np.stack([cx + pts[:, 0] * 0.58, 208 + pts[:, 1] * 0.58], 1)))
    g.append(text(cx, 272, "t=%.2f" % t, 6.6, GREY, anchor='middle'))
g.append(text(626, 292, "t≈0.5 处足与柄互不相容——形空间只在同拓扑内成立，此即证据", 7.0, INK2))

# 右下：笔压 1/f
g.append(text(626, 340, "笔 压 1/f：低频定势，高频生纹", 8.4, RED, ls=0.6))
for i, amp in enumerate([0.0, 1.2, 2.6, 4.4, 6.2]):
    y0 = 368 + i * 30
    xs = np.linspace(0, 320, 170)
    base = np.stack([xs + 626, np.zeros_like(xs) + y0], 1)
    pts = wobble(base, amp=amp, beta=1.75, seed=i) if amp else base
    g.append(stroke(pts, 1.15, col=INK, n=170, taper_start=0.08, taper_end=0.12))
    g.append(text(626, y0 - 5, "σ=%.1f" % amp, 6.2, GREY))
g.append(text(626, 520, "σ≤2.6 是「手气」，σ≥4.4 是「抖」；此界即笔触上限", 7.0, INK2))

g.append('<line x1="44" y1="556" x2="1096" y2="556" stroke="%s" stroke-width="0.8"/>' % GREY)
g.append(text(44, 578, "靶场一 · 器形由系数生 · drill-fourier", 7.4, GREY, ls=1))
g.append(text(1096, 578, "润泽说 道可道之诗经 · 图法", 7.4, GREY, anchor='end', ls=1))
g.append('</svg>')
open(OUT, 'w', encoding='utf-8').write('\n'.join(g))

import cairosvg
cairosvg.svg2png(url=OUT, write_to=os.path.join(ROOT, 'dist', 'drill-fourier.png'), output_width=1140)
print('ok')
