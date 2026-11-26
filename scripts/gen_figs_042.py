# -*- coding: utf-8 -*-
"""SJ042《静女》两图。图一：城隅·搔首踟蹰·彤管荑草。图二：俟我—不见—贻美。"""
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
d.append('  <text x="380" y="60" text-anchor="middle" font-size="26" letter-spacing="10" fill="%s" font-weight="700">靜 女</text>' % INK)
d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之四十二</text>' % INK3)
d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)

# 壹 · 城隅（两面墙转角＋墙堞短齿＋墙角）
# 正面墙（横）
d.append('  <path d="M104,356 L104,262 L192,262 L192,356 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % INK2)
# 转角纵深墙（右侧斜收）
d.append('  <path d="M192,262 L214,274 L214,356 L192,356 Z" fill="#F1ECE2" stroke="%s" stroke-width="0.9"/>' % INK3)
# 墙堞短齿（正面墙顶）
for k in range(4):
    dx = 112 + k * 20
    d.append('  <path d="M%d,262 L%d,250 L%d,250 L%d,262 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.8"/>' % (dx, dx, dx + 12, dx + 12, INK2))
# 墙面砖缝短线
for k in range(3):
    d.append('  <line x1="112" y1="%d" x2="184" y2="%d" stroke="%s" stroke-width="0.4"/>' % (286 + k * 20, 286 + k * 20, INK3))
# 墙角遮屏（女藏处，淡形）
d.append('  <path d="M150,356 L150,300 Q166,292 182,300 L182,356" fill="none" stroke="%s" stroke-width="0.6" stroke-dasharray="3 3"/>' % INK3)
d.append('  <text x="148" y="392" text-anchor="middle" font-size="7.0" fill="%s">俟我于城隅</text>' % RED)

# 贰 · 搔首踟蹰之人（背侧立，一手抬至头侧）
PX = 378
# 头（背侧）
d.append('  <ellipse cx="%d" cy="248" rx="8" ry="9" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % (PX, INK2))
d.append('  <circle cx="%d" cy="238" r="3" fill="#FCFAF6" stroke="%s" stroke-width="0.8"/>' % (PX, INK2))
# 颈
d.append('  <line x1="%d" y1="257" x2="%d" y2="264" stroke="%s" stroke-width="0.9"/>' % (PX - 3, PX - 3, INK2))
d.append('  <line x1="%d" y1="257" x2="%d" y2="264" stroke="%s" stroke-width="0.9"/>' % (PX + 3, PX + 3, INK2))
# 衣身
d.append('  <path d="M%d,264 C370,292 370,322 379,350 L397,350 C406,322 406,292 398,264 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % (PX, INK2))
d.append('  <line x1="%d" y1="266" x2="%d" y2="266" stroke="%s" stroke-width="0.9"/>' % (PX - 8, PX + 8, INK2))
# 抬起搔首之臂（同侧上举至头侧）
d.append('  <path d="M396,270 C402,262 400,254 394,248" fill="none" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <circle cx="393" cy="247" r="2.4" fill="#EFEAD6" stroke="%s" stroke-width="0.8"/>' % INK2)
# 另一袖下垂
d.append('  <path d="M370,270 C364,284 362,302 368,314" fill="none" stroke="%s" stroke-width="0.9"/>' % INK3)
# 踟蹰两步线（脚下左右短弧）
d.append('  <path d="M360,360 q10,-5 20,0" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
d.append('  <path d="M382,366 q10,-5 20,0" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
d.append('  <text x="378" y="392" text-anchor="middle" font-size="7.0" fill="%s">爱而不见，搔首踟蹰</text>' % RED)

# 叁 · 彤管与荑草（红管有炜；茅芽细长带叶）
# 彤管（斜置长管，一端管头）
d.append('  <path d="M576,330 L616,276" fill="none" stroke="%s" stroke-width="2.2"/>' % INK2)
d.append('  <path d="M576,330 L616,276" fill="none" stroke="%s" stroke-width="0.8"/>' % RED)
# 管头（钝头小帽）
d.append('  <ellipse cx="619" cy="273" rx="3.4" ry="2.4" fill="#EFEAD6" stroke="%s" stroke-width="0.8"/>' % INK2)
# 管身两节纹
d.append('  <line x1="588" y1="314" x2="594" y2="318" stroke="%s" stroke-width="0.5"/>' % INK3)
d.append('  <line x1="598" y1="300" x2="604" y2="304" stroke="%s" stroke-width="0.5"/>' % INK3)
# 荑草（细长茎＋两三叶芽）
d.append('  <line x1="650" y1="350" x2="650" y2="286" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <path d="M650,310 C642,304 638,296 640,288" fill="none" stroke="%s" stroke-width="0.7"/>' % INK2)
d.append('  <path d="M650,318 C658,312 662,304 660,296" fill="none" stroke="%s" stroke-width="0.7"/>' % INK2)
d.append('  <path d="M650,296 C646,290 646,284 650,280" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
# 芽尖
d.append('  <circle cx="650" cy="284" r="1.4" fill="%s"/>' % INK3)
d.append('  <text x="622" y="380" text-anchor="middle" font-size="7.0" fill="%s">贻我彤管，自牧归荑</text>' % RED)

for (x, t) in [(120, "壹"), (350, "贰"), (600, "叁")]:
    d.append('  <text x="%d" y="132" font-size="7.6" fill="%s">%s</text>' % (x, RED, t))
d.append('  <text x="44" y="466" font-size="7.8" fill="%s">壹 城隅　城角幽僻，相约之处</text>' % INK2)
d.append('  <text x="264" y="466" font-size="7.8" fill="%s">贰 踟蹰　等人那一刻，手足无措</text>' % INK2)
d.append('  <text x="486" y="466" font-size="7.8" fill="%s">叁 微物　彤管红亮，荑草细长</text>' % INK2)
d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">匪女之为美，美人之贻</text>' % INK)
d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">全《诗》最轻一篇，物因人而美</text>' % INK3)
d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj042a</text>' % INK3)
d.append('</svg>')
svg_a = "\n".join(d)
open(os.path.join(FIG, "sj042a-cheng-yu-sao-shou.svg"), "w", encoding="utf-8").write(svg_a)
bounds_ok(svg_a, "042a")

# 图二
e = []
e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="Noto Serif SC,Songti SC,serif">' % (W, H, W, H))
e.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
e.append('  <rect x="10" y="10" width="740" height="500" fill="none" stroke="%s" stroke-width="1"/>' % INK3)
e.append('  <rect x="16" y="16" width="728" height="488" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
e.append('  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="%s" font-weight="700">俟我 · 不见 · 贻美</text>' % INK)
e.append('  <text x="380" y="74" text-anchor="middle" font-size="9.6" letter-spacing="2" fill="%s">《诗经》邶风 · 第十七篇　静女</text>' % INK2)
e.append('  <defs><marker id="ar22" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % RED)
cells = [(70, "俟我", "俟我城隅", "静女其姝", INK2), (290, "不见", "爱而不见", "搔首踟蹰", RED), (510, "贻美", "美人之贻", "洵美且异", INK2)]
for (x, big, s1, s2, col) in cells:
    e.append('  <rect x="%d" y="150" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (x, col))
    e.append('  <text x="%d" y="214" text-anchor="middle" font-size="28" letter-spacing="2" fill="%s" font-weight="700">%s</text>' % (x + 75, col, big))
    e.append('  <text x="%d" y="252" text-anchor="middle" font-size="10" fill="#3B352F">%s</text>' % (x + 75, s1))
    e.append('  <text x="%d" y="278" text-anchor="middle" font-size="8" fill="%s">%s</text>' % (x + 75, INK3, s2))
e.append('  <line x1="220" y1="225" x2="288" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar22)"/>' % RED)
e.append('  <line x1="440" y1="225" x2="508" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar22)"/>' % RED)
e.append('  <text x="380" y="330" text-anchor="middle" font-size="8.4" fill="%s">轻悦相候：不见之时只是踟蹰，得赠之后只是欣喜；美不在物，在赠物之人</text>' % INK2)
e.append('  <line x1="120" y1="360" x2="640" y2="360" stroke="%s" stroke-width="0.8"/>' % INK3)
e.append('  <text x="230" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">踟蹰</text>' % RED)
e.append('  <text x="230" y="414" text-anchor="middle" font-size="7.4" fill="%s">轻巧之急，非深忧大痛</text>' % INK3)
e.append('  <text x="530" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">贻美</text>' % RED)
e.append('  <text x="530" y="414" text-anchor="middle" font-size="7.4" fill="%s">物因人情而重，非物自贵</text>' % INK3)
e.append('  <text x="380" y="446" text-anchor="middle" font-size="7.4" fill="%s">《郑风·溱洧》「赠之以勺药」同为微物相赠</text>' % INK3)
e.append('  <text x="120" y="512" font-size="5.6" fill="%s">诗经 · 邶风</text>' % INK2)
e.append('  <text x="640" y="512" text-anchor="end" font-size="5.6" fill="%s">图二 · 俟我不见贻美 · sj042b</text>' % INK2)
e.append('</svg>')
svg_b = "\n".join(e)
open(os.path.join(FIG, "sj042b-ai-er-bu-jian.svg"), "w", encoding="utf-8").write(svg_b)
bounds_ok(svg_b, "042b")

import cairosvg
for k in ["sj042a-cheng-yu-sao-shou", "sj042b-ai-er-bu-jian"]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok")
