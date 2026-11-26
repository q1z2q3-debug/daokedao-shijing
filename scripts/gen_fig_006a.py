# -*- coding: utf-8 -*-
"""SJ006《桃夭》图一（改）：一枝三态，花圆瓣有缝，桃带尖，叶狭长。"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fig_geo import *
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(ROOT, "assets", "fig")
INK, INK2, INK3, RED, PAPER = "#1F1B17", "#5C544A", "#9A9186", "#994433", "#F7F4EE"
W, H = 760, 540

d = []
d.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="\'Noto Serif SC\',\'Songti SC\',serif">' % (W, H, W, H))
d.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
d.append('  <text x="44" y="58" font-size="8.6" letter-spacing="2" fill="%s">周南 · 六</text>' % RED)
d.append('  <text x="380" y="60" text-anchor="middle" font-size="28" letter-spacing="14" fill="%s" font-weight="700">桃 夭</text>' % INK)
d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之六</text>' % INK3)
d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)


def flower(cx, cy, r):
    """桃花：五瓣圆润，瓣间留缝"""
    for i in range(5):
        a = math.radians(i * 72 - 90)
        px, py = cx + r * 0.60 * math.cos(a), cy + r * 0.60 * math.sin(a)
        d.append('  <ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="#F7E5E0" stroke="%s" stroke-width="0.45" transform="rotate(%.1f %.1f %.1f)"/>'
                 % (px, py, r * 0.42, r * 0.50, INK2, i * 72, px, py))
    d.append('  <circle cx="%d" cy="%d" r="2.6" fill="#E9D6B4" stroke="%s" stroke-width="0.35"/>' % (cx, cy, INK2))
    for i in range(9):
        a = math.radians(i * 40 + 12)
        L = r * 0.52
        ex, ey = cx + L * math.cos(a), cy + L * math.sin(a)
        d.append('  <path d="M%d,%d L%.1f,%.1f" stroke="%s" stroke-width="0.28"/>' % (cx, cy, ex, ey, INK3))
        d.append('  <circle cx="%.1f" cy="%.1f" r="0.85" fill="%s"/>' % (ex, ey, INK2))


def bud(cx, cy, ang):
    d.append('  <ellipse cx="%d" cy="%d" rx="4.4" ry="7.0" fill="#F4DCD4" stroke="%s" stroke-width="0.4" transform="rotate(%d %d %d)"/>'
             % (cx, cy, INK2, ang, cx, cy))
    d.append('  <path d="M%d,%d l%d,%d" stroke="%s" stroke-width="0.35" transform="rotate(%d %d %d)"/>'
             % (cx, cy + 5, 0, -11, INK3, ang, cx, cy))


def peach(cx, cy, r, ang=0):
    g = ell(cx, cy, r * 0.94, r)
    g = comb(g, poly([(cx - r * 0.62, cy + r * 0.60), (cx, cy + r * 1.34), (cx + r * 0.62, cy + r * 0.60)]))
    g = g.buffer(1.2).buffer(-1.2)
    for dd in to_path(g):
        d.append('  <path d="%s" fill="#F8E9DC" stroke="%s" stroke-width="0.5" transform="rotate(%.1f %d %d)"/>'
                 % (dd, INK2, ang, cx, cy))
    d.append('  <path d="M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="none" stroke="%s" stroke-width="0.34" transform="rotate(%.1f %d %d)"/>'
             % (cx, cy - r * 0.86, cx + r * 0.30, cy - r * 0.18, cx + r * 0.26, cy + r * 0.4, cx + 1, cy + r * 0.92, INK3, ang, cx, cy))


def leaf(cx, cy, ang, L=24, Wd=7.6):
    g = comb(ell(cx, cy, Wd, L), poly([(cx - Wd * 0.7, cy - L + 3), (cx, cy - L - 4), (cx + Wd * 0.7, cy - L + 3)]))
    g = g.buffer(0.9).buffer(-0.9)
    for dd in to_path(g):
        d.append('  <path d="%s" fill="#EEE8D4" stroke="%s" stroke-width="0.42" transform="rotate(%.1f %.1f %.1f)"/>'
                 % (dd, INK2, ang, cx, cy))
    d.append('  <path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="0.24" transform="rotate(%.1f %.1f %.1f)"/>'
             % (cx, cy + L - 2, cx, cy - L + 2, INK3, ang, cx, cy))


# —— 主枝（两段，有弯）——
TA = ((254, 452), (306, 404), (334, 352), (356, 306))
TB2 = ((356, 306), (368, 278), (376, 254), (390, 228))


def bz(p, n=30):
    (x0, y0), (x1, y1), (x2, y2), (x3, y3) = p
    out = []
    for i in range(n):
        t = i / (n - 1)
        u = 1 - t
        out.append((u**3 * x0 + 3 * u * u * t * x1 + 3 * u * t * t * x2 + t**3 * x3,
                    u**3 * y0 + 3 * u * u * t * y1 + 3 * u * t * t * y2 + t**3 * y3))
    return out


P1 = bz(TA)
P2 = bz(TB2)
dpath = "M" + " L".join("%.1f,%.1f" % q for q in P1 + P2)
d.append('  <path d="%s" fill="none" stroke="%s" stroke-width="3.2"/>' % (dpath, INK))
d.append('  <path d="M%s" fill="none" stroke="%s" stroke-width="0.7"/>'
         % (" L".join("%.1f,%.1f" % (x + 5, y) for (x, y) in P1 + P2), INK3))
for i in range(4, len(P1), 6):
    x, y = P1[i]
    d.append('  <path d="M%.1f,%.1f l6,-5" stroke="%s" stroke-width="0.26"/>' % (x - 4, y + 1, INK3))
for i in range(3, len(P2), 6):
    x, y = P2[i]
    d.append('  <path d="M%.1f,%.1f l6,-5" stroke="%s" stroke-width="0.26"/>' % (x - 4, y + 1, INK3))

# —— 花枝（左，自 t≈0.32 分叉）——
d.append('  <path d="M312,368 C292,350 274,338 254,332" fill="none" stroke="%s" stroke-width="1.7"/>' % INK2)
d.append('  <path d="M286,346 C268,342 254,346 246,354" fill="none" stroke="%s" stroke-width="1.2"/>' % INK2)
d.append('  <path d="M254,332 L246,320" fill="none" stroke="%s" stroke-width="1.0"/>' % INK2)
flower(246, 316, 19)
flower(282, 352, 12)
bud(302, 354, 24)
bud(240, 372, -34)

# —— 叶枝（中右，自 t≈0.62 分叉）——
d.append('  <path d="M352,312 C378,296 400,294 420,300" fill="none" stroke="%s" stroke-width="1.5"/>' % INK2)
leaf(376, 280, 22, 24, 7.4)
leaf(398, 286, 40, 22, 6.8)
leaf(418, 300, 58, 20, 6.4)
leaf(360, 298, -18, 21, 6.8)

# —— 果枝（右上）——
d.append('  <path d="M386,232 C402,212 424,208 444,216" fill="none" stroke="%s" stroke-width="1.4"/>' % INK2)
peach(424, 248, 14, 6)
peach(450, 224, 11, -14)

d.append('  <text x="212" y="288" font-size="7.6" fill="%s">①</text>' % RED)
d.append('  <text x="462" y="200" font-size="7.6" fill="%s">②</text>' % RED)
d.append('  <text x="398" y="330" font-size="7.6" fill="%s">③</text>' % RED)

d.append('  <text x="44" y="466" font-size="7.8" fill="%s">① 華　灼灼，华之盛：五瓣圆，蕊多</text>' % INK2)
d.append('  <text x="264" y="466" font-size="7.8" fill="%s">② 實　蕡，实之盛：下端带尖</text>' % INK2)
d.append('  <text x="486" y="466" font-size="7.8" fill="%s">③ 葉　蓁蓁，叶之盛</text>' % INK2)
d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">桃之夭夭，灼灼其華</text>' % INK)
d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">夭夭是少好，不是夭折</text>' % INK3)
d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj006a</text>' % INK3)
d.append('</svg>')
open(os.path.join(FIG, "sj006a-tao-hua-shi-ye.svg"), "w", encoding="utf-8").write("\n".join(d))

import cairosvg
cairosvg.svg2png(url=os.path.join(FIG, "sj006a-tao-hua-shi-ye.svg"), write_to="/tmp/sj006a.png", output_width=920)
print("ok")
