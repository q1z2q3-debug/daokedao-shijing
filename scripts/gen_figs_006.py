# -*- coding: utf-8 -*-
"""SJ006《桃夭》两图。图一：一枝三态（花、实、叶）。图二：宜——始／继／久。"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fig_geo import *
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(ROOT, "assets", "fig")
INK, INK2, INK3, RED, PAPER = "#1F1B17", "#5C544A", "#9A9186", "#994433", "#F7F4EE"
W, H = 760, 540


def header(d, left, title, right):
    d.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    d.append('  <text x="44" y="58" font-size="8.6" letter-spacing="2" fill="%s">%s</text>' % (RED, left))
    d.append('  <text x="380" y="60" text-anchor="middle" font-size="28" letter-spacing="14" fill="%s" font-weight="700">%s</text>' % (INK, title))
    d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">%s</text>' % (INK3, right))
    d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)


d = []
d.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="\'Noto Serif SC\',\'Songti SC\',serif">' % (W, H, W, H))
header(d, "周南 · 六", "桃 夭", "诗三百五篇 · 之六")


def petal(cx, cy, ang, rx=11, ry=17, fill="#F6E7E2"):
    g = comb(ell(cx, cy, rx, ry), poly([(cx - 4, cy - ry + 2), (cx, cy - ry - 3), (cx + 4, cy - ry + 2)]))
    g = g.buffer(1.0).buffer(-1.0)
    for dd in to_path(g):
        d.append('  <path d="%s" fill="%s" stroke="%s" stroke-width="0.5" transform="rotate(%.1f %d %d)"/>'
                 % (dd, fill, INK2, ang, cx, cy))


def flower(cx, cy, r, n=5, red_center=False):
    for i in range(n):
        ang = i * 360.0 / n
        petal(cx, cy - r, ang)
    d.append('  <circle cx="%d" cy="%d" r="3.2" fill="%s" stroke="%s" stroke-width="0.4"/>'
             % (cx, cy, (RED if red_center else "#E8D8BC"), INK2))
    for i in range(7):
        a = i * math.tau / 7 + 0.3
        d.append('  <path d="M%d,%d L%.1f,%.1f" stroke="%s" stroke-width="0.3"/>'
                 % (cx, cy, cx + (r - 2) * 0.72 * math.cos(a), cy + (r - 2) * 0.72 * math.sin(a), INK3))
        d.append('  <circle cx="%.1f" cy="%.1f" r="0.9" fill="%s"/>'
                 % (cx + (r - 2) * 0.72 * math.cos(a), cy + (r - 2) * 0.72 * math.sin(a), INK2))


def bud(cx, cy, ang):
    g = comb(ell(cx, cy, 5.2, 8.0), poly([(cx - 2.4, cy - 6.6), (cx, cy - 9.6), (cx + 2.4, cy - 6.6)]))
    g = g.buffer(0.8).buffer(-0.8)
    for dd in to_path(g):
        d.append('  <path d="%s" fill="#F3DDD6" stroke="%s" stroke-width="0.45" transform="rotate(%.1f %.1f %.1f)"/>'
                 % (dd, INK2, ang, cx, cy))


def peach(cx, cy, r, ang=0):
    g = ell(cx, cy, r, r * 1.02)
    g = comb(g, poly([(cx - r * 0.55, cy + r * 0.75), (cx, cy + r * 1.12), (cx + r * 0.55, cy + r * 0.75)]))
    g = g.buffer(1.2).buffer(-1.2)
    for dd in to_path(g):
        d.append('  <path d="%s" fill="%s" stroke="%s" stroke-width="0.55" transform="rotate(%.1f %d %d)"/>'
                 % (dd, "#F7E9DE", INK2, ang, cx, cy))
    d.append('  <path d="M%d,%d C%.1f,%.1f %.1f,%.1f %d,%.1f" fill="none" stroke="%s" stroke-width="0.36"/>'
             % (cx, cy - r * 0.9, cx + r * 0.3, cy - r * 0.2, cx + r * 0.28, cy + r * 0.4, cx + 2, cy + r * 0.85, INK3))


def leaf(cx, cy, ang, L=26, Wd=8.5, teeth=True, sh=0.9):
    """桃叶：狭长披针，缘有小齿"""
    g = comb(ell(cx, cy, Wd, L), poly([(cx - Wd * 0.8, cy - L + 4), (cx, cy - L - 5), (cx + Wd * 0.8, cy - L + 4)]))
    g = g.buffer(1.0).buffer(-1.0)
    for dd in to_path(g):
        d.append('  <path d="%s" fill="%s" stroke="%s" stroke-width="0.45" transform="rotate(%.1f %.1f %.1f)"/>'
                 % (dd, "#EDE7D2", INK2, ang, cx, cy))
    d.append('  <path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="0.26" transform="rotate(%.1f %.1f %.1f)"/>'
             % (cx, cy + L - 2, cx, cy - L + 3, INK3, ang, cx, cy))
    if teeth:
        for k in range(4):
            yy = cy + L * 0.5 - k * L * 0.38
            d.append('  <path d="M%.1f,%.1f l4,-2" stroke="%s" stroke-width="0.2" transform="rotate(%.1f %.1f %.1f)"/>'
                     % (cx + Wd * 0.98, yy, INK3, ang, cx, cy))
            d.append('  <path d="M%.1f,%.1f l-4,-2" stroke="%s" stroke-width="0.2" transform="rotate(%.1f %.1f %.1f)"/>'
                     % (cx - Wd * 0.98, yy, INK3, ang, cx, cy))


# —— 主枝 ——
d.append('  <path d="M286,452 C330,404 366,344 396,264" fill="none" stroke="%s" stroke-width="3.4"/>' % INK)
d.append('  <path d="M291,448 C334,400 370,340 400,262" fill="none" stroke="%s" stroke-width="0.8"/>' % INK3)
# 主枝树皮纹
for t in (0.15, 0.3, 0.45, 0.6, 0.75):
    x = 286 + (396 - 286) * t + 6
    y = 452 - (452 - 264) * t - 6
    d.append('  <path d="M%.1f,%.1f l6,-4" stroke="%s" stroke-width="0.28"/>' % (x, y, INK3))

# 花枝（左）
d.append('  <path d="M330,352 C306,336 284,326 262,318" fill="none" stroke="%s" stroke-width="1.8"/>' % INK2)
flower(246, 302, 24)
flower(292, 336, 17, red_center=True)
bud(268, 344, -28)
bud(310, 318, 20)
# 叶枝（中右）
d.append('  <path d="M366,314 C390,300 412,296 432,300" fill="none" stroke="%s" stroke-width="1.6"/>' % INK2)
leaf(392, 280, 26, 26, 8.4)
leaf(414, 288, 44, 24, 7.8, sh=0.85)
leaf(434, 300, 62, 22, 7.2)
leaf(376, 300, -14, 23, 7.6)
# 果枝（右上）
d.append('  <path d="M396,264 C412,242 432,236 452,242" fill="none" stroke="%s" stroke-width="1.5"/>' % INK2)
peach(430, 268, 15, 8)
peach(456, 246, 12, -12)

# 编号
d.append('  <text x="216" y="270" font-size="7.6" fill="%s">①</text>' % RED)
d.append('  <text x="464" y="222" font-size="7.6" fill="%s">②</text>' % RED)
d.append('  <text x="404" y="330" font-size="7.6" fill="%s">③</text>' % RED)

d.append('  <text x="44" y="466" font-size="7.8" fill="%s">① 華　灼灼，华之盛：五瓣，蕊多</text>' % INK2)
d.append('  <text x="264" y="466" font-size="7.8" fill="%s">② 實　蕡，实之盛：下端带尖</text>' % INK2)
d.append('  <text x="486" y="466" font-size="7.8" fill="%s">③ 葉　蓁蓁，叶之盛</text>' % INK2)
d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">桃之夭夭，灼灼其華</text>' % INK)
d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">夭夭是少好，不是夭折</text>' % INK3)
d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj006a</text>' % INK3)
d.append('</svg>')
open(os.path.join(FIG, "sj006a-tao-hua-shi-ye.svg"), "w", encoding="utf-8").write("\n".join(d))

# ============ 图二 ============
e = []
e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="\'Noto Serif SC\',\'Songti SC\',serif">' % (W, H, W, H))
e.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
e.append('  <rect x="10" y="10" width="740" height="500" fill="none" stroke="%s" stroke-width="1"/>' % INK3)
e.append('  <rect x="16" y="16" width="728" height="488" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
e.append('  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="%s" font-weight="700">始 · 繼 · 久</text>' % INK)
e.append('  <text x="380" y="74" text-anchor="middle" font-size="9.6" letter-spacing="2" fill="%s">《诗经》周南 · 第六篇　桃夭</text>' % INK2)
e.append('  <defs><marker id="ar6" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % RED)
cells = [(70, "華", "灼灼其华", "嫁时", INK2), (290, "實", "有蕡其实", "有后", RED), (510, "葉", "其叶蓁蓁", "族盛", INK2)]
for (x, big, s1, s2, col) in cells:
    e.append('  <rect x="%d" y="150" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (x, col))
    e.append('  <text x="%d" y="214" text-anchor="middle" font-size="26" letter-spacing="2" fill="%s" font-weight="700">%s</text>' % (x + 75, col, big))
    e.append('  <text x="%d" y="254" text-anchor="middle" font-size="10" fill="#3B352F">%s</text>' % (x + 75, s1))
    e.append('  <text x="%d" y="278" text-anchor="middle" font-size="8" fill="%s">%s</text>' % (x + 75, INK3, s2))
e.append('  <line x1="220" y1="225" x2="288" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar6)"/>' % RED)
e.append('  <line x1="440" y1="225" x2="508" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar6)"/>' % RED)
e.append('  <text x="380" y="330" text-anchor="middle" font-size="8.4" fill="%s">不夸色，不夸家世，只反复说一个「宜」——宜者，相安</text>' % INK2)
e.append('  <line x1="120" y1="360" x2="640" y2="360" stroke="%s" stroke-width="0.8"/>' % INK3)
e.append('  <text x="230" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">宜其室家</text>' % RED)
e.append('  <text x="230" y="414" text-anchor="middle" font-size="7.4" fill="%s">始：一人入门，一家先安</text>' % INK3)
e.append('  <text x="530" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">宜其家人</text>' % RED)
e.append('  <text x="530" y="414" text-anchor="middle" font-size="7.4" fill="%s">久：由家及人，字序升格</text>' % INK3)
e.append('  <text x="380" y="446" text-anchor="middle" font-size="7.4" fill="%s">《诗》三章　·　花一时，实一季，叶一年</text>' % INK3)
e.append('  <text x="120" y="512" font-size="5.6" fill="%s">诗经 · 周南</text>' % INK2)
e.append('  <text x="640" y="512" text-anchor="end" font-size="5.6" fill="%s">图二 · 始继久 · sj006b</text>' % INK2)
e.append('</svg>')
open(os.path.join(FIG, "sj006b-yi-wei-ti-yan.svg"), "w", encoding="utf-8").write("\n".join(e))

import cairosvg
for k in ["sj006a-tao-hua-shi-ye", "sj006b-yi-wei-ti-yan"]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok")
