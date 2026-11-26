# -*- coding: utf-8 -*-
"""SJ016《甘棠》两图。图一：甘棠·茇·憩说。图二：茇·憩·说。"""
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
d.append('  <text x="380" y="60" text-anchor="middle" font-size="26" letter-spacing="10" fill="%s" font-weight="700">甘 棠</text>' % INK)
d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之十六</text>' % INK3)
d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)

GROUND = 420

# 壹 · 甘棠全树（满冠）
FX = 148
d.append('  <path d="M%d,404 C%d,384 %d,356 %d,330" fill="none" stroke="%s" stroke-width="3.0"/>' % (FX, FX, FX, FX + 2, INK))
d.append('  <path d="M%d,352 C%d,336 %d,326 %d,320" fill="none" stroke="%s" stroke-width="1.6"/>' % (FX, FX - 16, FX - 28, FX - 38, INK2))
d.append('  <path d="M%d,346 C%d,332 %d,326 %d,322" fill="none" stroke="%s" stroke-width="1.6"/>' % (FX + 1, FX + 16, FX + 28, FX + 38, INK2))
d.append('  <ellipse cx="%d" cy="296" rx="58" ry="48" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (FX, INK2))
for k in range(6):
    x = FX - 38 + k * 15
    d.append('  <path d="M%d,286 q10,8 20,0" fill="none" stroke="%s" stroke-width="0.45"/>' % (x, INK3))
d.append('  <text x="%d" y="392" text-anchor="middle" font-size="7.0" fill="%s">蔽芾 · 冠大荫密</text>' % (FX, RED))

# 贰 · 所茇（草舍茅棚）
ZX = 378
d.append('  <path d="M%d,356 L%d,326 L%d,356 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (ZX - 34, ZX, ZX + 34, INK2))
d.append('  <line x1="%d" y1="356" x2="%d" y2="388" stroke="%s" stroke-width="0.9"/>' % (ZX - 24, ZX - 24, INK2))
d.append('  <line x1="%d" y1="356" x2="%d" y2="388" stroke="%s" stroke-width="0.9"/>' % (ZX + 24, ZX + 24, INK2))
for k in range(4):
    x = ZX - 24 + k * 16
    d.append('  <line x1="%d" y1="342" x2="%d" y2="336" stroke="%s" stroke-width="0.5"/>' % (x, x + 3, INK3))
d.append('  <text x="%d" y="392" text-anchor="middle" font-size="7.0" fill="%s">茇 · 草舍寄居</text>' % (ZX, RED))

# 叁 · 所憩所说（人息于树下，简笔人影 + 荫弧）
VX = 622
d.append('  <path d="M%d,310 C%d,292 %d,292 %d,310" fill="none" stroke="%s" stroke-width="0.9"/>' % (VX - 40, VX, VX, VX + 40, INK2))
# 坐息之人
d.append('  <circle cx="%d" cy="348" r="6" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % (VX, INK2))
d.append('  <path d="M%d,356 L%d,374 L%d,374" fill="none" stroke="%s" stroke-width="1.1"/>' % (VX, VX - 8, VX + 8, INK2))
d.append('  <path d="M%d,362 L%d,370" fill="none" stroke="%s" stroke-width="0.8"/>' % (VX - 6, VX - 14, INK3))
d.append('  <text x="%d" y="392" text-anchor="middle" font-size="7.0" fill="%s">憩 · 说（税）· 留止</text>' % (VX, RED))

for (x, t) in [(120, "壹"), (350, "贰"), (600, "叁")]:
    d.append('  <text x="%d" y="132" font-size="7.6" fill="%s">%s</text>' % (x, RED, t))
d.append('  <text x="44" y="466" font-size="7.8" fill="%s">壹 甘棠　杜梨，茂盛覆蔽</text>' % INK2)
d.append('  <text x="264" y="466" font-size="7.8" fill="%s">贰 茇　草舍，召伯寄居其下</text>' % INK2)
d.append('  <text x="486" y="466" font-size="7.8" fill="%s">叁 憩说　休息、留止，皆在树荫</text>' % INK2)
d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">蔽芾甘棠，勿翦勿伐</text>' % INK)
d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">不伐一树，是留一人之迹</text>' % INK3)
d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj016a</text>' % INK3)
d.append('</svg>')
open(os.path.join(FIG, "sj016a-gan-tang-mao-sheng.svg"), "w", encoding="utf-8").write("\n".join(d))

# ============ 图二 ============
e = []
e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="\'Noto Serif SC\',\'Songti SC\',serif">' % (W, H, W, H))
e.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
e.append('  <rect x="10" y="10" width="740" height="500" fill="none" stroke="%s" stroke-width="1"/>' % INK3)
e.append('  <rect x="16" y="16" width="728" height="488" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
e.append('  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="%s" font-weight="700">茇 · 憩 · 说</text>' % INK)
e.append('  <text x="380" y="74" text-anchor="middle" font-size="9.6" letter-spacing="2" fill="%s">《诗经》召南 · 第五篇　甘棠</text>' % INK2)
e.append('  <defs><marker id="ar16" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % RED)
cells = [(70, "茇", "草舍寄居", "召伯止于其下", INK2),
         (290, "憩", "树下暂歇", "爱其树而不忍伤", RED),
         (510, "说", "税也，留止", "树存一日，人迹留一日", INK2)]
for (x, big, s1, s2, col) in cells:
    e.append('  <rect x="%d" y="150" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (x, col))
    e.append('  <text x="%d" y="214" text-anchor="middle" font-size="28" letter-spacing="2" fill="%s" font-weight="700">%s</text>' % (x + 75, col, big))
    e.append('  <text x="%d" y="252" text-anchor="middle" font-size="10" fill="#3B352F">%s</text>' % (x + 75, s1))
    e.append('  <text x="%d" y="278" text-anchor="middle" font-size="8" fill="%s">%s</text>' % (x + 75, INK3, s2))
e.append('  <line x1="220" y1="225" x2="288" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar16)"/>' % RED)
e.append('  <line x1="440" y1="225" x2="508" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar16)"/>' % RED)
e.append('  <text x="380" y="330" text-anchor="middle" font-size="8.4" fill="%s">止息之序：寄居 → 暂歇 → 留止；护树之深，一层紧一层</text>' % INK2)
e.append('  <line x1="120" y1="360" x2="640" y2="360" stroke="%s" stroke-width="0.8"/>' % INK3)
e.append('  <text x="230" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">拜</text>' % RED)
e.append('  <text x="230" y="414" text-anchor="middle" font-size="7.4" fill="%s">屈折枝条也，非「跪拜」</text>' % INK3)
e.append('  <text x="530" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">说</text>' % RED)
e.append('  <text x="530" y="414" text-anchor="middle" font-size="7.4" fill="%s">通「税」，止息也，非言说</text>' % INK3)
e.append('  <text x="380" y="446" text-anchor="middle" font-size="7.4" fill="%s">德政不著于颂辞，留在一物之上；后人思其人，故爱其树</text>' % INK3)
e.append('  <text x="120" y="512" font-size="5.6" fill="%s">诗经 · 召南</text>' % INK2)
e.append('  <text x="640" y="512" text-anchor="end" font-size="5.6" fill="%s">图二 · 茇憩说 · sj016b</text>' % INK2)
e.append('</svg>')
open(os.path.join(FIG, "sj016b-ba-qi-shuo.svg"), "w", encoding="utf-8").write("\n".join(e))

import cairosvg
for k in ["sj016a-gan-tang-mao-sheng", "sj016b-ba-qi-shuo"]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok")
