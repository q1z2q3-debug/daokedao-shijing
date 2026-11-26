# -*- coding: utf-8 -*-
"""SJ019《殷其雷》两图。图一：雷声·南山·望归。图二：违斯·无遑·归哉。"""
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

GROUND = 420

# 壹 · 雷声与山脊
FX = 148
d.append('  <path d="M%d,380 L%d,316 L%d,380 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % (FX - 44, FX, FX + 44, INK2))
# 雷折线
d.append('  <path d="M%d,272 l8,14 l-8,2 l10,16" fill="none" stroke="%s" stroke-width="1.1"/>' % (FX - 6, RED))
d.append('  <path d="M%d,278 l7,12 l-7,2 l9,14" fill="none" stroke="%s" stroke-width="0.8"/>' % (FX + 18, INK3))
d.append('  <text x="%d" y="400" text-anchor="middle" font-size="7.0" fill="%s">殷其雷 · 声盛而震</text>' % (FX, RED))

# 贰 · 南山三位：阳、侧、下
ZX = 378
d.append('  <path d="M%d,380 L%d,310 L%d,380 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % (ZX - 48, ZX, ZX + 48, INK2))
d.append('  <text x="%d" y="332" text-anchor="middle" font-size="7.0" fill="%s">阳</text>' % (ZX - 20, RED))
d.append('  <text x="%d" y="356" text-anchor="middle" font-size="7.0" fill="%s">侧</text>' % (ZX + 22, RED))
d.append('  <text x="%d" y="374" text-anchor="middle" font-size="7.0" fill="%s">下</text>' % (ZX, RED))
d.append('  <text x="%d" y="400" text-anchor="middle" font-size="7.0" fill="%s">南山 · 阳侧下</text>' % (ZX, RED))

# 叁 · 望归之人（面山而立）
VX = 622
d.append('  <circle cx="%d" cy="326" r="7" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % (VX, INK2))
d.append('  <path d="M%d,336 L%d,366" fill="none" stroke="%s" stroke-width="1.6"/>' % (VX, VX, INK2))
d.append('  <path d="M%d,342 L%d,352" fill="none" stroke="%s" stroke-width="1.0"/>' % (VX - 8, VX - 16, INK3))
d.append('  <path d="M%d,366 L%d,380 M%d,366 L%d,380" fill="none" stroke="%s" stroke-width="1.1"/>' % (VX - 5, VX - 10, VX + 5, VX + 10, INK2))
# 远山一痕
d.append('  <path d="M%d,380 L%d,366 L%d,380" fill="none" stroke="%s" stroke-width="0.8"/>' % (VX + 24, VX + 38, VX + 52, INK3))
d.append('  <text x="%d" y="400" text-anchor="middle" font-size="7.0" fill="%s">望归 · 面山而立</text>' % (VX, RED))

for (x, t) in [(120, "壹"), (350, "贰"), (600, "叁")]:
    d.append('  <text x="%d" y="132" font-size="7.6" fill="%s">%s</text>' % (x, RED, t))
d.append('  <text x="44" y="466" font-size="7.8" fill="%s">壹 雷声 · 殷其雷，起于南山</text>' % INK2)
d.append('  <text x="264" y="466" font-size="7.8" fill="%s">贰 南山 · 阳、侧、下三位</text>' % INK2)
d.append('  <text x="486" y="466" font-size="7.8" fill="%s">叁 望归 · 室家闻雷而思</text>' % INK2)
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
