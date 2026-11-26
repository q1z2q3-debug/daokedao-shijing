# -*- coding: utf-8 -*-
"""SJ014《草虫》两图。图一：草螽·蚱蜢·采蕨手篮。图二：未见·既见·心降。"""
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
d.append('  <text x="380" y="60" text-anchor="middle" font-size="26" letter-spacing="10" fill="%s" font-weight="700">草 虫</text>' % INK)
d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之十四</text>' % INK3)
d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)

# ============ 壹 · 草螽（草虫，侧视朝右，长触角·短翅·胫节刺） ============
FX = 148
# 触角（两条长线，由头向右上分出，抵近图区上段）
d.append('  <path d="M180,204 C200,182 210,166 218,150" fill="none" stroke="%s" stroke-width="0.8"/>' % INK2)
d.append('  <path d="M178,210 C192,194 200,180 204,166" fill="none" stroke="%s" stroke-width="0.7"/>' % INK3)
# 头
d.append('  <path d="M168,204 C178,198 186,204 186,214 C186,224 178,228 168,224 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <circle cx="180" cy="208" r="1.7" fill="%s"/>' % INK)
# 胸背长梭形
d.append('  <path d="M104,224 C122,208 154,206 174,214 L174,236 C154,246 122,244 104,236 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % INK2)
# 覆翅（长过腹端）与翅脉
d.append('  <path d="M108,220 C128,212 152,212 166,218" fill="none" stroke="%s" stroke-width="0.7"/>' % INK3)
for k in range(3):
    x = 118 + k * 12
    d.append('  <line x1="%d" y1="224" x2="%d" y2="218" stroke="%s" stroke-width="0.5"/>' % (x, x + 4, INK3))
# 腹节
for k in range(3):
    x = 116 + k * 10
    d.append('  <path d="M%d,226 l2,6" fill="none" stroke="%s" stroke-width="0.5"/>' % (x, INK3))
# 前足、中足
d.append('  <path d="M164,236 l-4,30" fill="none" stroke="%s" stroke-width="0.8"/>' % INK2)
d.append('  <path d="M144,240 l-2,32" fill="none" stroke="%s" stroke-width="0.8"/>' % INK2)
# 后足：股节上扬，胫节下垂带刺
d.append('  <path d="M122,238 L102,262 L98,292" fill="none" stroke="%s" stroke-width="1.8"/>' % INK2)
for k in range(3):
    yy = 268 + k * 8
    d.append('  <line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="0.5"/>' % (100 - k, yy, 93 - k, yy + 3, INK3))
d.append('  <text x="%d" y="392" text-anchor="middle" font-size="7.0" fill="%s">草螽 · 长触角 · 短翅 · 胫节有刺</text>' % (FX, RED))

# ============ 贰 · 阜螽（蚱蜢，粗短，后足股节膨大） ============
ZX = 378
# 短触角
d.append('  <path d="M404,210 l10,-14" fill="none" stroke="%s" stroke-width="0.7"/>' % INK3)
d.append('  <path d="M402,214 l6,-16" fill="none" stroke="%s" stroke-width="0.7"/>' % INK3)
# 头
d.append('  <path d="M392,212 C402,206 410,212 410,222 C410,232 402,236 392,232 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <circle cx="404" cy="216" r="1.7" fill="%s"/>' % INK)
# 胸腹粗短
d.append('  <path d="M336,232 C352,218 386,216 400,224 L400,246 C384,256 352,254 336,246 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % INK2)
# 翅
d.append('  <path d="M340,228 C358,220 382,220 394,226" fill="none" stroke="%s" stroke-width="0.7"/>' % INK3)
# 膨大后足：股节粗弧，胫节下垂带刺
d.append('  <path d="M352,244 L328,262 L324,288" fill="none" stroke="%s" stroke-width="2.4"/>' % INK2)
d.append('  <path d="M324,288 L320,312" fill="none" stroke="%s" stroke-width="1.1"/>' % INK2)
for k in range(3):
    yy = 292 + k * 7
    d.append('  <line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="0.5"/>' % (321 - k, yy, 314 - k, yy + 3, INK3))
# 前中足
d.append('  <path d="M390,248 l2,26" fill="none" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <path d="M372,250 l-2,28" fill="none" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="%d" y="392" text-anchor="middle" font-size="7.0" fill="%s">蚱蜢 · 后足股节膨大善跳</text>' % (ZX, RED))

# ============ 叁 · 登南山采蕨：手与篮 ============
VX = 622
# 蕨茎（自篮旁上伸，顶端拳卷）
d.append('  <path d="M%d,404 C%d,384 %d,360 %d,330" fill="none" stroke="%s" stroke-width="1.2"/>' % (VX - 18, VX - 18, VX - 16, VX - 14, INK2))
# 拳卷叶头
d.append('  <path d="M%d,330 C%d,320 %d,320 %d,326 C%d,331 %d,329 %d,324" fill="none" stroke="%s" stroke-width="0.8"/>'
         % (VX - 14, VX - 24, VX - 24, VX - 18, VX - 14, VX - 16, VX - 18, INK2))
# 蕨裂片
for k in range(3):
    y = 388 - k * 13
    d.append('  <path d="M%d,%d l-11,-5" fill="none" stroke="%s" stroke-width="0.55"/>' % (VX - 18, y, INK3))
# 手：腕自右伸入，掌轮廓抱蕨茎，四指勾回可辨
d.append('  <path d="M656,302 C646,308 636,314 626,318" fill="none" stroke="%s" stroke-width="1.5"/>' % INK2)
d.append('  <path d="M656,312 C646,316 638,320 630,324" fill="none" stroke="%s" stroke-width="1.2"/>' % INK2)
d.append('  <path d="M626,318 C618,312 610,312 606,320 C602,328 608,336 616,334 L632,328" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <path d="M616,322 c-6,2 -8,6 -6,10" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
d.append('  <path d="M622,320 c-6,2 -8,7 -5,11" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
d.append('  <path d="M628,320 c-5,2 -6,6 -3,10" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
# 竹篮：斜口沿、提梁拱线、篾纹
d.append('  <path d="M%d,360 L%d,352 L%d,404 L%d,410 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (VX - 36, VX + 8, VX + 14, VX - 30, INK2))
d.append('  <path d="M%d,360 Q%d,338 %d,352" fill="none" stroke="%s" stroke-width="1.0"/>' % (VX - 36, VX - 14, VX + 8, INK2))
for k in range(3):
    yy = 372 + k * 10
    d.append('  <line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="0.45"/>' % (VX - 33, yy, VX + 11, yy - 2, INK3))
# 篮中蕨苗两点
d.append('  <circle cx="%d" cy="382" r="2.2" fill="#EFEAD6" stroke="%s" stroke-width="0.6"/>' % (VX - 14, INK3))
d.append('  <circle cx="%d" cy="388" r="2.2" fill="#EFEAD6" stroke="%s" stroke-width="0.6"/>' % (VX + 2, INK3))
d.append('  <text x="%d" y="392" text-anchor="middle" font-size="7.0" fill="%s">采蕨之手 · 与竹篮</text>' % (VX, RED))

for (x, t) in [(120, "壹"), (350, "贰"), (600, "叁")]:
    d.append('  <text x="%d" y="132" font-size="7.6" fill="%s">%s</text>' % (x, RED, t))
d.append('  <text x="44" y="466" font-size="7.8" fill="%s">壹 草蟲　草螽，鳴于草間</text>' % INK2)
d.append('  <text x="264" y="466" font-size="7.8" fill="%s">贰 阜螽　蚱蜢，善跳</text>' % INK2)
d.append('  <text x="486" y="466" font-size="7.8" fill="%s">叁 采蕨　登高所采，手籃並見</text>' % INK2)
d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">喓喓草蟲，趯趯阜螽</text>' % INK)
d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">未见则忧，既见则安</text>' % INK3)
d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj014a</text>' % INK3)
d.append('</svg>')
open(os.path.join(FIG, "sj014a-cao-chong-fu-zhong.svg"), "w", encoding="utf-8").write("\n".join(d))

# ============ 图二 ============
e = []
e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="\'Noto Serif SC\',\'Songti SC\',serif">' % (W, H, W, H))
e.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
e.append('  <rect x="10" y="10" width="740" height="500" fill="none" stroke="%s" stroke-width="1"/>' % INK3)
e.append('  <rect x="16" y="16" width="728" height="488" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
e.append('  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="%s" font-weight="700">未见 · 既见 · 心降</text>' % INK)
e.append('  <text x="380" y="74" text-anchor="middle" font-size="9.6" letter-spacing="2" fill="%s">《诗经》召南 · 第三篇　草虫</text>' % INK2)
e.append('  <defs><marker id="ar14" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % RED)
cells = [(70, "未见", "忡忡 · 惙惙 · 伤悲", "登高望远，忧在心上", INK2),
         (290, "既见", "亦既见止，亦既觏止", "遇上了，心一动", RED),
         (510, "心降", "降 · 说 · 夷", "忧落下来，心放平", INK2)]
for (x, big, s1, s2, col) in cells:
    e.append('  <rect x="%d" y="150" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (x, col))
    e.append('  <text x="%d" y="214" text-anchor="middle" font-size="28" letter-spacing="2" fill="%s" font-weight="700">%s</text>' % (x + 75, col, big))
    e.append('  <text x="%d" y="252" text-anchor="middle" font-size="10" fill="#3B352F">%s</text>' % (x + 75, s1))
    e.append('  <text x="%d" y="278" text-anchor="middle" font-size="8" fill="%s">%s</text>' % (x + 75, INK3, s2))
e.append('  <line x1="220" y1="225" x2="288" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar14)"/>' % RED)
e.append('  <line x1="440" y1="225" x2="508" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar14)"/>' % RED)
e.append('  <text x="380" y="330" text-anchor="middle" font-size="8.4" fill="%s">未见之忧一章重过一章，既见之安一章稳过一章</text>' % INK2)
e.append('  <line x1="120" y1="360" x2="640" y2="360" stroke="%s" stroke-width="0.8"/>' % INK3)
e.append('  <text x="230" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">觏</text>' % RED)
e.append('  <text x="230" y="414" text-anchor="middle" font-size="7.4" fill="%s">遇也，与媾同源，非媾合</text>' % INK3)
e.append('  <text x="530" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">降</text>' % RED)
e.append('  <text x="530" y="414" text-anchor="middle" font-size="7.4" fill="%s">下心也，非「投降」</text>' % INK3)
e.append('  <text x="380" y="446" text-anchor="middle" font-size="7.4" fill="%s">全篇不写相会场面，只写心从高处落下来的那一瞬</text>' % INK3)
e.append('  <text x="120" y="512" font-size="5.6" fill="%s">诗经 · 召南</text>' % INK2)
e.append('  <text x="640" y="512" text-anchor="end" font-size="5.6" fill="%s">图二 · 未见既见 · sj014b</text>' % INK2)
e.append('</svg>')
open(os.path.join(FIG, "sj014b-wei-jian-ji-jian.svg"), "w", encoding="utf-8").write("\n".join(e))

import cairosvg
for k in ["sj014a-cao-chong-fu-zhong", "sj014b-wei-jian-ji-jian"]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok")
