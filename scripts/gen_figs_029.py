# -*- coding: utf-8 -*-
"""SJ029《日月》两图。图一：日·月·下土。图二：古处—相好—无良。"""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fig_geo import *
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(ROOT, "assets", "fig")
INK, INK2, INK3, RED, PAPER = "#1F1B17", "#5C544A", "#9A9186", "#994433", "#F7F4EE"
W, H = 760, 540

def bounds_ok(svg, tag):
    s = re.sub(r"#[0-9A-Fa-f]{6}", "", svg)
    s = re.sub(r'font-size="[^"]*"', "", s)
    s = re.sub(r'letter-spacing="[^"]*"', "", s)
    nums = [float(x) for x in re.findall(r"-?\d+\.?\d*", s)]
    xs = nums[0::2]; ys = nums[1::2]
    bad = [n for n in xs if n < 0 or n > W] + [n for n in ys if n < 0 or n > H]
    print(tag, "x[%.1f,%.1f] y[%.1f,%.1f] %s" % (min(xs), max(xs), min(ys), max(ys), "OK" if not bad else "OUT: %s" % bad))

d = []
d.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="\'Noto Serif SC\',\'Songti SC\',serif">' % (W, H, W, H))
d.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
d.append('  <text x="44" y="58" font-size="8.6" letter-spacing="2" fill="%s">邶风 · 三</text>' % RED)
d.append('  <text x="380" y="60" text-anchor="middle" font-size="26" letter-spacing="10" fill="%s" font-weight="700">日 月</text>' % INK)
d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之二十九</text>' % INK3)
d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)

