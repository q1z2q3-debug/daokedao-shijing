# -*- coding: utf-8 -*-
"""SJ043《新台》两图。图一：新台·河水·鱼网鸿离。图二：所求—网离—戚施。"""
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
d.append('  <text x="380" y="60" text-anchor="middle" font-size="26" letter-spacing="10" fill="%s" font-weight="700">新 台</text>' % INK)
d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之四十三</text>' % INK3)
d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)

# 壹 · 新台（屋檐、栏楯、立柱、台基、台阶）
# 屋檐弧
d.append('  <path d="M108,236 Q150,224 192,236" fill="none" stroke="%s" stroke-width="1.2"/>' % INK2)
# 顶梁
d.append('  <line x1="116" y1="238" x2="184" y2="238" stroke="%s" stroke-width="1.2"/>' % INK)
# 栏楯短竖
for k in range(4):
    bx = 124 + k * 16
    d.append('  <line x1="%d" y1="238" x2="%d" y2="252" stroke="%s" stroke-width="0.7"/>' % (bx, bx, INK3))
# 两立柱
d.append('  <line x1="126" y1="252" x2="126" y2="294" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <line x1="174" y1="252" x2="174" y2="294" stroke="%s" stroke-width="1.0"/>' % INK2)
# 台身平台
d.append('  <rect x="120" y="262" width="60" height="32" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
# 台基（梯形）
d.append('  <path d="M114,294 L186,294 L192,316 L108,316 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % INK2)
# 基上线脚
d.append('  <line x1="114" y1="304" x2="186" y2="304" stroke="%s" stroke-width="0.5"/>' % INK3)
# 台阶（左侧两级）
d.append('  <line x1="108" y1="316" x2="94" y2="324" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <line x1="108" y1="324" x2="94" y2="332" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <text x="148" y="372" text-anchor="middle" font-size="7.0" fill="%s">「新臺有泚」台高临河</text>' % RED)

# 贰 · 河水（三道长波纹 + 细浪点）
for k, y in enumerate([252, 280, 308]):
    d.append('  <path d="M336,%d q14,-9 28,0 q14,9 28,0 q14,-9 28,0" fill="none" stroke="%s" stroke-width="1.1"/>' % (y, INK2 if k == 1 else INK3))
for k in range(4):
    x = 348 + k * 20
    d.append('  <line x1="%d" y1="322" x2="%d" y2="318" stroke="%s" stroke-width="0.45"/>' % (x, x + 4, INK3))
d.append('  <text x="378" y="386" text-anchor="middle" font-size="7.0" fill="%s">「河水彌彌」水盛之貌</text>' % RED)

# 叁 · 鱼网（双竿、顶梁、网目斜线、网中模糊一物，不坐实鸿为何物）
d.append('  <line x1="586" y1="236" x2="586" y2="330" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <line x1="658" y1="236" x2="658" y2="330" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <line x1="586" y1="236" x2="658" y2="236" stroke="%s" stroke-width="1.0"/>' % INK2)
# 网目：两组交叉斜线
for k in range(4):
    yy = 246 + k * 18
    d.append('  <line x1="590" y1="%d" x2="654" y2="%d" stroke="%s" stroke-width="0.45"/>' % (yy, yy + 14, INK3))
    d.append('  <line x1="654" y1="%d" x2="590" y2="%d" stroke="%s" stroke-width="0.45"/>' % (yy, yy + 14, INK3))
# 网中模糊轮廓（淡椭圆，不辨鸟蟾）
d.append('  <ellipse cx="622" cy="284" rx="18" ry="13" fill="none" stroke="%s" stroke-width="0.8" stroke-dasharray="3,2"/>' % INK3)
# 岸线
d.append('  <line x1="576" y1="330" x2="668" y2="330" stroke="%s" stroke-width="0.8"/>' % INK2)
d.append('  <text x="622" y="360" text-anchor="middle" font-size="7.0" fill="%s">「魚網之設，鴻則離之」</text>' % RED)

for (x, t) in [(120, "壹"), (350, "贰"), (600, "叁")]:
    d.append('  <text x="%d" y="132" font-size="7.6" fill="%s">%s</text>' % (x, RED, t))
d.append('  <text x="44" y="466" font-size="7.8" fill="%s">壹 新台　台高临河，鲜明高峻</text>' % INK2)
d.append('  <text x="264" y="466" font-size="7.8" fill="%s">贰 河水　弥弥浼浼，水盛满溢</text>' % INK2)
d.append('  <text x="486" y="466" font-size="7.8" fill="%s">叁 鱼网　网设鸿离，物不坐实</text>' % INK2)
d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">燕婉之求，得此戚施</text>' % INK)
d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">民间讥谣，对照自见而不骂</text>' % INK3)
d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj043a</text>' % INK3)
d.append('</svg>')
svg_a = "\n".join(d)
open(os.path.join(FIG, "sj043a-xin-tai-you-ci.svg"), "w", encoding="utf-8").write(svg_a)
bounds_ok(svg_a, "043a")

# 图二
e = []
e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="Noto Serif SC,Songti SC,serif">' % (W, H, W, H))
e.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
e.append('  <rect x="10" y="10" width="740" height="500" fill="none" stroke="%s" stroke-width="1"/>' % INK3)
e.append('  <rect x="16" y="16" width="728" height="488" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
e.append('  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="%s" font-weight="700">所求 · 网离 · 戚施</text>' % INK)
e.append('  <text x="380" y="74" text-anchor="middle" font-size="9.6" letter-spacing="2" fill="%s">《诗经》邶风 · 第十八篇　新台</text>' % INK2)
e.append('  <defs><marker id="ar23" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % RED)
cells = [(70, "所求", "燕婉之求", "安美好配", INK2), (290, "网离", "鴻則離之", "网设而落", RED), (510, "戚施", "得此戚施", "不能仰者", INK2)]
for (x, big, s1, s2, col) in cells:
    e.append('  <rect x="%d" y="150" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (x, col))
    e.append('  <text x="%d" y="214" text-anchor="middle" font-size="28" letter-spacing="2" fill="%s" font-weight="700">%s</text>' % (x + 75, col, big))
    e.append('  <text x="%d" y="252" text-anchor="middle" font-size="10" fill="#3B352F">%s</text>' % (x + 75, s1))
    e.append('  <text x="%d" y="278" text-anchor="middle" font-size="8" fill="%s">%s</text>' % (x + 75, INK3, s2))
e.append('  <line x1="220" y1="225" x2="288" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar23)"/>' % RED)
e.append('  <line x1="440" y1="225" x2="508" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar23)"/>' % RED)
e.append('  <text x="380" y="330" text-anchor="middle" font-size="8.4" fill="%s">外景愈盛，所遇愈丑；所求愈婉，所得愈恶，对照自见</text>' % INK2)
e.append('  <line x1="120" y1="360" x2="640" y2="360" stroke="%s" stroke-width="0.8"/>' % INK3)
e.append('  <text x="230" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">籧篨</text>' % RED)
e.append('  <text x="230" y="414" text-anchor="middle" font-size="7.4" fill="%s">不能俯者，一说恶疾</text>' % INK3)
e.append('  <text x="530" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">戚施</text>' % RED)
e.append('  <text x="530" y="414" text-anchor="middle" font-size="7.4" fill="%s">不能仰者，一说蟾蜍</text>' % INK3)
e.append('  <text x="380" y="446" text-anchor="middle" font-size="7.4" fill="%s">本事出《毛序》《左传》，系于宣公，标明为旧说</text>' % INK3)
e.append('  <text x="120" y="512" font-size="5.6" fill="%s">诗经 · 邶风</text>' % INK2)
e.append('  <text x="640" y="512" text-anchor="end" font-size="5.6" fill="%s">图二 · 所求网离戚施 · sj043b</text>' % INK2)
e.append('</svg>')
svg_b = "\n".join(e)
open(os.path.join(FIG, "sj043b-qu-chu-bu-xian.svg"), "w", encoding="utf-8").write(svg_b)
bounds_ok(svg_b, "043b")

import cairosvg
for k in ["sj043a-xin-tai-you-ci", "sj043b-qu-chu-bu-xian"]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok")
