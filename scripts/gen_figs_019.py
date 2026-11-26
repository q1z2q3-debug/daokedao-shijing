# -*- coding: utf-8 -*-
"""SJ019《殷其雷》两图。图一：雷山·行者·望归。图二：违斯·无遑·归哉。"""
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
d.append('  <text x="380" y="60" text-anchor="middle" font-size="26" letter-spacing="10" fill="%s" font-weight="700">殷其雷</text>' % INK)
d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之十九</text>' % INK3)
d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)

# ============ 壹 · 殷其雷：折线皴笔山 + 回旋雷纹 ============
FX = 148
# 山脊折线（两峰错落，非正三角）
d.append('  <path d="M%d,360 L%d,302 L%d,322 L%d,288 L%d,322 L%d,360 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>'
         % (FX - 44, FX - 20, FX - 8, FX + 8, FX + 22, FX + 44, INK2))
# 皴笔短线
for k in range(5):
    x = FX - 30 + k * 14
    d.append('  <path d="M%d,344 l2,-14" fill="none" stroke="%s" stroke-width="0.5"/>' % (x, INK3))
# 回旋雷纹（闪电折线）
d.append('  <path d="M%d,230 l10,16 l-10,2 l12,18" fill="none" stroke="%s" stroke-width="1.2"/>' % (FX - 8, RED))
d.append('  <path d="M%d,238 l8,13 l-8,2 l10,15" fill="none" stroke="%s" stroke-width="0.8"/>' % (FX + 20, INK3))
# 卷云气
d.append('  <path d="M%d,214 q14,-6 28,0 q14,6 28,0" fill="none" stroke="%s" stroke-width="0.5"/>' % (FX - 30, INK3))
d.append('  <text x="%d" y="392" text-anchor="middle" font-size="7.0" fill="%s">殷其雷 · 皴笔山巅回旋雷纹</text>' % (FX, RED))

# ============ 贰 · 何斯违斯：行者背影，负薪 ============
ZX = 378
# 发髻
d.append('  <circle cx="%d" cy="206" r="3.6" fill="#FCFAF6" stroke="%s" stroke-width="0.8"/>' % (ZX, INK2))
# 头轮廓
d.append('  <path d="M%d,210 C%d,202 %d,202 %d,210 L%d,220 C%d,226 %d,226 %d,220 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>'
         % (ZX - 7, ZX, ZX, ZX + 7, ZX + 7, ZX, ZX, ZX - 7, INK2))
# 颈肩
d.append('  <line x1="%d" y1="222" x2="%d" y2="228" stroke="%s" stroke-width="0.9"/>' % (ZX, ZX, INK2))
d.append('  <path d="M%d,232 C%d,226 %d,226 %d,232" fill="none" stroke="%s" stroke-width="1.0"/>' % (ZX - 18, ZX - 8, ZX + 8, ZX + 18, INK2))
# 袍身背影
d.append('  <path d="M%d,232 C%d,270 %d,316 %d,372 L%d,372 C%d,316 %d,270 %d,232" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>'
         % (ZX - 18, ZX - 24, ZX - 22, ZX - 12, ZX + 12, ZX + 22, ZX + 24, ZX + 18, INK2))
# 负薪：背右柴束（数枝+捆绳）
d.append('  <path d="M%d,240 L%d,226 M%d,246 L%d,232 M%d,252 L%d,238" fill="none" stroke="%s" stroke-width="0.8"/>'
         % (ZX + 16, ZX + 30, ZX + 18, ZX + 32, ZX + 18, ZX + 30, INK2))
d.append('  <path d="M%d,236 L%d,256" fill="none" stroke="%s" stroke-width="0.7"/>' % (ZX + 24, ZX + 24, INK3))
# 袖摆
d.append('  <path d="M%d,240 C%d,254 %d,280 %d,296" fill="none" stroke="%s" stroke-width="0.9"/>' % (ZX - 18, ZX - 28, ZX - 28, ZX - 22, INK2))
# 步姿两脚
d.append('  <path d="M%d,372 L%d,384 M%d,372 L%d,384" fill="none" stroke="%s" stroke-width="0.9"/>' % (ZX - 6, ZX - 12, ZX + 6, ZX + 10, INK2))
d.append('  <text x="%d" y="392" text-anchor="middle" font-size="7.0" fill="%s">何斯违斯 · 行者负薪而违</text>' % (ZX, RED))

