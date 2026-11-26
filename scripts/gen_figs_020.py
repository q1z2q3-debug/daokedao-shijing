# -*- coding: utf-8 -*-
"""SJ020《摽有梅》两图。图一：梅实七·梅实三·顷筐。图二：吉·今·谓。"""
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
d.append('  <text x="380" y="60" text-anchor="middle" font-size="26" letter-spacing="10" fill="%s" font-weight="700">摽有梅</text>' % INK)
d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之二十</text>' % INK3)
d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)

def plum_tree(cx, n_fruit, n_fallen, label):
    # 地面
    d.append('  <line x1="%d" y1="390" x2="%d" y2="390" stroke="%s" stroke-width="0.8"/>' % (cx - 38, cx + 38, INK3))
    # 主干（线画，微曲）
    d.append('  <path d="M%d,390 C%d,350 %d,312 %d,268" fill="none" stroke="%s" stroke-width="2.2"/>' % (cx, cx, cx + 2, cx + 1, INK))
    # 三枝折线
    d.append('  <path d="M%d,306 L%d,284 L%d,266" fill="none" stroke="%s" stroke-width="1.4"/>' % (cx, cx - 18, cx - 30, INK2))
    d.append('  <path d="M%d,300 L%d,280 L%d,262" fill="none" stroke="%s" stroke-width="1.4"/>' % (cx + 1, cx + 20, cx + 32, INK2))
    d.append('  <path d="M%d,286 L%d,258" fill="none" stroke="%s" stroke-width="1.2"/>' % (cx + 1, cx + 2, INK2))
    # 叶簇（枝端短线小叶，不开闭合圈）
    for (lx, ly) in [(cx - 30, 266), (cx - 20, 258), (cx + 32, 262), (cx + 22, 254), (cx + 2, 250)]:
        for k in range(3):
            d.append('  <path d="M%d,%d q6,-3 10,0" fill="none" stroke="%s" stroke-width="0.5"/>'
                     % (lx - 6 + k * 5, ly + (k % 2) * 4, INK3))
    # 果实（小圈辅助）
    pts = [(-24, -8), (-10, -18), (6, -20), (22, -10), (-18, 6), (0, 4), (18, 8), (-6, 16), (12, 16)]
    for k in range(n_fruit):
        px, py = pts[k]
        d.append('  <circle cx="%d" cy="%d" r="3.2" fill="#EFEAD6" stroke="%s" stroke-width="0.7"/>' % (cx + px, 280 + py, INK2))
    # 落梅（树下数点）
    for k in range(n_fallen):
        fx = cx - 26 + k * 12
        fy = 374 + (k % 2) * 8
        d.append('  <circle cx="%d" cy="%d" r="2.4" fill="#EFEAD6" stroke="%s" stroke-width="0.6"/>' % (fx, fy, INK3))
    d.append('  <text x="%d" y="392" text-anchor="middle" font-size="7.0" fill="%s">%s</text>' % (cx, RED, label))

# 壹 · 实七（存七成，落梅尚少）
plum_tree(148, 7, 3, "其实七 · 枝头尚繁")
# 贰 · 实三（落去过半，落梅增多）
plum_tree(378, 3, 7, "其实三 · 落去过半")

