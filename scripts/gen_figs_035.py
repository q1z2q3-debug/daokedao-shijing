# -*- coding: utf-8 -*-
"""SJ035《谷风》两图。图一：葑菲·梁笱·荼荠。图二：同心—持家—见弃。"""
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
d.append('  <text x="380" y="60" text-anchor="middle" font-size="26" letter-spacing="10" fill="%s" font-weight="700">谷 風</text>' % INK)
d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之三十五</text>' % INK3)
d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)

# 壹 · 葑菲：蔓菁圆根＋大叶，萝卜长根＋裂叶
# 蔓菁（左）
d.append('  <path d="M118,292 C108,306 110,326 124,332 C138,336 150,328 150,312 C150,298 138,288 118,292 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % INK2)
# 须根
d.append('  <line x1="124" y1="332" x2="122" y2="344" stroke="%s" stroke-width="0.6"/>' % INK3)
d.append('  <line x1="132" y1="334" x2="132" y2="346" stroke="%s" stroke-width="0.6"/>' % INK3)
# 叶柄＋大叶
d.append('  <line x1="128" y1="290" x2="124" y2="252" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <path d="M124,252 C106,238 96,252 104,268 C114,274 126,268 130,258 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <line x1="108" y1="260" x2="126" y2="256" stroke="%s" stroke-width="0.45"/>' % INK3)
d.append('  <line x1="132" y1="288" x2="142" y2="256" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <path d="M142,256 C158,244 168,258 160,272 C150,278 140,270 138,262 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % INK2)
# 萝卜（右）：长锥根
d.append('  <path d="M172,296 C168,312 170,330 180,340 C190,330 192,312 188,296 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % INK2)
d.append('  <line x1="180" y1="340" x2="180" y2="350" stroke="%s" stroke-width="0.6"/>' % INK3)
# 萝卜裂叶：中柄＋两瓣宽叶
d.append('  <line x1="180" y1="296" x2="180" y2="268" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <path d="M180,272 C166,258 156,268 164,282 C172,286 180,282 182,274 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <line x1="166" y1="274" x2="180" y2="272" stroke="%s" stroke-width="0.45"/>' % INK3)
d.append('  <path d="M180,272 C194,258 204,268 196,282 C188,286 180,282 178,274 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <line x1="194" y1="274" x2="180" y2="272" stroke="%s" stroke-width="0.45"/>' % INK3)
d.append('  <text x="148" y="386" text-anchor="middle" font-size="7.0" fill="%s">采葑采菲，不弃其叶</text>' % RED)

# 贰 · 梁笱：石堰横水，竹笱置堰口，游鱼迎笱
# 石堰：低墙横水，墙内嵌石
d.append('  <path d="M298,298 L358,298 L354,284 L302,284 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
for k in range(4):
    x = 310 + k * 12
    d.append('  <ellipse cx="%d" cy="291" rx="5" ry="3.5" fill="none" stroke="%s" stroke-width="0.5"/>' % (x, INK3))
# 笱（竹笼，梯形＋篾纹）
d.append('  <path d="M366,300 L396,300 L388,336 L374,336 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % INK2)
for k in range(3):
    y = 308 + k * 8
    d.append('  <line x1="370" y1="%d" x2="392" y2="%d" stroke="%s" stroke-width="0.45"/>' % (y, y, INK3))
# 鱼两条
d.append('  <path d="M330,316 C338,308 350,308 356,316 C350,324 338,324 330,316 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <path d="M330,316 L322,310 L322,322 Z" fill="#EFEAD6" stroke="%s" stroke-width="0.8"/>' % INK2)
d.append('  <circle cx="352" cy="314" r="1.2" fill="%s"/>' % INK)
d.append('  <path d="M414,326 C422,318 434,318 440,326 C434,334 422,334 414,326 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <path d="M414,326 L406,320 L406,332 Z" fill="#EFEAD6" stroke="%s" stroke-width="0.8"/>' % INK2)
# 水纹
for k in range(3):
    y = 348 + k * 10
    d.append('  <path d="M300,%d C314,%d 328,%d 342,%d C356,%d 370,%d 384,%d C398,%d 412,%d 426,%d" fill="none" stroke="%s" stroke-width="0.5"/>' % (y, y-3, y+3, y-3, y+3, y-3, y, y-3, y+3, y-3, INK3))
d.append('  <text x="378" y="386" text-anchor="middle" font-size="7.0" fill="%s">毋逝我梁，毋发我笱</text>' % RED)

# 叁 · 荼荠：荼细叶锯齿，荠圆叶莲座
# 荼（左）：三枚窄长锯齿叶
d.append('  <path d="M612,332 C610,306 610,282 612,258 C616,282 616,306 614,332 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <path d="M608,330 C600,308 596,290 598,272 C604,292 608,310 610,330 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <path d="M616,330 C624,308 628,290 626,272 C620,292 616,310 614,330 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % INK2)
# 叶缘锯齿
for j in range(3):
    yy = 278 + j * 12
    d.append('  <path d="M608,%d l-4,-2 l1,5 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.5"/>' % (yy, INK3))
    d.append('  <path d="M616,%d l4,-2 l-1,5 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.5"/>' % (yy, INK3))
# 荠（右）：莲座三圆叶
d.append('  <path d="M648,324 C634,312 626,314 628,326 C636,332 646,330 648,326 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <path d="M648,324 C646,308 650,300 654,308 C656,318 652,324 650,326 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <path d="M648,324 C662,312 670,314 668,326 C660,332 650,330 648,326 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <line x1="640" y1="322" x2="640" y2="338" stroke="%s" stroke-width="0.7"/>' % INK2)
# 根
d.append('  <line x1="636" y1="338" x2="634" y2="348" stroke="%s" stroke-width="0.6"/>' % INK3)
d.append('  <line x1="644" y1="338" x2="646" y2="348" stroke="%s" stroke-width="0.6"/>' % INK3)
d.append('  <text x="622" y="386" text-anchor="middle" font-size="7.0" fill="%s">谁谓荼苦，其甘如荠</text>' % RED)

for (x, t) in [(120, "壹"), (350, "贰"), (600, "叁")]:
    d.append('  <text x="%d" y="132" font-size="7.6" fill="%s">%s</text>' % (x, RED, t))
d.append('  <text x="44" y="466" font-size="7.8" fill="%s">壹 葑菲　根叶并采，不以根弃叶</text>' % INK2)
d.append('  <text x="264" y="466" font-size="7.8" fill="%s">贰 梁笱　鱼堰竹笼，护我旧业</text>' % INK2)
d.append('  <text x="486" y="466" font-size="7.8" fill="%s">叁 荼荠　苦菜甜菜，苦甘自陈</text>' % INK2)
d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">德音莫違，及爾同死</text>' % INK)
d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">一路叙事，一路自辩，不写控诉</text>' % INK3)
d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj035a</text>' % INK3)
d.append('</svg>')
svg_a = "\n".join(d)
open(os.path.join(FIG, "sj035a-feng-xu-fei.svg"), "w", encoding="utf-8").write(svg_a)
bounds_ok(svg_a, "035a")

# 图二
e = []
e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="Noto Serif SC,Songti SC,serif">' % (W, H, W, H))
e.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
e.append('  <rect x="10" y="10" width="740" height="500" fill="none" stroke="%s" stroke-width="1"/>' % INK3)
e.append('  <rect x="16" y="16" width="728" height="488" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
e.append('  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="%s" font-weight="700">同心 · 持家 · 見棄</text>' % INK)
e.append('  <text x="380" y="74" text-anchor="middle" font-size="9.6" letter-spacing="2" fill="%s">《诗经》邶风 · 第十篇　谷风</text>' % INK2)
e.append('  <defs><marker id="ar15" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % RED)
cells = [(70, "同心", "黽勉同心", "及尔同死", INK2), (290, "持家", "方舟游泳", "匍匐救之", RED), (510, "見棄", "我躬不閱", "遑恤我后", INK2)]
for (x, big, s1, s2, col) in cells:
    e.append('  <rect x="%d" y="150" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (x, col))
    e.append('  <text x="%d" y="214" text-anchor="middle" font-size="28" letter-spacing="2" fill="%s" font-weight="700">%s</text>' % (x + 75, col, big))
    e.append('  <text x="%d" y="252" text-anchor="middle" font-size="10" fill="#3B352F">%s</text>' % (x + 75, s1))
    e.append('  <text x="%d" y="278" text-anchor="middle" font-size="8" fill="%s">%s</text>' % (x + 75, INK3, s2))
e.append('  <line x1="220" y1="225" x2="288" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar15)"/>' % RED)
e.append('  <line x1="440" y1="225" x2="508" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar15)"/>' % RED)
e.append('  <text x="380" y="330" text-anchor="middle" font-size="8.4" fill="%s">苦处自陈，不平自明；辩的是事理，不是泄愤</text>' % INK2)
e.append('  <line x1="120" y1="360" x2="640" y2="360" stroke="%s" stroke-width="0.8"/>' % INK3)
e.append('  <text x="230" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">閱</text>' % RED)
e.append('  <text x="230" y="414" text-anchor="middle" font-size="7.4" fill="%s">容也，我躬不阅</text>' % INK3)
e.append('  <text x="530" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">恤</text>' % RED)
e.append('  <text x="530" y="414" text-anchor="middle" font-size="7.4" fill="%s">忧也，遑恤我后</text>' % INK3)
e.append('  <text x="380" y="446" text-anchor="middle" font-size="7.4" fill="%s">《邶风·谷风》「采葑采菲，无以下体」「我躬不阅，遑恤我后」</text>' % INK3)
e.append('  <text x="120" y="512" font-size="5.6" fill="%s">诗经 · 邶风</text>' % INK2)
e.append('  <text x="640" y="512" text-anchor="end" font-size="5.6" fill="%s">图二 · 同心持家见弃 · sj035b</text>' % INK2)
e.append('</svg>')
svg_b = "\n".join(e)
open(os.path.join(FIG, "sj035b-tong-xin-chi-jia.svg"), "w", encoding="utf-8").write(svg_b)
bounds_ok(svg_b, "035b")

import cairosvg
for k in ["sj035a-feng-xu-fei", "sj035b-tong-xin-chi-jia"]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok")
