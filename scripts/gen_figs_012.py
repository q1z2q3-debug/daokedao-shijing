# -*- coding: utf-8 -*-
"""SJ012《鹊巢》两图。图一：鹊巢鸠居。图二：居·方·盈。"""
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
d.append('  <text x="44" y="58" font-size="8.6" letter-spacing="2" fill="%s">召南 · 一</text>' % RED)
d.append('  <text x="380" y="60" text-anchor="middle" font-size="26" letter-spacing="10" fill="%s" font-weight="700">鹊 巢</text>' % INK)
d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之十二</text>' % INK3)
d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)

GROUND = 466
# —— 树：粗干三叉 ——
d.append('  <path d="M380,%d C379,424 380,392 381,352" fill="none" stroke="%s" stroke-width="3.4"/>' % (GROUND, INK))
d.append('  <path d="M381,372 C368,352 344,340 322,334" fill="none" stroke="%s" stroke-width="2.2"/>' % INK)
d.append('  <path d="M381,362 C398,344 424,336 446,332" fill="none" stroke="%s" stroke-width="2.2"/>' % INK)
d.append('  <path d="M381,392 C370,382 352,378 336,376" fill="none" stroke="%s" stroke-width="1.4"/>' % INK2)
for (x0, y0, x1, y1) in [(296, 306, 276, 296), (466, 306, 486, 298), (336, 376, 320, 372)]:
    d.append('  <line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="0.9"/>' % (x0, y0, x1, y1, INK2))

# —— 巢：碗形，有口 ——
d.append('  <path d="M332,330 C332,306 346,296 356,296 C368,308 392,308 404,296 C414,296 428,306 428,330 C428,352 406,362 380,362 C354,362 332,352 332,330 Z" fill="#EFEAD6" stroke="%s" stroke-width="1.1"/>' % INK2)
# 编枝纹理（横弧，长短交错）
for k in range(7):
    y = 312 + k * 6
    w = 34 - k * 2
    d.append('  <path d="M%.1f,%.1f q%.1f,%.1f %.1f,0" fill="none" stroke="%s" stroke-width="0.45" opacity="0.85"/>'
             % (380 - w, y, w, -1.5 + (k % 2) * 3, 2 * w, INK3))
# 伸出之枝（口沿与两侧）
for (x, y, dx, dy) in [(340, 300, -16, -8), (352, 294, -10, -12), (412, 294, 12, -12), (422, 300, 16, -8),
                       (334, 334, -12, 4), (426, 336, 12, 6)]:
    d.append('  <line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="0.8"/>' % (x, y, x + dx, y + dy, INK2))

# —— 鸠：露一头与胸 ——
d.append('  <circle cx="382" cy="300" r="9.0" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <path d="M373,308 C373,298 391,298 391,308 C391,316 373,316 373,308 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.8"/>' % INK2)
d.append('  <path d="M391,300 l11,3 l-11,4 Z" fill="#EFEAD6" stroke="%s" stroke-width="0.7"/>' % INK2)
d.append('  <circle cx="386" cy="297" r="1.4" fill="%s"/>' % INK)