# ============ 叁 · 归哉归哉：门扉半开，内有望者 ============
VX = 622
# 门框立柱与横梁
d.append('  <line x1="%d" y1="296" x2="%d" y2="386" stroke="%s" stroke-width="1.1"/>' % (VX - 34, VX - 34, INK2))
d.append('  <line x1="%d" y1="296" x2="%d" y2="386" stroke="%s" stroke-width="1.1"/>' % (VX + 34, VX + 34, INK2))
d.append('  <line x1="%d" y1="296" x2="%d" y2="296" stroke="%s" stroke-width="1.1"/>' % (VX - 34, VX + 34, INK2))
# 右扉（合）
d.append('  <path d="M%d,300 L%d,300 L%d,382 L%d,382 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % (VX + 6, VX + 30, VX + 30, VX + 6, INK2))
# 左扉（半开，斜出）
d.append('  <path d="M%d,300 L%d,312 L%d,380 L%d,382 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % (VX - 30, VX - 12, VX - 6, VX - 24, INK2))
# 门内望者（小背影）
d.append('  <circle cx="%d" cy="330" r="4" fill="#FCFAF6" stroke="%s" stroke-width="0.8"/>' % (VX, INK2))
d.append('  <path d="M%d,336 C%d,348 %d,360 %d,372" fill="none" stroke="%s" stroke-width="0.9"/>' % (VX - 5, VX - 6, VX - 5, VX - 3, INK2))
d.append('  <path d="M%d,336 C%d,348 %d,360 %d,372" fill="none" stroke="%s" stroke-width="0.9"/>' % (VX + 5, VX + 6, VX + 5, VX + 3, INK2))
# 门槛
d.append('  <line x1="%d" y1="386" x2="%d" y2="386" stroke="%s" stroke-width="0.9"/>' % (VX - 34, VX + 34, INK3))
d.append('  <text x="%d" y="392" text-anchor="middle" font-size="7.0" fill="%s">归哉归哉 · 门扉半开，内有望者</text>' % (VX, RED))

for (x, t) in [(120, "壹"), (350, "贰"), (600, "叁")]:
    d.append('  <text x="%d" y="132" font-size="7.6" fill="%s">%s</text>' % (x, RED, t))
d.append('  <text x="44" y="466" font-size="7.8" fill="%s">壹 雷声 · 殷其雷，起于南山</text>' % INK2)
d.append('  <text x="264" y="466" font-size="7.8" fill="%s">贰 违斯 · 行者负薪，离此从公</text>' % INK2)
d.append('  <text x="486" y="466" font-size="7.8" fill="%s">叁 归哉 · 门扉半开，室家望归</text>' % INK2)
d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">振振君子，歸哉歸哉</text>' % INK)
d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">怨而不怒，望其归尔</text>' % INK3)
d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj019a</text>' % INK3)
d.append('</svg>')
open(os.path.join(FIG, "sj019a-yin-qi-lei-nan-shan.svg"), "w", encoding="utf-8").write("\n".join(d))

# ============ 图二 ============
e = []
e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="\'Noto Serif SC\',\'Songti SC\',serif">' % (W, H, W, H))
e.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
e.append('  <rect x="10" y="10" width="740" height="500" fill="none" stroke="%s" stroke-width="1"/>' % INK3)
e.append('  <rect x="16" y="16" width="728" height="488" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
e.append('  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="%s" font-weight="700">违斯 · 无遑 · 归哉</text>' % INK)
e.append('  <text x="380" y="74" text-anchor="middle" font-size="9.6" letter-spacing="2" fill="%s">《诗经》召南 · 第八篇　殷其雷</text>' % INK2)
e.append('  <defs><marker id="ar19" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % RED)
cells = [(70, "违斯", "何斯违斯", "离此从公", INK2),
         (290, "无遑", "莫敢遑息 · 莫或遑处", "不敢暇逸安居", RED),
         (510, "归哉", "归哉归哉", "呼唤盼归，非已归", INK2)]
for (x, big, s1, s2, col) in cells:
    e.append('  <rect x="%d" y="150" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (x, col))
    e.append('  <text x="%d" y="214" text-anchor="middle" font-size="28" letter-spacing="2" fill="%s" font-weight="700">%s</text>' % (x + 75, col, big))
    e.append('  <text x="%d" y="252" text-anchor="middle" font-size="10" fill="#3B352F">%s</text>' % (x + 75, s1))
    e.append('  <text x="%d" y="278" text-anchor="middle" font-size="8" fill="%s">%s</text>' % (x + 75, INK3, s2))
e.append('  <line x1="220" y1="225" x2="288" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar19)"/>' % RED)
e.append('  <line x1="440" y1="225" x2="508" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar19)"/>' % RED)
e.append('  <text x="380" y="330" text-anchor="middle" font-size="8.4" fill="%s">山位三阶：阳 → 侧 → 下；人劳三阶：遑 → 息 → 处</text>' % INK2)
e.append('  <line x1="120" y1="360" x2="640" y2="360" stroke="%s" stroke-width="0.8"/>' % INK3)
e.append('  <text x="230" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">殷</text>' % RED)
e.append('  <text x="230" y="414" text-anchor="middle" font-size="7.4" fill="%s">读 yǐn，雷声殷殷，非殷勤</text>' % INK3)
e.append('  <text x="530" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">归哉</text>' % RED)
e.append('  <text x="530" y="414" text-anchor="middle" font-size="7.4" fill="%s">呼唤盼归，君子尚未归</text>' % INK3)
e.append('  <text x="380" y="446" text-anchor="middle" font-size="7.4" fill="%s">有思之切，无责之辞；闵其勤劳，而不替他分责</text>' % INK3)
e.append('  <text x="120" y="512" font-size="5.6" fill="%s">诗经 · 召南</text>' % INK2)
e.append('  <text x="640" y="512" text-anchor="end" font-size="5.6" fill="%s">图二 · 违斯归哉 · sj019b</text>' % INK2)
e.append('</svg>')
open(os.path.join(FIG, "sj019b-wei-si-gui-zai.svg"), "w", encoding="utf-8").write("\n".join(e))

import cairosvg
for k in ["sj019a-yin-qi-lei-nan-shan", "sj019b-wei-si-gui-zai"]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok")
