# -*- coding: utf-8 -*-
"""SJ003《卷耳》两图。名物：卷耳、顷筐、金罍与兕觥。义理：此地／怀人／彼处三格。"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fig_geo import *
from shapely.geometry import LineString

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
head(d, "周南 · 三", "卷 耳", "诗三百五篇 · 之三")

# 地平（浅）
d.append('  <path d="M52,404 C160,394 300,390 430,394 C560,398 660,402 708,404" fill="none" stroke="%s" stroke-width="0.25" stroke-dasharray="8 5 2 5"/>' % INK3)

# 卷耳：茎 + 三叶 + 两果
d.append('  <path d="M96,404 C104,378 112,352 126,330 C136,314 148,300 162,292" fill="none" stroke="%s" stroke-width="1.9"/>' % INK2)
d.append('  <path d="M126,330 C140,338 156,342 172,342" fill="none" stroke="%s" stroke-width="1.1"/>' % INK2)
d.append('  <path d="M140,316 C156,320 170,318 182,312" fill="none" stroke="%s" stroke-width="1.0"/>' % INK2)


def sunlef(cx, cy, rot=0, sc=1.0, dark=False):
    """苍耳叶：卵形而阔，端有尖"""
    g = comb(ell(cx, cy, 12 * sc, 15 * sc), poly([(cx - 5 * sc, cy - 13 * sc), (cx, cy - 19 * sc), (cx + 5 * sc, cy - 13 * sc)]))
    g = g.buffer(1.4).buffer(-1.4)
    d.append('  <path d="%s" fill="%s" stroke="%s" stroke-width="%s" transform="rotate(%s %s %s)"/>'
             % (to_path(g)[0], PAPER, INK if dark else INK2, 0.55 if dark else 0.42, rot, cx, cy))
    d.append('  <path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="0.22" transform="rotate(%s %s %s)"/>'
             % (cx, cy + 8 * sc, cx, cy - 16 * sc, INK3, rot, cx, cy))
    for s2 in (-1, 1):
        d.append('  <path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="0.18" transform="rotate(%s %s %s)"/>'
                 % (cx + s2 * 3 * sc, cy - 2 * sc, cx + s2 * 8 * sc, cy + 6 * sc, INK3, rot, cx, cy))


sunlef(112, 336, -16, 1.25)
sunlef(150, 302, 10, 1.15, True)
sunlef(186, 318, 26, 1.0)
sunlef(96, 374, -34, 1.0)

# 果实：带刺球 ×2
for (fx, fy, r) in [(196, 288, 11), (178, 268, 9)]:
    d.append('  <circle cx="%d" cy="%d" r="%d" fill="%s" stroke="%s" stroke-width="0.55"/>' % (fx, fy, r, "#EFE8DB", INK))
    for a in range(14):
        import math
        ang = a * math.tau / 14
        x1, y1 = fx + r * math.cos(ang), fy + r * math.sin(ang)
        x2, y2 = fx + (r + 3.6) * math.cos(ang + 0.18), fy + (r + 3.6) * math.sin(ang + 0.18)
        d.append('  <path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="0.3"/>' % (x1, y1, x2, y2, INK2))
d.append('  <path d="M186,300 C192,296 196,292 196,288" fill="none" stroke="%s" stroke-width="0.4"/>' % INK2)
d.append('  <text x="212" y="264" font-size="7.6" fill="%s">①</text>' % RED)

# 顷筐
d.append('  <path d="M286,356 C286,392 300,412 330,414 C360,412 374,392 374,356" fill="none" stroke="%s" stroke-width="0.6"/>' % INK)
d.append('  <ellipse cx="330" cy="356" rx="44" ry="9" fill="%s" stroke="%s" stroke-width="0.6"/>' % (PAPER, INK))
d.append('  <ellipse cx="330" cy="357" rx="38" ry="6.4" fill="none" stroke="%s" stroke-width="0.3"/>' % INK3)
for i in range(1, 6):
    y = 364 + i * 7
    w = 42 - i * 1.6
    d.append('  <path d="M%.1f,%d C%d,%d %.1f,%d %.1f,%d" fill="none" stroke="%s" stroke-width="0.28"/>' % (330 - w, y, 330 - w * 0.4, y + 2, 330 + w * 0.4, y + 2, 330 + w, y, INK3))
for k in (-0.6, -0.2, 0.2, 0.6):
    d.append('  <path d="M%.1f,%d L%.1f,%d" stroke="%s" stroke-width="0.3"/>' % (330 + 42 * k, 358, 330 + 40 * k, 410, INK2))
# 筐中三枚果
for (gx, gy) in [(322, 352), (338, 351), (330, 347)]:
    d.append('  <circle cx="%d" cy="%d" r="5" fill="#EFE8DB" stroke="%s" stroke-width="0.4"/>' % (gx, gy, INK2))
    for a in range(8):
        import math
        ang = a * math.tau / 8
        d.append('  <path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="0.22"/>' % (gx + 5 * math.cos(ang), gy + 5 * math.sin(ang), gx + 7 * math.cos(ang), gy + 7 * math.sin(ang), INK3))
d.append('  <text x="284" y="340" font-size="7.6" fill="%s">②</text>' % RED)

# 金罍
d.append('  <path d="M470,268 C462,282 458,296 458,310 C458,340 476,360 502,360 C528,360 546,340 546,310 C546,296 542,282 534,268" fill="%s" stroke="%s" stroke-width="0.6"/>' % (PAPER, INK))
d.append('  <path d="M470,268 C476,262 528,262 534,268" fill="none" stroke="%s" stroke-width="0.5"/>' % INK)
d.append('  <ellipse cx="502" cy="264" rx="13" ry="3.4" fill="none" stroke="%s" stroke-width="0.45"/>' % INK2)
# 双耳
for sx in (-1, 1):
    d.append('  <path d="M%.1f,276 C%.1f,272 %.1f,286 %.1f,296" fill="none" stroke="%s" stroke-width="0.5"/>' % (502 + sx * 32, 502 + sx * 46, 502 + sx * 48, 502 + sx * 34, INK2))
# 圈足
d.append('  <path d="M474,360 L484,378 L520,378 L530,360" fill="none" stroke="%s" stroke-width="0.5"/>' % INK2)
# 纹带
for y in (296, 318):
    d.append('  <path d="M462,%d C480,%d 524,%d 542,%d" fill="none" stroke="%s" stroke-width="0.3"/>' % (y, y - 2, y - 2, y, INK3))
d.append('  <path d="M478,332 C492,338 512,338 526,332" fill="none" stroke="%s" stroke-width="0.26"/>' % INK3)

# 兕觥（角杯，竖置，口宽底窄）
d.append('  <path d="M578,268 L644,268 C646,300 638,344 622,382 L604,382 C584,346 576,302 578,268 Z" fill="%s" stroke="%s" stroke-width="0.6"/>' % (PAPER, INK))
d.append('  <path d="M578,268 L644,268" fill="none" stroke="%s" stroke-width="0.35"/>' % INK2)
d.append('  <path d="M582,276 C594,282 628,282 640,276" fill="none" stroke="%s" stroke-width="0.3"/>' % INK3)
d.append('  <path d="M584,306 C596,300 626,300 638,306" fill="none" stroke="%s" stroke-width="0.32"/>' % INK2)
d.append('  <path d="M590,336 C602,332 622,332 632,336" fill="none" stroke="%s" stroke-width="0.26"/>' % INK3)
d.append('  <ellipse cx="613" cy="382" rx="9.5" ry="3" fill="none" stroke="%s" stroke-width="0.4"/>' % INK2)
d.append('  <path d="M580,284 C572,288 572,300 580,304" fill="none" stroke="%s" stroke-width="0.4"/>' % INK2)
d.append('  <text x="502" y="252" font-size="7.6" fill="%s">③</text>' % RED)
d.append('  <text x="470" y="398" text-anchor="middle" font-size="7.2" fill="%s">金罍</text>' % INK2)
d.append('  <text x="624" y="408" text-anchor="middle" font-size="7.2" fill="%s">兕觥</text>' % INK2)

d.append('  <text x="44" y="466" font-size="7.8" fill="%s">① 卷耳　苓耳即苍耳，果带短刺，扎手难采</text>' % INK2)
d.append('  <text x="286" y="466" font-size="7.8" fill="%s">② 顷筐　畚属，易盈之器</text>' % INK2)
d.append('  <text x="486" y="466" font-size="7.8" fill="%s">③ 金罍与兕觥　一盛一分，皆酒器</text>' % INK2)
foot(d, "采采卷耳，不盈頃筐", "器易盈，而筐不盈", "图一 · 名物 · sj003a")
d.append('</svg>')
open(os.path.join(FIG, "sj003a-juan-er-qing-kuang.svg"), "w", encoding="utf-8").write("\n".join(d))

# ============ 图二：此地／怀人／彼处 ============
e = []
e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="\'Noto Serif SC\',\'Songti SC\',serif">' % (W, H, W, H))
e.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
e.append('  <rect x="10" y="10" width="740" height="500" fill="none" stroke="%s" stroke-width="1"/>' % INK3)
e.append('  <rect x="16" y="16" width="728" height="488" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
e.append('  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="%s" font-weight="700">此 地 · 彼 处</text>' % INK)
e.append('  <text x="380" y="74" text-anchor="middle" font-size="9.6" letter-spacing="2" fill="%s">《诗经》周南 · 第三篇　卷耳</text>' % INK2)
e.append('  <defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % RED)
for (x, big, s1, s2, col) in [(70, "此地", "采采卷耳", "一章", INK2), (290, "怀人", "不盈顷筐", "中轴", RED), (510, "彼处", "马瘏仆痡", "二至四章", INK2)]:
    e.append('  <rect x="%d" y="150" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (x, col))
    e.append('  <text x="%d" y="212" text-anchor="middle" font-size="24" letter-spacing="3" fill="%s" font-weight="700">%s</text>' % (x + 75, col, big))
    e.append('  <text x="%d" y="250" text-anchor="middle" font-size="10" fill="#3B352F">%s</text>' % (x + 75, s1))
    e.append('  <text x="%d" y="276" text-anchor="middle" font-size="8" fill="%s">%s</text>' % (x + 75, INK3, s2))
e.append('  <line x1="220" y1="225" x2="288" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar)"/>' % RED)
e.append('  <line x1="440" y1="225" x2="508" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar)"/>' % RED)
e.append('  <text x="380" y="330" text-anchor="middle" font-size="8.4" fill="%s">两幅并置，中间一根线：她在此，他在彼——诗不许他们相见</text>' % INK2)
e.append('  <line x1="120" y1="360" x2="640" y2="360" stroke="%s" stroke-width="0.8"/>' % INK3)
e.append('  <text x="230" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">维以不永怀</text>' % RED)
e.append('  <text x="230" y="414" text-anchor="middle" font-size="7.4" fill="%s">酒为忘，不为乐</text>' % INK3)
e.append('  <text x="530" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">云何吁矣</text>' % RED)
e.append('  <text x="530" y="414" text-anchor="middle" font-size="7.4" fill="%s">三「矣」之后，唯一的出声</text>' % INK3)
e.append('  <text x="380" y="446" text-anchor="middle" font-size="7.4" fill="%s">《诗》四章　·　一幅独起，三幅一排</text>' % INK3)
e.append('  <text x="120" y="512" font-size="5.6" fill="%s">诗经 · 周南</text>' % INK2)
e.append('  <text x="640" y="512" text-anchor="end" font-size="5.6" fill="%s">图二 · 此地彼处 · sj003b</text>' % INK2)
e.append('</svg>')
open(os.path.join(FIG, "sj003b-ci-bi-bi-ci.svg"), "w", encoding="utf-8").write("\n".join(e))

import cairosvg
for k in ["sj003a-juan-er-qing-kuang", "sj003b-ci-bi-bi-ci"]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok")
