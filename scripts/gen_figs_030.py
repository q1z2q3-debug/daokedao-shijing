# -*- coding: utf-8 -*-
"""SJ030《终风》两图。图一：风·霾曀·阴雷。图二：暴—思—系。"""
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
d.append('  <text x="380" y="60" text-anchor="middle" font-size="26" letter-spacing="10" fill="%s" font-weight="700">终 风</text>' % INK)
d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之三十</text>' % INK3)
d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)

# 壹 · 风与扬尘（霾）
for i, y in enumerate([220, 250, 280]):
    d.append('  <path d="M104,%d C124,%d 164,%d 192,%d" fill="none" stroke="%s" stroke-width="0.9"/>' % (y, y - 8, y + 6, y - 2, INK2))
for k in range(6):
    x = 110 + k * 13
    d.append('  <circle cx="%d" cy="300" r="1.2" fill="%s"/>' % (x, INK3))
d.append('  <text x="148" y="330" text-anchor="middle" font-size="7.0" fill="%s">终风且霾，风夹尘土</text>' % RED)

# 贰 · 蔽日之曀
d.append('  <circle cx="378" cy="238" r="22" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK3)
d.append('  <path d="M336,252 C350,238 406,238 420,252 C406,264 350,264 336,252 Z" fill="#EFEAD6" stroke="%s" stroke-width="0.9"/>' % INK2)
for k in range(3):
    y = 278 + k * 12
    d.append('  <line x1="348" y1="%d" x2="408" y2="%d" stroke="%s" stroke-width="0.5"/>' % (y, y, INK3))
d.append('  <text x="378" y="330" text-anchor="middle" font-size="7.0" fill="%s">曀曀其阴，不见晴日</text>' % RED)

# 叁 · 虺虺之雷
d.append('  <path d="M580,236 C592,222 650,222 664,236 C652,248 592,248 580,236 Z" fill="#EFEAD6" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <path d="M622,246 L612,272 L624,270 L614,298" fill="none" stroke="%s" stroke-width="1.3"/>' % RED)
for k in range(3):
    d.append('  <path d="M570,%d q10,-4 20,0" fill="none" stroke="%s" stroke-width="0.5"/>' % (262 + k * 12, INK3))
d.append('  <text x="622" y="330" text-anchor="middle" font-size="7.0" fill="%s">虺虺其雷，声将发</text>' % RED)

for (x, t) in [(120, "壹"), (350, "贰"), (600, "叁")]:
    d.append('  <text x="%d" y="132" font-size="7.6" fill="%s">%s</text>' % (x, RED, t))
d.append('  <text x="44" y="466" font-size="7.8" fill="%s">壹 终风　既风且暴，终日不息</text>' % INK2)
d.append('  <text x="264" y="466" font-size="7.8" fill="%s">贰 霾曀　蔽日阴沉</text>' % INK2)
d.append('  <text x="486" y="466" font-size="7.8" fill="%s">叁 雷　虺虺将发之声</text>' % INK2)
d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">曀曀其阴，虺虺其雷</text>' % INK)
d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">天变即情变，一章坏过一章</text>' % INK3)
d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj030a</text>' % INK3)
d.append('</svg>')
svg_a = "\n".join(d)
open(os.path.join(FIG, "sj030a-zhong-feng-tian-ying.svg"), "w", encoding="utf-8").write(svg_a)
bounds_ok(svg_a, "030a")

# 图二
e = []
e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="Noto Serif SC,Songti SC,serif">' % (W, H, W, H))
e.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
e.append('  <rect x="10" y="10" width="740" height="500" fill="none" stroke="%s" stroke-width="1"/>' % INK3)
e.append('  <rect x="16" y="16" width="728" height="488" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
e.append('  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="%s" font-weight="700">悼 · 思 · 怀</text>' % INK)
e.append('  <text x="380" y="74" text-anchor="middle" font-size="9.6" letter-spacing="2" fill="%s">《诗经》邶风 · 第五篇　终风</text>' % INK2)
e.append('  <defs><marker id="ar30" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % RED)
cells = [(70, "悼", "中心是悼", "遇人之暴", INK2), (290, "思", "悠悠我思", "莫往莫来", RED), (510, "怀", "愿言则怀", "断不了", INK2)]
for (x, big, s1, s2, col) in cells:
    e.append('  <rect x="%d" y="150" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (x, col))
    e.append('  <text x="%d" y="214" text-anchor="middle" font-size="28" letter-spacing="2" fill="%s" font-weight="700">%s</text>' % (x + 75, col, big))
    e.append('  <text x="%d" y="252" text-anchor="middle" font-size="10" fill="#3B352F">%s</text>' % (x + 75, s1))
    e.append('  <text x="%d" y="278" text-anchor="middle" font-size="8" fill="%s">%s</text>' % (x + 75, INK3, s2))
e.append('  <line x1="220" y1="225" x2="288" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar30)"/>' % RED)
e.append('  <line x1="440" y1="225" x2="508" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar30)"/>' % RED)
e.append('  <text x="380" y="330" text-anchor="middle" font-size="8.4" fill="%s">天象四转：暴—霾—曀—阴雷；心情一节缠过一节</text>' % INK2)
e.append('  <line x1="120" y1="360" x2="640" y2="360" stroke="%s" stroke-width="0.8"/>' % INK3)
e.append('  <text x="230" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">嚏</text>' % RED)
e.append('  <text x="230" y="414" text-anchor="middle" font-size="7.4" fill="%s">俗信：被人念及则嚏</text>' % INK3)
e.append('  <text x="530" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">怀</text>' % RED)
e.append('  <text x="530" y="414" text-anchor="middle" font-size="7.4" fill="%s">念沉为怀，怨中夹念</text>' % INK3)
e.append('  <text x="380" y="446" text-anchor="middle" font-size="7.4" fill="%s">遇人之暴而心犹系，念落到生理上</text>' % INK3)
e.append('  <text x="120" y="512" font-size="5.6" fill="%s">诗经 · 邶风</text>' % INK2)
e.append('  <text x="640" y="512" text-anchor="end" font-size="5.6" fill="%s">图二 · 暴思系 · sj030b</text>' % INK2)
e.append('</svg>')
svg_b = "\n".join(e)
open(os.path.join(FIG, "sj030b-bao-er-you-xi.svg"), "w", encoding="utf-8").write(svg_b)
bounds_ok(svg_b, "030b")

import cairosvg
for k in ["sj030a-zhong-feng-tian-ying", "sj030b-bao-er-you-xi"]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok")
