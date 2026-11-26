# -*- coding: utf-8 -*-
"""SJ036《式微》两图。图一：草露·泥涂·晚役者。图二：自问—留役—不叛。"""
import os, sys, re, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fig_geo import *
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(ROOT, "assets", "fig")
INK, INK2, INK3, RED, PAPER = "#1F1B17", "#5C544A", "#9A9186", "#994433", "#F7F4EE"
W, H = 760, 540

def bounds_ok(svg, tag):
    s = re.sub(r'xmlns="[^"]*"', "", svg)
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
d.append('  <text x="380" y="60" text-anchor="middle" font-size="26" letter-spacing="10" fill="%s" font-weight="700">式 微</text>' % INK)
d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之三十六</text>' % INK3)
d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)

# 壹 · 草露：草叶三枚＋露珠＋远天
d.append('  <line x1="126" y1="332" x2="170" y2="332" stroke="%s" stroke-width="0.6"/>' % INK3)
d.append('  <path d="M132,332 C124,306 120,282 124,262" fill="none" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <path d="M148,332 C148,306 148,282 148,260" fill="none" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <path d="M164,332 C172,306 176,282 172,262" fill="none" stroke="%s" stroke-width="0.9"/>' % INK2)
# 侧叶
d.append('  <path d="M128,296 l-8,-4 l2,7 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.6"/>' % INK3)
d.append('  <path d="M168,296 l8,-4 l-2,7 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.6"/>' % INK3)
# 露珠三枚
for (cx, cy) in [(132, 296), (150, 282), (166, 298)]:
    d.append('  <circle cx="%d" cy="%d" r="4" fill="#FCFAF6" stroke="%s" stroke-width="0.8"/>' % (cx, cy, INK2))
    d.append('  <circle cx="%d" cy="%d" r="1" fill="%s"/>' % (cx-1, cy-1, INK3))