# ============ 叁 · 顷筐塈之：竹筐口沿篾纹提梁，筐中拾梅 ============
VX = 622
# 旁空枝一小段
d.append('  <path d="M%d,330 C%d,318 %d,310 %d,302" fill="none" stroke="%s" stroke-width="1.2"/>' % (VX - 28, VX - 28, VX - 28, VX - 26, INK2))
d.append('  <path d="M%d,312 l-8,-4 M%d,318 l-8,-3" fill="none" stroke="%s" stroke-width="0.5"/>' % (VX - 27, VX - 27, INK3))
# 筐身（斜口梯形）
d.append('  <path d="M%d,356 L%d,346 L%d,392 L%d,400 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (VX - 30, VX + 22, VX + 28, VX - 24, INK2))
# 口沿
d.append('  <path d="M%d,356 L%d,346" fill="none" stroke="%s" stroke-width="1.2"/>' % (VX - 30, VX + 22, INK2))
# 提梁拱线
d.append('  <path d="M%d,356 Q%d,330 %d,346" fill="none" stroke="%s" stroke-width="1.0"/>' % (VX - 30, VX - 4, VX + 22, INK2))
# 篾纹（横编三道 + 竖编）
for k in range(3):
    y = 366 + k * 10
    d.append('  <line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="0.45"/>' % (VX - 27, y, VX + 25, y - 2, INK3))
for k in range(3):
    x = VX - 20 + k * 14
    d.append('  <line x1="%d" y1="360" x2="%d" y2="394" stroke="%s" stroke-width="0.45"/>' % (x, x + 2, INK3))
# 筐中拾梅数颗
for k in range(3):
    d.append('  <circle cx="%d" cy="%d" r="2.6" fill="#EFEAD6" stroke="%s" stroke-width="0.6"/>' % (VX - 14 + k * 12, 372 + (k % 2) * 6, INK2))
d.append('  <text x="%d" y="392" text-anchor="middle" font-size="7.0" fill="%s">顷筐塈之 · 口沿篾纹提梁</text>' % (VX, RED))

for (x, t) in [(120, "壹"), (350, "贰"), (600, "叁")]:
    d.append('  <text x="%d" y="132" font-size="7.6" fill="%s">%s</text>' % (x, RED, t))
d.append('  <text x="44" y="466" font-size="7.8" fill="%s">壹 梅实七　枝头尚繁，落梅尚少</text>' % INK2)
d.append('  <text x="264" y="466" font-size="7.8" fill="%s">贰 梅实三　落去过半，疏枝多点</text>' % INK2)
d.append('  <text x="486" y="466" font-size="7.8" fill="%s">叁 顷筐　落尽以筐拾取，篾纹提梁</text>' % INK2)
d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">摽有梅，其實七兮</text>' % INK)
d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">梅落计时，及时而待</text>' % INK3)
d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj020a</text>' % INK3)
d.append('</svg>')
open(os.path.join(FIG, "sj020a-biao-you-mei.svg"), "w", encoding="utf-8").write("\n".join(d))

# ============ 图二 ============
e = []
e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="\'Noto Serif SC\',\'Songti SC\',serif">' % (W, H, W, H))
e.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
e.append('  <rect x="10" y="10" width="740" height="500" fill="none" stroke="%s" stroke-width="1"/>' % INK3)
e.append('  <rect x="16" y="16" width="728" height="488" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
e.append('  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="%s" font-weight="700">吉 · 今 · 谓</text>' % INK)
e.append('  <text x="380" y="74" text-anchor="middle" font-size="9.6" letter-spacing="2" fill="%s">《诗经》召南 · 第九篇　摽有梅</text>' % INK2)
e.append('  <defs><marker id="ar20" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % RED)
cells = [(70, "吉", "迨其吉兮", "趁良辰吉日，从容相求", INK2),
         (290, "今", "迨其今兮", "就趁今日，时已迫近", RED),
         (510, "谓", "迨其谓之", "趁开口相谓，不能再缓", INK2)]
for (x, big, s1, s2, col) in cells:
    e.append('  <rect x="%d" y="150" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (x, col))
    e.append('  <text x="%d" y="214" text-anchor="middle" font-size="28" letter-spacing="2" fill="%s" font-weight="700">%s</text>' % (x + 75, col, big))
    e.append('  <text x="%d" y="252" text-anchor="middle" font-size="10" fill="#3B352F">%s</text>' % (x + 75, s1))
    e.append('  <text x="%d" y="278" text-anchor="middle" font-size="8" fill="%s">%s</text>' % (x + 75, INK3, s2))
e.append('  <line x1="220" y1="225" x2="288" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar20)"/>' % RED)
e.append('  <line x1="440" y1="225" x2="508" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar20)"/>' % RED)
e.append('  <text x="380" y="330" text-anchor="middle" font-size="8.4" fill="%s">果之三阶：七 → 三 → 尽；时之三阶：吉 → 今 → 谓</text>' % INK2)
e.append('  <line x1="120" y1="360" x2="640" y2="360" stroke="%s" stroke-width="0.8"/>' % INK3)
e.append('  <text x="230" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">迨</text>' % RED)
e.append('  <text x="230" y="414" text-anchor="middle" font-size="7.4" fill="%s">及也、趁也，非「等待」</text>' % INK3)
e.append('  <text x="530" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">摽</text>' % RED)
e.append('  <text x="530" y="414" text-anchor="middle" font-size="7.4" fill="%s">落也、击也，非「标志」之標</text>' % INK3)
e.append('  <text x="380" y="446" text-anchor="middle" font-size="7.4" fill="%s">树上空一分，心上急一分；所求在及时之配，不在苟合</text>' % INK3)
e.append('  <text x="120" y="512" font-size="5.6" fill="%s">诗经 · 召南</text>' % INK2)
e.append('  <text x="640" y="512" text-anchor="end" font-size="5.6" fill="%s">图二 · 吉今谓 · sj020b</text>' % INK2)
e.append('</svg>')
open(os.path.join(FIG, "sj020b-dai-qi-jin-wei.svg"), "w", encoding="utf-8").write("\n".join(e))

import cairosvg
for k in ["sj020a-biao-you-mei", "sj020b-dai-qi-jin-wei"]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok")
