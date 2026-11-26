# -*- coding: utf-8 -*-
"""SJ011《麟之趾》两图。图一：麟之趾/定/角。图二：身三处·族三阶。"""
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
d.append('  <text x="44" y="58" font-size="8.6" letter-spacing="2" fill="%s">周南 · 十一</text>' % RED)
d.append('  <text x="380" y="60" text-anchor="middle" font-size="26" letter-spacing="10" fill="%s" font-weight="700">麟 之 趾</text>' % INK)
d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之十一</text>' % INK3)
d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)

def cell(x, y, label):
    d.append('  <rect x="%d" y="%d" width="190" height="180" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % (x, y, INK3))
    d.append('  <text x="%d" y="%d" font-size="8.2" letter-spacing="3" fill="%s">%s</text>' % (x + 12, y + 20, RED, label))


CY = 190
cell(84, CY, "壹　趾")
cell(285, CY, "贰　定")
cell(486, CY, "叁　角")

# —— 壹 · 蹄（圆厚不裂） ——
d.append('  <path d="M150,318 C150,282 198,282 198,318 Z" fill="#EFEAD6" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <line x1="174" y1="286" x2="174" y2="318" stroke="%s" stroke-width="0.7"/>' % INK3)
d.append('  <path d="M150,318 C160,322 188,322 198,318" fill="none" stroke="%s" stroke-width="1.6"/>' % INK)
d.append('  <path d="M158,284 L150,240 M192,284 L200,240" stroke="%s" stroke-width="1.6"/>' % INK2)
d.append('  <text x="179" y="342" text-anchor="middle" font-size="7.4" fill="%s">蹄　圆厚，不裂</text>' % INK2)

# —— 贰 · 额（定即题） ——
d.append('  <path d="M322,300 C330,286 344,280 358,280 C374,280 386,288 392,300 C398,312 396,324 388,332 C376,342 350,344 334,338 L322,300" fill="#EFEAD6" stroke="%s" stroke-width="1.1"/>' % INK2)
# 角基与角
d.append('  <path d="M358,280 C354,270 356,260 362,254" fill="none" stroke="%s" stroke-width="2.2"/>' % INK)
d.append('  <circle cx="363" cy="250" r="4.2" fill="#EFEAD6" stroke="%s" stroke-width="0.8"/>' % INK2)
# 耳
d.append('  <path d="M330,292 l-11,-7 l12,-1 Z" fill="#EFEAD6" stroke="%s" stroke-width="0.7"/>' % INK2)
# 眼与吻
d.append('  <circle cx="360" cy="306" r="2.3" fill="none" stroke="%s" stroke-width="0.7"/>' % INK)
d.append('  <path d="M392,306 q6,5 0,10" fill="none" stroke="%s" stroke-width="0.5"/>' % INK3)
# 额标红
d.append('  <circle cx="372" cy="292" r="2.8" fill="none" stroke="%s" stroke-width="1.0"/>' % RED)
d.append('  <text x="384" y="286" font-size="6.6" fill="%s">额</text>' % RED)
d.append('  <text x="380" y="352" text-anchor="middle" font-size="7.4" fill="%s">定　题也，即额</text>' % INK2)

# —— 叁 · 角（端有肉） ——
d.append('  <path d="M556,336 C548,300 552,268 570,246" fill="none" stroke="%s" stroke-width="2.4"/>' % INK)
d.append('  <path d="M566,338 C558,302 562,270 578,250" fill="none" stroke="%s" stroke-width="1.0" opacity="0.75"/>' % INK3)
d.append('  <circle cx="573" cy="242" r="8.0" fill="#EFEAD6" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <circle cx="573" cy="242" r="4.6" fill="none" stroke="%s" stroke-width="0.7"/>' % INK3)
d.append('  <text x="592" y="238" font-size="6.6" fill="%s">端有肉</text>' % RED)
d.append('  <text x="583" y="342" text-anchor="middle" font-size="7.4" fill="%s">角　钝而不刺</text>' % INK2)

# 说明
d.append('  <text x="44" y="466" font-size="7.8" fill="%s">麟：麕身、牛尾、马蹄、一角</text>' % INK2)
d.append('  <text x="264" y="466" font-size="7.8" fill="%s">三处皆能伤，而皆不伤</text>' % INK2)
d.append('  <text x="486" y="466" font-size="7.8" fill="%s">角端一圈钝，是其仁处</text>' % INK2)
d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">麟之趾，振振公子</text>' % INK)
d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">贵在不害</text>' % INK3)
d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj011a</text>' % INK3)
d.append('</svg>')
open(os.path.join(FIG, "sj011a-lin-zhi-zhi-ding-jiao.svg"), "w", encoding="utf-8").write("\n".join(d))

# ============ 图二 ============
e = []
e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="\'Noto Serif SC\',\'Songti SC\',serif">' % (W, H, W, H))
e.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
e.append('  <rect x="10" y="10" width="740" height="500" fill="none" stroke="%s" stroke-width="1"/>' % INK3)
e.append('  <rect x="16" y="16" width="728" height="488" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
e.append('  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="%s" font-weight="700">身 三 处 · 族 三 阶</text>' % INK)
e.append('  <text x="380" y="74" text-anchor="middle" font-size="9.6" letter-spacing="2" fill="%s">《诗经》周南 · 第十一篇　麟之趾</text>' % INK2)
e.append('  <defs><marker id="ar11" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % RED)
cells = [(70, "趾", "振振公子", "一人之足", INK2), (290, "定", "振振公姓", "同姓之额", RED), (510, "角", "振振公族", "一族之锋", INK2)]
for (x, big, s1, s2, col) in cells:
    e.append('  <rect x="%d" y="150" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (x, col))
    e.append('  <text x="%d" y="214" text-anchor="middle" font-size="28" letter-spacing="2" fill="%s" font-weight="700">%s</text>' % (x + 75, col, big))
    e.append('  <text x="%d" y="252" text-anchor="middle" font-size="10" fill="#3B352F">%s</text>' % (x + 75, s1))
    e.append('  <text x="%d" y="278" text-anchor="middle" font-size="8" fill="%s">%s</text>' % (x + 75, INK3, s2))
e.append('  <line x1="220" y1="225" x2="288" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar11)"/>' % RED)
e.append('  <line x1="440" y1="225" x2="508" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar11)"/>' % RED)
e.append('  <text x="380" y="322" text-anchor="middle" font-size="8.4" fill="%s">身自下而上（趾→额→角）　族自近而远（公子→公姓→公族）</text>' % INK2)
e.append('  <text x="380" y="338" text-anchor="middle" font-size="7.6" fill="%s">两序交叉，全篇只换四字</text>' % INK3)
e.append('  <line x1="120" y1="360" x2="640" y2="360" stroke="%s" stroke-width="0.8"/>' % INK3)
e.append('  <text x="230" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">振振</text>' % RED)
e.append('  <text x="230" y="414" text-anchor="middle" font-size="7.4" fill="%s">仁厚之貌，非「振作」</text>' % INK3)
e.append('  <text x="530" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">于嗟</text>' % RED)
e.append('  <text x="530" y="414" text-anchor="middle" font-size="7.4" fill="%s">叹也，「于」通「吁」</text>' % INK3)
e.append('  <text x="380" y="446" text-anchor="middle" font-size="7.4" fill="%s">周南十一篇终　·　以夫妇始，以公族终</text>' % INK3)
e.append('  <text x="120" y="512" font-size="5.6" fill="%s">诗经 · 周南</text>' % INK2)
e.append('  <text x="640" y="512" text-anchor="end" font-size="5.6" fill="%s">图二 · 身三处族三阶 · sj011b</text>' % INK2)
e.append('</svg>')
open(os.path.join(FIG, "sj011b-shen-san-chu-zu-san-jie.svg"), "w", encoding="utf-8").write("\n".join(e))

import cairosvg
for k in ["sj011a-lin-zhi-zhi-ding-jiao", "sj011b-shen-san-chu-zu-san-jie"]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok")