# —— 车（百两，缩为两乘，轮着地） ——
for ox in (206, 556):
    d.append('  <rect x="%d" y="%d" width="54" height="22" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % (ox, GROUND - 78, INK2))
    for wx in (ox + 12, ox + 42):
        d.append('  <circle cx="%d" cy="%d" r="7" fill="none" stroke="%s" stroke-width="1.0"/>' % (wx, GROUND - 51, INK2))
        d.append('  <circle cx="%d" cy="%d" r="2" fill="none" stroke="%s" stroke-width="0.5"/>' % (wx, GROUND - 51, INK3))
    if ox < 380:
        d.append('  <line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="0.9"/>' % (ox + 54, GROUND - 72, ox + 82, GROUND - 84, INK2))
    else:
        d.append('  <line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="0.9"/>' % (ox, GROUND - 72, ox - 28, GROUND - 84, INK2))

# 标注
d.append('  <text x="252" y="270" font-size="7.6" fill="%s">壹　鹊巢</text>' % RED)
d.append('  <line x1="288" y1="268" x2="336" y2="300" stroke="%s" stroke-width="0.5" stroke-dasharray="3 3"/>' % RED)
d.append('  <text x="420" y="268" font-size="7.6" fill="%s">贰　鸠</text>' % RED)
d.append('  <line x1="418" y1="274" x2="400" y2="294" stroke="%s" stroke-width="0.5" stroke-dasharray="3 3"/>' % RED)
d.append('  <text x="622" y="366" font-size="7.6" fill="%s">叁　百两</text>' % RED)
d.append('  <line x1="618" y1="372" x2="600" y2="386" stroke="%s" stroke-width="0.5" stroke-dasharray="3 3"/>' % RED)
d.append('  <path d="M120,%d C180,%d 300,%d 380,%d" fill="none" stroke="%s" stroke-width="0.28" stroke-dasharray="7 4 1.5 4"/>'
         % (GROUND + 4, GROUND + 8, GROUND + 8, GROUND + 4, INK3))

d.append('  <text x="44" y="466" font-size="7.8" fill="%s">壹 鹊巢　枝编成巢，先筑而后有</text>' % INK2)
d.append('  <text x="264" y="466" font-size="7.8" fill="%s">贰 鸠　鸤鸠，居而不筑</text>' % INK2)
d.append('  <text x="486" y="466" font-size="7.8" fill="%s">叁 百两　诸侯嫁女之车</text>' % INK2)
d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">维鹊有巢，维鸠居之</text>' % INK)
d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">先筑而后居</text>' % INK3)
d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj012a</text>' % INK3)
d.append('</svg>')
open(os.path.join(FIG, "sj012a-que-chao-jiu-ju.svg"), "w", encoding="utf-8").write("\n".join(d))

# ============ 图二 ============
e = []
e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="\'Noto Serif SC\',\'Songti SC\',serif">' % (W, H, W, H))
e.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
e.append('  <rect x="10" y="10" width="740" height="500" fill="none" stroke="%s" stroke-width="1"/>' % INK3)
e.append('  <rect x="16" y="16" width="728" height="488" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
e.append('  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="%s" font-weight="700">居 · 方 · 盈</text>' % INK)
e.append('  <text x="380" y="74" text-anchor="middle" font-size="9.6" letter-spacing="2" fill="%s">《诗经》召南 · 第一篇　鹊巢</text>' % INK2)
e.append('  <defs><marker id="ar12" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % RED)
cells = [(70, "居", "御之", "住进去", INK2), (290, "方", "将之", "据而有之", RED), (510, "盈", "成之", "人满了巢", INK2)]
for (x, big, s1, s2, col) in cells:
    e.append('  <rect x="%d" y="150" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (x, col))
    e.append('  <text x="%d" y="214" text-anchor="middle" font-size="28" letter-spacing="2" fill="%s" font-weight="700">%s</text>' % (x + 75, col, big))
    e.append('  <text x="%d" y="252" text-anchor="middle" font-size="10" fill="#3B352F">%s</text>' % (x + 75, s1))
    e.append('  <text x="%d" y="278" text-anchor="middle" font-size="8" fill="%s">%s</text>' % (x + 75, INK3, s2))
e.append('  <line x1="220" y1="225" x2="288" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar12)"/>' % RED)
e.append('  <line x1="440" y1="225" x2="508" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar12)"/>' % RED)
e.append('  <text x="380" y="330" text-anchor="middle" font-size="8.4" fill="%s">巢之三阶：住 → 有 → 满　　礼之三阶：迎 → 送 → 成</text>' % INK2)
e.append('  <line x1="120" y1="360" x2="640" y2="360" stroke="%s" stroke-width="0.8"/>' % INK3)
e.append('  <text x="230" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">方</text>' % RED)
e.append('  <text x="230" y="414" text-anchor="middle" font-size="7.4" fill="%s">毛传：有之也，非「方形」</text>' % INK3)
e.append('  <text x="530" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">鸠</text>' % RED)
e.append('  <text x="530" y="414" text-anchor="middle" font-size="7.4" fill="%s">鸤鸠，诗中喻「仪一」，非恶鸟</text>' % INK3)
e.append('  <text x="380" y="446" text-anchor="middle" font-size="7.4" fill="%s">今语「鸠占鹊巢」言强占；诗义则「备而后居」</text>' % INK3)
e.append('  <text x="120" y="512" font-size="5.6" fill="%s">诗经 · 召南</text>' % INK2)
e.append('  <text x="640" y="512" text-anchor="end" font-size="5.6" fill="%s">图二 · 居方盈 · sj012b</text>' % INK2)
e.append('</svg>')
open(os.path.join(FIG, "sj012b-ju-fang-ying.svg"), "w", encoding="utf-8").write("\n".join(e))

import cairosvg
for k in ["sj012a-que-chao-jiu-ju", "sj012b-ju-fang-ying"]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok")
