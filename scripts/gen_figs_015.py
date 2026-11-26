# -*- coding: utf-8 -*-
"""SJ015《采蘋》两图。图一：蘋藻·筐筥·錡釜。图二：采·盛湘·奠尸。"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fig_geo import *
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(ROOT, "assets", "fig")
INK, INK2, INK3, RED, PAPER = "#1F1B17", "#5C544A", "#9A9186", "#994433", "#F7F4EE"
W, H = 760, 540

d = []
d.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="\'Noto Serif SC\',\'Songti SC\',serif">' % (W, H, W, H))
d.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
d.append('  <text x="44" y="58" font-size="8.6" letter-spacing="2" fill="%s">召南 · 二</text>' % RED)
d.append('  <text x="380" y="60" text-anchor="middle" font-size="26" letter-spacing="10" fill="%s" font-weight="700">采 蘋</text>' % INK)
d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之十五</text>' % INK3)
d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)

GROUND = 420

# 壹 · 蘋（田字四叶水草）
FX = 148
for (dx, dy) in [(0, -13), (13, 0), (0, 13), (-13, 0)]:
    d.append('  <ellipse cx="%d" cy="%d" rx="11" ry="8" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % (FX + dx, 362 + dy, INK2))
d.append('  <circle cx="%d" cy="362" r="3" fill="%s"/>' % (FX, INK3))
# 水纹
for k in range(3):
    y = 392 + k * 9
    d.append('  <path d="M%d,%d q22,-4 44,0 q22,4 44,0" fill="none" stroke="%s" stroke-width="0.5"/>' % (FX - 44, y, INK3))
# 藻：细长叶两丛
for sx in (-1, 1):
    for k in range(3):
        x = FX + sx * 30 + k * 4
        d.append('  <path d="M%d,420 C%d,406 %d,396 %d,386" fill="none" stroke="%s" stroke-width="0.6"/>' % (x, x, x - sx * 4, x - sx * 6, INK3))
d.append('  <text x="%d" y="330" text-anchor="middle" font-size="7.0" fill="%s">蘋 · 四叶如田</text>' % (FX, RED))

# 贰 · 筐（方）筥（圆）
ZX = 378
# 筐：方口梯形
d.append('  <path d="M%d,330 L%d,330 L%d,372 L%d,372 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % (ZX - 34, ZX - 6, ZX - 12, ZX - 28, INK2))
for k in range(3):
    y = 340 + k * 10
    d.append('  <line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="0.45"/>' % (ZX - 31, y, ZX - 9, y, INK3))
# 筥：圆腹
d.append('  <ellipse cx="%d" cy="352" rx="22" ry="20" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % (ZX + 26, INK2))
for k in range(3):
    yy = 342 + k * 9
    d.append('  <path d="M%d,%d q11,4 22,0" fill="none" stroke="%s" stroke-width="0.45"/>' % (ZX + 15, yy, INK3))
d.append('  <text x="%d" y="392" text-anchor="middle" font-size="7.0" fill="%s">筐方 · 筥圆</text>' % (ZX, RED))

# 叁 · 錡（有足）釜（无足）
VX = 622
# 錡：锅身 + 三足
d.append('  <ellipse cx="%d" cy="348" rx="20" ry="15" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % (VX - 24, INK2))
for lx in (-12, 0, 12):
    d.append('  <line x1="%d" y1="360" x2="%d" y2="386" stroke="%s" stroke-width="0.9"/>' % (VX - 24 + lx, VX - 24 + lx * 1.1, INK2))
# 釜：圆锅无足
d.append('  <ellipse cx="%d" cy="352" rx="21" ry="16" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % (VX + 26, INK2))
d.append('  <path d="M%d,338 q21,-8 42,0" fill="none" stroke="%s" stroke-width="0.7"/>' % (VX + 5, INK3))
d.append('  <text x="%d" y="392" text-anchor="middle" font-size="7.0" fill="%s">錡有足 · 釜无足</text>' % (VX, RED))

for (x, t) in [(120, "壹"), (350, "贰"), (600, "叁")]:
    d.append('  <text x="%d" y="132" font-size="7.6" fill="%s">%s</text>' % (x, RED, t))
d.append('  <text x="44" y="466" font-size="7.8" fill="%s">壹 蘋藻　涧滨行潦之水菜</text>' % INK2)
d.append('  <text x="264" y="466" font-size="7.8" fill="%s">贰 筐筥　方圆竹器</text>' % INK2)
d.append('  <text x="486" y="466" font-size="7.8" fill="%s">叁 錡釜　有足无足之烹器</text>' % INK2)
d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">于以采蘋？南澗之濱</text>' % INK)
d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">教女以祭，五事成礼</text>' % INK3)
d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj015a</text>' % INK3)
d.append('</svg>')
open(os.path.join(FIG, "sj015a-pin-zao-qi-fu.svg"), "w", encoding="utf-8").write("\n".join(d))

# ============ 图二 ============
e = []
e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="\'Noto Serif SC\',\'Songti SC\',serif">' % (W, H, W, H))
e.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
e.append('  <rect x="10" y="10" width="740" height="500" fill="none" stroke="%s" stroke-width="1"/>' % INK3)
e.append('  <rect x="16" y="16" width="728" height="488" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
e.append('  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="%s" font-weight="700">采 · 盛湘 · 奠尸</text>' % INK)
e.append('  <text x="380" y="74" text-anchor="middle" font-size="9.6" letter-spacing="2" fill="%s">《诗经》召南 · 第四篇　采蘋</text>' % INK2)
e.append('  <defs><marker id="ar15" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % RED)
cells = [(70, "采", "南涧之滨 · 行潦", "备物于野", INK2),
         (290, "盛湘", "筐筥 · 錡釜", "备器于家", RED),
         (510, "奠尸", "宗室牖下 · 有齐季女", "成祭于人", INK2)]
for (x, big, s1, s2, col) in cells:
    e.append('  <rect x="%d" y="150" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (x, col))
    e.append('  <text x="%d" y="214" text-anchor="middle" font-size="28" letter-spacing="2" fill="%s" font-weight="700">%s</text>' % (x + 75, col, big))
    e.append('  <text x="%d" y="252" text-anchor="middle" font-size="10" fill="#3B352F">%s</text>' % (x + 75, s1))
    e.append('  <text x="%d" y="278" text-anchor="middle" font-size="8" fill="%s">%s</text>' % (x + 75, INK3, s2))
e.append('  <line x1="220" y1="225" x2="288" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar15)"/>' % RED)
e.append('  <line x1="440" y1="225" x2="508" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar15)"/>' % RED)
e.append('  <text x="380" y="330" text-anchor="middle" font-size="8.4" fill="%s">备物 → 备器 → 成祭：教女成礼的一条弧线</text>' % INK2)
e.append('  <line x1="120" y1="360" x2="640" y2="360" stroke="%s" stroke-width="0.8"/>' % INK3)
e.append('  <text x="230" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">湘</text>' % RED)
e.append('  <text x="230" y="414" text-anchor="middle" font-size="7.4" fill="%s">烹煮也，非「箱」</text>' % INK3)
e.append('  <text x="530" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">尸</text>' % RED)
e.append('  <text x="530" y="414" text-anchor="middle" font-size="7.4" fill="%s">主祭受祭者，非尸身</text>' % INK3)
e.append('  <text x="380" y="446" text-anchor="middle" font-size="7.4" fill="%s">采、盛、湘、奠、尸五事一步不乱；礼成而敬立</text>' % INK3)
e.append('  <text x="120" y="512" font-size="5.6" fill="%s">诗经 · 召南</text>' % INK2)
e.append('  <text x="640" y="512" text-anchor="end" font-size="5.6" fill="%s">图二 · 采盛奠尸 · sj015b</text>' % INK2)
e.append('</svg>')
open(os.path.join(FIG, "sj015b-cai-sheng-dian-shi.svg"), "w", encoding="utf-8").write("\n".join(e))

import cairosvg
for k in ["sj015a-pin-zao-qi-fu", "sj015b-cai-sheng-dian-shi"]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok")
