# -*- coding: utf-8 -*-
"""SJ008《芣苢》两图。图一：车前（平行脉、穗、须根）。图二：由手及襟。"""
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
d.append('  <text x="44" y="58" font-size="8.6" letter-spacing="2" fill="%s">周南 · 八</text>' % RED)
d.append('  <text x="380" y="60" text-anchor="middle" font-size="26" letter-spacing="10" fill="%s" font-weight="700">芣 苢</text>' % INK)
d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之八</text>' % INK3)
d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)

CX, CY = 380, 396

# —— 叶（基生辐射，宽卵，脉平行）——
LEAVES = [(-64, 86, 17), (-28, 96, 18), (8, 100, 19), (44, 92, 18), (78, 78, 16)]


def leaf(cx, cy, ang, L, Wd):
    """叶基在 (cx,cy)，叶轴竖直向上，整体绕基点转 ang"""
    g = ell(cx, cy - L / 2, Wd, L / 2)
    g = comb(g, poly([(cx - Wd * 0.55, cy - L * 0.93), (cx, cy - L - 7), (cx + Wd * 0.55, cy - L * 0.93)]))
    g = g.buffer(1.2).buffer(-1.2)
    for dd in to_path(g):
        d.append('  <path d="%s" fill="#EFEAD6" stroke="%s" stroke-width="0.55" transform="rotate(%.1f %d %d)"/>'
                 % (dd, INK2, ang, cx, cy))
    for k in (-2, -1, 0, 1, 2):
        off = k * Wd * 0.30
        d.append('  <path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="0.3" transform="rotate(%.1f %d %d)"/>'
                 % (cx + off, cy - L * 0.18, cx + off * 0.6, cy - L * 0.76, INK3, ang, cx, cy))


for (ang, L, Wd) in LEAVES:
    leaf(CX, CY, ang, L, Wd)

# —— 花穗（三根，细长，密点）——
for (dx, L, bend) in [(-14, 76, -12), (2, 92, 5), (16, 68, 18)]:
    pts = []
    for i in range(26):
        t = i / 25
        x = CX + dx * (1 - t * 0.4) + bend * t * t * 0.9
        y = CY - 6 - L * t
        pts.append((x, y))
    d.append('  <path d="M%s" fill="none" stroke="%s" stroke-width="2.0"/>'
             % (" L".join("%.1f,%.1f" % q for q in pts), INK2))
    for i in range(3, len(pts) - 1):
        x, y = pts[i]
        side = 1 if i % 2 else -1
        d.append('  <circle cx="%.1f" cy="%.1f" r="1.7" fill="#F3EBD8" stroke="%s" stroke-width="0.3"/>'
                 % (x + side * 1.9, y, INK3))

# —— 须根 ——
d.append('  <path d="M%d,%d L%d,%d" stroke="%s" stroke-width="1.8"/>' % (CX, CY + 2, CX, CY + 20, INK2))
for k in range(7):
    a = -50 + k * 17
    d.append('  <path d="M%d,%d C%.1f,%d %.1f,%d %.1f,%d" fill="none" stroke="%s" stroke-width="0.5"/>'
             % (CX, CY + 24,
                CX + 8 * math.sin(math.radians(a)), CY + 28,
                CX + 16 * math.sin(math.radians(a)), CY + 38,
                CX + 21 * math.sin(math.radians(a)), CY + 45 + (k % 2) * 3, INK3))

# 地平
d.append('  <path d="M290,%d C340,%d 420,%d 470,%d" fill="none" stroke="%s" stroke-width="0.28" stroke-dasharray="7 4 1.5 4"/>'
         % (CY + 22, CY + 26, CY + 26, CY + 22, INK3))

# 编号
d.append('  <text x="300" y="322" font-size="7.6" fill="%s">①</text>' % RED)
d.append('  <text x="416" y="300" font-size="7.6" fill="%s">②</text>' % RED)
d.append('  <text x="346" y="486" font-size="7.6" fill="%s">③</text>' % RED)

