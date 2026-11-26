# -*- coding: utf-8 -*-
"""SJ040《北门》两图。图一：北门·王事簿册·室谪。图二：窭贫—敦事—归天。"""
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
d.append('  <text x="380" y="60" text-anchor="middle" font-size="26" letter-spacing="10" fill="%s" font-weight="700">北 门</text>' % INK)
d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之四十</text>' % INK3)
d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)

# 壹 · 北门门阙（两立柱＋横梁＋门洞＋门槛＋门钉）
# 两立柱
d.append('  <line x1="112" y1="232" x2="112" y2="368" stroke="%s" stroke-width="1.3"/>' % INK2)
d.append('  <line x1="184" y1="232" x2="184" y2="368" stroke="%s" stroke-width="1.3"/>' % INK2)
# 横梁
d.append('  <line x1="104" y1="232" x2="192" y2="232" stroke="%s" stroke-width="1.4"/>' % INK)
d.append('  <line x1="104" y1="232" x2="104" y2="224" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <line x1="192" y1="232" x2="192" y2="224" stroke="%s" stroke-width="1.0"/>' % INK2)
# 门洞（内空）
d.append('  <path d="M122,368 L122,252 L174,252 L174,368 Z" fill="%s" stroke="%s" stroke-width="0.9"/>' % (PAPER, INK3))
# 门槛
d.append('  <line x1="112" y1="368" x2="184" y2="368" stroke="%s" stroke-width="1.3"/>' % INK)
# 门钉两排
for k in range(3):
    d.append('  <circle cx="130" cy="268" r="1.2" fill="%s"/>' % INK3)
    d.append('  <circle cx="166" cy="268" r="1.2" fill="%s"/>' % INK3)
    d.append('  <circle cx="130" cy="296" r="1.2" fill="%s"/>' % INK3)
    d.append('  <circle cx="166" cy="296" r="1.2" fill="%s"/>' % INK3)
# 柱础
d.append('  <line x1="106" y1="368" x2="118" y2="368" stroke="%s" stroke-width="1.0"/>' % INK3)
d.append('  <line x1="178" y1="368" x2="190" y2="368" stroke="%s" stroke-width="1.0"/>' % INK3)
d.append('  <text x="148" y="404" text-anchor="middle" font-size="7.0" fill="%s">出自北门，忧心殷殷</text>' % RED)

