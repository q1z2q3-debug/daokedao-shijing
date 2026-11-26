# -*- coding: utf-8 -*-
"""SJ004《樛木》图一线描版：立干、垂枝、葛藟三段（疏—满—旋）。"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fig_geo import *
from shapely.geometry import LineString, Point

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(ROOT, "assets", "fig")
INK, INK2, INK3, RED, PAPER = "#1F1B17", "#5C544A", "#9A9186", "#994433", "#F7F4EE"
W, H = 760, 540

TB = ((300, 448), (290, 358), (304, 268), (296, 198))
BR = ((296, 198), (340, 212), (404, 256), (450, 312))
TP = ((450, 312), (466, 340), (448, 358), (432, 344))


def bez(p, n=48):
    (x0, y0), (x1, y1), (x2, y2), (x3, y3) = p
    out = []
    for i in range(n):
        t = i / (n - 1)
        u = 1 - t
        out.append((u**3 * x0 + 3 * u * u * t * x1 + 3 * u * t * t * x2 + t**3 * x3,
                    u**3 * y0 + 3 * u * u * t * y1 + 3 * u * t * t * y2 + t**3 * y3))
    return out


d = []
d.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="\'Noto Serif SC\',\'Songti SC\',serif">' % (W, H, W, H))
d.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
d.append('  <text x="44" y="58" font-size="8.6" letter-spacing="2" fill="%s">周南 · 四</text>' % RED)
d.append('  <text x="380" y="60" text-anchor="middle" font-size="28" letter-spacing="14" fill="%s" font-weight="700">樛 木</text>' % INK)
d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之四</text>' % INK3)
d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)

# 地平
d.append('  <path d="M212,448 C252,452 342,453 398,448" fill="none" stroke="%s" stroke-width="0.28" stroke-dasharray="7 4 1.5 4"/>' % INK3)

# —— 木 ——
d.append('  <path d="M300,448 C290,358 304,268 296,198" fill="none" stroke="%s" stroke-width="3.4" stroke-linecap="round"/>' % INK)
d.append('  <path d="M303,442 C294,356 307,266 299,204" fill="none" stroke="%s" stroke-width="0.7"/>' % INK3)
d.append('  <path d="M296,440 L282,452 M303,442 L318,454" fill="none" stroke="%s" stroke-width="1.4"/>' % INK2)
d.append('  <path d="M296,198 C302,180 308,168 311,160" fill="none" stroke="%s" stroke-width="1.5"/>' % INK2)
# 垂枝
d.append('  <path d="M296,198 C340,212 404,256 450,312" fill="none" stroke="%s" stroke-width="2.6" stroke-linecap="round"/>' % INK)
d.append('  <path d="M450,312 C466,340 448,358 432,344" fill="none" stroke="%s" stroke-width="1.6"/>' % INK2)
# 侧枝
d.append('  <path d="M299,330 C270,336 248,356 244,376" fill="none" stroke="%s" stroke-width="1.5"/>' % INK2)
d.append('  <path d="M298,258 C326,244 344,244 355,257" fill="none" stroke="%s" stroke-width="1.2"/>' % INK2)
# 树皮短横
for (x, y) in [(298, 420), (299, 392), (298, 360), (301, 326), (300, 292), (298, 258), (297, 226)]:
    d.append('  <path d="M%.1f,%d q5,-1.5 9,0" fill="none" stroke="%s" stroke-width="0.3"/>' % (x - 4, int(y), INK3))

BRPL = bez(BR, 60)


def frame(pl):
    out = []
    for i in range(len(pl) - 1):
        x, y = pl[i]
        x2, y2 = pl[i + 1]
        dx, dy = x2 - x, y2 - y
        L = max(0.01, math.hypot(dx, dy))
        out.append((x, y, -dy / L, dx / L))
    out.append((pl[-1][0], pl[-1][1], out[-1][2], out[-1][3]))
    return out


FR = frame(BRPL)


def at(u):
    i = min(len(FR) - 1, max(0, int(u * (len(FR) - 1))))
    return FR[i]


def leaf(cx, cy, rot, sc=1.0, red=False):
    g = comb(ell(cx, cy, 6.4 * sc, 11.0 * sc), poly([(cx - 3.0 * sc, cy - 9.2 * sc), (cx, cy - 14.2 * sc), (cx + 3.0 * sc, cy - 9.2 * sc)]))
    g = g.buffer(1.0).buffer(-1.0)
    for dd in to_path(g):
        d.append('  <path d="%s" fill="%s" stroke="%s" stroke-width="0.42" transform="rotate(%.1f %.1f %.1f)"/>'
                 % (dd, ("#F7E7DE" if red else "#E7DFCB"), (RED if red else INK2), rot, cx, cy))
    d.append('  <path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="0.2" transform="rotate(%.1f %.1f %.1f)"/>'
             % (cx, cy + 6.6 * sc, cx, cy - 9 * sc, (RED if red else INK3), rot, cx, cy))


def strand(u0, u1, half_waves, amp, leaves=0, red=False, wdt=1.5, leaf_sc=1.0, leaf_shift=0.0):
    pts, norms = [], []
    n = 54
    for i in range(n):
        u = u0 + (u1 - u0) * i / (n - 1)
        x, y, nx, ny = at(u)
        s = amp * math.sin((i / (n - 1)) * half_waves * math.pi + leaf_shift)
        pts.append((x + nx * s, y + ny * s))
        norms.append((nx, ny, s))
    d.append('  <path d="M%s" fill="none" stroke="%s" stroke-width="%.2f"/>'
             % (" L".join("%.1f,%.1f" % q for q in pts), (RED if red else INK2), wdt))
    if leaves:
        for k in range(leaves):
            j = int((k + 0.5) / leaves * (n - 1))
            x, y = pts[j]
            nx, ny, s = norms[j]
            side = 1 if s >= 0 else -1
            ang = math.degrees(math.atan2(-ny * side, -nx * side))
            leaf(x + nx * side * 5.0, y + ny * side * 5.0, ang + (8 if k % 2 else -8), leaf_sc, red)
    return pts


# 累：疏系（三片叶）
strand(0.03, 0.35, 1.6, 16, leaves=3, wdt=1.5)
# 荒：满覆（叶密、遮枝）
strand(0.34, 0.72, 2.2, 17, leaves=6, wdt=1.6, leaf_sc=0.95)
# 萦：旋梢（赭）
strand(0.71, 1.0, 2.4, 14, leaves=4, red=True, wdt=1.5, leaf_sc=0.9)
# 卷须
d.append('  <path d="M462,332 c8,10 20,4 17,-8 c-3,-9 -12,-7 -13,1" fill="none" stroke="%s" stroke-width="1.2"/>' % RED)
d.append('  <path d="M448,350 c4,10 14,8 15,-1" fill="none" stroke="%s" stroke-width="1.0"/>' % INK2)
# 侧枝上的藤（细）
strand(0.28, 1.0, 1.8, 10, leaves=3, wdt=1.2, leaf_sc=0.78)

d.append('  <text x="352" y="190" font-size="7.6" fill="%s">①</text>' % RED)
d.append('  <text x="412" y="252" font-size="7.6" fill="%s">②</text>' % RED)
d.append('  <text x="474" y="322" font-size="7.6" fill="%s">③</text>' % RED)
d.append('  <text x="264" y="208" font-size="7.2" fill="%s">樛</text>' % INK2)
d.append('  <text x="436" y="372" font-size="7.2" fill="%s">垂</text>' % INK2)

d.append('  <text x="44" y="466" font-size="7.8" fill="%s">① 樛木　木下曲曰樛：枝肯垂，高处才让得出来</text>' % INK2)
d.append('  <text x="300" y="466" font-size="7.8" fill="%s">② 葛藟　似葛而细，蔓生附木</text>' % INK2)
d.append('  <text x="516" y="466" font-size="7.8" fill="%s">③ 累／荒／萦　系、掩、旋</text>' % INK2)
d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">南有樛木，葛藟縈之</text>' % INK)
d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">下曲非折，是让</text>' % INK3)
d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj004a</text>' % INK3)
d.append('</svg>')
open(os.path.join(FIG, "sj004a-jiong-mu-ge-lei.svg"), "w", encoding="utf-8").write("\n".join(d))

import cairosvg
cairosvg.svg2png(url=os.path.join(FIG, "sj004a-jiong-mu-ge-lei.svg"), write_to="/tmp/sj004a.png", output_width=920)
print("ok")
