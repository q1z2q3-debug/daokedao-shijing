# -*- coding: utf-8 -*-
"""SJ010《汝坟》两图。图一：汝坟/条枚/赪尾。图二：待·见·醒。"""
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
d.append('  <text x="44" y="58" font-size="8.6" letter-spacing="2" fill="%s">周南 · 十</text>' % RED)
d.append('  <text x="380" y="60" text-anchor="middle" font-size="26" letter-spacing="10" fill="%s" font-weight="700">汝 坟</text>' % INK)
d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之十</text>' % INK3)
d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)

# ============ 壹 · 汝坟（堤高于水） ============
BX0, BX1 = 76, 256
T0, T1 = 344, 384          # 堤顶 / 堤脚
WB = 384                    # 水面
d.append('  <path d="M%d,%d L%d,%d L%d,%d L%d,%d Z" fill="#EFEAD6" stroke="%s" stroke-width="0.7"/>'
         % (BX0 + 8, T0, BX1 - 8, T0, BX1, T1, BX0, T1, INK3))
for k in range(10):
    x = BX0 + 10 + k * 17
    d.append('  <circle cx="%d" cy="%d" r="1.0" fill="%s" opacity="0.5"/>' % (x, T0 + 18 + (k % 3) * 7, INK3))
for i in range(4):
    y = WB + 12 + i * 15
    d.append('  <path d="M%d,%d C%d,%d %d,%d %d,%d" fill="none" stroke="%s" stroke-width="%.1f"/>'
             % (BX0 - 4, y, BX0 + 52, y - 4, BX1 - 52, y + 4, BX1 + 4, y, INK3, 0.8 if i == 0 else 0.5))
# 堤上之人
PX, PY = 146, T0
d.append('  <circle cx="%d" cy="%d" r="3.6" fill="none" stroke="%s" stroke-width="0.9"/>' % (PX, PY - 34, INK2))
d.append('  <path d="M%d,%d L%d,%d" stroke="%s" stroke-width="0.9"/>' % (PX, PY - 30, PX, PY - 12, INK2))
d.append('  <path d="M%d,%d L%d,%d" stroke="%s" stroke-width="0.9"/>' % (PX, PY - 12, PX - 7, PY, INK2))
d.append('  <path d="M%d,%d L%d,%d" stroke="%s" stroke-width="0.9"/>' % (PX, PY - 12, PX + 7, PY, INK2))
# 持斧之臂与斧
d.append('  <path d="M%d,%d L%d,%d" stroke="%s" stroke-width="0.8"/>' % (PX, PY - 26, PX + 10, PY - 34, INK2))
d.append('  <line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.2"/>' % (PX + 10, PY - 34, PX + 26, PY - 44, INK2))
d.append('  <path d="M%d,%d l8,-2 l3,9 l-8,2 Z" fill="none" stroke="%s" stroke-width="0.7"/>' % (PX + 26, PY - 45, INK))
d.append('  <text x="%d" y="%d" text-anchor="middle" font-size="7.2" fill="%s">大防</text>' % (BX0 + 34, T0 + 24, RED))

# ============ 贰 · 条枚（砍下的枝与干） ============
# 干（枚）：直
d.append('  <line x1="316" y1="430" x2="404" y2="252" stroke="%s" stroke-width="2.4"/>' % INK)
# 枝（条）：自右侧另起，曲而上
d.append('  <path d="M352,430 C382,368 424,320 486,274" fill="none" stroke="%s" stroke-width="1.2"/>' % INK)
for k in range(-1, 2):
    ang = -66 + k * 20
    d.append('  <ellipse cx="%.1f" cy="%.1f" rx="1.9" ry="6.0" fill="#EFEAD6" stroke="%s" stroke-width="0.45" transform="rotate(%.0f 486 274)"/>'
             % (486 + 3.6 * math.cos(math.radians(ang)), 274 + 3.6 * math.sin(math.radians(ang)), INK3, ang + 90))
# 断口（砍断处）在干上
d.append('  <line x1="352" y1="344" x2="368" y2="358" stroke="%s" stroke-width="1.0"/>' % RED)
for (dx, dy) in [(-10, -13), (3, -15), (-3, -20)]:
    d.append('  <path d="M%d,%d q%d,%d %d,%d" fill="none" stroke="%s" stroke-width="0.8"/>'
             % (360, 351, dx / 2, dy / 2, dx, dy, INK2))
# 斧立左侧
d.append('  <line x1="286" y1="404" x2="322" y2="336" stroke="%s" stroke-width="1.4"/>' % INK2)
d.append('  <path d="M322,336 l13,-7 l5,11 l-13,7 Z" fill="none" stroke="%s" stroke-width="0.7"/>' % INK)
d.append('  <text x="412" y="246" font-size="7.2" fill="%s">干曰枚</text>' % INK3)
d.append('  <text x="492" y="264" font-size="7.2" fill="%s">枝曰条</text>' % INK3)
d.append('  <text x="336" y="384" text-anchor="end" font-size="7.2" fill="%s">条肄</text>' % RED)
d.append('  <text x="282" y="420" font-size="6.6" fill="%s">斧痕</text>' % INK3)

