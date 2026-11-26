# -*- coding: utf-8 -*-
"""SJ038《简兮》两图。图一：干戚·龠翟·渥赭舞师。图二：登场—武容—思贤。"""
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
d.append('  <text x="380" y="60" text-anchor="middle" font-size="26" letter-spacing="10" fill="%s" font-weight="700">簡 兮</text>' % INK)
d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之三十八</text>' % INK3)
d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)

# 壹 · 干戚：盾形＋戚斧
# 盾（干）
d.append('  <path d="M118,236 C108,252 108,286 122,304 C134,316 152,316 162,304 C176,286 176,252 166,236 C152,228 132,228 118,236 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % INK2)
# 盾面纹
d.append('  <line x1="142" y1="240" x2="142" y2="306" stroke="%s" stroke-width="0.5"/>' % INK3)
d.append('  <path d="M126,268 L158,268" fill="none" stroke="%s" stroke-width="0.5"/>' % INK3)
# 戚（斧）：柄＋刃
d.append('  <line x1="180" y1="240" x2="180" y2="310" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <path d="M180,244 L196,250 L192,262 L180,258 Z" fill="#EFEAD6" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <text x="148" y="372" text-anchor="middle" font-size="7.0" fill="%s">武舞干戚，勇力如虎</text>' % RED)

# 贰 · 龠翟：管乐＋羽柄
# 龠（管）
d.append('  <rect x="356" y="236" width="10" height="76" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
for k in range(4):
    d.append('  <circle cx="361" cy="252" r="1.6" fill="%s"/>' % INK)
    d.append('  <circle cx="361" cy="268" r="1.6" fill="%s"/>' % INK)
# 翟（羽柄）
d.append('  <line x1="396" y1="250" x2="396" y2="312" stroke="%s" stroke-width="1.0"/>' % INK2)
# 羽翮三瓣
d.append('  <path d="M396,250 C386,236 388,224 396,218 C404,224 406,236 396,250 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <path d="M396,250 C390,240 392,232 396,228" fill="none" stroke="%s" stroke-width="0.45"/>' % INK3)
d.append('  <path d="M396,250 C402,240 400,232 396,228" fill="none" stroke="%s" stroke-width="0.45"/>' % INK3)
d.append('  <text x="378" y="372" text-anchor="middle" font-size="7.0" fill="%s">文舞龠翟，左右秉持</text>' % RED)

# 叁 · 渥赭舞师：舞势背影，首服、宽袖、袍裾，赭色块
# 赭色块（容色赤盛）
d.append('  <ellipse cx="622" cy="238" rx="10" ry="11" fill="#E8C9C0" stroke="%s" stroke-width="0.9"/>' % RED)
# 首服
d.append('  <path d="M614,234 C616,226 628,226 630,234" fill="#EFEAD6" stroke="%s" stroke-width="0.8"/>' % INK2)
# 身＋宽袖（舞势：一袖扬起）
d.append('  <path d="M608,252 L636,252" fill="none" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <path d="M606,252 C600,262 602,284 608,302 L614,314 L630,314 L636,302 C640,284 642,262 636,252 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
# 扬袖
d.append('  <path d="M636,258 L654,244" fill="none" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <path d="M650,246 C658,242 662,248 658,252 C654,254 650,252 648,250 Z" fill="#EFEAD6" stroke="%s" stroke-width="0.7"/>' % INK2)
# 垂袖褶
d.append('  <line x1="614" y1="262" x2="614" y2="298" stroke="%s" stroke-width="0.45"/>' % INK3)
d.append('  <line x1="630" y1="262" x2="630" y2="298" stroke="%s" stroke-width="0.45"/>' % INK3)
d.append('  <text x="622" y="372" text-anchor="middle" font-size="7.0" fill="%s">赫如渥赭，公言锡爵</text>' % RED)

for (x, t) in [(120, "壹"), (350, "贰"), (600, "叁")]:
    d.append('  <text x="%d" y="132" font-size="7.6" fill="%s">%s</text>' % (x, RED, t))
d.append('  <text x="44" y="466" font-size="7.8" fill="%s">壹 干戚　盾面戚刃，武舞道具</text>' % INK2)
d.append('  <text x="264" y="466" font-size="7.8" fill="%s">贰 龠翟　管孔羽翮，文舞所持</text>' % INK2)
d.append('  <text x="486" y="466" font-size="7.8" fill="%s">叁 舞师　舞势赭颜，才美不掩</text>' % INK2)
d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">有力如虎，執轡如組</text>' % INK)
d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">全《诗》写身体最猛的一篇</text>' % INK3)
d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj038a</text>' % INK3)
d.append('</svg>')
svg_a = "\n".join(d)
open(os.path.join(FIG, "sj038a-wan-wu-rong.svg"), "w", encoding="utf-8").write(svg_a)
bounds_ok(svg_a, "038a")

# 图二
e = []
e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="Noto Serif SC,Songti SC,serif">' % (W, H, W, H))
e.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
e.append('  <rect x="10" y="10" width="740" height="500" fill="none" stroke="%s" stroke-width="1"/>' % INK3)
e.append('  <rect x="16" y="16" width="728" height="488" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
e.append('  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="%s" font-weight="700">登場 · 武容 · 思賢</text>' % INK)
e.append('  <text x="380" y="74" text-anchor="middle" font-size="9.6" letter-spacing="2" fill="%s">《诗经》邶风 · 第十三篇　简兮</text>' % INK2)
e.append('  <defs><marker id="ar18" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % RED)
cells = [(70, "登場", "日之方中", "在前上处", INK2), (290, "武容", "有力如虎", "执辔如组", RED), (510, "思賢", "西方美人", "惜其屈官", INK2)]
for (x, big, s1, s2, col) in cells:
    e.append('  <rect x="%d" y="150" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (x, col))
    e.append('  <text x="%d" y="214" text-anchor="middle" font-size="28" letter-spacing="2" fill="%s" font-weight="700">%s</text>' % (x + 75, col, big))
    e.append('  <text x="%d" y="252" text-anchor="middle" font-size="10" fill="#3B352F">%s</text>' % (x + 75, s1))
    e.append('  <text x="%d" y="278" text-anchor="middle" font-size="8" fill="%s">%s</text>' % (x + 75, INK3, s2))
e.append('  <line x1="220" y1="225" x2="288" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar18)"/>' % RED)
e.append('  <line x1="440" y1="225" x2="508" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar18)"/>' % RED)
e.append('  <text x="380" y="330" text-anchor="middle" font-size="8.4" fill="%s">勇力如虎，整暇如组；容色赤盛，思其人而惜其屈</text>' % INK2)
e.append('  <line x1="120" y1="360" x2="640" y2="360" stroke="%s" stroke-width="0.8"/>' % INK3)
e.append('  <text x="230" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">組</text>' % RED)
e.append('  <text x="230" y="414" text-anchor="middle" font-size="7.4" fill="%s">丝带，执辔如组</text>' % INK3)
e.append('  <text x="530" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">赭</text>' % RED)
e.append('  <text x="530" y="414" text-anchor="middle" font-size="7.4" fill="%s">赤土，赫如渥赭</text>' % INK3)
e.append('  <text x="380" y="446" text-anchor="middle" font-size="7.4" fill="%s">《邶风·简兮》「有力如虎，执辔如组」「赫如渥赭」</text>' % INK3)
e.append('  <text x="120" y="512" font-size="5.6" fill="%s">诗经 · 邶风</text>' % INK2)
e.append('  <text x="640" y="512" text-anchor="end" font-size="5.6" fill="%s">图二 · 登场武容思贤 · sj038b</text>' % INK2)
e.append('</svg>')
svg_b = "\n".join(e)
open(os.path.join(FIG, "sj038b-you-li-ru-hu.svg"), "w", encoding="utf-8").write(svg_b)
bounds_ok(svg_b, "038b")

import cairosvg
for k in ["sj038a-wan-wu-rong", "sj038b-you-li-ru-hu"]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok")
