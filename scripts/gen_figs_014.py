# -*- coding: utf-8 -*-
"""SJ014《草虫》两图。图一：草虫·阜螽·蕨薇。图二：未见·既见·心降。"""
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

GROUND = 420

# 壹 · 草螽（草虫，长身、长须）
FX = 148
# 身
d.append('  <ellipse cx="%d" cy="348" rx="28" ry="10" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (FX, INK2))
# 头
d.append('  <circle cx="%d" cy="344" r="8" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % (FX + 28, INK2))
# 触角（两条长线，向右上）
d.append('  <path d="M%d,338 C%d,316 %d,302 %d,286" fill="none" stroke="%s" stroke-width="0.7"/>' % (FX + 32, FX + 46, FX + 58, FX + 72, INK2))
d.append('  <path d="M%d,342 C%d,326 %d,314 %d,302" fill="none" stroke="%s" stroke-width="0.7"/>' % (FX + 32, FX + 44, FX + 54, FX + 62, INK3))
# 翅脉
d.append('  <path d="M%d,344 C%d,340 %d,340 %d,344" fill="none" stroke="%s" stroke-width="0.6"/>' % (FX - 22, FX - 6, FX + 12, FX + 22, INK3))
for k in range(3):
    x = FX - 16 + k * 10
    d.append('  <line x1="%d" y1="346" x2="%d" y2="341" stroke="%s" stroke-width="0.5"/>' % (x, x + 3, INK3))
# 步足（至地面）
for k in range(3):
    x = FX - 14 + k * 11
    d.append('  <path d="M%d,356 l-4,28" fill="none" stroke="%s" stroke-width="0.7"/>' % (x, INK2))
d.append('  <text x="%d" y="392" text-anchor="middle" font-size="7.0" fill="%s">草螽 · 长身长须</text>' % (FX, RED))

# 贰 · 阜螽（蚱蜢，粗短、后腿善跳）
ZX = 378
d.append('  <ellipse cx="%d" cy="350" rx="24" ry="11" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (ZX, INK2))
d.append('  <circle cx="%d" cy="346" r="8.5" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % (ZX + 23, INK2))
# 后腿（粗大：腿节上扬，胫节下垂）
d.append('  <path d="M%d,356 L%d,374 L%d,390" fill="none" stroke="%s" stroke-width="2.0"/>' % (ZX - 4, ZX - 22, ZX - 28, INK2))
for k in range(3):
    yy = 378 + k * 6
    d.append('  <line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="0.5"/>' % (ZX - 24 - k * 2, yy, ZX - 32 - k * 2, yy + 3, INK3))
# 前足
for k in range(2):
    x = ZX + 6 + k * 9
    d.append('  <path d="M%d,358 l2,22" fill="none" stroke="%s" stroke-width="0.7"/>' % (x, INK3))
d.append('  <text x="%d" y="392" text-anchor="middle" font-size="7.0" fill="%s">蚱蜢 · 后腿善跳</text>' % (ZX, RED))

# 叁 · 蕨与薇
VX = 622
# 蕨：拳卷初生叶
d.append('  <path d="M%d,420 C%d,400 %d,384 %d,362" fill="none" stroke="%s" stroke-width="1.2"/>' % (VX - 24, VX - 24, VX - 24, VX - 22, INK2))
d.append('  <path d="M%d,362 C%d,352 %d,352 %d,358 C%d,363 %d,361 %d,356" fill="none" stroke="%s" stroke-width="0.8"/>'
         % (VX - 22, VX - 32, VX - 32, VX - 26, VX - 22, VX - 24, VX - 26, INK2))
# 蕨叶裂片
for k in range(3):
    y = 396 - k * 11
    d.append('  <path d="M%d,%d l-10,-5" fill="none" stroke="%s" stroke-width="0.55"/>' % (VX - 24, y, INK3))
# 薇：蔓生豆苗，对生小叶
d.append('  <path d="M%d,420 C%d,400 %d,384 %d,368" fill="none" stroke="%s" stroke-width="1.1"/>' % (VX + 20, VX + 20, VX + 20, VX + 22, INK2))
for k in range(3):
    y = 400 - k * 12
    d.append('  <ellipse cx="%d" cy="%d" rx="5" ry="2.6" fill="#FCFAF6" stroke="%s" stroke-width="0.55"/>' % (VX + 14, y, INK3))
    d.append('  <ellipse cx="%d" cy="%d" rx="5" ry="2.6" fill="#FCFAF6" stroke="%s" stroke-width="0.55"/>' % (VX + 28, y - 2, INK3))
d.append('  <text x="%d" y="344" text-anchor="middle" font-size="7.0" fill="%s">蕨（春）· 薇（秋）</text>' % (VX, RED))

for (x, t) in [(120, "壹"), (350, "贰"), (600, "叁")]:
    d.append('  <text x="%d" y="132" font-size="7.6" fill="%s">%s</text>' % (x, RED, t))
d.append('  <text x="44" y="466" font-size="7.8" fill="%s">壹 草蟲　草螽，鳴于草間</text>' % INK2)
d.append('  <text x="264" y="466" font-size="7.8" fill="%s">贰 阜螽　蚱蜢，善跳</text>' % INK2)
d.append('  <text x="486" y="466" font-size="7.8" fill="%s">叁 蕨薇　登高所采，春秋異時</text>' % INK2)
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
