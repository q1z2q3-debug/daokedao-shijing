# -*- coding: utf-8 -*-
"""SJ030《终风》两图。图一：风·霾曀·阴雷。图二：暴—思—系。"""
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
d.append('  <text x="380" y="60" text-anchor="middle" font-size="26" letter-spacing="10" fill="%s" font-weight="700">终 风</text>' % INK)
d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之三十</text>' % INK3)
d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)

# 壹 · 终风（云气回旋线＋飞尘疏密）
# 回旋风势三道弧
d.append('  <path d="M106,252 C116,226 180,226 190,252" fill="none" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <path d="M116,262 C126,244 170,244 180,262" fill="none" stroke="%s" stroke-width="0.8"/>' % INK2)
d.append('  <path d="M150,252 q12,5 6,14" fill="none" stroke="%s" stroke-width="0.7"/>' % INK2)
# 飞尘：右侧密、左侧疏
for (dx, dy) in [(176, 282), (184, 280), (192, 283), (200, 281), (180, 294), (190, 292), (200, 295), (112, 288), (121, 290)]:
    d.append('  <circle cx="%d" cy="%d" r="1.2" fill="%s"/>' % (dx, dy, INK3))
d.append('  <text x="148" y="330" text-anchor="middle" font-size="7.0" fill="%s">终风且霾，云气回旋</text>' % RED)

# 贰 · 顾我则笑（两人侧影：一人回顾，一人低头）
# 回顾者（左，身朝右，首回顾）
d.append('  <path d="M336,256 C332,280 334,302 340,318 L356,318 C362,302 362,280 358,256 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <ellipse cx="347" cy="240" rx="7" ry="8" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <path d="M338,262 C334,276 334,290 338,300" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
# 低头者（右，首俯）
d.append('  <path d="M396,256 C392,280 394,302 400,318 L416,318 C422,302 422,280 418,256 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <ellipse cx="407" cy="247" rx="7" ry="8" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <path d="M416,262 C420,276 420,290 416,300" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
# 相顾之间的视线（淡形虚线）
d.append('  <line x1="354" y1="242" x2="398" y2="247" stroke="%s" stroke-width="0.5" stroke-dasharray="3 3"/>' % INK3)
d.append('  <text x="378" y="330" text-anchor="middle" font-size="7.0" fill="%s">顾我则笑，相顾低头</text>' % RED)

# 叁 · 曀阴与雷（云层叠三笔＋雷纹回旋）
d.append('  <path d="M588,226 C598,214 646,214 656,226 Z" fill="#EFEAD6" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <path d="M582,238 C594,226 650,226 662,238 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <path d="M588,250 C598,240 646,240 656,250 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.8"/>' % INK3)
# 雷纹回旋：曲折闪电＋两侧小涡
d.append('  <path d="M622,256 L614,276 L626,274 L618,294" fill="none" stroke="%s" stroke-width="1.3"/>' % RED)
d.append('  <path d="M596,268 q6,-6 12,0" fill="none" stroke="%s" stroke-width="0.5"/>' % INK3)
d.append('  <path d="M648,268 q6,-6 12,0" fill="none" stroke="%s" stroke-width="0.5"/>' % INK3)
d.append('  <text x="622" y="330" text-anchor="middle" font-size="7.0" fill="%s">曀曀其阴，虺虺其雷</text>' % RED)

for (x, t) in [(120, "壹"), (350, "贰"), (600, "叁")]:
    d.append('  <text x="%d" y="132" font-size="7.6" fill="%s">%s</text>' % (x, RED, t))
d.append('  <text x="44" y="466" font-size="7.8" fill="%s">壹 终风　云气回旋，风夹尘土</text>' % INK2)
d.append('  <text x="264" y="466" font-size="7.8" fill="%s">贰 顾我　回顾相顾，低头含情</text>' % INK2)
d.append('  <text x="486" y="466" font-size="7.8" fill="%s">叁 阴雷　叠云蔽日，雷纹将发</text>' % INK2)
d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">曀曀其阴，虺虺其雷</text>' % INK)
d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">天变即情变，一章坏过一章</text>' % INK3)
d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj030a</text>' % INK3)
d.append('</svg>')
svg_a = "\n".join(d)
open(os.path.join(FIG, "sj030a-zhong-feng-tian-ying.svg"), "w", encoding="utf-8").write(svg_a)
bounds_ok(svg_a, "030a")

# 图二
e = []
e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="Noto Serif SC,Songti SC,serif">' % (W, H, W, H))
e.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
e.append('  <rect x="10" y="10" width="740" height="500" fill="none" stroke="%s" stroke-width="1"/>' % INK3)
e.append('  <rect x="16" y="16" width="728" height="488" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
e.append('  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="%s" font-weight="700">悼 · 思 · 怀</text>' % INK)
e.append('  <text x="380" y="74" text-anchor="middle" font-size="9.6" letter-spacing="2" fill="%s">《诗经》邶风 · 第五篇　终风</text>' % INK2)
e.append('  <defs><marker id="ar30" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % RED)
cells = [(70, "悼", "中心是悼", "遇人之暴", INK2), (290, "思", "悠悠我思", "莫往莫来", RED), (510, "怀", "愿言则怀", "断不了", INK2)]
for (x, big, s1, s2, col) in cells:
    e.append('  <rect x="%d" y="150" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (x, col))
    e.append('  <text x="%d" y="214" text-anchor="middle" font-size="28" letter-spacing="2" fill="%s" font-weight="700">%s</text>' % (x + 75, col, big))
    e.append('  <text x="%d" y="252" text-anchor="middle" font-size="10" fill="#3B352F">%s</text>' % (x + 75, s1))
    e.append('  <text x="%d" y="278" text-anchor="middle" font-size="8" fill="%s">%s</text>' % (x + 75, INK3, s2))
e.append('  <line x1="220" y1="225" x2="288" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar30)"/>' % RED)
e.append('  <line x1="440" y1="225" x2="508" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar30)"/>' % RED)
e.append('  <text x="380" y="330" text-anchor="middle" font-size="8.4" fill="%s">天象四转：暴—霾—曀—阴雷；心情一节缠过一节</text>' % INK2)
e.append('  <line x1="120" y1="360" x2="640" y2="360" stroke="%s" stroke-width="0.8"/>' % INK3)
e.append('  <text x="230" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">嚏</text>' % RED)
e.append('  <text x="230" y="414" text-anchor="middle" font-size="7.4" fill="%s">俗信：被人念及则嚏</text>' % INK3)
e.append('  <text x="530" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">怀</text>' % RED)
e.append('  <text x="530" y="414" text-anchor="middle" font-size="7.4" fill="%s">念沉为怀，怨中夹念</text>' % INK3)
e.append('  <text x="380" y="446" text-anchor="middle" font-size="7.4" fill="%s">遇人之暴而心犹系，念落到生理上</text>' % INK3)
e.append('  <text x="120" y="512" font-size="5.6" fill="%s">诗经 · 邶风</text>' % INK2)
e.append('  <text x="640" y="512" text-anchor="end" font-size="5.6" fill="%s">图二 · 暴思系 · sj030b</text>' % INK2)
e.append('</svg>')
svg_b = "\n".join(e)
open(os.path.join(FIG, "sj030b-bao-er-you-xi.svg"), "w", encoding="utf-8").write(svg_b)
bounds_ok(svg_b, "030b")

import cairosvg
for k in ["sj030a-zhong-feng-tian-ying", "sj030b-bao-er-you-xi"]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok")
