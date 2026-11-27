# -*- coding: utf-8 -*-
"""SJ053 三旗 · 笔压白描 v4。"""
import os, sys, math
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fig_brush import qbez

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "fig", "sj053a-san-qi-zai-jun-v2.svg")
INK, INK2, PAPER, RED, GREY = "#1F1B17", "#5C544A", "#F7F4EE", "#994433", "#9A9186"
W, H = 760, 540
g = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" '
     'font-family="Noto Serif SC,Songti SC,serif" stroke-linejoin="round" stroke-linecap="round">' % (W, H, W, H)]
g.append('<rect width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))


def line(pts, w=0.9, col=INK):
    d = 'M%.2f,%.2f' % pts[0]
    for x, y in pts[1:]:
        d += ' L%.2f,%.2f' % (x, y)
    return '<path d="%s" fill="none" stroke="%s" stroke-width="%s"/>' % (d, col, w)


def curve(p0, p1, p2, w=0.9, col=INK, n=16):
    return line(qbez(p0, p1, p2, n), w, col)


def closed(pts, w=0.9, col=INK):
    d = 'M%.2f,%.2f' % pts[0]
    for x, y in pts[1:]:
        d += ' L%.2f,%.2f' % (x, y)
    d += ' L%.2f,%.2f Z' % pts[0]
    return '<path d="%s" fill="none" stroke="%s" stroke-width="%s"/>' % (d, col, w)


g.append('<text x="44" y="58" font-size="8.6" letter-spacing="2" fill="%s">鄘风 · 四</text>' % RED)
g.append('<text x="380" y="60" text-anchor="middle" font-size="26" letter-spacing="10" fill="%s" font-weight="700">干 旄</text>' % INK)
g.append('<text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之五十三</text>' % GREY)
g.append('<line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % GREY)

TOP, BASE = 124, 428


def pole(cx):
    out = [line([(cx - 1.6, BASE), (cx - 1.6, TOP - 2)], 0.85),
           line([(cx + 1.6, BASE), (cx + 1.6, TOP - 2)], 0.85),
           line([(cx - 1.6, BASE - 2), (cx + 1.6, BASE - 2)], 0.5, INK2)]
    # 顶饰：小箍 + 短锥
    out.append(line([(cx - 5.6, TOP), (cx + 5.6, TOP)], 1.1))
    out.append(closed([(cx - 5.2, TOP - 1), (cx - 4.4, TOP - 5.5), (cx - 2.6, TOP - 11),
                       (cx, TOP - 15), (cx + 2.6, TOP - 11), (cx + 4.4, TOP - 5.5),
                       (cx + 5.2, TOP - 1)], 0.85))
    out.append(line([(cx - 1.6, TOP - 2), (cx - 1.6, TOP - 10)], 0.35, INK2))
    out.append(line([(cx + 1.6, TOP - 2), (cx + 1.6, TOP - 10)], 0.35, INK2))
    return out


# 壹 干旄
cx = 152
g += pole(cx)
g.append(curve((cx - 7, 133), (cx - 10, 158), (cx - 9, 184), 0.85, INK2))
g.append(curve((cx + 7, 133), (cx + 10, 158), (cx + 9, 184), 0.85, INK2))
rng = np.random.default_rng(5)
for i in range(20):
    x0 = cx - 8.4 + i * 0.54
    sy = 156 + (i % 7) * 6.0
    amp = (-1) ** i * (3 + rng.random() * 5.5)
    ey = 252 + rng.random() * 58
    col = INK2 if i % 4 else GREY
    g.append(curve((x0, sy), (x0 + amp * 0.5, ey - 36), (x0 + amp * 1.7, ey), 0.52 if i % 4 else 0.36, col))
for y in (140, 150):
    g.append(curve((cx - 11.4, y), (cx, y + 3.4), (cx + 11.4, y), 0.55, INK2))
g.append(closed([(cx - 5.2, 126), (cx + 5.2, 126), (cx + 5.2, 131), (cx - 5.2, 131)], 0.45, INK2))

# 贰 干旟
cx = 380
g += pole(cx)
g.append(line([(330, 148), (430, 148)], 1.3))
g.append(line([(330, 151.4), (430, 151.4)], 0.55, INK2))
g.append(line([(330, 145), (330, 154.4)], 0.45, INK2))
g.append(line([(430, 145), (430, 154.4)], 0.45, INK2))
g.append(closed([(340, 156), (420, 156), (420, 262), (340, 262)], 0.95))
g.append(closed([(343.2, 159.2), (416.8, 159.2), (416.8, 258.8), (343.2, 258.8)], 0.32, INK2))
g.append(line([(381, 127), (430, 148)], 0.65))
g.append(line([(430, 149), (430, 156)], 0.45, INK2))


def bird(bx, by, s, flip=1):
    p = [curve((bx - 11 * s * flip, by + 3 * s), (bx, by - 4 * s), (bx + 11 * s * flip, by + 1 * s), 0.7),
         curve((bx - 1 * s, by - 1 * s), (bx - 10 * s, by - 15 * s), (bx - 21 * s, by - 7 * s), 0.62),
         curve((bx + 3 * s, by - 1 * s), (bx + 9 * s, by - 13 * s), (bx + 20 * s, by - 3 * s), 0.62),
         line([(bx - 11 * s * flip, by + 3 * s), (bx - 21 * s * flip, by + 6 * s)], 0.45),
         line([(bx - 11 * s * flip, by + 3 * s), (bx - 19 * s * flip, by + 10 * s)], 0.45),
         line([(bx + 11 * s * flip, by + 1 * s), (bx + 15 * s * flip, by - 1 * s)], 0.4)]
    return p


g += bird(372, 190, 0.74, 1)
g += bird(396, 224, 0.54, -1)
for i in range(7):
    x0 = 345 + i * 11.6
    ln = 50 + (i % 3) * 12
    sgn = 1 if i % 2 else -1
    g.append(curve((x0, 262), (x0 + sgn * 2.4, 262 + ln * 0.6), (x0 + sgn * 3.4, 262 + ln), 0.85, INK2))

# 叁 干旌
cx = 608
g += pole(cx)


def feather(bx, by, length, width, ang, w=0.7):
    dx, dy = math.sin(ang), -math.cos(ang)
    nx, ny = -dy, dx
    ts = np.linspace(0, 1, 16)
    left, right = [], []
    for t in ts:
        wd = width * (max(0.0, math.sin(math.pi * (0.08 + t * 0.92))) ** 0.55) * 0.5
        px, py = bx + dx * length * t, by + dy * length * t
        left.append((px + nx * wd, py + ny * wd))
        right.append((px - nx * wd, py - ny * wd))
    out = [line(left, w), line(right, w), line([(bx, by), (bx + dx * length * 0.94, by + dy * length * 0.94)], 0.3, INK2)]
    for m in range(2):
        t = 0.34 + m * 0.28
        px, py = bx + dx * length * t, by + dy * length * t
        wd = width * (max(0.0, math.sin(math.pi * (0.08 + t * 0.92))) ** 0.55) * 0.38
        out.append(line([(px, py), (px + nx * wd, py + ny * wd - 3)], 0.24, GREY))
        out.append(line([(px, py), (px - nx * wd, py - ny * wd - 3)], 0.24, GREY))
    return out


for k in range(5):
    by = 186 + k * 42
    tilt = 0.20 if k % 2 == 0 else -0.20
    g += feather(cx + (2 if k % 2 == 0 else -2), by, 74, 14, tilt)
    g += feather(cx + (-3 if k % 2 == 0 else 3), by + 7, 64, 12, tilt * 1.9)
    g.append(closed([(cx - 3.4, by - 4), (cx + 3.4, by - 4), (cx + 2.2, by + 2), (cx - 2.2, by + 2)], 0.4, INK2))

for (x, t) in [(118, "壹"), (348, "贰"), (588, "叁")]:
    g.append('<text x="%d" y="132" font-size="7.6" fill="%s">%s</text>' % (x, RED, t))
g.append('<text x="44" y="466" font-size="7.8" fill="%s">壹 干旄　旄牛尾注杆首</text>' % INK2)
g.append('<text x="264" y="466" font-size="7.8" fill="%s">贰 干旟　鸟隼为饰</text>' % INK2)
g.append('<text x="486" y="466" font-size="7.8" fill="%s">叁 干旌　析羽为饰</text>' % INK2)
g.append('<line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % GREY)
g.append('<text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">孑孑干旄，在浚之郊</text>' % INK)
g.append('<text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">三旗三制，礼愈近</text>' % GREY)
g.append('<text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj053a-v2</text>' % GREY)
g.append('</svg>')
open(OUT, 'w', encoding='utf-8').write('\n'.join(g))
import cairosvg
cairosvg.svg2png(url=OUT, write_to='/tmp/sj053a-v2.png', output_width=1140)
print('ok')
