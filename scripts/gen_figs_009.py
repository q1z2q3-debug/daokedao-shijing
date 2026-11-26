# -*- coding: utf-8 -*-
"""SJ009《汉广》两图。图一：乔木/汉广/江永 三喻。图二：立界与即界。"""
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
d.append('  <text x="44" y="58" font-size="8.6" letter-spacing="2" fill="%s">周南 · 九</text>' % RED)
d.append('  <text x="380" y="60" text-anchor="middle" font-size="26" letter-spacing="10" fill="%s" font-weight="700">汉 广</text>' % INK)
d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之九</text>' % INK3)
d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)

GROUND = 430

# ============ 一 · 乔木 ============
TX = 168
GROUND = 430
d.append('  <line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="3.2"/>' % (TX, GROUND, TX + 3, 192, INK))
# 上扬之枝（无一下垂）
BR = [((TX + 2, 300), (TX - 34, 272), -6), ((TX + 3, 336), (TX - 46, 312), -2),
      ((TX + 2, 262), (TX + 36, 232), 6), ((TX + 3, 356), (TX + 44, 330), 4),
      ((TX + 1, 226), (TX - 16, 190), -3), ((TX + 2, 250), (TX + 14, 212), 4),
      ((TX + 3, 386), (TX + 26, 366), 2), ((TX + 2, 208), (TX + 24, 196), 2)]
for (a, b, cx) in BR:
    d.append('  <path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" fill="none" stroke="%s" stroke-width="1.5"/>'
             % (a[0], a[1], (a[0] + b[0]) / 2 + cx, (a[1] + b[1]) / 2 - 6, b[0], b[1], INK))
# 叶簇（小叶片向上扇开，示冠在上而不垂）
for (x, y) in [(TX - 34, 272), (TX - 46, 312), (TX + 36, 232), (TX + 44, 330),
               (TX - 16, 190), (TX + 14, 212), (TX + 26, 366), (TX + 24, 196), (TX + 3, 192)]:
    for k in range(-2, 3):
        ang = -78 + k * 16
        d.append('  <ellipse cx="%.1f" cy="%.1f" rx="2.2" ry="7.0" fill="#EFEAD6" stroke="%s" stroke-width="0.5" transform="rotate(%.0f %.1f %.1f)"/>'
                 % (x + 3.2 * math.cos(math.radians(ang)), y + 3.0 * math.sin(math.radians(ang)),
                    INK3, ang + 90, x + 3.2 * math.cos(math.radians(ang)), y + 3.0 * math.sin(math.radians(ang))))

# 人影：立于树侧，头顶无覆
PX, PY = TX + 62, GROUND
d.append('  <circle cx="%d" cy="%d" r="4.0" fill="none" stroke="%s" stroke-width="1"/>' % (PX, PY - 40, INK2))
d.append('  <path d="M%d,%d L%d,%d" stroke="%s" stroke-width="1"/>' % (PX, PY - 36, PX, PY - 16, INK2))
d.append('  <path d="M%d,%d L%d,%d M%d,%d L%d,%d" stroke="%s" stroke-width="0.9"/>'
         % (PX, PY - 30, PX - 9, PY - 20, PX, PY - 30, PX + 9, PY - 20, INK2))
d.append('  <path d="M%d,%d L%d,%d M%d,%d L%d,%d" stroke="%s" stroke-width="0.9"/>'
         % (PX, PY - 16, PX - 7, PY, PX, PY - 16, PX + 7, PY, INK2))
d.append('  <path d="M96,%d C136,%d 200,%d 240,%d" fill="none" stroke="%s" stroke-width="0.28" stroke-dasharray="7 4 1.5 4"/>'
         % (GROUND + 2, GROUND + 6, GROUND + 6, GROUND + 2, INK3))
d.append('  <path d="M%d,%d Q%d,%d %d,%d" fill="none" stroke="%s" stroke-width="0.6" stroke-dasharray="4 3"/>'
         % (PX - 26, PY - 56, PX, PY - 70, PX + 26, PY - 56, RED))
d.append('  <text x="%d" y="%d" text-anchor="start" font-size="7.2" fill="%s">无荫</text>' % (PX + 16, PY - 52, RED))

# ============ 二 · 汉广（横流） ============
HX0, HX1 = 268, 486
TOP, BOT = 330, 430
for i in range(5):
    y = TOP + i * 22
    d.append('  <path d="M%d,%d C%d,%d %d,%d %d,%d" fill="none" stroke="%s" stroke-width="%.1f"/>'
             % (HX0, y, HX0 + 52, y - 5, HX1 - 52, y + 5, HX1, y, INK2 if i == 0 else INK3, 1.0 if i == 0 else 0.55))
# 泳者（在水面，朝对岸）
SX, SY = 372, 372
d.append('  <circle cx="%d" cy="%d" r="3.8" fill="none" stroke="%s" stroke-width="0.9"/>' % (SX, SY - 4, INK2))
d.append('  <path d="M%d,%d L%d,%d" stroke="%s" stroke-width="0.9"/>' % (SX, SY, SX, SY + 8, INK2))
d.append('  <path d="M%d,%d q6,-3 12,0" fill="none" stroke="%s" stroke-width="0.8"/>' % (SX - 12, SY + 2, INK2))
# 对岸屏障（红虚线，不可越）
d.append('  <line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="0.8" stroke-dasharray="5 3"/>'
         % (HX0 + 6, TOP - 16, HX1 - 6, TOP - 16, RED))
