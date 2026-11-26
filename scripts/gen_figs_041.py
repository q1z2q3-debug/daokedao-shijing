# -*- coding: utf-8 -*-
"""SJ041《北风》两图。图一：风雪·携手同行·狐乌。图二：同行—同归—同车。"""
import os, sys, re, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fig_geo import *
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(ROOT, "assets", "fig")
INK, INK2, INK3, RED, PAPER = "#1F1B17", "#5C544A", "#9A9186", "#994433", "#F7F4EE"
W, H = 760, 540

def bounds_ok(svg, tag):
    s = re.sub(r"#[0-9A-Fa-f]{6}", "", svg)
    s = re.sub(r'font-size="[^"]*"', "", s)
    s = re.sub(r'letter-spacing="[^"]*"', "", s)
    nums = [float(x) for x in re.findall(r"-?\d+\.?\d*", s)]
    xs = nums[0::2]; ys = nums[1::2]
    bad = [n for n in xs if n < 0 or n > W] + [n for n in ys if n < 0 or n > H]
    print(tag, "x[%.1f,%.1f] y[%.1f,%.1f] %s" % (min(xs), max(xs), min(ys), max(ys), "OK" if not bad else "OUT: %s" % bad))

d = []
d.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="\'Noto Serif SC\',\'Songti SC\',serif">' % (W, H, W, H))
d.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
d.append('  <text x="44" y="58" font-size="8.6" letter-spacing="2" fill="%s">邶风 · 三</text>' % RED)
d.append('  <text x="380" y="60" text-anchor="middle" font-size="26" letter-spacing="10" fill="%s" font-weight="700">北 风</text>' % INK)
d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之四十一</text>' % INK3)
d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)

# 壹 · 风雪（风三缕斜笔＋雪点疏密＋地面短线）
# 风三缕（左上斜向右下，渐细）
d.append('  <path d="M96,220 C124,232 150,244 176,258" fill="none" stroke="%s" stroke-width="1.1"/>' % INK2)
d.append('  <path d="M88,252 C120,262 152,274 184,290" fill="none" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <path d="M100,286 C126,294 150,304 172,316" fill="none" stroke="%s" stroke-width="0.7"/>' % INK3)
# 雪点：三簇，上疏下密
for (cx, cy, n) in [(130, 236, 5), (158, 268, 7), (120, 300, 6)]:
    for k in range(n):
        ox = (k * 13) % 26 - 13
        oy = (k * 17) % 20 - 10
        d.append('  <circle cx="%.1f" cy="%.1f" r="1.1" fill="%s"/>' % (cx + ox, cy + oy, INK3))
# 地面积雪短线
d.append('  <line x1="104" y1="356" x2="192" y2="356" stroke="%s" stroke-width="0.7"/>' % INK3)
for k in range(4):
    gx = 112 + k * 22
    d.append('  <line x1="%d" y1="356" x2="%d" y2="350" stroke="%s" stroke-width="0.5"/>' % (gx, gx, INK3))
d.append('  <text x="148" y="392" text-anchor="middle" font-size="7.0" fill="%s">北风其凉，雨雪其雱</text>' % RED)