# 贰 · 王事簿册（上卷轴＋下简编两道编绳）
# 卷轴
d.append('  <rect x="330" y="236" width="96" height="26" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % INK2)
d.append('  <line x1="330" y1="236" x2="330" y2="262" stroke="%s" stroke-width="1.3"/>' % INK)
d.append('  <line x1="426" y1="236" x2="426" y2="262" stroke="%s" stroke-width="1.3"/>' % INK)
d.append('  <circle cx="330" cy="236" r="2.4" fill="#EFEAD6" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <circle cx="426" cy="262" r="2.4" fill="#EFEAD6" stroke="%s" stroke-width="0.8"/>' % INK3)
# 卷内栏线
for k in range(3):
    d.append('  <line x1="342" y1="%d" x2="414" y2="%d" stroke="%s" stroke-width="0.45"/>' % (243 + k * 6, 243 + k * 6, INK3))
# 下方简编：五枚简并列
for k in range(5):
    sx = 340 + k * 15
    d.append('  <rect x="%d" y="286" width="11" height="52" rx="2" fill="#FCFAF6" stroke="%s" stroke-width="0.8"/>' % (sx, INK2))
# 两道编绳
d.append('  <line x1="338" y1="300" x2="418" y2="300" stroke="%s" stroke-width="0.9"/>' % INK3)
d.append('  <line x1="338" y1="324" x2="418" y2="324" stroke="%s" stroke-width="0.9"/>' % INK3)
# 简端刻齿
for k in range(5):
    sx = 340 + k * 15
    d.append('  <line x1="%d" y1="292" x2="%d" y2="292" stroke="%s" stroke-width="0.4"/>' % (sx, sx + 11, INK3))
d.append('  <text x="378" y="372" text-anchor="middle" font-size="7.0" fill="%s">王事适我，政事一埤益我</text>' % RED)

# 叁 · 室家相谪（门框内二人：一责一俯，侧背身）
# 门框
d.append('  <line x1="552" y1="236" x2="552" y2="368" stroke="%s" stroke-width="1.1"/>' % INK2)
d.append('  <line x1="692" y1="236" x2="692" y2="368" stroke="%s" stroke-width="1.1"/>' % INK2)
d.append('  <line x1="552" y1="236" x2="692" y2="236" stroke="%s" stroke-width="1.1"/>' % INK2)
# 责者（左，侧身朝右，抬臂）
AX = 586
d.append('  <ellipse cx="%d" cy="266" rx="7.5" ry="8.5" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % (AX, INK2))
d.append('  <line x1="%d" y1="274" x2="%d" y2="280" stroke="%s" stroke-width="0.9"/>' % (AX - 3, AX - 3, INK2))
d.append('  <line x1="%d" y1="274" x2="%d" y2="280" stroke="%s" stroke-width="0.9"/>' % (AX + 3, AX + 3, INK2))
d.append('  <path d="M%d,280 C578,300 578,326 586,350 L604,350 C612,326 612,300 604,280 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % (AX, INK2))
# 抬起的责让臂
d.append('  <path d="M604,286 C616,282 624,276 628,268" fill="none" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <circle cx="629" cy="266" r="2.2" fill="#EFEAD6" stroke="%s" stroke-width="0.8"/>' % INK2)
# 俯者（右，侧身朝左，低头缩肩）
BX = 656
d.append('  <ellipse cx="%d" cy="272" rx="7.5" ry="8.5" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % (BX, INK2))
d.append('  <line x1="%d" y1="280" x2="%d" y2="286" stroke="%s" stroke-width="0.9"/>' % (BX - 3, BX - 3, INK2))
d.append('  <line x1="%d" y1="280" x2="%d" y2="286" stroke="%s" stroke-width="0.9"/>' % (BX + 3, BX + 3, INK2))
d.append('  <path d="M%d,286 C648,306 648,328 656,350 L672,350 C680,328 680,306 672,286 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % (BX, INK2))
# 俯者垂臂
d.append('  <path d="M648,292 C644,306 644,318 648,328" fill="none" stroke="%s" stroke-width="0.9"/>' % INK3)
# 两人间责让短线
d.append('  <line x1="632" y1="276" x2="646" y2="282" stroke="%s" stroke-width="0.5" stroke-dasharray="2 2"/>' % INK3)
d.append('  <text x="622" y="384" text-anchor="middle" font-size="7.0" fill="%s">室人交遍谪我</text>' % RED)

for (x, t) in [(120, "壹"), (350, "贰"), (600, "叁")]:
    d.append('  <text x="%d" y="132" font-size="7.6" fill="%s">%s</text>' % (x, RED, t))
d.append('  <text x="44" y="466" font-size="7.8" fill="%s">壹 北门　出门阴寒，忧心殷殷</text>' % INK2)
d.append('  <text x="264" y="466" font-size="7.8" fill="%s">贰 簿册　王事政事，一埤益我</text>' % INK2)
d.append('  <text x="486" y="466" font-size="7.8" fill="%s">叁 室谪　家人更番，交相责让</text>' % INK2)
d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">终窭且贫，莫知我艰</text>' % INK)
d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">公中加派，室家相谪，怨而守分</text>' % INK3)
d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj040a</text>' % INK3)
d.append('</svg>')
svg_a = "\n".join(d)
open(os.path.join(FIG, "sj040a-zhi-bei-men-you.svg"), "w", encoding="utf-8").write(svg_a)
bounds_ok(svg_a, "040a")

# 图二
e = []
e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="Noto Serif SC,Songti SC,serif">' % (W, H, W, H))
e.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
e.append('  <rect x="10" y="10" width="740" height="500" fill="none" stroke="%s" stroke-width="1"/>' % INK3)
e.append('  <rect x="16" y="16" width="728" height="488" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
e.append('  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="%s" font-weight="700">窭贫 · 敦事 · 归天</text>' % INK)
e.append('  <text x="380" y="74" text-anchor="middle" font-size="9.6" letter-spacing="2" fill="%s">《诗经》邶风 · 第十五篇　北门</text>' % INK2)
e.append('  <defs><marker id="ar20" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % RED)
cells = [(70, "窭贫", "终窭且贫", "莫知我艰", INK2), (290, "敦事", "王事敦我", "一埤遗我", RED), (510, "归天", "天实为之", "谓之何哉", INK2)]
for (x, big, s1, s2, col) in cells:
    e.append('  <rect x="%d" y="150" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (x, col))
    e.append('  <text x="%d" y="214" text-anchor="middle" font-size="28" letter-spacing="2" fill="%s" font-weight="700">%s</text>' % (x + 75, col, big))
    e.append('  <text x="%d" y="252" text-anchor="middle" font-size="10" fill="#3B352F">%s</text>' % (x + 75, s1))
    e.append('  <text x="%d" y="278" text-anchor="middle" font-size="8" fill="%s">%s</text>' % (x + 75, INK3, s2))
e.append('  <line x1="220" y1="225" x2="288" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar20)"/>' % RED)
e.append('  <line x1="440" y1="225" x2="508" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar20)"/>' % RED)
e.append('  <text x="380" y="330" text-anchor="middle" font-size="8.4" fill="%s">怨而守分：公中加派、室家相谪，怨辞尽而事仍办，难处归于天</text>' % INK2)
e.append('  <line x1="120" y1="360" x2="640" y2="360" stroke="%s" stroke-width="0.8"/>' % INK3)
e.append('  <text x="230" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">埤益</text>' % RED)
e.append('  <text x="230" y="414" text-anchor="middle" font-size="7.4" fill="%s">皆尽加派，政事集身</text>' % INK3)
e.append('  <text x="530" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">交谪</text>' % RED)
e.append('  <text x="530" y="414" text-anchor="middle" font-size="7.4" fill="%s">轮流更番，言语相责</text>' % INK3)
e.append('  <text x="380" y="446" text-anchor="middle" font-size="7.4" fill="%s">《小雅·北山》「大夫不均，我从事独贤」对读</text>' % INK3)
e.append('  <text x="120" y="512" font-size="5.6" fill="%s">诗经 · 邶风</text>' % INK2)
e.append('  <text x="640" y="512" text-anchor="end" font-size="5.6" fill="%s">图二 · 窭贫敦事归天 · sj040b</text>' % INK2)
e.append('</svg>')
svg_b = "\n".join(e)
open(os.path.join(FIG, "sj040b-yuan-er-shou-fen.svg"), "w", encoding="utf-8").write(svg_b)
bounds_ok(svg_b, "040b")

import cairosvg
for k in ["sj040a-zhi-bei-men-you", "sj040b-yuan-er-shou-fen"]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok")
