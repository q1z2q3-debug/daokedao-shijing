# -*- coding: utf-8 -*-
"""SJ017《行露》两图。图一：行露·雀穿屋·鼠穿墉。图二：礼不足·不惧讼·不女从。"""
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
d.append('  <text x="380" y="60" text-anchor="middle" font-size="26" letter-spacing="10" fill="%s" font-weight="700">行 露</text>' % INK)
d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之十七</text>' % INK3)
d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)

GROUND = 420

# 壹 · 行露：一条路 + 露滴
FX = 148
d.append('  <path d="M%d,420 L%d,340" fill="none" stroke="%s" stroke-width="1.0"/>' % (FX - 40, FX - 20, INK2))
d.append('  <path d="M%d,420 L%d,340" fill="none" stroke="%s" stroke-width="1.0"/>' % (FX + 40, FX + 20, INK2))
for k in range(6):
    x = FX - 26 + k * 10
    y = 388 - k * 6
    d.append('  <circle cx="%d" cy="%d" r="1.8" fill="none" stroke="%s" stroke-width="0.6"/>' % (x, y, INK3))
d.append('  <text x="%d" y="326" text-anchor="middle" font-size="7.0" fill="%s">行（háng）· 道上之露</text>' % (FX, RED))

# 贰 · 雀穿屋
ZX = 378
# 屋
d.append('  <path d="M%d,356 L%d,326 L%d,356" fill="none" stroke="%s" stroke-width="1.1"/>' % (ZX - 30, ZX, ZX + 30, INK2))
d.append('  <rect x="%d" y="356" width="48" height="30" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % (ZX - 24, INK2))
# 破口
d.append('  <path d="M%d,360 l6,4 l-6,4 l-6,-4 Z" fill="%s"/>' % (ZX + 18, RED))
# 雀（小头在屋边）
d.append('  <circle cx="%d" cy="330" r="5" fill="#FCFAF6" stroke="%s" stroke-width="0.8"/>' % (ZX + 26, INK2))
d.append('  <path d="M%d,330 l8,2 l-8,3 Z" fill="#EFEAD6" stroke="%s" stroke-width="0.6"/>' % (ZX + 30, INK3))
d.append('  <text x="%d" y="392" text-anchor="middle" font-size="7.0" fill="%s">雀无角而穿屋</text>' % (ZX, RED))

# 叁 · 鼠穿墉
VX = 622
d.append('  <rect x="%d" y="340" width="56" height="46" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % (VX - 28, INK2))
# 墙缝啮口
d.append('  <path d="M%d,358 l8,5 l-8,5 l-8,-5 Z" fill="%s"/>' % (VX, RED))
# 鼠（简笔）
d.append('  <ellipse cx="%d" cy="352" rx="10" ry="6" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % (VX - 34, INK2))
d.append('  <circle cx="%d" cy="348" r="3" fill="#FCFAF6" stroke="%s" stroke-width="0.7"/>' % (VX - 42, INK2))
d.append('  <path d="M%d,356 q10,6 20,2" fill="none" stroke="%s" stroke-width="0.6"/>' % (VX - 34, INK3))
d.append('  <text x="%d" y="392" text-anchor="middle" font-size="7.0" fill="%s">鼠无牙而穿墉</text>' % (VX, RED))

for (x, t) in [(120, "壹"), (350, "贰"), (600, "叁")]:
    d.append('  <text x="%d" y="132" font-size="7.6" fill="%s">%s</text>' % (x, RED, t))
d.append('  <text x="44" y="466" font-size="7.8" fill="%s">壹 行露　道上沾濡之露</text>' % INK2)
d.append('  <text x="264" y="466" font-size="7.8" fill="%s">贰 雀穿屋　无角而能穿，喻强</text>' % INK2)
d.append('  <text x="486" y="466" font-size="7.8" fill="%s">叁 鼠穿墉　无牙而能啮，喻逼</text>' % INK2)
d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">誰謂雀無角？何以穿我屋</text>' % INK)
d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">礼与讼之间，守礼不退</text>' % INK3)
d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj017a</text>' % INK3)
d.append('</svg>')
open(os.path.join(FIG, "sj017a-xing-lu-que-shu.svg"), "w", encoding="utf-8").write("\n".join(d))

# ============ 图二 ============
e = []
e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="\'Noto Serif SC\',\'Songti SC\',serif">' % (W, H, W, H))
e.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
e.append('  <rect x="10" y="10" width="740" height="500" fill="none" stroke="%s" stroke-width="1"/>' % INK3)
e.append('  <rect x="16" y="16" width="728" height="488" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
e.append('  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="%s" font-weight="700">礼不足 · 不惧讼 · 不女从</text>' % INK)
e.append('  <text x="380" y="74" text-anchor="middle" font-size="9.6" letter-spacing="2" fill="%s">《诗经》召南 · 第六篇　行露</text>' % INK2)
e.append('  <defs><marker id="ar17" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % RED)
cells = [(70, "礼不足", "无媒聘之礼", "室家不足", INK2),
         (290, "不惧讼", "虽速我狱 · 虽速我讼", "逼以公堂，志不可夺", RED),
         (510, "不女从", "亦不女从", "守礼而拒，斩截收住", INK2)]
for (x, big, s1, s2, col) in cells:
    e.append('  <rect x="%d" y="150" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (x, col))
    e.append('  <text x="%d" y="214" text-anchor="middle" font-size="28" letter-spacing="2" fill="%s" font-weight="700">%s</text>' % (x + 75, col, big))
    e.append('  <text x="%d" y="252" text-anchor="middle" font-size="10" fill="#3B352F">%s</text>' % (x + 75, s1))
    e.append('  <text x="%d" y="278" text-anchor="middle" font-size="8" fill="%s">%s</text>' % (x + 75, INK3, s2))
e.append('  <line x1="220" y1="225" x2="288" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar17)"/>' % RED)
e.append('  <line x1="440" y1="225" x2="508" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar17)"/>' % RED)
e.append('  <text x="380" y="330" text-anchor="middle" font-size="8.4" fill="%s">二章说「礼不足」是理，三章说「不女从」是志；由辩理到立志</text>' % INK2)
e.append('  <line x1="120" y1="360" x2="640" y2="360" stroke="%s" stroke-width="0.8"/>' % INK3)
e.append('  <text x="230" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">女</text>' % RED)
e.append('  <text x="230" y="414" text-anchor="middle" font-size="7.4" fill="%s">通「汝」，你也，非男女之女</text>' % INK3)
e.append('  <text x="530" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">速</text>' % RED)
e.append('  <text x="530" y="414" text-anchor="middle" font-size="7.4" fill="%s">招致也，非「迅速」</text>' % INK3)
e.append('  <text x="380" y="446" text-anchor="middle" font-size="7.4" fill="%s">守礼不是温顺，是在狱讼相逼之下，仍不退让半步</text>' % INK3)
e.append('  <text x="120" y="512" font-size="5.6" fill="%s">诗经 · 召南</text>' % INK2)
e.append('  <text x="640" y="512" text-anchor="end" font-size="5.6" fill="%s">图二 · 守礼不从 · sj017b</text>' % INK2)
e.append('</svg>')
open(os.path.join(FIG, "sj017b-shou-li-bu-cong.svg"), "w", encoding="utf-8").write("\n".join(e))

import cairosvg
for k in ["sj017a-xing-lu-que-shu", "sj017b-shou-li-bu-cong"]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok")