# 壹 · 日居月诸（日轮带晕圈与光芒，旁伴月轮缺蚀线）
CX, CY, R = 128, 250, 23
# 日晕圈
d.append('  <circle cx="%d" cy="%d" r="%d" fill="none" stroke="%s" stroke-width="0.5"/>' % (CX, CY, R + 8, INK3))
d.append('  <circle cx="%d" cy="%d" r="%d" fill="#FCFAF6" stroke="%s" stroke-width="1.2"/>' % (CX, CY, R, INK2))
# 两笔光芒
d.append('  <line x1="128" y1="220" x2="128" y2="212" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <line x1="148" y1="232" x2="155" y2="225" stroke="%s" stroke-width="0.9"/>' % INK2)
# 伴月：缺蚀弦线
d.append('  <circle cx="176" cy="238" r="11" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK3)
d.append('  <circle cx="181" cy="235" r="8" fill="%s" stroke="none"/>' % PAPER)
d.append('  <path d="M172,230 A9,9 0 0 0 172,246" fill="none" stroke="%s" stroke-width="0.5"/>' % INK3)
d.append('  <text x="%d" y="316" text-anchor="middle" font-size="7.0" fill="%s">日居月诸，日月并见</text>' % (CX, RED))

# 贰 · 照临下土（土阜、田畴三垄、投影）
d.append('  <line x1="300" y1="300" x2="456" y2="300" stroke="%s" stroke-width="1.0"/>' % INK2)
# 土阜
d.append('  <path d="M332,300 Q378,266 424,300 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
# 阜下投影
d.append('  <path d="M336,300 Q378,310 420,300" fill="none" stroke="%s" stroke-width="0.5"/>' % INK3)
# 田畴三垄
d.append('  <line x1="360" y1="300" x2="346" y2="362" stroke="%s" stroke-width="0.6"/>' % INK3)
d.append('  <line x1="378" y1="300" x2="378" y2="362" stroke="%s" stroke-width="0.6"/>' % INK3)
d.append('  <line x1="396" y1="300" x2="410" y2="362" stroke="%s" stroke-width="0.6"/>' % INK3)
# 照临两射线
d.append('  <line x1="366" y1="250" x2="372" y2="272" stroke="%s" stroke-width="0.5"/>' % INK3)
d.append('  <line x1="390" y1="250" x2="384" y2="272" stroke="%s" stroke-width="0.5"/>' % INK3)
d.append('  <text x="378" y="384" text-anchor="middle" font-size="7.0" fill="%s">照临下土，田畴受照</text>' % RED)

# 叁 · 日升月降（日轮半出地平，月轮半落）
GX0, GX1 = 536, 708
d.append('  <line x1="%d" y1="348" x2="%d" y2="348" stroke="%s" stroke-width="1.0"/>' % (GX0, GX1, INK2))
# 日轮：上半圆半出地平，两笔光芒
d.append('  <path d="M565,348 A17,17 0 0 1 599,348" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % INK2)
d.append('  <line x1="582" y1="322" x2="582" y2="315" stroke="%s" stroke-width="0.8"/>' % INK2)
d.append('  <line x1="570" y1="326" x2="566" y2="320" stroke="%s" stroke-width="0.8"/>' % INK2)
# 月轮：下半圆半落
d.append('  <path d="M648,348 A14,14 0 0 0 676,348" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % INK3)
# 升落轨迹：两道淡形弧线
d.append('  <path d="M556,372 Q568,356 578,340" fill="none" stroke="%s" stroke-width="0.5"/>' % INK3)
d.append('  <path d="M666,356 Q676,370 690,376" fill="none" stroke="%s" stroke-width="0.5"/>' % INK3)
for k in range(5):
    x = 548 + k * 32
    d.append('  <line x1="%d" y1="356" x2="%d" y2="364" stroke="%s" stroke-width="0.5"/>' % (x, x + 2, INK3))
d.append('  <text x="622" y="392" text-anchor="middle" font-size="7.0" fill="%s">日升月降，出自东方</text>' % RED)

for (x, t) in [(120, "壹"), (350, "贰"), (600, "叁")]:
    d.append('  <text x="%d" y="132" font-size="7.6" fill="%s">%s</text>' % (x, RED, t))
d.append('  <text x="44" y="466" font-size="7.8" fill="%s">壹 日月　日晕月蚀，并见天上</text>' % INK2)
d.append('  <text x="264" y="466" font-size="7.8" fill="%s">贰 下土　土阜田畴，受照之地</text>' % INK2)
d.append('  <text x="486" y="466" font-size="7.8" fill="%s">叁 日月　半出半落</text>' % INK2)
d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">日居月诸，照临下土</text>' % INK)
d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">呼日月为证，怨而不绝</text>' % INK3)
d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj029a</text>' % INK3)
d.append('</svg>')
svg_a = "\n".join(d)
open(os.path.join(FIG, "sj029a-ri-yue-zhao-lin.svg"), "w", encoding="utf-8").write(svg_a)
bounds_ok(svg_a, "029a")

# 图二
e = []
e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="Noto Serif SC,Songti SC,serif">' % (W, H, W, H))
e.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
e.append('  <rect x="10" y="10" width="740" height="500" fill="none" stroke="%s" stroke-width="1"/>' % INK3)
e.append('  <rect x="16" y="16" width="728" height="488" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
e.append('  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="%s" font-weight="700">古处 · 相好 · 无良</text>' % INK)
e.append('  <text x="380" y="74" text-anchor="middle" font-size="9.6" letter-spacing="2" fill="%s">《诗经》邶风 · 第四篇　日月</text>' % INK2)
e.append('  <defs><marker id="ar29" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % RED)
cells = [(70, "古处", "逝不古处", "失其常道", INK2), (290, "相好", "逝不相好", "失其亲爱", RED), (510, "无良", "德音无良", "失其善心", INK2)]
for (x, big, s1, s2, col) in cells:
    e.append('  <rect x="%d" y="150" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (x, col))
    e.append('  <text x="%d" y="214" text-anchor="middle" font-size="28" letter-spacing="2" fill="%s" font-weight="700">%s</text>' % (x + 75, col, big))
    e.append('  <text x="%d" y="252" text-anchor="middle" font-size="10" fill="#3B352F">%s</text>' % (x + 75, s1))
    e.append('  <text x="%d" y="278" text-anchor="middle" font-size="8" fill="%s">%s</text>' % (x + 75, INK3, s2))
e.append('  <line x1="220" y1="225" x2="288" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar29)"/>' % RED)
e.append('  <line x1="440" y1="225" x2="508" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar29)"/>' % RED)
e.append('  <text x="380" y="330" text-anchor="middle" font-size="8.4" fill="%s">三章一问紧一问，由行为到心肠；末章犹盼一「定」</text>' % INK2)
e.append('  <line x1="120" y1="360" x2="640" y2="360" stroke="%s" stroke-width="0.8"/>' % INK3)
e.append('  <text x="230" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">定</text>' % RED)
e.append('  <text x="230" y="414" text-anchor="middle" font-size="7.4" fill="%s">安也，非「决定」</text>' % INK3)
e.append('  <text x="530" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">述</text>' % RED)
e.append('  <text x="530" y="414" text-anchor="middle" font-size="7.4" fill="%s">循常理也，不述即失序</text>' % INK3)
e.append('  <text x="380" y="446" text-anchor="middle" font-size="7.4" fill="%s">怨而不绝：责之愈切，犹望有定</text>' % INK3)
e.append('  <text x="120" y="512" font-size="5.6" fill="%s">诗经 · 邶风</text>' % INK2)
e.append('  <text x="640" y="512" text-anchor="end" font-size="5.6" fill="%s">图二 · 古处相好无良 · sj029b</text>' % INK2)
e.append('</svg>')
svg_b = "\n".join(e)
open(os.path.join(FIG, "sj029b-yuan-er-bu-jue.svg"), "w", encoding="utf-8").write(svg_b)
bounds_ok(svg_b, "029b")

import cairosvg
for k in ["sj029a-ri-yue-zhao-lin", "sj029b-yuan-er-bu-jue"]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok")