d.append('  <text x="%d" y="%d" text-anchor="middle" font-size="7.2" fill="%s">不可泳</text>' % ((HX0 + HX1) / 2, TOP - 24, RED))

# ============ 三 · 江永（纵远） ============
RX0, RX1 = 546, 706
FAR = 300
d.append('  <path d="M%d,%d L%d,%d" stroke="%s" stroke-width="1.0"/>' % (RX0, GROUND, RX0 + 26, FAR, INK2))
d.append('  <path d="M%d,%d L%d,%d" stroke="%s" stroke-width="1.0"/>' % (RX1, GROUND, RX1 - 26, FAR, INK2))
for i in range(6):
    t = i / 5
    y = GROUND - (GROUND - FAR) * (0.12 + 0.82 * t)
    x0 = RX0 + 26 * (0.12 + 0.82 * t) + 6
    x1 = RX1 - 26 * (0.12 + 0.82 * t) - 6
    d.append('  <path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="0.5" stroke-dasharray="6 4"/>'
             % (x0, y, x1, y, INK3))
# 筏（近处，未行）
rx, ry = (RX0 + RX1) / 2, GROUND - 16
for k in range(4):
    d.append('  <line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="0.8"/>'
             % (rx - 34, ry + k * 5, rx + 34, ry + k * 5, INK2))
d.append('  <text x="%d" y="%d" text-anchor="middle" font-size="7.2" fill="%s">不可方</text>' % (rx, FAR - 12, RED))

# 编号与说明
d.append('  <text x="120" y="132" font-size="7.6" fill="%s">壹</text>' % RED)
d.append('  <text x="366" y="132" font-size="7.6" fill="%s">贰</text>' % RED)
d.append('  <text x="618" y="132" font-size="7.6" fill="%s">叁</text>' % RED)

d.append('  <text x="44" y="466" font-size="7.8" fill="%s">壹 乔木　上竦无枝，垂荫不生</text>' % INK2)
d.append('  <text x="264" y="466" font-size="7.8" fill="%s">贰 汉广　横不可越</text>' % INK2)
d.append('  <text x="486" y="466" font-size="7.8" fill="%s">叁 江永　长不可筏</text>' % INK2)
d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">汉之广矣，不可泳思</text>' % INK)
d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">三喻一理：够不着</text>' % INK3)
d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj009a</text>' % INK3)
d.append('</svg>')
open(os.path.join(FIG, "sj009a-qiao-mu-han-jiang.svg"), "w", encoding="utf-8").write("\n".join(d))

# ============ 图二 ============
e = []
e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="\'Noto Serif SC\',\'Songti SC\',serif">' % (W, H, W, H))
e.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
e.append('  <rect x="10" y="10" width="740" height="500" fill="none" stroke="%s" stroke-width="1"/>' % INK3)
e.append('  <rect x="16" y="16" width="728" height="488" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
e.append('  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="%s" font-weight="700">立 界 与 即 界</text>' % INK)
e.append('  <text x="380" y="74" text-anchor="middle" font-size="9.6" letter-spacing="2" fill="%s">《诗经》周南 · 第九篇　汉广</text>' % INK2)
e.append('  <defs><marker id="ar9" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % RED)
cells = [(70, "不可休", "乔木高而无荫", "见界", INK2), (290, "不可泳·方", "汉广、江永", "认界", RED), (510, "秣其马", "刈楚、饲驹", "界内尽力", INK2)]
for (x, big, s1, s2, col) in cells:
    e.append('  <rect x="%d" y="150" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (x, col))
    e.append('  <text x="%d" y="206" text-anchor="middle" font-size="19" letter-spacing="0.5" fill="%s" font-weight="700">%s</text>' % (x + 75, col, big))
    e.append('  <text x="%d" y="248" text-anchor="middle" font-size="10" fill="#3B352F">%s</text>' % (x + 75, s1))
    e.append('  <text x="%d" y="276" text-anchor="middle" font-size="8" fill="%s">%s</text>' % (x + 75, INK3, s2))
e.append('  <line x1="220" y1="225" x2="288" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar9)"/>' % RED)
e.append('  <line x1="440" y1="225" x2="508" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar9)"/>' % RED)
e.append('  <text x="380" y="330" text-anchor="middle" font-size="8.4" fill="%s">界不消失，人只换动作：不渡、不追，去割柴、去喂马</text>' % INK2)
e.append('  <line x1="120" y1="360" x2="640" y2="360" stroke="%s" stroke-width="0.8"/>' % INK3)
e.append('  <text x="230" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">思</text>' % RED)
e.append('  <text x="230" y="414" text-anchor="middle" font-size="7.4" fill="%s">语辞，无义　六见</text>' % INK3)
e.append('  <text x="530" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">方</text>' % RED)
e.append('  <text x="530" y="414" text-anchor="middle" font-size="7.4" fill="%s">筏也，非「方正」</text>' % INK3)
e.append('  <text x="380" y="446" text-anchor="middle" font-size="7.4" fill="%s">三章末四句一字不易　·　《诗》中最不肯放手的重复</text>' % INK3)
e.append('  <text x="120" y="512" font-size="5.6" fill="%s">诗经 · 周南</text>' % INK2)
e.append('  <text x="640" y="512" text-anchor="end" font-size="5.6" fill="%s">图二 · 立界与即界 · sj009b</text>' % INK2)
e.append('</svg>')
open(os.path.join(FIG, "sj009b-jian-jie-er-xing.svg"), "w", encoding="utf-8").write("\n".join(e))

import cairosvg
for k in ["sj009a-qiao-mu-han-jiang", "sj009b-jian-jie-er-xing"]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok")
