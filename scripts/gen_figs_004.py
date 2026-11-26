# -*- coding: utf-8 -*-
"""SJ004《樛木》两图。名物：下曲之木 + 葛藟三态。义理：樛／累／成 三格。"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fig_geo import *
from shapely.geometry import LineString, Point

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(ROOT, "assets", "fig")
INK, INK2, INK3, RED, PAPER = "#1F1B17", "#5C544A", "#9A9186", "#994433", "#F7F4EE"
W, H = 760, 540


def head(d, no, title, right):
    d.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    d.append('  <text x="44" y="58" font-size="8.6" letter-spacing="2" fill="%s">%s</text>' % (RED, no))
    d.append('  <text x="380" y="60" text-anchor="middle" font-size="28" letter-spacing="14" fill="%s" font-weight="700">%s</text>' % (INK, title))
    d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">%s</text>' % (INK3, right))
    d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)


def foot(d, quote, lefts, tag):
    d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
    d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">%s</text>' % (INK, quote))
    d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">%s</text>' % (INK3, lefts))
    d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">%s</text>' % (INK3, tag))


# ============ 图一 ============
d = []
d.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="\'Noto Serif SC\',\'Songti SC\',serif">' % (W, H, W, H))
head(d, "周南 · 四", "樛 木", "诗三百五篇 · 之四")

TB = ((300, 448), (290, 352), (302, 252), (297, 196))
BR = ((297, 196), (340, 210), (404, 254), (450, 312))
TP = ((450, 312), (466, 338), (450, 354), (434, 342))
S1 = ((300, 322), (264, 330), (242, 356), (238, 376))
S2 = ((299, 254), (328, 240), (346, 242), (356, 256))


def bez(p, n=40):
    (x0, y0), (x1, y1), (x2, y2), (x3, y3) = p
    out = []
    for i in range(n):
        t = i / (n - 1)
        u = 1 - t
        out.append((u**3 * x0 + 3 * u * u * t * x1 + 3 * u * t * t * x2 + t**3 * x3,
                    u**3 * y0 + 3 * u * u * t * y1 + 3 * u * t * t * y2 + t**3 * y3))
    return out


def wood(p, wdt, n=44):
    pl = bez(p, n)
    discs = [Point(x, y).buffer(wdt, resolution=14) for (x, y) in pl]
    g = comb(*discs).buffer(-1.5, resolution=4)
    for dd in to_path(g):
        d.append('  <path d="%s" fill="%s" stroke="%s" stroke-width="0.6"/>' % (dd, "#F1EBDD", INK))
    return pl


TR = wood(TB, 6.6)
BRPL = wood(BR, 5.0, 48)
wood(TP, 2.2, 14)
wood(S1, 2.0, 16)
wood(S2, 1.6, 12)

for off in (-2.4, 0.6, 2.9):
    seg = []
    for i in range(12, len(TR) - 14, 2):
        x, y = TR[i]
        seg.append((x + off + math.sin(i * 0.7) * 0.5, y))
    if seg:
        d.append('  <path d="M%s" fill="none" stroke="%s" stroke-width="0.22"/>'
                 % (" L".join("%.1f,%.1f" % q for q in seg), INK3))

d.append('  <path d="M206,448 C248,452 340,453 402,448" fill="none" stroke="%s" stroke-width="0.28" stroke-dasharray="7 4 1.5 4"/>' % INK3)


def rnd(k):
    return (math.sin(k * 12.9898) * 43758.5453) % 1.0


def leaf(cx, cy, rot, sc=1.0, red=False):
    g = comb(ell(cx, cy, 4.4 * sc, 7.4 * sc), poly([(cx - 2.1 * sc, cy - 6.2 * sc), (cx, cy - 9.8 * sc), (cx + 2.1 * sc, cy - 6.2 * sc)]))
    g = g.buffer(0.8).buffer(-0.8)
    for dd in to_path(g):
        d.append('  <path d="%s" fill="%s" stroke="%s" stroke-width="0.32" transform="rotate(%.1f %.1f %.1f)"/>'
                 % (dd, ("#FAEDE7" if red else "#F4F0E4"), (RED if red else INK3), rot, cx, cy))
    d.append('  <path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="0.16" transform="rotate(%.1f %.1f %.1f)"/>'
             % (cx, cy + 5 * sc, cx, cy - 6.8 * sc, (RED if red else INK3), rot, cx, cy))


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


def cluster(u0, u1, n, sz, red=False, spread=7.0):
    for k in range(n):
        u = u0 + (u1 - u0) * (k / max(1, n - 1))
        x, y, nx, ny = at(u)
        r1, r2 = rnd(k * 1.7), rnd(k * 3.1 + 4)
        side = 1 if k % 2 == 0 else -1
        off = 2.0 + r2 * spread
        cx = x + nx * side * off + ny * (r1 - 0.5) * 16
        cy = y + ny * side * off - nx * (r1 - 0.5) * 16
        ang = math.degrees(math.atan2(-ny * side, -nx * side)) + (r1 - 0.5) * 46
        leaf(cx, cy, ang, sz * (0.85 + r2 * 0.3), red)


def strand(u0, u1, loops, amp, wdt=1.3):
    pts = []
    for i in range(60):
        u = u0 + (u1 - u0) * i / 59
        x, y, nx, ny = at(u)
        s = amp * math.sin((i / 59) * loops * math.tau)
        pts.append((x + nx * s, y + ny * s))
    d.append('  <path d="M%s" fill="none" stroke="%s" stroke-width="%.2f"/>'
             % (" L".join("%.1f,%.1f" % q for q in pts), INK2, wdt))


strand(0.04, 0.34, 1.6, 5.0)
cluster(0.04, 0.34, 7, 0.9, spread=4.5)
strand(0.33, 0.72, 2.4, 6.2)
cluster(0.33, 0.72, 22, 0.95, spread=6.0)
strand(0.71, 1.0, 2.0, 5.2)
cluster(0.71, 1.0, 11, 0.86, red=True, spread=5.0)
d.append('  <path d="M456,330 c7,7 15,2 13,-6 c-2,-7 -9,-6 -10,1" fill="none" stroke="%s" stroke-width="1.0"/>' % RED)
d.append('  <path d="M446,344 c5,9 14,6 14,-2" fill="none" stroke="%s" stroke-width="0.9"/>' % INK2)
strand(0.3, 1.0, 1.8, 4.5, 1.15)
cluster(0.45, 1.0, 6, 0.72, spread=3.6)

d.append('  <text x="352" y="192" font-size="7.6" fill="%s">①</text>' % RED)
d.append('  <text x="406" y="250" font-size="7.6" fill="%s">②</text>' % RED)
d.append('  <text x="470" y="326" font-size="7.6" fill="%s">③</text>' % RED)
d.append('  <text x="268" y="206" font-size="7.2" fill="%s">樛</text>' % INK2)
d.append('  <text x="440" y="370" font-size="7.2" fill="%s">垂</text>' % INK2)

d.append('  <text x="44" y="466" font-size="7.8" fill="%s">① 樛木　木下曲曰樛：枝肯垂，高处才让得出来</text>' % INK2)
d.append('  <text x="300" y="466" font-size="7.8" fill="%s">② 葛藟　似葛而细，蔓生附木</text>' % INK2)
d.append('  <text x="516" y="466" font-size="7.8" fill="%s">③ 累／荒／萦　系、掩、旋</text>' % INK2)
foot(d, "南有樛木，葛藟縈之", "下曲非折，是让", "图一 · 名物 · sj004a")
d.append('</svg>')
open(os.path.join(FIG, "sj004a-jiong-mu-ge-lei.svg"), "w", encoding="utf-8").write("\n".join(d))

# ============ 图二 ============
e = []
e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="\'Noto Serif SC\',\'Songti SC\',serif">' % (W, H, W, H))
e.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
e.append('  <rect x="10" y="10" width="740" height="500" fill="none" stroke="%s" stroke-width="1"/>' % INK3)
e.append('  <rect x="16" y="16" width="728" height="488" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
e.append('  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="%s" font-weight="700">下 逮 · 上 附</text>' % INK)
e.append('  <text x="380" y="74" text-anchor="middle" font-size="9.6" letter-spacing="2" fill="%s">《诗经》周南 · 第四篇　樛木</text>' % INK2)
e.append('  <defs><marker id="ar4" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % RED)
cells = [(70, "樛", "木下曲", "让位", INK2), (290, "累", "葛藟得上", "得所附", RED), (510, "成", "福履成之", "打成结", INK2)]
for (x, big, s1, s2, col) in cells:
    e.append('  <rect x="%d" y="150" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (x, col))
    e.append('  <text x="%d" y="212" text-anchor="middle" font-size="24" letter-spacing="3" fill="%s" font-weight="700">%s</text>' % (x + 75, col, big))
    e.append('  <text x="%d" y="250" text-anchor="middle" font-size="10" fill="#3B352F">%s</text>' % (x + 75, s1))
    e.append('  <text x="%d" y="276" text-anchor="middle" font-size="8" fill="%s">%s</text>' % (x + 75, INK3, s2))
e.append('  <line x1="220" y1="225" x2="288" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar4)"/>' % RED)
e.append('  <line x1="440" y1="225" x2="508" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar4)"/>' % RED)
e.append('  <text x="380" y="330" text-anchor="middle" font-size="8.4" fill="%s">木肯垂一寸，藤才上得一尺——德不是给，是让</text>' % INK2)
e.append('  <line x1="120" y1="360" x2="640" y2="360" stroke="%s" stroke-width="0.8"/>' % INK3)
e.append('  <text x="230" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">下逮</text>' % RED)
e.append('  <text x="230" y="414" text-anchor="middle" font-size="7.4" fill="%s">在上者肯下，非屈尊</text>' % INK3)
e.append('  <text x="530" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">上附</text>' % RED)
e.append('  <text x="530" y="414" text-anchor="middle" font-size="7.4" fill="%s">在下者得所，非攀附</text>' % INK3)
e.append('  <text x="380" y="446" text-anchor="middle" font-size="7.4" fill="%s">《诗》三章　·　一韵一换，祝福三阶</text>' % INK3)
e.append('  <text x="120" y="512" font-size="5.6" fill="%s">诗经 · 周南</text>' % INK2)
e.append('  <text x="640" y="512" text-anchor="end" font-size="5.6" fill="%s">图二 · 下逮上附 · sj004b</text>' % INK2)
e.append('</svg>')
open(os.path.join(FIG, "sj004b-xia-dai-shang-fu.svg"), "w", encoding="utf-8").write("\n".join(e))

import cairosvg
for k in ["sj004a-jiong-mu-ge-lei", "sj004b-xia-dai-shang-fu"]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok")
