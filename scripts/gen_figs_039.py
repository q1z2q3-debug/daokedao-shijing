# -*- coding: utf-8 -*-
"""SJ039《泉水》两图。图一：泉眼·淇水·嫁时车路。图二：怀卫—谋归—不归。"""
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
d.append('  <text x="380" y="60" text-anchor="middle" font-size="26" letter-spacing="10" fill="%s" font-weight="700">泉 水</text>' % INK)
d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之三十九</text>' % INK3)
d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)

# 壹 · 泉眼（石围泉口＋三股涌出＋两重水纹）
# 石围泉口
d.append('  <path d="M112,352 Q148,336 184,352" fill="none" stroke="%s" stroke-width="1.2"/>' % INK2)
d.append('  <path d="M118,356 Q148,344 178,356" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
# 泉口内沿
d.append('  <ellipse cx="148" cy="354" rx="22" ry="6" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % INK2)
# 三股涌出
d.append('  <path d="M140,352 C136,342 138,332 144,324" fill="none" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <path d="M148,350 C148,338 148,328 148,318" fill="none" stroke="%s" stroke-width="1.0"/>' % INK)
d.append('  <path d="M156,352 C160,342 158,332 152,324" fill="none" stroke="%s" stroke-width="0.9"/>' % INK2)
# 涌出细点
d.append('  <circle cx="143" cy="318" r="1.1" fill="%s"/>' % INK3)
d.append('  <circle cx="153" cy="320" r="1.1" fill="%s"/>' % INK3)
# 两重水纹（渐隐虚线）
d.append('  <path d="M116,372 q16,-6 32,0 q16,6 32,0" fill="none" stroke="%s" stroke-width="0.6" stroke-dasharray="4 3"/>' % INK3)
d.append('  <path d="M122,384 q13,-5 26,0 q13,5 26,0" fill="none" stroke="%s" stroke-width="0.5" stroke-dasharray="3 3"/>' % INK3)
d.append('  <text x="148" y="404" text-anchor="middle" font-size="7.0" fill="%s">毖彼泉水，亦流于淇</text>' % RED)

# 贰 · 淇水与临流女子（背影，望左方水）
# 横水纹两道
d.append('  <path d="M300,372 q18,-6 36,0 q18,6 36,0 q18,-6 36,0" fill="none" stroke="%s" stroke-width="0.7" stroke-dasharray="4 3"/>' % INK3)
d.append('  <path d="M306,384 q16,-5 32,0 q16,5 32,0 q16,-5 32,0" fill="none" stroke="%s" stroke-width="0.5" stroke-dasharray="3 3"/>' % INK3)
# 女子背影（头髻、肩线、宽袖、衣裾），立于水畔 x378
PX = 386
d.append('  <ellipse cx="%d" cy="246" rx="8" ry="9" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % (PX, INK2))
# 发髻
d.append('  <circle cx="%d" cy="236" r="3.2" fill="#FCFAF6" stroke="%s" stroke-width="0.8"/>' % (PX, INK2))
d.append('  <line x1="%d" y1="234" x2="%d" y2="228" stroke="%s" stroke-width="0.7"/>' % (PX, PX, INK3))
# 颈
d.append('  <line x1="%d" y1="255" x2="%d" y2="262" stroke="%s" stroke-width="0.9"/>' % (PX - 3, PX - 3, INK2))
d.append('  <line x1="%d" y1="255" x2="%d" y2="262" stroke="%s" stroke-width="0.9"/>' % (PX + 3, PX + 3, INK2))
# 衣身
d.append('  <path d="M%d,262 C378,290 378,322 387,352 L407,352 C416,322 416,290 408,262 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % (PX, INK2))
d.append('  <line x1="%d" y1="264" x2="%d" y2="264" stroke="%s" stroke-width="0.9"/>' % (PX - 8, PX + 8, INK2))
# 衣裾中缝
d.append('  <line x1="%d" y1="272" x2="%d" y2="348" stroke="%s" stroke-width="0.45"/>' % (PX, PX, INK3))
# 宽袖下垂（外轮廓＋内褶）
d.append('  <path d="M%d,266 C372,280 370,300 376,314" fill="none" stroke="%s" stroke-width="1.0"/>' % (PX, INK2))
d.append('  <path d="M%d,266 C418,280 420,300 414,314" fill="none" stroke="%s" stroke-width="1.0"/>' % (PX, INK2))
d.append('  <path d="M%d,272 C370,284 370,298 375,308" fill="none" stroke="%s" stroke-width="0.5"/>' % (PX, INK3))
d.append('  <path d="M%d,272 C420,284 420,298 415,308" fill="none" stroke="%s" stroke-width="0.5"/>' % (PX, INK3))
# 望水视线（淡虚线，投向左方）
d.append('  <line x1="%d" y1="246" x2="344" y2="238" stroke="%s" stroke-width="0.5" stroke-dasharray="3 3"/>' % (PX - 6, INK3))
d.append('  <line x1="%d" y1="250" x2="342" y2="250" stroke="%s" stroke-width="0.5" stroke-dasharray="3 3"/>' % (PX - 6, INK3))
d.append('  <text x="378" y="404" text-anchor="middle" font-size="7.0" fill="%s">有怀于卫，靡日不思</text>' % RED)

# 叁 · 待发车舆（两轮辐条＋舆栏＋辖键＋车辕）
# 两轮
for wx in (576, 660):
    d.append('  <circle cx="%d" cy="352" r="17" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (wx, INK2))
    d.append('  <circle cx="%d" cy="352" r="3" fill="#FCFAF6" stroke="%s" stroke-width="0.8"/>' % (wx, INK3))
    for k in range(4):
        a = k * math.pi / 2
        d.append('  <line x1="%d" y1="352" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="0.5"/>' % (wx, wx + 13 * math.cos(a), 352 + 13 * math.sin(a), INK3))
# 舆栏
d.append('  <path d="M566,322 L670,322 L664,340 L572,340 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % INK2)
d.append('  <line x1="566" y1="322" x2="670" y2="322" stroke="%s" stroke-width="1.3"/>' % INK)
# 栏板竖格
for k in range(4):
    gx = 582 + k * 22
    d.append('  <line x1="%d" y1="324" x2="%d" y2="338" stroke="%s" stroke-width="0.5"/>' % (gx, gx, INK3))
# 车辕前伸
d.append('  <path d="M670,328 L700,322" fill="none" stroke="%s" stroke-width="1.0"/>' % INK2)
# 轴头辖键（竖键插在轴端）
d.append('  <line x1="660" y1="335" x2="660" y2="326" stroke="%s" stroke-width="1.1"/>' % INK)
d.append('  <circle cx="660" cy="325" r="1.6" fill="%s"/>' % INK)
# 涂油小刷
d.append('  <line x1="560" y1="312" x2="572" y2="320" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <path d="M556,308 L562,304 L570,312 L564,316 Z" fill="#EFEAD6" stroke="%s" stroke-width="0.7"/>' % INK3)
d.append('  <text x="622" y="404" text-anchor="middle" font-size="7.0" fill="%s">载脂载舝，还车言迈</text>' % RED)

for (x, t) in [(120, "壹"), (350, "贰"), (600, "叁")]:
    d.append('  <text x="%d" y="132" font-size="7.6" fill="%s">%s</text>' % (x, RED, t))
d.append('  <text x="44" y="466" font-size="7.8" fill="%s">壹 泉眼　涌出入淇，以水归卫起兴</text>' % INK2)
d.append('  <text x="264" y="466" font-size="7.8" fill="%s">贰 临流　女子背影，望水怀卫</text>' % INK2)
d.append('  <text x="486" y="466" font-size="7.8" fill="%s">叁 车路　脂舝既备，待发未发</text>' % INK2)
d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">遄臻于卫，不瑕有害</text>' % INK)
d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">嫁女思归，念至深而人未行</text>' % INK3)
d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj039a</text>' % INK3)
d.append('</svg>')
svg_a = "\n".join(d)
open(os.path.join(FIG, "sj039a-quan-shui-liu-qi.svg"), "w", encoding="utf-8").write(svg_a)
bounds_ok(svg_a, "039a")

# 图二
e = []
e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="Noto Serif SC,Songti SC,serif">' % (W, H, W, H))
e.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
e.append('  <rect x="10" y="10" width="740" height="500" fill="none" stroke="%s" stroke-width="1"/>' % INK3)
e.append('  <rect x="16" y="16" width="728" height="488" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
e.append('  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="%s" font-weight="700">怀卫 · 谋归 · 不归</text>' % INK)
e.append('  <text x="380" y="74" text-anchor="middle" font-size="9.6" letter-spacing="2" fill="%s">《诗经》邶风 · 第十四篇　泉水</text>' % INK2)
e.append('  <defs><marker id="ar19" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % RED)
cells = [(70, "怀卫", "有怀于卫", "靡日不思", INK2), (290, "谋归", "聊与之谋", "女子有行", RED), (510, "不归", "驾言出游", "以写我忧", INK2)]
for (x, big, s1, s2, col) in cells:
    e.append('  <rect x="%d" y="150" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (x, col))
    e.append('  <text x="%d" y="214" text-anchor="middle" font-size="28" letter-spacing="2" fill="%s" font-weight="700">%s</text>' % (x + 75, col, big))
    e.append('  <text x="%d" y="252" text-anchor="middle" font-size="10" fill="#3B352F">%s</text>' % (x + 75, s1))
    e.append('  <text x="%d" y="278" text-anchor="middle" font-size="8" fill="%s">%s</text>' % (x + 75, INK3, s2))
e.append('  <line x1="220" y1="225" x2="288" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar19)"/>' % RED)
e.append('  <line x1="440" y1="225" x2="508" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar19)"/>' % RED)
e.append('  <text x="380" y="330" text-anchor="middle" font-size="8.4" fill="%s">思归而不归：谋之路、之车皆设想，末章出游只写忧</text>' % INK2)
e.append('  <line x1="120" y1="360" x2="640" y2="360" stroke="%s" stroke-width="0.8"/>' % INK3)
e.append('  <text x="230" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">遄臻</text>' % RED)
e.append('  <text x="230" y="414" text-anchor="middle" font-size="7.4" fill="%s">疾至设想，非已归卫</text>' % INK3)
e.append('  <text x="530" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">写忧</text>' % RED)
e.append('  <text x="530" y="414" text-anchor="middle" font-size="7.4" fill="%s">宣泄舒散，非书写也</text>' % INK3)
e.append('  <text x="380" y="446" text-anchor="middle" font-size="7.4" fill="%s">《鄘风·载驰》「女子善怀，亦各有行」同旨</text>' % INK3)
e.append('  <text x="120" y="512" font-size="5.6" fill="%s">诗经 · 邶风</text>' % INK2)
e.append('  <text x="640" y="512" text-anchor="end" font-size="5.6" fill="%s">图二 · 怀卫谋归不归 · sj039b</text>' % INK2)
e.append('</svg>')
svg_b = "\n".join(e)
open(os.path.join(FIG, "sj039b-si-gui-bu-gui.svg"), "w", encoding="utf-8").write(svg_b)
bounds_ok(svg_b, "039b")

import cairosvg
for k in ["sj039a-quan-shui-liu-qi", "sj039b-si-gui-bu-gui"]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok")
