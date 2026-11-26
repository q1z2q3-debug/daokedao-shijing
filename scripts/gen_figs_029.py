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

# 壹 · 日轮
CX, CY, R = 148, 250, 34
d.append('  <circle cx="%d" cy="%d" r="%d" fill="#FCFAF6" stroke="%s" stroke-width="1.2"/>' % (CX, CY, R, INK2))
for k in range(8):
    a = k * math.tau / 8
    x1 = CX + R * math.cos(a); y1 = CY + R * math.sin(a)
    x2 = CX + (R + 10) * math.cos(a); y2 = CY + (R + 10) * math.sin(a)
    d.append('  <line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="0.8"/>' % (x1, y1, x2, y2, INK3))
d.append('  <text x="%d" y="316" text-anchor="middle" font-size="7.0" fill="%s">日居月诸，居诸语助</text>' % (CX, RED))

# 贰 · 月轮（残月）
MX, MY, MR = 378, 250, 30
d.append('  <circle cx="%d" cy="%d" r="%d" fill="#FCFAF6" stroke="%s" stroke-width="1.2"/>' % (MX, MY, MR, INK2))
d.append('  <circle cx="%d" cy="%d" r="%d" fill="%s" stroke="none"/>' % (MX + 12, MY - 4, MR - 6, PAPER))
for (sx, sy) in [(350, 220), (410, 236), (360, 286)]:
    d.append('  <circle cx="%d" cy="%d" r="1.3" fill="%s"/>' % (sx, sy, INK3))
d.append('  <text x="%d" y="316" text-anchor="middle" font-size="7.0" fill="%s">照临下土</text>' % (MX, RED))

# 叁 · 下土受照
GX0, GX1 = 536, 708
d.append('  <line x1="%d" y1="380" x2="%d" y2="380" stroke="%s" stroke-width="1.0"/>' % (GX0, GX1, INK2))
for k in range(7):
    x = GX0 + 10 + k * 24
    d.append('  <line x1="%d" y1="380" x2="%d" y2="392" stroke="%s" stroke-width="0.5"/>' % (x, x + 2, INK3))
for k in range(3):
    x = 560 + k * 50
    d.append('  <line x1="%d" y1="300" x2="%d" y2="372" stroke="%s" stroke-width="0.5" stroke-dasharray="4 3"/>' % (x, x + 10, INK3))
d.append('  <text x="622" y="360" text-anchor="middle" font-size="7.0" fill="%s">下土是冒</text>' % RED)

for (x, t) in [(120, "壹"), (350, "贰"), (600, "叁")]:
    d.append('  <text x="%d" y="132" font-size="7.6" fill="%s">%s</text>' % (x, RED, t))
d.append('  <text x="44" y="466" font-size="7.8" fill="%s">壹 日月　居、诸皆语助</text>' % INK2)
d.append('  <text x="264" y="466" font-size="7.8" fill="%s">贰 照临　日月覆照下土</text>' % INK2)
d.append('  <text x="486" y="466" font-size="7.8" fill="%s">叁 下土　受照之地</text>' % INK2)
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