# 远天弧线（暮色）
d.append('  <path d="M110,210 C130,200 166,200 186,210" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
d.append('  <text x="148" y="372" text-anchor="middle" font-size="7.0" fill="%s">中露，露天之中</text>' % RED)

# 贰 · 泥涂：软泥带＋足迹＋水渍
d.append('  <path d="M316,300 L440,300 L432,336 L324,336 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
# 足迹两枚
for k, fx in enumerate([338, 388]):
    d.append('  <ellipse cx="%d" cy="312" rx="7" ry="4.5" fill="#EFEAD6" stroke="%s" stroke-width="0.7"/>' % (fx, INK3))
    d.append('  <line x1="%d" y1="312" x2="%d" y2="312" stroke="%s" stroke-width="0.4"/>' % (fx-5, fx+5, INK3))
# 水渍
d.append('  <path d="M326,328 C340,325 354,331 368,328 C382,325 396,331 410,328" fill="none" stroke="%s" stroke-width="0.5"/>' % INK3)
d.append('  <path d="M332,334 C346,331 360,337 374,334 C388,331 402,337 416,334" fill="none" stroke="%s" stroke-width="0.5"/>' % INK3)
d.append('  <text x="378" y="372" text-anchor="middle" font-size="7.0" fill="%s">泥中，泥涂之中</text>' % RED)

# 叁 · 晚役者：背影，首服、肩线、宽袖、袍裾，行于暮色路
# 路
d.append('  <path d="M586,340 L658,340 L640,300 L604,300 Z" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
# 人（背影）
d.append('  <circle cx="622" cy="236" r="10" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % INK2)
# 首服
d.append('  <path d="M614,232 C616,224 628,224 630,232" fill="#EFEAD6" stroke="%s" stroke-width="0.8"/>' % INK2)
d.append('  <line x1="618" y1="246" x2="618" y2="250" stroke="%s" stroke-width="0.8"/>' % INK2)
# 肩线＋宽袖＋袍身
d.append('  <path d="M608,252 L636,252" fill="none" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <path d="M606,252 C600,262 602,282 608,300 L614,312 L630,312 L636,300 C640,282 642,262 636,252 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
# 袖褶
d.append('  <line x1="612" y1="262" x2="612" y2="296" stroke="%s" stroke-width="0.45"/>' % INK3)
d.append('  <line x1="632" y1="262" x2="632" y2="296" stroke="%s" stroke-width="0.45"/>' % INK3)
# 杖
d.append('  <line x1="640" y1="260" x2="646" y2="312" stroke="%s" stroke-width="0.8"/>' % INK2)
d.append('  <text x="622" y="372" text-anchor="middle" font-size="7.0" fill="%s">日暮役者，自问不归</text>' % RED)

for (x, t) in [(120, "壹"), (350, "贰"), (600, "叁")]:
    d.append('  <text x="%d" y="132" font-size="7.6" fill="%s">%s</text>' % (x, RED, t))
d.append('  <text x="44" y="466" font-size="7.8" fill="%s">壹 草露　叶面水珠，暮色未晚</text>' % INK2)
d.append('  <text x="264" y="466" font-size="7.8" fill="%s">贰 泥涂　足迹水渍，役处愈下</text>' % INK2)
d.append('  <text x="486" y="466" font-size="7.8" fill="%s">叁 役者　背影袍裾，自问自解</text>' % INK2)
d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">式微式微，胡不歸</text>' % INK)
d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">怨从自问出，不向君前发</text>' % INK3)
d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj036a</text>' % INK3)
d.append('</svg>')
svg_a = "\n".join(d)
open(os.path.join(FIG, "sj036a-shi-wei-lu-ni.svg"), "w", encoding="utf-8").write(svg_a)
bounds_ok(svg_a, "036a")

# 图二
e = []
e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="Noto Serif SC,Songti SC,serif">' % (W, H, W, H))
e.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
e.append('  <rect x="10" y="10" width="740" height="500" fill="none" stroke="%s" stroke-width="1"/>' % INK3)
e.append('  <rect x="16" y="16" width="728" height="488" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
e.append('  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="%s" font-weight="700">自問 · 留役 · 不叛</text>' % INK)
e.append('  <text x="380" y="74" text-anchor="middle" font-size="9.6" letter-spacing="2" fill="%s">《诗经》邶风 · 第十一篇　式微</text>' % INK2)
e.append('  <defs><marker id="ar16" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % RED)
cells = [(70, "自問", "胡不歸", "归念起矣", INK2), (290, "留役", "微君之故", "为君而留", RED), (510, "不叛", "怨而尽职", "不背其事", INK2)]
for (x, big, s1, s2, col) in cells:
    e.append('  <rect x="%d" y="150" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (x, col))
    e.append('  <text x="%d" y="214" text-anchor="middle" font-size="28" letter-spacing="2" fill="%s" font-weight="700">%s</text>' % (x + 75, col, big))
    e.append('  <text x="%d" y="252" text-anchor="middle" font-size="10" fill="#3B352F">%s</text>' % (x + 75, s1))
    e.append('  <text x="%d" y="278" text-anchor="middle" font-size="8" fill="%s">%s</text>' % (x + 75, INK3, s2))
e.append('  <line x1="220" y1="225" x2="288" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar16)"/>' % RED)
e.append('  <line x1="440" y1="225" x2="508" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar16)"/>' % RED)
e.append('  <text x="380" y="330" text-anchor="middle" font-size="8.4" fill="%s">若非为君之故，何至于露中泥中；怨是自问，不是颂，亦不是叛</text>' % INK2)
e.append('  <line x1="120" y1="360" x2="640" y2="360" stroke="%s" stroke-width="0.8"/>' % INK3)
e.append('  <text x="230" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">微</text>' % RED)
e.append('  <text x="230" y="414" text-anchor="middle" font-size="7.4" fill="%s">若非，微君之故</text>' % INK3)
e.append('  <text x="530" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">躬</text>' % RED)
e.append('  <text x="530" y="414" text-anchor="middle" font-size="7.4" fill="%s">身也，微君之躬</text>' % INK3)
e.append('  <text x="380" y="446" text-anchor="middle" font-size="7.4" fill="%s">《邶风·式微》「微君之故，胡为乎中露」「微君之躬，胡为乎泥中」</text>' % INK3)
e.append('  <text x="120" y="512" font-size="5.6" fill="%s">诗经 · 邶风</text>' % INK2)
e.append('  <text x="640" y="512" text-anchor="end" font-size="5.6" fill="%s">图二 · 自问留役不叛 · sj036b</text>' % INK2)
e.append('</svg>')
svg_b = "\n".join(e)
open(os.path.join(FIG, "sj036b-zi-wen-bu-gui.svg"), "w", encoding="utf-8").write(svg_b)
bounds_ok(svg_b, "036b")

import cairosvg
for k in ["sj036a-shi-wei-lu-ni", "sj036b-zi-wen-bu-gui"]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok")
