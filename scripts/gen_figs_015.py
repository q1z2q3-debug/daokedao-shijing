# -*- coding: utf-8 -*-
"""SJ015《采蘋》两图。图一：蘋藻·鼎釜·主祭。图二：采·盛湘·奠尸。"""
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

# ============ 壹 · 蘋：四叶田字水草，叶下承水 ============
FX = 148
# 四瓣叶（十字田字），叶背白留白
for (dx, dy, rx, ry) in [(0, -15, 12, 8), (0, 15, 12, 8), (-15, 0, 8, 12), (15, 0, 8, 12)]:
    d.append('  <ellipse cx="%d" cy="%d" rx="%d" ry="%d" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % (FX + dx, 250 + dy, rx, ry, INK2))
# 十字叶脉
d.append('  <line x1="%d" y1="250" x2="%d" y2="250" stroke="%s" stroke-width="0.5"/>' % (FX - 12, FX + 12, INK3))
d.append('  <line x1="%d" y1="250" x2="%d" y2="250" stroke="%s" stroke-width="0.5"/>' % (FX, FX, INK3))
# 细茎扎入水下
d.append('  <path d="M%d,262 C%d,278 %d,290 %d,306" fill="none" stroke="%s" stroke-width="1.0"/>' % (FX, FX, FX, FX + 2, INK2))
# 水线（在叶之下）
for k in range(3):
    y = 318 + k * 11
    d.append('  <path d="M%d,%d q22,-4 44,0 q22,4 44,0" fill="none" stroke="%s" stroke-width="0.5"/>' % (FX - 48, y, INK3))
# 旁生细藻两丛
for sx in (-1, 1):
    for k in range(3):
        x = FX + sx * 34 + k * sx * 3
        d.append('  <path d="M%d,352 C%d,340 %d,332 %d,322" fill="none" stroke="%s" stroke-width="0.55"/>' % (x, x, x - sx * 3, x - sx * 5, INK3))
d.append('  <text x="%d" y="392" text-anchor="middle" font-size="7.0" fill="%s">蘋 · 四叶如田，叶背白，生于水</text>' % (FX, RED))

# ============ 贰 · 鼎釜（湘）：口沿·双耳·三足·汽线 ============
ZX = 378
# 汽线（鼎口上升）
d.append('  <path d="M%d,214 C%d,204 %d,204 %d,194" fill="none" stroke="%s" stroke-width="0.6"/>' % (ZX - 12, ZX - 12, ZX - 12, ZX - 10, INK3))
d.append('  <path d="M%d,214 C%d,206 %d,206 %d,196" fill="none" stroke="%s" stroke-width="0.6"/>' % (ZX + 12, ZX + 12, ZX + 12, ZX + 14, INK3))
# 双耳
d.append('  <path d="M%d,236 L%d,220 L%d,236" fill="none" stroke="%s" stroke-width="1.0"/>' % (ZX - 30, ZX - 34, ZX - 34, INK2))
d.append('  <path d="M%d,236 L%d,220 L%d,236" fill="none" stroke="%s" stroke-width="1.0"/>' % (ZX + 30, ZX + 34, ZX + 34, INK2))
# 鼎腹
d.append('  <path d="M%d,238 C%d,266 %d,292 %d,296 C%d,292 %d,266 %d,238 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>'
         % (ZX - 32, ZX - 36, ZX - 30, ZX, ZX + 30, ZX + 36, ZX + 32, INK2))
# 口沿椭圆弧
d.append('  <path d="M%d,238 q32,-10 64,0" fill="none" stroke="%s" stroke-width="1.0"/>' % (ZX - 32, INK2))
# 腹纹一道
d.append('  <path d="M%d,262 q30,8 60,0" fill="none" stroke="%s" stroke-width="0.5"/>' % (ZX - 30, INK3))
# 三足
for lx in (-18, 0, 18):
    d.append('  <path d="M%d,294 L%d,322" fill="none" stroke="%s" stroke-width="1.1"/>' % (ZX + lx, ZX + lx * 1.1, INK2))
d.append('  <text x="%d" y="392" text-anchor="middle" font-size="7.0" fill="%s">鼎釜 · 口沿双耳三足汽线</text>' % (ZX, RED))

# ============ 叁 · 尸：主祭者侧背影，冠·宽袖·执爵 ============
VX = 622
# 发髻与冠
d.append('  <circle cx="%d" cy="198" r="3.6" fill="#FCFAF6" stroke="%s" stroke-width="0.8"/>' % (VX, INK2))
d.append('  <line x1="%d" y1="194" x2="%d" y2="188" stroke="%s" stroke-width="0.7"/>' % (VX, VX + 4, INK3))
# 头轮廓
d.append('  <path d="M%d,202 C%d,194 %d,194 %d,202 L%d,212 C%d,218 %d,218 %d,212 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>'
         % (VX - 7, VX, VX, VX + 7, VX + 7, VX, VX, VX - 7, INK2))
# 颈
d.append('  <line x1="%d" y1="218" x2="%d" y2="226" stroke="%s" stroke-width="0.9"/>' % (VX, VX, INK2))
# 肩线
d.append('  <path d="M%d,230 C%d,224 %d,224 %d,230" fill="none" stroke="%s" stroke-width="1.0"/>' % (VX - 18, VX - 8, VX + 8, VX + 18, INK2))
# 宽袖袍身（背影）
d.append('  <path d="M%d,230 C%d,268 %d,316 %d,378 L%d,378 C%d,316 %d,268 %d,230" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>'
         % (VX - 18, VX - 24, VX - 22, VX - 14, VX + 14, VX + 22, VX + 24, VX + 18, INK2))
# 左右宽袖垂摆
d.append('  <path d="M%d,238 C%d,252 %d,282 %d,298" fill="none" stroke="%s" stroke-width="0.9"/>' % (VX - 18, VX - 30, VX - 30, VX - 24, INK2))
d.append('  <path d="M%d,238 C%d,252 %d,282 %d,298" fill="none" stroke="%s" stroke-width="0.9"/>' % (VX + 18, VX + 30, VX + 30, VX + 24, INK2))
# 袖褶
d.append('  <path d="M%d,256 C%d,268 %d,284 %d,294" fill="none" stroke="%s" stroke-width="0.5"/>' % (VX - 14, VX - 18, VX - 18, VX - 15, INK3))
# 衣裾下摆与分衩
d.append('  <path d="M%d,378 L%d,386 M%d,378 L%d,386" fill="none" stroke="%s" stroke-width="0.9"/>' % (VX - 8, VX - 10, VX + 8, VX + 10, INK2))
# 双手前执爵（朝左）
d.append('  <path d="M%d,272 L%d,266 L%d,274 L%d,278 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.8"/>' % (VX - 18, VX - 30, VX - 30, VX - 18, INK2))
d.append('  <line x1="%d" y1="278" x2="%d" y2="284" stroke="%s" stroke-width="0.7"/>' % (VX - 24, VX - 24, INK3))
d.append('  <text x="%d" y="392" text-anchor="middle" font-size="7.0" fill="%s">尸 · 主祭者侧背影，执爵</text>' % (VX, RED))

for (x, t) in [(120, "壹"), (350, "贰"), (600, "叁")]:
    d.append('  <text x="%d" y="132" font-size="7.6" fill="%s">%s</text>' % (x, RED, t))
d.append('  <text x="44" y="466" font-size="7.8" fill="%s">壹 蘋　四叶田字，生于水中</text>' % INK2)
d.append('  <text x="264" y="466" font-size="7.8" fill="%s">贰 湘　鼎釜烹煮，口耳足汽可辨</text>' % INK2)
d.append('  <text x="486" y="466" font-size="7.8" fill="%s">叁 尸　主祭者，执爵立于牖下</text>' % INK2)
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
