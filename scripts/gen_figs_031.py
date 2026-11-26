# -*- coding: utf-8 -*-
"""SJ031《击鼓》两图。图一：鼓·南行·林下马。图二：行役—旧誓—阔绝。"""
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
d.append('  <text x="380" y="60" text-anchor="middle" font-size="26" letter-spacing="10" fill="%s" font-weight="700">击 鼓</text>' % INK)
d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之三十一</text>' % INK3)
d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)

# 壹 · 鼓（鼓架横木＋两排鼓钉）
# 鼓架：两侧立柱与底横木
d.append('  <line x1="110" y1="228" x2="110" y2="296" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <line x1="186" y1="228" x2="186" y2="296" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <line x1="110" y1="296" x2="186" y2="296" stroke="%s" stroke-width="1.0"/>' % INK2)
# 鼓身
d.append('  <path d="M116,232 L180,232 L172,286 L124,286 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % INK2)
# 上下口沿弧
d.append('  <path d="M116,232 Q148,225 180,232" fill="none" stroke="%s" stroke-width="1.0"/>' % INK)
d.append('  <path d="M124,286 Q148,293 172,286" fill="none" stroke="%s" stroke-width="1.0"/>' % INK)
d.append('  <line x1="116" y1="232" x2="180" y2="232" stroke="%s" stroke-width="1.4"/>' % INK)
d.append('  <line x1="124" y1="286" x2="172" y2="286" stroke="%s" stroke-width="1.4"/>' % INK)
# 两排鼓钉
for k in range(5):
    sx = 126 + k * 11
    d.append('  <circle cx="%d" cy="240" r="1.2" fill="%s"/>' % (sx, INK3))
    d.append('  <circle cx="%d" cy="278" r="1.2" fill="%s"/>' % (sx, INK3))
d.append('  <line x1="150" y1="214" x2="176" y2="226" stroke="%s" stroke-width="1.1"/>' % INK2)
d.append('  <circle cx="180" cy="228" r="4" fill="#EFEAD6" stroke="%s" stroke-width="0.8"/>' % INK2)
for k in range(3):
    d.append('  <path d="M104,%d q-6,3 0,6" fill="none" stroke="%s" stroke-width="0.6"/>' % (240 + k * 12, INK3))
d.append('  <text x="148" y="320" text-anchor="middle" font-size="7.0" fill="%s">击鼓其镗，踊跃用兵</text>' % RED)

# 贰 · 城漕（雉堞三门洞）与南行之路
d.append('  <path d="M336,380 L336,348 L340,348 L340,336 L352,336 L352,348 L372,348 L372,336 L384,336 L384,348 L400,348 L400,336 L412,336 L412,348 L420,348 L420,380 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
# 城门洞
d.append('  <path d="M368,380 L368,364 Q378,354 388,364 L388,380 Z" fill="%s" stroke="%s" stroke-width="0.9"/>' % (PAPER, INK2))
# 南行之路与箭矢（上移缩短，避让注文）
d.append('  <path d="M378,380 L386,318" fill="none" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <path d="M382,324 L386,316 L392,324" fill="none" stroke="%s" stroke-width="0.9"/>' % RED)
d.append('  <text x="378" y="404" text-anchor="middle" font-size="7.0" fill="%s">土国城漕，我独南行</text>' % RED)

# 叁 · 林下丧马（主干＋分枝＋叶簇之木，四足之马）
# 三株木：主干、分枝、叶簇短线
for (tx, th) in [(558, 336), (596, 328), (676, 338)]:
    d.append('  <line x1="%d" y1="380" x2="%d" y2="%d" stroke="%s" stroke-width="1.2"/>' % (tx, tx, th, INK2))
    d.append('  <path d="M%d,%d L%d,%d" fill="none" stroke="%s" stroke-width="0.8"/>' % (tx, th + 18, tx - 10, th + 10, INK2))
    d.append('  <path d="M%d,%d L%d,%d" fill="none" stroke="%s" stroke-width="0.8"/>' % (tx, th + 14, tx + 10, th + 6, INK2))
    # 叶簇：三枚短弧
    d.append('  <path d="M%d,%d q8,-7 16,0" fill="none" stroke="%s" stroke-width="0.7"/>' % (tx - 8, th - 2, INK3))
    d.append('  <path d="M%d,%d q8,-7 16,0" fill="none" stroke="%s" stroke-width="0.7"/>' % (tx - 4, th - 8, INK3))
# 马（侧影：身、颈首、耳、鬃、尾、四足）
d.append('  <path d="M596,370 C596,358 624,356 634,366 C628,376 604,378 596,370 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <path d="M634,366 L642,352" fill="none" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <path d="M642,352 L651,354 L644,363 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <line x1="643" y1="351" x2="645" y2="346" stroke="%s" stroke-width="0.7"/>' % INK2)
# 鬃毛短纹
d.append('  <line x1="636" y1="360" x2="640" y2="356" stroke="%s" stroke-width="0.5"/>' % INK3)
d.append('  <line x1="638" y1="364" x2="642" y2="360" stroke="%s" stroke-width="0.5"/>' % INK3)
# 尾
d.append('  <path d="M596,368 L586,359" fill="none" stroke="%s" stroke-width="0.9"/>' % INK2)
# 四足
for lx in (602, 610, 624, 630):
    d.append('  <line x1="%d" y1="376" x2="%d" y2="392" stroke="%s" stroke-width="0.8"/>' % (lx, lx, INK2))
d.append('  <circle cx="646" cy="355" r="1.1" fill="%s"/>' % INK)
d.append('  <text x="622" y="410" text-anchor="middle" font-size="7.0" fill="%s">爰丧其马，于林之下</text>' % RED)

for (x, t) in [(120, "壹"), (350, "贰"), (600, "叁")]:
    d.append('  <text x="%d" y="132" font-size="7.6" fill="%s">%s</text>' % (x, RED, t))
d.append('  <text x="44" y="466" font-size="7.8" fill="%s">壹 鼓　镗然聚众</text>' % INK2)
d.append('  <text x="264" y="466" font-size="7.8" fill="%s">贰 南行　独我出征</text>' % INK2)
d.append('  <text x="486" y="466" font-size="7.8" fill="%s">叁 林下　失马失所</text>' % INK2)
d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">击鼓其镗，踊跃用兵</text>' % INK)
d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">人被征出家门，约誓悬在远方</text>' % INK3)
d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj031a</text>' % INK3)
d.append('</svg>')
svg_a = "\n".join(d)
open(os.path.join(FIG, "sj031a-ji-gu-nan-xing.svg"), "w", encoding="utf-8").write(svg_a)
bounds_ok(svg_a, "031a")

# 图二
e = []
e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="Noto Serif SC,Songti SC,serif">' % (W, H, W, H))
e.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
e.append('  <rect x="10" y="10" width="740" height="500" fill="none" stroke="%s" stroke-width="1"/>' % INK3)
e.append('  <rect x="16" y="16" width="728" height="488" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
e.append('  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="%s" font-weight="700">行役 · 旧誓 · 阔绝</text>' % INK)
e.append('  <text x="380" y="74" text-anchor="middle" font-size="9.6" letter-spacing="2" fill="%s">《诗经》邶风 · 第六篇　击鼓</text>' % INK2)
e.append('  <defs><marker id="ar31" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % RED)
cells = [(70, "行役", "我独南行", "不我以归", INK2), (290, "旧誓", "与子成说", "执手偕老", RED), (510, "阔绝", "不我活兮", "不我信兮", INK2)]
for (x, big, s1, s2, col) in cells:
    e.append('  <rect x="%d" y="150" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (x, col))
    e.append('  <text x="%d" y="214" text-anchor="middle" font-size="28" letter-spacing="2" fill="%s" font-weight="700">%s</text>' % (x + 75, col, big))
    e.append('  <text x="%d" y="252" text-anchor="middle" font-size="10" fill="#3B352F">%s</text>' % (x + 75, s1))
    e.append('  <text x="%d" y="278" text-anchor="middle" font-size="8" fill="%s">%s</text>' % (x + 75, INK3, s2))
e.append('  <line x1="220" y1="225" x2="288" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar31)"/>' % RED)
e.append('  <line x1="440" y1="225" x2="508" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar31)"/>' % RED)
e.append('  <text x="380" y="330" text-anchor="middle" font-size="8.4" fill="%s">公中之事与家中之誓，中间一誓相接，终被行役扯断</text>' % INK2)
e.append('  <line x1="120" y1="360" x2="640" y2="360" stroke="%s" stroke-width="0.8"/>' % INK3)
e.append('  <text x="230" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">契阔</text>' % RED)
e.append('  <text x="230" y="414" text-anchor="middle" font-size="7.4" fill="%s">契合阔离，非「契约广阔」</text>' % INK3)
e.append('  <text x="530" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">偕老</text>' % RED)
e.append('  <text x="530" y="414" text-anchor="middle" font-size="7.4" fill="%s">临别旧约，军中悬空未践</text>' % INK3)
e.append('  <text x="380" y="446" text-anchor="middle" font-size="7.4" fill="%s">末章「不我活」「不我信」是绝语，非婚礼赞歌</text>' % INK3)
e.append('  <text x="120" y="512" font-size="5.6" fill="%s">诗经 · 邶风</text>' % INK2)
e.append('  <text x="640" y="512" text-anchor="end" font-size="5.6" fill="%s">图二 · 行役旧誓阔绝 · sj031b</text>' % INK2)
e.append('</svg>')
svg_b = "\n".join(e)
open(os.path.join(FIG, "sj031b-qi-kuo-zhi-shi.svg"), "w", encoding="utf-8").write(svg_b)
bounds_ok(svg_b, "031b")

import cairosvg
for k in ["sj031a-ji-gu-nan-xing", "sj031b-qi-kuo-zhi-shi"]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok")
