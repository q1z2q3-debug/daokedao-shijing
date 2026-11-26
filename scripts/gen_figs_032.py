# -*- coding: utf-8 -*-
"""SJ032《凯风》两图。图一：南风·棘心·寒泉黄鸟。图二：母劳—子愧—慰心。"""
import os, sys, re, math
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
d.append('  <text x="380" y="60" text-anchor="middle" font-size="26" letter-spacing="10" fill="%s" font-weight="700">凯 风</text>' % INK)
d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之三十二</text>' % INK3)
d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)

# 壹 · 棘心嫩芽
d.append('  <line x1="148" y1="380" x2="148" y2="300" stroke="%s" stroke-width="1.4"/>' % INK2)
d.append('  <path d="M148,316 C136,310 128,300 130,292 C142,296 148,306 148,316 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.8"/>' % INK2)
d.append('  <path d="M148,308 C160,302 168,292 166,284 C154,288 148,298 148,308 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.8"/>' % INK2)
for k in range(3):
    d.append('  <line x1="132" y1="392" x2="164" y2="392" stroke="%s" stroke-width="0.5"/>' % INK3)
d.append('  <text x="148" y="410" text-anchor="middle" font-size="7.0" fill="%s">棘心夭夭，子之稚弱</text>' % RED)

# 贰 · 棘薪长成
d.append('  <line x1="378" y1="380" x2="378" y2="250" stroke="%s" stroke-width="1.8"/>' % INK)
d.append('  <path d="M378,320 C366,306 352,300 340,298" fill="none" stroke="%s" stroke-width="1.1"/>' % INK2)
d.append('  <path d="M378,300 C392,288 406,284 418,282" fill="none" stroke="%s" stroke-width="1.1"/>' % INK2)
for (bx, by, dx) in [(350, 302, -8), (406, 286, 8), (378, 270, 0)]:
    d.append('  <line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="0.6"/>' % (bx, by, bx + dx, by - 6, INK3))
for k in range(3):
    d.append('  <line x1="362" y1="392" x2="394" y2="392" stroke="%s" stroke-width="0.5"/>' % INK3)
d.append('  <text x="378" y="410" text-anchor="middle" font-size="7.0" fill="%s">吹彼棘薪，子之长成</text>' % RED)

# 叁 · 寒泉与黄鸟
d.append('  <line x1="560" y1="300" x2="684" y2="300" stroke="%s" stroke-width="0.9"/>' % INK2)
for k in range(3):
    y = 316 + k * 12
    d.append('  <path d="M572,%d q26,-4 52,0 q26,4 52,0" fill="none" stroke="%s" stroke-width="0.5"/>' % (y, INK3))
# 黄鸟
d.append('  <ellipse cx="622" cy="252" rx="16" ry="10" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <circle cx="634" cy="246" r="6" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <path d="M640,245 L650,247 L640,250 Z" fill="#EFEAD6" stroke="%s" stroke-width="0.6"/>' % INK2)
for k in range(3):
    d.append('  <path d="M656,%d q8,-3 16,0" fill="none" stroke="%s" stroke-width="0.5"/>' % (240 + k * 8, INK3))
d.append('  <text x="622" y="356" text-anchor="middle" font-size="7.0" fill="%s">睍睆黄鸟，载好其音</text>' % RED)

for (x, t) in [(120, "壹"), (350, "贰"), (600, "叁")]:
    d.append('  <text x="%d" y="132" font-size="7.6" fill="%s">%s</text>' % (x, RED, t))
d.append('  <text x="44" y="466" font-size="7.8" fill="%s">壹 棘心　酸枣嫩芽，喻子之稚</text>' % INK2)
d.append('  <text x="264" y="466" font-size="7.8" fill="%s">贰 棘薪　棘已长成，可为薪</text>' % INK2)
d.append('  <text x="486" y="466" font-size="7.8" fill="%s">叁 黄鸟　鸣声清圆和好</text>' % INK2)
d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">凯风自南，吹彼棘心</text>' % INK)
d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">风长养物，母恩也；子长而母劳未息</text>' % INK3)
d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj032a</text>' % INK3)
d.append('</svg>')
svg_a = "\n".join(d)
open(os.path.join(FIG, "sj032a-kai-feng-ji-xin.svg"), "w", encoding="utf-8").write(svg_a)
bounds_ok(svg_a, "032a")

# 图二
e = []
e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="Noto Serif SC,Songti SC,serif">' % (W, H, W, H))
e.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
e.append('  <rect x="10" y="10" width="740" height="500" fill="none" stroke="%s" stroke-width="1"/>' % INK3)
e.append('  <rect x="16" y="16" width="728" height="488" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
e.append('  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="%s" font-weight="700">母劳 · 子愧 · 慰心</text>' % INK)
e.append('  <text x="380" y="74" text-anchor="middle" font-size="9.6" letter-spacing="2" fill="%s">《诗经》邶风 · 第七篇　凯风</text>' % INK2)
e.append('  <defs><marker id="ar32" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % RED)
cells = [(70, "母劳", "母氏劬劳", "母氏圣善", INK2), (290, "子愧", "我无令人", "莫慰母心", RED), (510, "慰心", "载好其音", "期慰母心", INK2)]
for (x, big, s1, s2, col) in cells:
    e.append('  <rect x="%d" y="150" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (x, col))
    e.append('  <text x="%d" y="214" text-anchor="middle" font-size="28" letter-spacing="2" fill="%s" font-weight="700">%s</text>' % (x + 75, col, big))
    e.append('  <text x="%d" y="252" text-anchor="middle" font-size="10" fill="#3B352F">%s</text>' % (x + 75, s1))
    e.append('  <text x="%d" y="278" text-anchor="middle" font-size="8" fill="%s">%s</text>' % (x + 75, INK3, s2))
e.append('  <line x1="220" y1="225" x2="288" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar32)"/>' % RED)
e.append('  <line x1="440" y1="225" x2="508" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar32)"/>' % RED)
e.append('  <text x="380" y="330" text-anchor="middle" font-size="8.4" fill="%s">棘由嫩及长，子已立；母之劳未减，子之愧愈深</text>' % INK2)
e.append('  <line x1="120" y1="360" x2="640" y2="360" stroke="%s" stroke-width="0.8"/>' % INK3)
e.append('  <text x="230" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">令</text>' % RED)
e.append('  <text x="230" y="414" text-anchor="middle" font-size="7.4" fill="%s">善也，令人即成材之子</text>' % INK3)
e.append('  <text x="530" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">慰</text>' % RED)
e.append('  <text x="530" y="414" text-anchor="middle" font-size="7.4" fill="%s">安于心，非徒养口体</text>' % INK3)
e.append('  <text x="380" y="446" text-anchor="middle" font-size="7.4" fill="%s">有子七人，莫慰母心——愧在子，不在母</text>' % INK3)
e.append('  <text x="120" y="512" font-size="5.6" fill="%s">诗经 · 邶风</text>' % INK2)
e.append('  <text x="640" y="512" text-anchor="end" font-size="5.6" fill="%s">图二 · 母劳子愧慰心 · sj032b</text>' % INK2)
e.append('</svg>')
svg_b = "\n".join(e)
open(os.path.join(FIG, "sj032b-zi-ze-mu-xin.svg"), "w", encoding="utf-8").write(svg_b)
bounds_ok(svg_b, "032b")

import cairosvg
for k in ["sj032a-kai-feng-ji-xin", "sj032b-zi-ze-mu-xin"]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok")
