# -*- coding: utf-8 -*-
"""SJ028《燕燕》两图。图一：燕羽·旷野·伫立。图二：送·望·泣。"""
import os, sys, re
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
d.append('  <text x="380" y="60" text-anchor="middle" font-size="26" letter-spacing="10" fill="%s" font-weight="700">燕 燕</text>' % INK)
d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之二十八</text>' % INK3)
d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)

GROUND = 440
# 壹 · 燕（剪尾叉尾特写）
FX = 148
# 身
d.append('  <path d="M132,250 C130,238 150,232 164,238 C156,250 138,256 132,250 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
# 头与喙
d.append('  <circle cx="166" cy="236" r="7" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <path d="M173,233 L186,236 L173,240 Z" fill="#EFEAD6" stroke="%s" stroke-width="0.7"/>' % INK2)
d.append('  <circle cx="169" cy="234" r="1.3" fill="%s"/>' % INK)
# 叉尾
d.append('  <line x1="132" y1="250" x2="110" y2="240" stroke="%s" stroke-width="1.1"/>' % INK2)
d.append('  <line x1="132" y1="250" x2="110" y2="260" stroke="%s" stroke-width="1.1"/>' % INK2)
# 参差羽翼（三枚短羽，长短不齐）
for (dx, dy, l) in [(138, 244, 16), (144, 248, 13), (150, 251, 10)]:
    d.append('  <line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="0.8"/>' % (dx, dy, dx - l, dy - 8, INK3))
# 远处一燕（小）
d.append('  <path d="M186,206 q6,-6 12,0 q6,-6 12,0" fill="none" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="%d" y="300" text-anchor="middle" font-size="7.0" fill="%s">剪尾叉尾，羽翅参差</text>' % (FX, RED))

# 贰 · 旷野与远路
WX0, WX1 = 288, 470
d.append('  <line x1="%d" y1="380" x2="%d" y2="380" stroke="%s" stroke-width="0.9"/>' % (WX0, WX1, INK2))
d.append('  <path d="M360,440 L372,380" fill="none" stroke="%s" stroke-width="0.8"/>' % INK2)
d.append('  <path d="M396,440 L384,380" fill="none" stroke="%s" stroke-width="0.8"/>' % INK2)
for k in range(6):
    x = 296 + k * 28
    d.append('  <line x1="%d" y1="410" x2="%d" y2="402" stroke="%s" stroke-width="0.5"/>' % (x, x + 3, INK3))
d.append('  <path d="M372,320 q5,-5 10,0 q5,-5 10,0" fill="none" stroke="%s" stroke-width="0.7"/>' % INK3)
d.append('  <text x="378" y="360" text-anchor="middle" font-size="7.0" fill="%s">远送于野</text>' % RED)

# 叁 · 伫立之人（背影立姿，宽袖衣裾到地，脚不可见）
PX = 622
# 头（背影，无面）
d.append('  <ellipse cx="%d" cy="240" rx="8" ry="9" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % (PX, INK2))
# 衣身：两肩下垂，衣裾收锋到地
d.append('  <path d="M608,256 C600,284 600,318 609,348 L635,348 C644,318 644,284 636,256 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <line x1="608" y1="258" x2="636" y2="258" stroke="%s" stroke-width="0.9"/>' % INK2)
# 两袖下垂（宽袖）
d.append('  <path d="M608,260 C599,274 597,294 603,306" fill="none" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <path d="M636,260 C645,274 647,294 641,306" fill="none" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <path d="M606,268 C602,282 602,294 606,302" fill="none" stroke="%s" stroke-width="0.5"/>' % INK3)
d.append('  <path d="M638,268 C642,282 642,294 638,302" fill="none" stroke="%s" stroke-width="0.5"/>' % INK3)
# 望：身侧两三笔淡形虚线视线，投向远处
d.append('  <line x1="614" y1="240" x2="580" y2="232" stroke="%s" stroke-width="0.5" stroke-dasharray="3 3"/>' % INK3)
d.append('  <line x1="614" y1="244" x2="578" y2="244" stroke="%s" stroke-width="0.5" stroke-dasharray="3 3"/>' % INK3)
d.append('  <line x1="614" y1="248" x2="582" y2="256" stroke="%s" stroke-width="0.5" stroke-dasharray="3 3"/>' % INK3)
d.append('  <text x="%d" y="360" text-anchor="middle" font-size="7.0" fill="%s">伫立以泣</text>' % (PX, RED))

for (x, t) in [(120, "壹"), (350, "贰"), (600, "叁")]:
    d.append('  <text x="%d" y="132" font-size="7.6" fill="%s">%s</text>' % (x, RED, t))
d.append('  <text x="44" y="466" font-size="7.8" fill="%s">壹 燕　剪尾叉尾，羽翅差池</text>' % INK2)
d.append('  <text x="264" y="466" font-size="7.8" fill="%s">贰 旷野　远送于野，路向南方</text>' % INK2)
d.append('  <text x="486" y="466" font-size="7.8" fill="%s">叁 伫立　久立不忍去</text>' % INK2)
d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">瞻望弗及，泣涕如雨</text>' % INK)
d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">送别之祖，情在「不及」</text>' % INK3)
d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj028a</text>' % INK3)
d.append('</svg>')
svg_a = "\n".join(d)
open(os.path.join(FIG, "sj028a-yan-yu-yu-fei.svg"), "w", encoding="utf-8").write(svg_a)
bounds_ok(svg_a, "028a")

# 图二
e = []
e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="Noto Serif SC,Songti SC,serif">' % (W, H, W, H))
e.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
e.append('  <rect x="10" y="10" width="740" height="500" fill="none" stroke="%s" stroke-width="1"/>' % INK3)
e.append('  <rect x="16" y="16" width="728" height="488" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
e.append('  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="%s" font-weight="700">送 · 望 · 泣</text>' % INK)
e.append('  <text x="380" y="74" text-anchor="middle" font-size="9.6" letter-spacing="2" fill="%s">《诗经》邶风 · 第三篇　燕燕</text>' % INK2)
e.append('  <defs><marker id="ar28" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % RED)
cells = [(70, "送", "远送于野", "地愈送愈远", INK2), (290, "望", "瞻望弗及", "望不见其人", RED), (510, "泣", "泣涕如雨", "情愈深愈痛", INK2)]
for (x, big, s1, s2, col) in cells:
    e.append('  <rect x="%d" y="150" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (x, col))
    e.append('  <text x="%d" y="214" text-anchor="middle" font-size="28" letter-spacing="2" fill="%s" font-weight="700">%s</text>' % (x + 75, col, big))
    e.append('  <text x="%d" y="252" text-anchor="middle" font-size="10" fill="#3B352F">%s</text>' % (x + 75, s1))
    e.append('  <text x="%d" y="278" text-anchor="middle" font-size="8" fill="%s">%s</text>' % (x + 75, INK3, s2))
e.append('  <line x1="220" y1="225" x2="288" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar28)"/>' % RED)
e.append('  <line x1="440" y1="225" x2="508" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar28)"/>' % RED)
e.append('  <text x="380" y="330" text-anchor="middle" font-size="8.4" fill="%s">送者立在原地，被送者愈去愈远；情全在「不及」二字</text>' % INK2)
e.append('  <line x1="120" y1="360" x2="640" y2="360" stroke="%s" stroke-width="0.8"/>' % INK3)
e.append('  <text x="230" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">不及</text>' % RED)
e.append('  <text x="230" y="414" text-anchor="middle" font-size="7.4" fill="%s">望不见，才落泪</text>' % INK3)
e.append('  <text x="530" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">伫</text>' % RED)
e.append('  <text x="530" y="414" text-anchor="middle" font-size="7.4" fill="%s">久立不忍去</text>' % INK3)
e.append('  <text x="380" y="446" text-anchor="middle" font-size="7.4" fill="%s">送别之祖：三章重「瞻望弗及」，一章深过一章</text>' % INK3)
e.append('  <text x="120" y="512" font-size="5.6" fill="%s">诗经 · 邶风</text>' % INK2)
e.append('  <text x="640" y="512" text-anchor="end" font-size="5.6" fill="%s">图二 · 送望泣 · sj028b</text>' % INK2)
e.append('</svg>')
svg_b = "\n".join(e)
open(os.path.join(FIG, "sj028b-song-wang-qi.svg"), "w", encoding="utf-8").write(svg_b)
bounds_ok(svg_b, "028b")

import cairosvg
for k in ["sj028a-yan-yu-yu-fei", "sj028b-song-wang-qi"]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok")