d.append('  <text x="44" y="466" font-size="7.8" fill="%s">① 芣苢　即车前：叶基生，脉平行</text>' % INK2)
d.append('  <text x="264" y="466" font-size="7.8" fill="%s">② 穗　花密如串，从叶丛抽出</text>' % INK2)
d.append('  <text x="486" y="466" font-size="7.8" fill="%s">③ 根　须根浅生，拔之即起</text>' % INK2)
d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">采采芣苢，薄言采之</text>' % INK)
d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">六动一事，最纯的歌</text>' % INK3)
d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj008a</text>' % INK3)
d.append('</svg>')
open(os.path.join(FIG, "sj008a-fu-yi-che-qian.svg"), "w", encoding="utf-8").write("\n".join(d))

# ============ 图二 ============
e = []
e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="\'Noto Serif SC\',\'Songti SC\',serif">' % (W, H, W, H))
e.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
e.append('  <rect x="10" y="10" width="740" height="500" fill="none" stroke="%s" stroke-width="1"/>' % INK3)
e.append('  <rect x="16" y="16" width="728" height="488" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
e.append('  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="%s" font-weight="700">由 手 及 襟</text>' % INK)
e.append('  <text x="380" y="74" text-anchor="middle" font-size="9.6" letter-spacing="2" fill="%s">《诗经》周南 · 第八篇　芣苢</text>' % INK2)
e.append('  <defs><marker id="ar8" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % RED)
cells = [(70, "采·有", "取而得之", "手取", INK2), (290, "掇·捋", "拾地、抹枝", "聚之", RED), (510, "袺·襭", "提襟、掖襟", "襟兜", INK2)]
for (x, big, s1, s2, col) in cells:
    e.append('  <rect x="%d" y="150" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (x, col))
    e.append('  <text x="%d" y="206" text-anchor="middle" font-size="20" letter-spacing="1" fill="%s" font-weight="700">%s</text>' % (x + 75, col, big))
    e.append('  <text x="%d" y="248" text-anchor="middle" font-size="10" fill="#3B352F">%s</text>' % (x + 75, s1))
    e.append('  <text x="%d" y="276" text-anchor="middle" font-size="8" fill="%s">%s</text>' % (x + 75, INK3, s2))
e.append('  <line x1="220" y1="225" x2="288" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar8)"/>' % RED)
e.append('  <line x1="440" y1="225" x2="508" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar8)"/>' % RED)
e.append('  <text x="380" y="330" text-anchor="middle" font-size="8.4" fill="%s">工具从身体里长出来：先用手，手不够用衣襟</text>' % INK2)
e.append('  <line x1="120" y1="360" x2="640" y2="360" stroke="%s" stroke-width="0.8"/>' % INK3)
e.append('  <text x="230" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">采采</text>' % RED)
e.append('  <text x="230" y="414" text-anchor="middle" font-size="7.4" fill="%s">朱子：非一采也</text>' % INK3)
e.append('  <text x="530" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">薄言</text>' % RED)
e.append('  <text x="530" y="414" text-anchor="middle" font-size="7.4" fill="%s">语助，无实义；解错则全篇皆变</text>' % INK3)
e.append('  <text x="380" y="446" text-anchor="middle" font-size="7.4" fill="%s">《诗》三章　·　全篇只换六字　·　顾炎武尝据此论叠字</text>' % INK3)
e.append('  <text x="120" y="512" font-size="5.6" fill="%s">诗经 · 周南</text>' % INK2)
e.append('  <text x="640" y="512" text-anchor="end" font-size="5.6" fill="%s">图二 · 由手及襟 · sj008b</text>' % INK2)
e.append('</svg>')
open(os.path.join(FIG, "sj008b-you-shou-ji-jin.svg"), "w", encoding="utf-8").write("\n".join(e))

import cairosvg
for k in ["sj008a-fu-yi-che-qian", "sj008b-you-shou-ji-jin"]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok")
