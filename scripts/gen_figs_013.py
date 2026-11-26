# -*- coding: utf-8 -*-
"""SJ013《采蘩》两图。图一：蘩/沼沚/涧。图二：采·用·归。"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fig_geo import *
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(ROOT, "assets", "fig")
INK, INK2, INK3, RED, PAPER = "#1F1B17", "#5C544A", "#9A9186", "#994433", "#F7F4EE"
W, H = 760, 540

d = []
d.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="\'Noto Serif SC\',Songti SC,serif">' % (W, H, W, H))
d.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
d.append('  <text x="44" y="58" font-size="8.6" letter-spacing="2" fill="%s">召南 · 二</text>' % RED)
d.append('  <text x="380" y="60" text-anchor="middle" font-size="26" letter-spacing="10" fill="%s" font-weight="700">采 蘩</text>' % INK)
d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之十三</text>' % INK3)
d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)

GROUND = 440
# 壹 · 蘩
FX = 148
d.append('  <line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.8"/>' % (FX, GROUND, FX + 2, 226, INK))
for k in range(4):
    y = GROUND - 40 - k * 46
    L = 52 - k * 6
    for side in (-1, 1):
        x0, y0 = FX + side * 4, y
        x1, y1 = FX + side * L, y - 18
        d.append('  <path d="M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="none" stroke="%s" stroke-width="0.85"/>'
                 % (x0, y0, x0 + side * L * 0.45, y0 - 4, x0 + side * L * 0.8, y1 + 6, x1, y1, INK2))
        for j in range(5):
            t = 0.18 + j * 0.18
            px = x0 + (x1 - x0) * t
            py = y0 + (y1 - y0) * t - 2
            d.append('  <line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="0.55"/>'
                     % (px, py, px + side * 5 - side * t * 2, py - 7 + t * 2, INK3))
            d.append('  <line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="0.55"/>'
                     % (px, py, px + side * 3 - side * t * 1.5, py + 5 - t * 2, INK3))
d.append('  <text x="%d" y="%d" text-anchor="middle" font-size="7.0" fill="%s">叶背白，故曰皤蒿</text>' % (FX + 96, 268, RED))

# 贰 · 沼与沚
WX0, WX1 = 268, 470
d.append('  <path d="M%d,%d L%d,%d" stroke="%s" stroke-width="0.9"/>' % (WX0, GROUND - 34, WX1, GROUND - 34, INK2))
for i in range(4):
    y = GROUND - 22 + i * 12
    d.append('  <path d="M%d,%d C%d,%d %d,%d %d,%d" fill="none" stroke="%s" stroke-width="%.1f"/>'
             % (WX0, y, WX0 + 46, y - 4, WX1 - 46, y + 4, WX1, y, INK3, 0.7 if i == 0 else 0.45))
d.append('  <path d="M354,%d C362,%d 392,%d 402,%d C392,%d 362,%d 354,%d Z" fill="#EFEAD6" stroke="%s" stroke-width="0.8"/>'
         % (GROUND - 10, GROUND - 24, GROUND - 4, GROUND - 6, GROUND + 6, GROUND + 4, GROUND - 10, INK2))
for k in range(5):
    x = 362 + k * 9
    d.append('  <line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="0.5"/>' % (x, GROUND - 6, x + 2, GROUND - 16, INK3))
d.append('  <text x="378" y="%d" text-anchor="middle" font-size="7.0" fill="%s">沚</text>' % (GROUND - 26, RED))
d.append('  <text x="290" y="%d" text-anchor="middle" font-size="7.0" fill="%s">沼</text>' % (GROUND - 42, RED))

# 叁 · 涧
IX0, IX1 = 536, 708
TOP = 292
d.append('  <path d="M%d,%d L%d,%d L%d,%d L%d,%d" fill="none" stroke="%s" stroke-width="1.0"/>'
         % (IX0, GROUND, IX0 + 16, 360, IX0 + 62, TOP + 10, IX0 + 74, TOP, INK2))
d.append('  <path d="M%d,%d L%d,%d L%d,%d L%d,%d" fill="none" stroke="%s" stroke-width="1.0"/>'
         % (IX1, GROUND, IX1 - 14, 356, IX1 - 58, TOP + 8, IX1 - 66, TOP - 4, INK2))
for i in range(5):
    t = i / 4.0
    y = GROUND - 16 - t * 108
    x0 = IX0 + 16 + t * 44
    x1 = IX1 - 14 - t * 44
    w = (x1 - x0)
    d.append('  <path d="M%.1f,%.1f q%.1f,-3 %.1f,0 q%.1f,3 %.1f,0" fill="none" stroke="%s" stroke-width="0.5"/>'
             % (x0, y, w * 0.25, w * 0.5, w * 0.25, w, INK3))
# 石（三块，大小异）
for (x, y, s1, s2) in [(566, 412, 16, 10), (648, 372, 13, 8), (606, 340, 9, 6)]:
    d.append('  <path d="M%d,%d l-%d,-%d l%d,-%d l%d,%d Z" fill="#EFEAD6" stroke="%s" stroke-width="0.6"/>'
             % (x, y, s1, s2, s1, s2 * 0.6, s1, s2 * 0.5, INK2))
d.append('  <text x="622" y="%d" text-anchor="middle" font-size="7.0" fill="%s">涧</text>' % (TOP - 18, RED))

for (x, t) in [(120, "壹"), (350, "贰"), (600, "叁")]:
    d.append('  <text x="%d" y="132" font-size="7.6" fill="%s">%s</text>' % (x, RED, t))
d.append('  <text x="44" y="466" font-size="7.8" fill="%s">壹 蘩　白蒿，叶背白</text>' % INK2)
d.append('  <text x="264" y="466" font-size="7.8" fill="%s">贰 沼沚　岸与洲</text>' % INK2)
d.append('  <text x="486" y="466" font-size="7.8" fill="%s">叁 涧　石间之水</text>' % INK2)
d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">于以采蘩？于沼于沚</text>' % INK)
d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">采在最野，用在最严</text>' % INK3)
d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj013a</text>' % INK3)
d.append('</svg>')
open(os.path.join(FIG, "sj013a-fan-zhao-zhi-jian.svg"), "w", encoding="utf-8").write("\n".join(d))

# 图二
e = []
e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="Noto Serif SC,Songti SC,serif">' % (W, H, W, H))
e.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
e.append('  <rect x="10" y="10" width="740" height="500" fill="none" stroke="%s" stroke-width="1"/>' % INK3)
e.append('  <rect x="16" y="16" width="728" height="488" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
e.append('  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="%s" font-weight="700">采 · 用 · 归</text>' % INK)
e.append('  <text x="380" y="74" text-anchor="middle" font-size="9.6" letter-spacing="2" fill="%s">《诗经》召南 · 第二篇　采蘩</text>' % INK2)
e.append('  <defs><marker id="ar13" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % RED)
cells = [(70, "采", "沼、沚、涧", "在最野处", INK2), (290, "用", "公侯之宫", "在最严处", RED), (510, "归", "薄言还归", "事毕脚轻", INK2)]
for (x, big, s1, s2, col) in cells:
    e.append('  <rect x="%d" y="150" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (x, col))
    e.append('  <text x="%d" y="214" text-anchor="middle" font-size="28" letter-spacing="2" fill="%s" font-weight="700">%s</text>' % (x + 75, col, big))
    e.append('  <text x="%d" y="252" text-anchor="middle" font-size="10" fill="#3B352F">%s</text>' % (x + 75, s1))
    e.append('  <text x="%d" y="278" text-anchor="middle" font-size="8" fill="%s">%s</text>' % (x + 75, INK3, s2))
e.append('  <line x1="220" y1="225" x2="288" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar13)"/>' % RED)
e.append('  <line x1="440" y1="225" x2="508" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar13)"/>' % RED)
e.append('  <text x="380" y="330" text-anchor="middle" font-size="8.4" fill="%s">由野入庙，再由庙归家：一次祭祀的完整弧线</text>' % INK2)
e.append('  <line x1="120" y1="360" x2="640" y2="360" stroke="%s" stroke-width="0.8"/>' % INK3)
e.append('  <text x="230" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">于以</text>' % RED)
e.append('  <text x="230" y="414" text-anchor="middle" font-size="7.4" fill="%s">于何也，非「于是」</text>' % INK3)
e.append('  <text x="530" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">被</text>' % RED)
e.append('  <text x="530" y="414" text-anchor="middle" font-size="7.4" fill="%s">首饰也，非「披」</text>' % INK3)
e.append('  <text x="380" y="446" text-anchor="middle" font-size="7.4" fill="%s">全篇不言敬，只言「夙夜」——敬在事上，不在话上</text>' % INK3)
e.append('  <text x="120" y="512" font-size="5.6" fill="%s">诗经 · 召南</text>' % INK2)
e.append('  <text x="640" y="512" text-anchor="end" font-size="5.6" fill="%s">图二 · 采用归 · sj013b</text>' % INK2)
e.append('</svg>')
open(os.path.join(FIG, "sj013b-cai-yong-gui.svg"), "w", encoding="utf-8").write("\n".join(e))

import cairosvg
for k in ["sj013a-fan-zhao-zhi-jian", "sj013b-cai-yong-gui"]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok")
