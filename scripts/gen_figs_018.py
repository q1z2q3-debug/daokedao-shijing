# -*- coding: utf-8 -*-
"""SJ018《羔羊》两图。图一：羔裘·素丝·委蛇。图二：皮·革·缝。"""
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
d.append('  <text x="380" y="60" text-anchor="middle" font-size="26" letter-spacing="10" fill="%s" font-weight="700">羔 羊</text>' % INK)
d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之十八</text>' % INK3)
d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)

GROUND = 420

# 壹 · 羔裘轮廓（交领大衣）
FX = 148
d.append('  <path d="M%d,316 L%d,306 L%d,316 L%d,392 L%d,392 L%d,340" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>'
         % (FX - 26, FX, FX + 26, FX + 30, FX - 30, FX - 26, INK2))
d.append('  <path d="M%d,316 L%d,336 M%d,316 L%d,336" fill="none" stroke="%s" stroke-width="0.7"/>'
         % (FX - 12, FX + 12, FX + 12, FX - 12, INK3))
# 裘缘毛边
for k in range(5):
    x = FX - 26 + k * 13
    d.append('  <line x1="%d" y1="392" x2="%d" y2="398" stroke="%s" stroke-width="0.5"/>' % (x, x + 2, INK3))
d.append('  <text x="%d" y="408" text-anchor="middle" font-size="7.0" fill="%s">羔羊之皮 · 大夫之裘</text>' % (FX, RED))

# 贰 · 素丝缝合特写
ZX = 378
d.append('  <rect x="%d" y="316" width="52" height="72" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % (ZX - 26, INK2))
for k in range(3):
    y = 330 + k * 18
    d.append('  <line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="0.8"/>' % (ZX - 26, y, ZX + 26, y, INK2))
    d.append('  <circle cx="%d" cy="%d" r="2.4" fill="%s"/>' % (ZX, y, RED))
d.append('  <text x="%d" y="392" text-anchor="middle" font-size="7.0" fill="%s">素丝 · 五紽五緎五总</text>' % (ZX, RED))

# 叁 · 委蛇背影（缓步）
VX = 622
d.append('  <circle cx="%d" cy="326" r="7" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % (VX, INK2))
d.append('  <path d="M%d,336 L%d,372" fill="none" stroke="%s" stroke-width="1.6"/>' % (VX, VX, INK2))
d.append('  <path d="M%d,344 L%d,356" fill="none" stroke="%s" stroke-width="1.0"/>' % (VX - 8, VX - 16, INK3))
d.append('  <path d="M%d,344 L%d,356" fill="none" stroke="%s" stroke-width="1.0"/>' % (VX + 8, VX + 16, INK3))
d.append('  <path d="M%d,372 L%d,388 M%d,372 L%d,388" fill="none" stroke="%s" stroke-width="1.1"/>' % (VX - 5, VX - 10, VX + 5, VX + 10, INK2))
d.append('  <text x="%d" y="392" text-anchor="middle" font-size="7.0" fill="%s">委蛇 · 从容缓步</text>' % (VX, RED))

for (x, t) in [(120, "壹"), (350, "贰"), (600, "叁")]:
    d.append('  <text x="%d" y="132" font-size="7.6" fill="%s">%s</text>' % (x, RED, t))
d.append('  <text x="44" y="466" font-size="7.8" fill="%s">壹 羔裘　小羊之皮，大夫服</text>' % INK2)
d.append('  <text x="264" y="466" font-size="7.8" fill="%s">贰 素丝　缝合缀饰之白丝</text>' % INK2)
d.append('  <text x="486" y="466" font-size="7.8" fill="%s">叁 委蛇　退食自公，从容自得</text>' % INK2)
d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">退食自公，委蛇委蛇</text>' % INK)
d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">礼见于衣冠步履之微</text>' % INK3)
d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj018a</text>' % INK3)
d.append('</svg>')
open(os.path.join(FIG, "sj018a-gao-yang-su-si.svg"), "w", encoding="utf-8").write("\n".join(d))

# ============ 图二 ============
e = []
e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="\'Noto Serif SC\',\'Songti SC\',serif">' % (W, H, W, H))
e.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
e.append('  <rect x="10" y="10" width="740" height="500" fill="none" stroke="%s" stroke-width="1"/>' % INK3)
e.append('  <rect x="16" y="16" width="728" height="488" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
e.append('  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="%s" font-weight="700">皮 · 革 · 缝</text>' % INK)
e.append('  <text x="380" y="74" text-anchor="middle" font-size="9.6" letter-spacing="2" fill="%s">《诗经》召南 · 第七篇　羔羊</text>' % INK2)
e.append('  <defs><marker id="ar18" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % RED)
cells = [(70, "皮", "素丝五紽", "带毛之裘，初成", INK2),
         (290, "革", "素丝五緎", "去毛之里，缝界", RED),
         (510, "缝", "素丝五总", "全裘缝成，丝缕总聚", INK2)]
for (x, big, s1, s2, col) in cells:
    e.append('  <rect x="%d" y="150" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (x, col))
    e.append('  <text x="%d" y="214" text-anchor="middle" font-size="28" letter-spacing="2" fill="%s" font-weight="700">%s</text>' % (x + 75, col, big))
    e.append('  <text x="%d" y="252" text-anchor="middle" font-size="10" fill="#3B352F">%s</text>' % (x + 75, s1))
    e.append('  <text x="%d" y="278" text-anchor="middle" font-size="8" fill="%s">%s</text>' % (x + 75, INK3, s2))
e.append('  <line x1="220" y1="225" x2="288" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar18)"/>' % RED)
e.append('  <line x1="440" y1="225" x2="508" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar18)"/>' % RED)
e.append('  <text x="380" y="330" text-anchor="middle" font-size="8.4" fill="%s">裘之三阶：由材而里而成；衣愈成，步愈定</text>' % INK2)
e.append('  <line x1="120" y1="360" x2="640" y2="360" stroke="%s" stroke-width="0.8"/>' % INK3)
e.append('  <text x="230" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">委蛇</text>' % RED)
e.append('  <text x="230" y="414" text-anchor="middle" font-size="7.4" fill="%s">读 wēi yí，从容缓步，非逶迤</text>' % INK3)
e.append('  <text x="530" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">退食</text>' % RED)
e.append('  <text x="530" y="414" text-anchor="middle" font-size="7.4" fill="%s">自公门退而就食，非公家供食</text>' % INK3)
e.append('  <text x="380" y="446" text-anchor="middle" font-size="7.4" fill="%s">礼不独在朝仪大节，也在衣冠缝缀、行步容止的细微处</text>' % INK3)
e.append('  <text x="120" y="512" font-size="5.6" fill="%s">诗经 · 召南</text>' % INK2)
e.append('  <text x="640" y="512" text-anchor="end" font-size="5.6" fill="%s">图二 · 皮革缝 · sj018b</text>' % INK2)
e.append('</svg>')
open(os.path.join(FIG, "sj018b-tui-shi-wei-yi.svg"), "w", encoding="utf-8").write("\n".join(e))

import cairosvg
for k in ["sj018a-gao-yang-su-si", "sj018b-tui-shi-wei-yi"]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok")
