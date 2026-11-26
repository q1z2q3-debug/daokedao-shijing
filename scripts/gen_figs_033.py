# -*- coding: utf-8 -*-
"""SJ033《雄雉》两图。图一：雉冠·长尾·日月远路。图二：思远—不忮—不求。"""
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
d.append('  <text x="380" y="60" text-anchor="middle" font-size="26" letter-spacing="10" fill="%s" font-weight="700">雄 雉</text>' % INK)
d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之三十三</text>' % INK3)
d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)

# 壹 · 雉头特写（冠羽、短厚喙；长尾曳出画格，不画全鸟）
d.append('  <circle cx="148" cy="250" r="16" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % INK2)
# 冠羽：两三根竖笔
d.append('  <line x1="142" y1="236" x2="137" y2="222" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <line x1="148" y1="234" x2="148" y2="218" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <line x1="154" y1="236" x2="159" y2="222" stroke="%s" stroke-width="0.9"/>' % INK2)
# 短而厚的喙
d.append('  <path d="M162,245 L176,250 L162,255 Z" fill="#EFEAD6" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <circle cx="152" cy="248" r="1.5" fill="%s"/>' % INK)
# 长尾曳出（一条长弧，两段羽纹）
d.append('  <path d="M134,256 C118,286 106,314 102,344" fill="none" stroke="%s" stroke-width="1.3"/>' % INK2)
d.append('  <path d="M134,256 C124,284 116,310 114,338" fill="none" stroke="%s" stroke-width="0.5"/>' % INK3)
d.append('  <line x1="118" y1="296" x2="128" y2="292" stroke="%s" stroke-width="0.45"/>' % INK3)
d.append('  <line x1="110" y1="322" x2="120" y2="318" stroke="%s" stroke-width="0.45"/>' % INK3)
d.append('  <text x="148" y="372" text-anchor="middle" font-size="7.0" fill="%s">雄者有冠，雉之识别</text>' % RED)

# 贰 · 两枚长尾羽交叉并置（一正一背，背面淡形）
# 背面（淡）
d.append('  <path d="M400,238 C390,276 372,316 356,350" fill="none" stroke="%s" stroke-width="1.1"/>' % INK3)
d.append('  <path d="M392,240 C384,274 370,310 360,344" fill="none" stroke="%s" stroke-width="0.45"/>' % INK3)
# 正面（深）
d.append('  <path d="M356,238 C366,276 384,316 400,350" fill="none" stroke="%s" stroke-width="1.3"/>' % INK2)
d.append('  <path d="M364,240 C374,276 390,314 404,350" fill="none" stroke="%s" stroke-width="0.5"/>' % INK2)
# 羽纹
for k in range(3):
    y = 272 + k * 22
    d.append('  <line x1="364" y1="%d" x2="388" y2="%d" stroke="%s" stroke-width="0.45"/>' % (y, y + 4, INK3))
d.append('  <text x="378" y="386" text-anchor="middle" font-size="7.0" fill="%s">泄泄其羽，长尾舒徐</text>' % RED)

# 叁 · 日月与远路
d.append('  <circle cx="596" cy="232" r="16" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <circle cx="650" cy="232" r="13" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK3)
d.append('  <line x1="560" y1="380" x2="622" y2="300" stroke="%s" stroke-width="0.8"/>' % INK2)
d.append('  <line x1="684" y1="380" x2="622" y2="300" stroke="%s" stroke-width="0.8"/>' % INK2)
for k in range(4):
    x = 572 + k * 28
    d.append('  <line x1="%d" y1="392" x2="%d" y2="384" stroke="%s" stroke-width="0.5"/>' % (x, x + 3, INK3))
d.append('  <text x="622" y="360" text-anchor="middle" font-size="7.0" fill="%s">瞻彼日月，道之云远</text>' % RED)

for (x, t) in [(120, "壹"), (350, "贰"), (600, "叁")]:
    d.append('  <text x="%d" y="132" font-size="7.6" fill="%s">%s</text>' % (x, RED, t))
d.append('  <text x="44" y="466" font-size="7.8" fill="%s">壹 雉冠　雄雉有冠</text>' % INK2)
d.append('  <text x="264" y="466" font-size="7.8" fill="%s">贰 长尾　雉之识别，不求全鸟</text>' % INK2)
d.append('  <text x="486" y="466" font-size="7.8" fill="%s">叁 日月　流转不息，道远难来</text>' % INK2)
d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">雄雉于飞，泄泄其羽</text>' % INK)
d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">见雉闻声，思远役之人</text>' % INK3)
d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj033a</text>' % INK3)
d.append('</svg>')
svg_a = "\n".join(d)
open(os.path.join(FIG, "sj033a-xiong-zhi-yu-fei.svg"), "w", encoding="utf-8").write(svg_a)
bounds_ok(svg_a, "033a")

# 图二
e = []
e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="Noto Serif SC,Songti SC,serif">' % (W, H, W, H))
e.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
e.append('  <rect x="10" y="10" width="740" height="500" fill="none" stroke="%s" stroke-width="1"/>' % INK3)
e.append('  <rect x="16" y="16" width="728" height="488" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
e.append('  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="%s" font-weight="700">思远 · 不忮 · 不求</text>' % INK)
e.append('  <text x="380" y="74" text-anchor="middle" font-size="9.6" letter-spacing="2" fill="%s">《诗经》邶风 · 第八篇　雄雉</text>' % INK2)
e.append('  <defs><marker id="ar33" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % RED)
cells = [(70, "思远", "悠悠我思", "道之云远", INK2), (290, "不忮", "不忮", "无害忌", RED), (510, "不求", "不求", "无贪求", INK2)]
for (x, big, s1, s2, col) in cells:
    e.append('  <rect x="%d" y="150" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (x, col))
    e.append('  <text x="%d" y="214" text-anchor="middle" font-size="28" letter-spacing="2" fill="%s" font-weight="700">%s</text>' % (x + 75, col, big))
    e.append('  <text x="%d" y="252" text-anchor="middle" font-size="10" fill="#3B352F">%s</text>' % (x + 75, s1))
    e.append('  <text x="%d" y="278" text-anchor="middle" font-size="8" fill="%s">%s</text>' % (x + 75, INK3, s2))
e.append('  <line x1="220" y1="225" x2="288" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar33)"/>' % RED)
e.append('  <line x1="440" y1="225" x2="508" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar33)"/>' % RED)
e.append('  <text x="380" y="330" text-anchor="middle" font-size="8.4" fill="%s">思而有守，怨而不失德；不忮不求，则何用不臧</text>' % INK2)
e.append('  <line x1="120" y1="360" x2="640" y2="360" stroke="%s" stroke-width="0.8"/>' % INK3)
e.append('  <text x="230" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">臧</text>' % RED)
e.append('  <text x="230" y="414" text-anchor="middle" font-size="7.4" fill="%s">善也，何用不臧即无往不善</text>' % INK3)
e.append('  <text x="530" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">展</text>' % RED)
e.append('  <text x="530" y="414" text-anchor="middle" font-size="7.4" fill="%s">诚也，展矣君子</text>' % INK3)
e.append('  <text x="380" y="446" text-anchor="middle" font-size="7.4" fill="%s">《论语·子罕》引「不忮不求，何用不臧」赞子路</text>' % INK3)
e.append('  <text x="120" y="512" font-size="5.6" fill="%s">诗经 · 邶风</text>' % INK2)
e.append('  <text x="640" y="512" text-anchor="end" font-size="5.6" fill="%s">图二 · 思远不忮不求 · sj033b</text>' % INK2)
e.append('</svg>')
svg_b = "\n".join(e)
open(os.path.join(FIG, "sj033b-bu-zhi-bu-qiu.svg"), "w", encoding="utf-8").write(svg_b)
bounds_ok(svg_b, "033b")

import cairosvg
for k in ["sj033a-xiong-zhi-yu-fei", "sj033b-bu-zhi-bu-qiu"]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok")
