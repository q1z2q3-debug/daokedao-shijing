# -*- coding: utf-8 -*-
"""SJ018《羔羊》两图。图一：羔裘·素丝五紽·委蛇。图二：皮·革·缝。"""
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

# ============ 壹 · 羔裘平铺：领·襟·袖·毛边 ============
FX = 148
# 两袖
d.append('  <path d="M%d,220 C%d,236 %d,268 %d,288" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % (FX - 26, FX - 40, FX - 44, FX - 38, INK2))
d.append('  <path d="M%d,220 C%d,236 %d,268 %d,288" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % (FX + 26, FX + 40, FX + 44, FX + 38, INK2))
# 衣身轮廓
d.append('  <path d="M%d,214 L%d,204 L%d,214 C%d,262 %d,312 %d,356 L%d,356 C%d,312 %d,262 %d,214 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>'
         % (FX - 26, FX, FX + 26, FX - 28, FX - 26, FX - 22, FX + 22, FX + 26, FX + 28, FX + 26, INK2))
# 交领
d.append('  <path d="M%d,210 L%d,234 L%d,210" fill="none" stroke="%s" stroke-width="0.9"/>' % (FX - 12, FX, FX + 12, INK2))
# 右襟
d.append('  <path d="M%d,234 L%d,262" fill="none" stroke="%s" stroke-width="0.7"/>' % (FX, FX + 16, INK3))
# 袖缘毛边
for k in range(3):
    d.append('  <line x1="%d" y1="284" x2="%d" y2="290" stroke="%s" stroke-width="0.5"/>' % (FX - 40 + k * 3, FX - 40 + k * 3, INK3))
    d.append('  <line x1="%d" y1="284" x2="%d" y2="290" stroke="%s" stroke-width="0.5"/>' % (FX + 34 + k * 3, FX + 34 + k * 3, INK3))
# 下摆毛边
for k in range(6):
    x = FX - 20 + k * 8
    d.append('  <line x1="%d" y1="356" x2="%d" y2="362" stroke="%s" stroke-width="0.5"/>' % (x, x + 2, INK3))
d.append('  <text x="%d" y="392" text-anchor="middle" font-size="7.0" fill="%s">羔羊之皮 · 领襟袖缘毛边</text>' % (FX, RED))

# ============ 贰 · 素丝五紽：五道缝合针脚 ============
ZX = 378
# 皮片（局部放大）
d.append('  <path d="M%d,220 L%d,220 L%d,356 L%d,356 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % (ZX - 28, ZX + 28, ZX + 28, ZX - 28, INK2))
# 五道缝合针脚
for k in range(5):
    y = 238 + k * 26
    d.append('  <line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="0.8"/>' % (ZX - 28, y, ZX + 28, y, INK2))
    # 丝结小结
    d.append('  <circle cx="%d" cy="%d" r="2.3" fill="%s"/>' % (ZX, y, RED))
    # 线迹短针
    for px in range(3):
        d.append('  <line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="0.45"/>' % (ZX - 20 + px * 16, y - 2, ZX - 16 + px * 16, y + 2, INK3))
# 皮缘毛边
for k in range(5):
    x = ZX - 22 + k * 11
    d.append('  <line x1="%d" y1="356" x2="%d" y2="362" stroke="%s" stroke-width="0.5"/>' % (x, x + 2, INK3))
d.append('  <text x="%d" y="392" text-anchor="middle" font-size="7.0" fill="%s">素丝五紽 · 缝合处五道针脚</text>' % (ZX, RED))

# ============ 叁 · 委蛇：从容行走侧影，宽袖摆 ============
VX = 622
# 发髻
d.append('  <circle cx="%d" cy="206" r="3.6" fill="#FCFAF6" stroke="%s" stroke-width="0.8"/>' % (VX, INK2))
# 头侧轮廓（朝右）
d.append('  <path d="M%d,210 C%d,202 %d,202 %d,210 L%d,220 C%d,226 %d,226 %d,220 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>'
         % (VX - 6, VX, VX, VX + 6, VX + 6, VX, VX, VX - 6, INK2))
# 颈与肩线
d.append('  <line x1="%d" y1="222" x2="%d" y2="228" stroke="%s" stroke-width="0.9"/>' % (VX, VX, INK2))
d.append('  <path d="M%d,232 C%d,226 %d,226 %d,232" fill="none" stroke="%s" stroke-width="1.0"/>' % (VX - 16, VX - 6, VX + 10, VX + 18, INK2))
# 袍身（侧行，宽袖后摆）
d.append('  <path d="M%d,232 C%d,268 %d,312 %d,372 L%d,372 C%d,320 %d,272 %d,232" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>'
         % (VX - 14, VX - 20, VX - 18, VX - 10, VX + 14, VX + 16, VX + 14, VX + 18, INK2))
# 宽袖前摆（朝右）与后摆
d.append('  <path d="M%d,240 C%d,254 %d,278 %d,292" fill="none" stroke="%s" stroke-width="0.9"/>' % (VX + 16, VX + 28, VX + 30, VX + 24, INK2))
d.append('  <path d="M%d,240 C%d,254 %d,276 %d,288" fill="none" stroke="%s" stroke-width="0.9"/>' % (VX - 14, VX - 24, VX - 24, VX - 18, INK2))
# 袖褶
d.append('  <path d="M%d,258 C%d,270 %d,282 %d,288" fill="none" stroke="%s" stroke-width="0.5"/>' % (VX - 10, VX - 14, VX - 14, VX - 11, INK3))
# 衣裾与两步
d.append('  <path d="M%d,372 L%d,384 M%d,372 L%d,384" fill="none" stroke="%s" stroke-width="0.9"/>' % (VX - 6, VX - 10, VX + 6, VX + 12, INK2))
d.append('  <text x="%d" y="392" text-anchor="middle" font-size="7.0" fill="%s">委蛇 · 从容行步，宽袖摆裾</text>' % (VX, RED))

for (x, t) in [(120, "壹"), (350, "贰"), (600, "叁")]:
    d.append('  <text x="%d" y="132" font-size="7.6" fill="%s">%s</text>' % (x, RED, t))
d.append('  <text x="44" y="466" font-size="7.8" fill="%s">壹 羔裘　小羊之皮，大夫之裘</text>' % INK2)
d.append('  <text x="264" y="466" font-size="7.8" fill="%s">贰 素丝　缝合缀饰之白丝五紽</text>' % INK2)
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