# ============ 叁 · 鲂鱼赪尾 ============
CX, CY = 632, 340
# 鳊鱼侧形（菱形身、尖头、叉尾）
d.append('  <path d="M%d,%d C%d,%d %d,%d %d,%d C%d,%d %d,%d %d,%d Z" fill="#EFEAD6" stroke="%s" stroke-width="0.8"/>'
         % (CX - 58, CY, CX - 26, CY - 30, CX + 26, CY - 26, CX + 56, CY,
            CX + 26, CY + 26, CX - 26, CY + 30, CX - 58, CY, INK2))
# 尾（分叉，赤色）
d.append('  <path d="M%d,%d l-22,-16 l8,16 l-8,16 Z" fill="%s" opacity="0.85" stroke="%s" stroke-width="0.6"/>' % (CX - 56, CY, RED, RED))
# 眼与鳃
d.append('  <circle cx="%d" cy="%d" r="2.2" fill="none" stroke="%s" stroke-width="0.7"/>' % (CX + 44, CY - 4, INK2))
d.append('  <path d="M%d,%d q6,10 0,18" fill="none" stroke="%s" stroke-width="0.5"/>' % (CX + 38, CY - 6, INK3))
# 背鳍
d.append('  <text x="%d" y="%d" text-anchor="middle" font-size="7.2" fill="%s">赪 · 鱼劳则尾赤</text>' % (CX, CY + 62, RED))

# 编号与说明
for (x, t) in [(96, "壹"), (360, "贰"), (612, "叁")]:
    d.append('  <text x="%d" y="132" font-size="7.6" fill="%s">%s</text>' % (x, RED, t))
d.append('  <text x="44" y="466" font-size="7.8" fill="%s">壹 汝坟　汝水大防，堤高于水</text>' % INK2)
d.append('  <text x="264" y="466" font-size="7.8" fill="%s">贰 条枚　枝曰条，干曰枚</text>' % INK2)
d.append('  <text x="486" y="466" font-size="7.8" fill="%s">叁 鲂鱼　赪尾，劳形也</text>' % INK2)
d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">未见君子，惄如调饥</text>' % INK)
d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">坟者大防，非墓也</text>' % INK3)
d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj010a</text>' % INK3)
d.append('</svg>')
open(os.path.join(FIG, "sj010a-ru-fen-tiao-mei.svg"), "w", encoding="utf-8").write("\n".join(d))

# ============ 图二 ============
e = []
e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="\'Noto Serif SC\',\'Songti SC\',serif">' % (W, H, W, H))
e.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
e.append('  <rect x="10" y="10" width="740" height="500" fill="none" stroke="%s" stroke-width="1"/>' % INK3)
e.append('  <rect x="16" y="16" width="728" height="488" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
e.append('  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="%s" font-weight="700">待 · 见 · 醒</text>' % INK)
e.append('  <text x="380" y="74" text-anchor="middle" font-size="9.6" letter-spacing="2" fill="%s">《诗经》周南 · 第十篇　汝坟</text>' % INK2)
e.append('  <defs><marker id="ar10" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % RED)
cells = [(70, "待", "惄如调饥", "未见", INK2), (290, "见", "不我遐弃", "既见", RED), (510, "醒", "父母孔迩", "虽燬而守近", INK2)]
for (x, big, s1, s2, col) in cells:
    e.append('  <rect x="%d" y="150" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (x, col))
    e.append('  <text x="%d" y="212" text-anchor="middle" font-size="26" letter-spacing="2" fill="%s" font-weight="700">%s</text>' % (x + 75, col, big))
    e.append('  <text x="%d" y="252" text-anchor="middle" font-size="10" fill="#3B352F">%s</text>' % (x + 75, s1))
    e.append('  <text x="%d" y="278" text-anchor="middle" font-size="8" fill="%s">%s</text>' % (x + 75, INK3, s2))
e.append('  <line x1="220" y1="225" x2="288" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar10)"/>' % RED)
e.append('  <line x1="440" y1="225" x2="508" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar10)"/>' % RED)
e.append('  <text x="380" y="330" text-anchor="middle" font-size="8.4" fill="%s">喜只占一章，清醒占一章：喜在中间，两头都是空的</text>' % INK2)
e.append('  <line x1="120" y1="360" x2="640" y2="360" stroke="%s" stroke-width="0.8"/>' % INK3)
e.append('  <text x="230" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">坟</text>' % RED)
e.append('  <text x="230" y="414" text-anchor="middle" font-size="7.4" fill="%s">大防也，非坟墓</text>' % INK3)
e.append('  <text x="530" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">调</text>' % RED)
e.append('  <text x="530" y="414" text-anchor="middle" font-size="7.4" fill="%s">通「朝」，朝饥也</text>' % INK3)
e.append('  <text x="380" y="446" text-anchor="middle" font-size="7.4" fill="%s">三章韵：微 · 質 · 微　——声皆贴身：饥、弃、迩</text>' % INK3)
e.append('  <text x="120" y="512" font-size="5.6" fill="%s">诗经 · 周南</text>' % INK2)
e.append('  <text x="640" y="512" text-anchor="end" font-size="5.6" fill="%s">图二 · 待见醒 · sj010b</text>' % INK2)
e.append('</svg>')
open(os.path.join(FIG, "sj010b-dai-jian-xing.svg"), "w", encoding="utf-8").write("\n".join(e))

import cairosvg
for k in ["sj010a-ru-fen-tiao-mei", "sj010b-dai-jian-xing"]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok")
