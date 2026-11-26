# -*- coding: utf-8 -*-
"""SJ044《二子乘舟》两图。图一：乘舟·舟上二人·舟影远去。图二：目送—思子—无害。"""
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
d.append('  <text x="380" y="60" text-anchor="middle" font-size="26" letter-spacing="10" fill="%s" font-weight="700">乘 舟</text>' % INK)
d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之四十四</text>' % INK3)
d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)

# 壹 · 舟（舟身弧线、船舷、坐板、楫桨）
# 舟身侧视
d.append('  <path d="M112,278 Q148,306 184,278 L176,266 L120,266 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % INK2)
# 船舷
d.append('  <line x1="120" y1="266" x2="176" y2="266" stroke="%s" stroke-width="1.2"/>' % INK)
# 坐板
d.append('  <line x1="132" y1="276" x2="164" y2="276" stroke="%s" stroke-width="0.6"/>' % INK3)
# 楫桨（斜出船尾，桨叶小四边形）
d.append('  <line x1="176" y1="272" x2="198" y2="242" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <path d="M198,242 L206,236 L202,248 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.8"/>' % INK2)
# 舟下两道水纹
d.append('  <path d="M116,318 q12,-7 24,0 q12,7 24,0" fill="none" stroke="%s" stroke-width="0.7"/>' % INK3)
d.append('  <path d="M124,330 q12,-7 24,0 q12,7 24,0" fill="none" stroke="%s" stroke-width="0.5"/>' % INK3)
d.append('  <text x="148" y="372" text-anchor="middle" font-size="7.0" fill="%s">「二子乘舟」舟身有桨</text>' % RED)

# 贰 · 舟上二人（背影立姿：冠发、肩线、宽袖、衣裾）
# 舟身托底
d.append('  <path d="M338,298 Q378,316 418,298 L412,286 L344,286 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
# 前一人（深）
AX = 366
d.append('  <ellipse cx="%d" cy="250" rx="7" ry="8" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % (AX, INK2))
d.append('  <circle cx="%d" cy="244" r="1.4" fill="%s"/>' % (AX, INK))
d.append('  <path d="M%d,260 C357,276 357,292 361,304 L371,304 C375,292 375,276 371,260 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % (AX, INK2))
d.append('  <line x1="358" y1="262" x2="374" y2="262" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <path d="M358,264 C351,276 350,290 355,300" fill="none" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <path d="M374,264 C381,276 382,290 377,300" fill="none" stroke="%s" stroke-width="0.9"/>' % INK2)
# 后一人（淡，略小）
BX = 394
d.append('  <ellipse cx="%d" cy="254" rx="6" ry="7" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % (BX, INK3))
d.append('  <circle cx="%d" cy="249" r="1.2" fill="%s"/>' % (BX, INK3))
d.append('  <path d="M%d,263 C387,277 387,291 390,302 L398,302 C401,291 401,277 398,263 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % (BX, INK3))
d.append('  <path d="M387,266 C382,276 381,288 385,296" fill="none" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <path d="M398,266 C403,276 404,288 400,296" fill="none" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="378" y="386" text-anchor="middle" font-size="7.0" fill="%s">舟上二人，背影宽袖</text>' % RED)

# 叁 · 远舟与舟影（小舟、桅影、拖水淡影、三纹水线）
d.append('  <path d="M598,252 Q622,262 646,252 L641,244 L603,244 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <line x1="622" y1="244" x2="622" y2="226" stroke="%s" stroke-width="0.8"/>' % INK2)
d.append('  <path d="M622,228 L634,240 L622,240 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.7"/>' % INK3)
# 拖水淡影（虚线椭圆）
d.append('  <ellipse cx="622" cy="284" rx="24" ry="6" fill="none" stroke="%s" stroke-width="0.7" stroke-dasharray="3,2"/>' % INK3)
# 三纹水线
for k, y in enumerate([300, 316, 332]):
    d.append('  <path d="M586,%d q12,-6 24,0 q12,6 24,0 q12,-6 24,0" fill="none" stroke="%s" stroke-width="0.6"/>' % (y, INK3))
d.append('  <text x="622" y="360" text-anchor="middle" font-size="7.0" fill="%s">「汎汎其景」舟影远去</text>' % RED)

for (x, t) in [(120, "壹"), (350, "贰"), (600, "叁")]:
    d.append('  <text x="%d" y="132" font-size="7.6" fill="%s">%s</text>' % (x, RED, t))
d.append('  <text x="44" y="466" font-size="7.8" fill="%s">壹 舟　舟身船舷，楫桨斜出</text>' % INK2)
d.append('  <text x="264" y="466" font-size="7.8" fill="%s">贰 二人　背影宽袖，衣裾到舟</text>' % INK2)
d.append('  <text x="486" y="466" font-size="7.8" fill="%s">叁 远影　汎汎其景，渐行渐空</text>' % INK2)
d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">汎汎其景，中心養養</text>' % INK)
d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">二子之去，忧在不言</text>' % INK3)
d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj044a</text>' % INK3)
d.append('</svg>')
svg_a = "\n".join(d)
open(os.path.join(FIG, "sj044a-fan-fan-qi-jing.svg"), "w", encoding="utf-8").write(svg_a)
bounds_ok(svg_a, "044a")

# 图二
e = []
e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="Noto Serif SC,Songti SC,serif">' % (W, H, W, H))
e.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
e.append('  <rect x="10" y="10" width="740" height="500" fill="none" stroke="%s" stroke-width="1"/>' % INK3)
e.append('  <rect x="16" y="16" width="728" height="488" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
e.append('  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="%s" font-weight="700">目送 · 思子 · 无害</text>' % INK)
e.append('  <text x="380" y="74" text-anchor="middle" font-size="9.6" letter-spacing="2" fill="%s">《诗经》邶风 · 第十九篇　二子乘舟</text>' % INK2)
e.append('  <defs><marker id="ar24" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % RED)
cells = [(70, "目送", "汎汎其景", "舟影远去", INK2), (290, "思子", "願言思子", "中心养养", RED), (510, "无害", "不瑕有害", "但愿无祸", INK2)]
for (x, big, s1, s2, col) in cells:
    e.append('  <rect x="%d" y="150" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (x, col))
    e.append('  <text x="%d" y="214" text-anchor="middle" font-size="28" letter-spacing="2" fill="%s" font-weight="700">%s</text>' % (x + 75, col, big))
    e.append('  <text x="%d" y="252" text-anchor="middle" font-size="10" fill="#3B352F">%s</text>' % (x + 75, s1))
    e.append('  <text x="%d" y="278" text-anchor="middle" font-size="8" fill="%s">%s</text>' % (x + 75, INK3, s2))
e.append('  <line x1="220" y1="225" x2="288" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar24)"/>' % RED)
e.append('  <line x1="440" y1="225" x2="508" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar24)"/>' % RED)
e.append('  <text x="380" y="330" text-anchor="middle" font-size="8.4" fill="%s">舟去人留，忧在不言；送的是谁、有何祸，诗一字不提</text>' % INK2)
e.append('  <line x1="120" y1="360" x2="640" y2="360" stroke="%s" stroke-width="0.8"/>' % INK3)
e.append('  <text x="230" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">养养</text>' % RED)
e.append('  <text x="230" y="414" text-anchor="middle" font-size="7.4" fill="%s">忧思不定之貌，非养育</text>' % INK3)
e.append('  <text x="530" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">不瑕</text>' % RED)
e.append('  <text x="530" y="414" text-anchor="middle" font-size="7.4" fill="%s">瑕通遐，何也；揣愿之辞</text>' % INK3)
e.append('  <text x="380" y="446" text-anchor="middle" font-size="7.4" fill="%s">毛序思伋寿，本事出《左传》，标明为旧说</text>' % INK3)
e.append('  <text x="120" y="512" font-size="5.6" fill="%s">诗经 · 邶风</text>' % INK2)
e.append('  <text x="640" y="512" text-anchor="end" font-size="5.6" fill="%s">图二 · 目送思子无害 · sj044b</text>' % INK2)
e.append('</svg>')
svg_b = "\n".join(e)
open(os.path.join(FIG, "sj044b-zhong-xin-yang-yang.svg"), "w", encoding="utf-8").write(svg_b)
bounds_ok(svg_b, "044b")

import cairosvg
for k in ["sj044a-fan-fan-qi-jing", "sj044b-zhong-xin-yang-yang"]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok")
