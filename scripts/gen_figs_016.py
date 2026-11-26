# -*- coding: utf-8 -*-
"""SJ016《甘棠》两图。图一：甘棠树·茇舍·憩坐。图二：茇·憩·说。"""
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

# ============ 壹 · 甘棠树（线画：主干·三枝·叶簇·结疤，无圆冠） ============
FX = 148
# 地面
d.append('  <line x1="%d" y1="390" x2="%d" y2="390" stroke="%s" stroke-width="0.8"/>' % (FX - 40, FX + 40, INK3))
# 主干（微曲）
d.append('  <path d="M%d,390 C%d,346 %d,300 %d,242" fill="none" stroke="%s" stroke-width="2.6"/>' % (FX, FX, FX + 2, FX + 1, INK))
# 树皮竖纹
d.append('  <path d="M%d,372 l2,-22" fill="none" stroke="%s" stroke-width="0.5"/>' % (FX - 4, INK3))
d.append('  <path d="M%d,360 l-1,-18" fill="none" stroke="%s" stroke-width="0.5"/>' % (FX + 5, INK3))
# 三枝：左上、右上、中上
d.append('  <path d="M%d,280 L%d,258 L%d,240" fill="none" stroke="%s" stroke-width="1.5"/>' % (FX, FX - 18, FX - 30, INK2))
d.append('  <path d="M%d,274 L%d,254 L%d,236" fill="none" stroke="%s" stroke-width="1.5"/>' % (FX + 1, FX + 20, FX + 32, INK2))
d.append('  <path d="M%d,260 L%d,232" fill="none" stroke="%s" stroke-width="1.3"/>' % (FX + 1, FX + 2, INK2))
# 叶簇（枝端成组短线小叶，不开闭合圈）
for (lx, ly) in [(FX - 30, 240), (FX - 20, 232), (FX + 32, 236), (FX + 22, 228), (FX + 2, 224)]:
    for k in range(3):
        a = k * 22 - 20
        d.append('  <path d="M%d,%d q%d,-3 %d,0" fill="none" stroke="%s" stroke-width="0.5"/>'
                 % (lx - 6 + k * 5, ly + (k % 2) * 4, a, 8, INK3))
# 结疤
d.append('  <ellipse cx="%d" cy="338" rx="3" ry="4.5" fill="none" stroke="%s" stroke-width="0.7"/>' % (FX + 4, INK3))
d.append('  <ellipse cx="%d" cy="362" rx="2.6" ry="3.8" fill="none" stroke="%s" stroke-width="0.7"/>' % (FX - 4, INK3))
d.append('  <text x="%d" y="392" text-anchor="middle" font-size="7.0" fill="%s">甘棠 · 主干三枝叶簇结疤</text>' % (FX, RED))

# ============ 贰 · 茇：草舍（茅顶·立柱·檐口） ============
ZX = 378
# 茅顶坡脊与檐口
d.append('  <path d="M%d,292 L%d,254 L%d,292" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (ZX - 36, ZX, ZX + 36, INK2))
# 檐口出梢
d.append('  <path d="M%d,292 L%d,298 M%d,292 L%d,298" fill="none" stroke="%s" stroke-width="0.9"/>' % (ZX - 36, ZX - 42, ZX + 36, ZX + 42, INK2))
# 茅草秆排线（自脊向檐）
for k in range(5):
    x = ZX - 26 + k * 13
    d.append('  <line x1="%d" y1="262" x2="%d" y2="292" stroke="%s" stroke-width="0.5"/>' % (x, x + 3, INK3))
# 横梁
d.append('  <line x1="%d" y1="298" x2="%d" y2="298" stroke="%s" stroke-width="1.0"/>' % (ZX - 30, ZX + 30, INK2))
# 两立柱
d.append('  <line x1="%d" y1="298" x2="%d" y2="386" stroke="%s" stroke-width="1.1"/>' % (ZX - 22, ZX - 22, INK2))
d.append('  <line x1="%d" y1="298" x2="%d" y2="386" stroke="%s" stroke-width="1.1"/>' % (ZX + 22, ZX + 22, INK2))
# 地基
d.append('  <line x1="%d" y1="386" x2="%d" y2="386" stroke="%s" stroke-width="0.8"/>' % (ZX - 30, ZX + 30, INK3))
d.append('  <text x="%d" y="392" text-anchor="middle" font-size="7.0" fill="%s">茇 · 茅顶立柱檐口之草舍</text>' % (ZX, RED))

# ============ 叁 · 憩说：人倚树而坐侧影 ============
VX = 622
# 树一小段干
d.append('  <line x1="%d" y1="256" x2="%d" y2="390" stroke="%s" stroke-width="2.2"/>' % (VX - 16, VX - 16, INK2))
d.append('  <line x1="%d" y1="390" x2="%d" y2="390" stroke="%s" stroke-width="0.8"/>' % (VX - 34, VX + 24, INK3))
# 头（侧倚树干，有发髻）
d.append('  <path d="M%d,232 C%d,224 %d,224 %d,232 L%d,242 C%d,248 %d,248 %d,242 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>'
         % (VX - 8, VX - 2, VX - 2, VX + 4, VX + 4, VX - 2, VX - 2, VX - 8, INK2))
d.append('  <circle cx="%d" cy="228" r="3" fill="#FCFAF6" stroke="%s" stroke-width="0.7"/>' % (VX - 2, INK3))
# 背线（贴树干下延）
d.append('  <path d="M%d,242 C%d,262 %d,300 %d,336" fill="none" stroke="%s" stroke-width="1.0"/>' % (VX - 8, VX - 10, VX - 10, VX - 6, INK2))
# 胸腹前轮廓
d.append('  <path d="M%d,246 C%d,266 %d,300 %d,336" fill="none" stroke="%s" stroke-width="1.0"/>' % (VX + 2, VX + 12, VX + 12, VX + 8, INK2))
# 屈膝前伸
d.append('  <path d="M%d,336 C%d,340 %d,342 %d,340" fill="none" stroke="%s" stroke-width="1.0"/>' % (VX - 6, VX + 10, VX + 24, VX + 30, INK2))
d.append('  <path d="M%d,340 L%d,352 L%d,352" fill="none" stroke="%s" stroke-width="0.9"/>' % (VX + 30, VX + 24, VX + 14, INK2))
# 宽袖搭于膝
d.append('  <path d="M%d,258 C%d,274 %d,316 %d,336" fill="none" stroke="%s" stroke-width="0.9"/>' % (VX + 2, VX + 10, VX + 16, VX + 18, INK2))
# 衣裾铺地
d.append('  <path d="M%d,336 L%d,352" fill="none" stroke="%s" stroke-width="0.8"/>' % (VX - 6, VX - 2, INK3))
d.append('  <text x="%d" y="392" text-anchor="middle" font-size="7.0" fill="%s">憩说 · 倚树而坐之侧影</text>' % (VX, RED))

for (x, t) in [(120, "壹"), (350, "贰"), (600, "叁")]:
    d.append('  <text x="%d" y="132" font-size="7.6" fill="%s">%s</text>' % (x, RED, t))
d.append('  <text x="44" y="466" font-size="7.8" fill="%s">壹 甘棠　杜梨，线画枝干叶疤</text>' % INK2)
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
