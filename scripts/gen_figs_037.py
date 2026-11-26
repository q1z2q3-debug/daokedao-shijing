# -*- coding: utf-8 -*-
"""SJ037《旄丘》两图。图一：葛蔓·狐裘·流离之子。图二：呼伯—揣故—不闻。"""
import os, sys, re, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fig_geo import *
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(ROOT, "assets", "fig")
INK, INK2, INK3, RED, PAPER = "#1F1B17", "#5C544A", "#9A9186", "#994433", "#F7F4EE"
W, H = 760, 540

def bounds_ok(svg, tag):
    s = re.sub(r'xmlns="[^"]*"', "", svg)
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
d.append('  <text x="380" y="60" text-anchor="middle" font-size="26" letter-spacing="10" fill="%s" font-weight="700">旄 丘</text>' % INK)
d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之三十七</text>' % INK3)
d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)

# 壹 · 葛蔓：丘坡＋长藤节结＋叶簇卷须
# 丘坡
d.append('  <path d="M104,330 L148,250 L192,330 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % INK3)
# 长藤
d.append('  <path d="M120,326 C132,300 126,278 140,256 C150,240 156,232 158,220" fill="none" stroke="%s" stroke-width="1.0"/>' % INK2)
# 节结
for (nx, ny) in [(128,306), (134,282), (146,260), (154,238)]:
    d.append('  <circle cx="%d" cy="%d" r="2" fill="#FCFAF6" stroke="%s" stroke-width="0.7"/>' % (nx, ny, INK2))
# 叶簇
for (lx, ly, dx) in [(126,296,-1), (142,272,1), (156,246,1)]:
    d.append('  <path d="M%d,%d C%d,%d %d,%d %d,%d Z" fill="#FCFAF6" stroke="%s" stroke-width="0.8"/>' % (lx, ly, lx+dx*10, ly-8, lx+dx*14, ly, lx+dx*8, ly+6, INK2))
# 卷须
d.append('  <path d="M158,220 C168,214 172,222 166,226" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
d.append('  <text x="148" y="372" text-anchor="middle" font-size="7.0" fill="%s">葛节延长，多日不至</text>' % RED)

# 贰 · 狐裘：裘衣轮廓＋毛锋＋领缘
# 裘身
d.append('  <path d="M336,236 L420,236 L430,320 L330,320 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % INK2)
# 领缘
d.append('  <path d="M336,236 L354,252 L402,252 L420,236" fill="none" stroke="%s" stroke-width="0.9"/>' % INK2)
# 毛锋（短竖线，蓬松乱貌）
for k in range(9):
    x = 338 + k * 10
    d.append('  <line x1="%d" y1="262" x2="%d" y2="272" stroke="%s" stroke-width="0.5"/>' % (x, x+2, INK3))
for k in range(9):
    x = 338 + k * 10
    d.append('  <line x1="%d" y1="286" x2="%d" y2="296" stroke="%s" stroke-width="0.5"/>' % (x, x-2, INK3))
# 下摆毛边
d.append('  <path d="M330,320 l6,-6 l6,6 l6,-6 l6,6 l6,-6 l6,6 l6,-6 l6,6 l6,-6 l6,6 l6,-6 l6,6" fill="none" stroke="%s" stroke-width="0.7"/>' % INK2)
d.append('  <text x="378" y="372" text-anchor="middle" font-size="7.0" fill="%s">狐裘蒙戎，蓬松敝乱</text>' % RED)

# 叁 · 流离之子：孤小背影＋风线＋远处空路
# 风线
d.append('  <path d="M586,250 C600,246 612,252 624,248" fill="none" stroke="%s" stroke-width="0.5"/>' % INK3)
d.append('  <path d="M628,272 C642,268 654,274 666,270" fill="none" stroke="%s" stroke-width="0.5"/>' % INK3)
# 孤小之人（背影，首服、肩线、窄袖、袍裾）
d.append('  <circle cx="622" cy="256" r="8" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <path d="M616,252 C618,246 626,246 628,252" fill="#EFEAD6" stroke="%s" stroke-width="0.8"/>' % INK2)
d.append('  <path d="M612,268 L632,268" fill="none" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <path d="M610,268 C606,278 608,296 612,308 L618,314 L626,314 L632,308 C636,296 638,278 632,268 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
# 空路
d.append('  <path d="M596,320 L648,320 L636,300 L608,300 Z" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
d.append('  <text x="622" y="372" text-anchor="middle" font-size="7.0" fill="%s">琐尾流离，漂散之子</text>' % RED)

for (x, t) in [(120, "壹"), (350, "贰"), (600, "叁")]:
    d.append('  <text x="%d" y="132" font-size="7.6" fill="%s">%s</text>' % (x, RED, t))
d.append('  <text x="44" y="466" font-size="7.8" fill="%s">壹 葛蔓　长藤节结，叶簇卷须</text>' % INK2)
d.append('  <text x="264" y="466" font-size="7.8" fill="%s">贰 狐裘　毛锋领缘，蓬松敝乱</text>' % INK2)
d.append('  <text x="486" y="466" font-size="7.8" fill="%s">叁 流离　孤小背影，风落空路</text>' % INK2)
d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">叔兮伯兮，褎如充耳</text>' % INK)
d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">呼者自呼，听者自听</text>' % INK3)
d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj037a</text>' % INK3)
d.append('</svg>')
svg_a = "\n".join(d)
open(os.path.join(FIG, "sj037a-mao-qiu-ge-man.svg"), "w", encoding="utf-8").write(svg_a)
bounds_ok(svg_a, "037a")

# 图二
e = []
e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="Noto Serif SC,Songti SC,serif">' % (W, H, W, H))
e.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
e.append('  <rect x="10" y="10" width="740" height="500" fill="none" stroke="%s" stroke-width="1"/>' % INK3)
e.append('  <rect x="16" y="16" width="728" height="488" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
e.append('  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="%s" font-weight="700">呼伯 · 揣故 · 不聞</text>' % INK)
e.append('  <text x="380" y="74" text-anchor="middle" font-size="9.6" letter-spacing="2" fill="%s">《诗经》邶风 · 第十二篇　旄丘</text>' % INK2)
e.append('  <defs><marker id="ar17" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % RED)
cells = [(70, "呼伯", "叔兮伯兮", "呼而不应", INK2), (290, "揣故", "必有與也", "替彼寻由", RED), (510, "不聞", "褎如充耳", "听而不闻", INK2)]
for (x, big, s1, s2, col) in cells:
    e.append('  <rect x="%d" y="150" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (x, col))
    e.append('  <text x="%d" y="214" text-anchor="middle" font-size="28" letter-spacing="2" fill="%s" font-weight="700">%s</text>' % (x + 75, col, big))
    e.append('  <text x="%d" y="252" text-anchor="middle" font-size="10" fill="#3B352F">%s</text>' % (x + 75, s1))
    e.append('  <text x="%d" y="278" text-anchor="middle" font-size="8" fill="%s">%s</text>' % (x + 75, INK3, s2))
e.append('  <line x1="220" y1="225" x2="288" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar17)"/>' % RED)
e.append('  <line x1="440" y1="225" x2="508" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar17)"/>' % RED)
e.append('  <text x="380" y="330" text-anchor="middle" font-size="8.4" fill="%s">理由找尽，车终不来；责在不言中，礼在称呼里</text>' % INK2)
e.append('  <line x1="120" y1="360" x2="640" y2="360" stroke="%s" stroke-width="0.8"/>' % INK3)
e.append('  <text x="230" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">與</text>' % RED)
e.append('  <text x="230" y="414" text-anchor="middle" font-size="7.4" fill="%s">同盟，必有与也</text>' % INK3)
e.append('  <text x="530" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">同</text>' % RED)
e.append('  <text x="530" y="414" text-anchor="middle" font-size="7.4" fill="%s">同心，靡所与同</text>' % INK3)
e.append('  <text x="380" y="446" text-anchor="middle" font-size="7.4" fill="%s">《邶风·旄丘》「叔兮伯兮，靡所与同」「褎如充耳」</text>' % INK3)
e.append('  <text x="120" y="512" font-size="5.6" fill="%s">诗经 · 邶风</text>' % INK2)
e.append('  <text x="640" y="512" text-anchor="end" font-size="5.6" fill="%s">图二 · 呼伯揣故不闻 · sj037b</text>' % INK2)
e.append('</svg>')
svg_b = "\n".join(e)
open(os.path.join(FIG, "sj037b-hu-er-bu-ying.svg"), "w", encoding="utf-8").write(svg_b)
bounds_ok(svg_b, "037b")

import cairosvg
for k in ["sj037a-mao-qiu-ge-man", "sj037b-hu-er-bu-ying"]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok")