# 贰 · 二人并肩相携背影
# 左人
L = 356
d.append('  <ellipse cx="%d" cy="246" rx="8" ry="9" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % (L, INK2))
d.append('  <line x1="%d" y1="255" x2="%d" y2="262" stroke="%s" stroke-width="0.9"/>' % (L - 3, L - 3, INK2))
d.append('  <line x1="%d" y1="255" x2="%d" y2="262" stroke="%s" stroke-width="0.9"/>' % (L + 3, L + 3, INK2))
d.append('  <path d="M%d,262 C348,290 348,320 357,348 L375,348 C384,320 384,290 376,262 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % (L, INK2))
d.append('  <line x1="%d" y1="264" x2="%d" y2="264" stroke="%s" stroke-width="0.9"/>' % (L - 8, L + 8, INK2))
# 右人
R = 402
d.append('  <ellipse cx="%d" cy="246" rx="8" ry="9" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % (R, INK2))
d.append('  <line x1="%d" y1="255" x2="%d" y2="262" stroke="%s" stroke-width="0.9"/>' % (R - 3, R - 3, INK2))
d.append('  <line x1="%d" y1="255" x2="%d" y2="262" stroke="%s" stroke-width="0.9"/>' % (R + 3, R + 3, INK2))
d.append('  <path d="M%d,262 C394,290 394,320 403,348 L421,348 C430,320 430,290 422,262 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % (R, INK2))
d.append('  <line x1="%d" y1="264" x2="%d" y2="264" stroke="%s" stroke-width="0.9"/>' % (R - 8, R + 8, INK2))
# 相携之手（两人内侧臂相接）
d.append('  <path d="M376,272 C382,280 384,288 385,292" fill="none" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <path d="M394,272 C388,280 386,288 385,292" fill="none" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <circle cx="385" cy="292" r="2.4" fill="#EFEAD6" stroke="%s" stroke-width="0.8"/>' % INK2)
# 外侧宽袖
d.append('  <path d="M348,268 C342,282 340,300 346,312" fill="none" stroke="%s" stroke-width="0.9"/>' % INK3)
d.append('  <path d="M422,268 C428,282 430,300 424,312" fill="none" stroke="%s" stroke-width="0.9"/>' % INK3)
d.append('  <text x="378" y="372" text-anchor="middle" font-size="7.0" fill="%s">惠而好我，携手同行</text>' % RED)

# 叁 · 狐与乌（狐侧身；乌侧身）
# 狐（朝右）
d.append('  <path d="M566,332 C566,318 592,314 604,324 C598,336 574,338 566,332 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <path d="M604,324 L612,312" fill="none" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <path d="M612,312 L622,314 L614,323 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % INK2)
# 狐耳
d.append('  <line x1="612" y1="312" x2="614" y2="306" stroke="%s" stroke-width="0.7"/>' % INK2)
d.append('  <circle cx="616" cy="315" r="1.1" fill="%s"/>' % INK)
# 狐尾（蓬松大尾上翘）
d.append('  <path d="M566,330 C554,326 548,316 552,306" fill="none" stroke="%s" stroke-width="1.1"/>' % INK2)
d.append('  <path d="M562,333 C554,331 550,324 552,316" fill="none" stroke="%s" stroke-width="0.5"/>' % INK3)
# 狐足
for fx in (574, 582, 596, 602):
    d.append('  <line x1="%d" y1="336" x2="%d" y2="348" stroke="%s" stroke-width="0.8"/>' % (fx, fx, INK2))
# 乌（朝左，立于右侧）
d.append('  <ellipse cx="664" cy="322" rx="16" ry="12" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <circle cx="652" cy="310" r="7.5" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <path d="M645,308 L634,311 L645,315 Z" fill="#EFEAD6" stroke="%s" stroke-width="0.7"/>' % INK2)
d.append('  <circle cx="650" cy="308" r="1.3" fill="%s"/>' % INK)
# 翅
d.append('  <path d="M660,318 C668,322 672,330 670,338" fill="none" stroke="%s" stroke-width="0.8"/>' % INK3)
# 尾羽
d.append('  <path d="M678,326 L690,330 M678,322 L690,324" fill="none" stroke="%s" stroke-width="0.8"/>' % INK2)
# 乌足
d.append('  <line x1="660" y1="334" x2="660" y2="348" stroke="%s" stroke-width="0.8"/>' % INK2)
d.append('  <line x1="668" y1="334" x2="668" y2="348" stroke="%s" stroke-width="0.8"/>' % INK2)
d.append('  <text x="622" y="380" text-anchor="middle" font-size="7.0" fill="%s">莫赤匪狐，莫黑匪乌</text>' % RED)

for (x, t) in [(120, "壹"), (350, "贰"), (600, "叁")]:
    d.append('  <text x="%d" y="132" font-size="7.6" fill="%s">%s</text>' % (x, RED, t))
d.append('  <text x="44" y="466" font-size="7.8" fill="%s">壹 风雪　风斜雪盛，气象愁急</text>' % INK2)
d.append('  <text x="264" y="466" font-size="7.8" fill="%s">贰 相携　惠好之人，并肩同行</text>' % INK2)
d.append('  <text x="486" y="466" font-size="7.8" fill="%s">叁 狐乌　赤黑皆非，在位可厌</text>' % INK2)
d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">惠而好我，携手同归</text>' % INK)
d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">乱世相携，非独自逃亡</text>' % INK3)
d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj041a</text>' % INK3)
d.append('</svg>')
svg_a = "\n".join(d)
open(os.path.join(FIG, "sj041a-bei-feng-yu-xue.svg"), "w", encoding="utf-8").write(svg_a)
bounds_ok(svg_a, "041a")

# 图二
e = []
e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="Noto Serif SC,Songti SC,serif">' % (W, H, W, H))
e.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
e.append('  <rect x="10" y="10" width="740" height="500" fill="none" stroke="%s" stroke-width="1"/>' % INK3)
e.append('  <rect x="16" y="16" width="728" height="488" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
e.append('  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="%s" font-weight="700">同行 · 同归 · 同车</text>' % INK)
e.append('  <text x="380" y="74" text-anchor="middle" font-size="9.6" letter-spacing="2" fill="%s">《诗经》邶风 · 第十六篇　北风</text>' % INK2)
e.append('  <defs><marker id="ar21" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % RED)
cells = [(70, "同行", "携手同行", "风雪其凉", INK2), (290, "同归", "携手同归", "雨雪其霏", RED), (510, "同车", "携手同车", "莫黑匪乌", INK2)]
for (x, big, s1, s2, col) in cells:
    e.append('  <rect x="%d" y="150" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (x, col))
    e.append('  <text x="%d" y="214" text-anchor="middle" font-size="28" letter-spacing="2" fill="%s" font-weight="700">%s</text>' % (x + 75, col, big))
    e.append('  <text x="%d" y="252" text-anchor="middle" font-size="10" fill="#3B352F">%s</text>' % (x + 75, s1))
    e.append('  <text x="%d" y="278" text-anchor="middle" font-size="8" fill="%s">%s</text>' % (x + 75, INK3, s2))
e.append('  <line x1="220" y1="225" x2="288" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar21)"/>' % RED)
e.append('  <line x1="440" y1="225" x2="508" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar21)"/>' % RED)
e.append('  <text x="380" y="330" text-anchor="middle" font-size="8.4" fill="%s">乱世相携：三阶递进，所携始终是惠而好我之人；去之以亟，不离以情</text>' % INK2)
e.append('  <line x1="120" y1="360" x2="640" y2="360" stroke="%s" stroke-width="0.8"/>' % INK3)
e.append('  <text x="230" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">惠好</text>' % RED)
e.append('  <text x="230" y="414" text-anchor="middle" font-size="7.4" fill="%s">相爱相善，相知相携</text>' % INK3)
e.append('  <text x="530" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">既亟</text>' % RED)
e.append('  <text x="530" y="414" text-anchor="middle" font-size="7.4" fill="%s">时已急，不能复舒缓</text>' % INK3)
e.append('  <text x="380" y="446" text-anchor="middle" font-size="7.4" fill="%s">《毛序》「百姓不亲，莫不相携持而去焉」</text>' % INK3)
e.append('  <text x="120" y="512" font-size="5.6" fill="%s">诗经 · 邶风</text>' % INK2)
e.append('  <text x="640" y="512" text-anchor="end" font-size="5.6" fill="%s">图二 · 同行同归同车 · sj041b</text>' % INK2)
e.append('</svg>')
svg_b = "\n".join(e)
open(os.path.join(FIG, "sj041b-xie-shou-tong-gui.svg"), "w", encoding="utf-8").write(svg_b)
bounds_ok(svg_b, "041b")

import cairosvg
for k in ["sj041a-bei-feng-yu-xue", "sj041b-xie-shou-tong-gui"]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok")
