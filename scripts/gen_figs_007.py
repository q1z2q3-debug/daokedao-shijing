# -*- coding: utf-8 -*-
"""SJ007《兔罝》两图。图一：网与桩（网脚留空）。图二：由外及内。"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(ROOT, "assets", "fig")
INK, INK2, INK3, RED, PAPER = "#1F1B17", "#5C544A", "#9A9186", "#994433", "#F7F4EE"
W, H = 760, 540

d = []
d.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="\'Noto Serif SC\',\'Songti SC\',serif">' % (W, H, W, H))
d.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
d.append('  <text x="44" y="58" font-size="8.6" letter-spacing="2" fill="%s">周南 · 七</text>' % RED)
d.append('  <text x="380" y="60" text-anchor="middle" font-size="28" letter-spacing="14" fill="%s" font-weight="700">兔 罝</text>' % INK)
d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之七</text>' % INK3)
d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)

# 地
d.append('  <path d="M206,414 C290,418 470,419 596,414" fill="none" stroke="%s" stroke-width="0.3" stroke-dasharray="8 5 1.5 5"/>' % INK3)

# 网（宽扁，剪裁网目）
d.append('  <defs><clipPath id="net7"><rect x="240" y="280" width="320" height="112"/></clipPath></defs>')
d.append('  <rect x="240" y="280" width="320" height="112" fill="#FAF6EA" stroke="none"/>')
d.append('  <g clip-path="url(#net7)">')
for k in range(-24, 26):
    x = 240 + k * 18
    d.append('  <path d="M%d,280 L%d,392" stroke="%s" stroke-width="0.32"/>' % (x, x + 112, INK3))
    d.append('  <path d="M%d,280 L%d,392" stroke="%s" stroke-width="0.32"/>' % (x, x - 112, INK3))
d.append('  </g>')
d.append('  <path d="M240,280 L560,280" stroke="%s" stroke-width="1.3"/>' % INK2)
d.append('  <path d="M240,392 L560,392" stroke="%s" stroke-width="1.3"/>' % INK2)
d.append('  <path d="M240,280 L240,392" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <path d="M560,280 L560,392" stroke="%s" stroke-width="0.9"/>' % INK2)

# 桩
d.append('  <path d="M238,406 L240,238" stroke="%s" stroke-width="4.4"/>' % INK)
d.append('  <path d="M243,404 L245,240" stroke="%s" stroke-width="0.7"/>' % INK3)
d.append('  <path d="M558,408 L560,250" stroke="%s" stroke-width="4.0"/>' % INK)
d.append('  <path d="M563,406 L565,252" stroke="%s" stroke-width="0.7"/>' % INK3)
d.append('  <path d="M228,240 L252,237" stroke="%s" stroke-width="1.8"/>' % INK2)
d.append('  <path d="M548,252 L572,249" stroke="%s" stroke-width="1.8"/>' % INK2)
d.append('  <path d="M238,406 L224,416 M242,408 L256,417" stroke="%s" stroke-width="1.3"/>' % INK2)
d.append('  <path d="M558,408 L544,418 M562,410 L576,419" stroke="%s" stroke-width="1.3"/>' % INK2)
for y in (262, 292, 322, 352, 386):
    d.append('  <path d="M%d,%d l5,-3" stroke="%s" stroke-width="0.24"/>' % (237, y, INK3))
    d.append('  <path d="M%d,%d l5,-3" stroke="%s" stroke-width="0.24"/>' % (557, y + 6, INK3))

# 网脚与地之间的空隙（强调）
d.append('  <path d="M240,392 L240,414" stroke="%s" stroke-width="0.6" stroke-dasharray="2 3"/>' % RED)
d.append('  <path d="M560,392 L560,414" stroke="%s" stroke-width="0.6" stroke-dasharray="2 3"/>' % RED)
d.append('  <path d="M256,404 L544,404" stroke="%s" stroke-width="0.4" stroke-dasharray="3 5"/>' % INK3)
d.append('  <text x="240" y="428" font-size="7.4" fill="%s">网脚离地一寸——留空，兔才肯钻</text>' % RED)

# 草
for (x, y, dx, h) in [(196, 414, 6, 30), (206, 416, -5, 22), (216, 415, 9, 26),
                      (598, 414, -6, 30), (608, 416, 5, 22), (618, 415, -9, 26),
                      (392, 422, 7, 30), (450, 422, -7, 26)]:
    d.append('  <path d="M%d,%d C%.1f,%d %.1f,%d %d,%d" fill="none" stroke="%s" stroke-width="1.0"/>'
             % (x, y, x + dx * 0.35, y - h * 0.45, x + dx * 0.75, y - h * 0.8, x + dx, y - h, INK2))

d.append('  <text x="330" y="268" font-size="7.6" fill="%s">①</text>' % RED)
d.append('  <text x="210" y="330" font-size="7.6" fill="%s">②</text>' % RED)
d.append('  <text x="566" y="380" font-size="7.6" fill="%s">③</text>' % RED)

d.append('  <text x="44" y="466" font-size="7.8" fill="%s">① 兔罝　捕兔之网，目密曰肃肃</text>' % INK2)
d.append('  <text x="286" y="466" font-size="7.8" fill="%s">② 椓之丁丁　钉桩，声从桩出</text>' % INK2)
d.append('  <text x="526" y="466" font-size="7.8" fill="%s">③ 中逵／中林　布网之地</text>' % INK2)
d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">肅肅兔罝，椓之丁丁</text>' % INK)
d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">网之整，与人之武对举</text>' % INK3)
d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj007a</text>' % INK3)
d.append('</svg>')
open(os.path.join(FIG, "sj007a-tu-wang-mu-zhuang.svg"), "w", encoding="utf-8").write("\n".join(d))

# ============ 图二 ============
e = []
e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="\'Noto Serif SC\',\'Songti SC\',serif">' % (W, H, W, H))
e.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
e.append('  <rect x="10" y="10" width="740" height="500" fill="none" stroke="%s" stroke-width="1"/>' % INK3)
e.append('  <rect x="16" y="16" width="728" height="488" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
e.append('  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="%s" font-weight="700">由 外 及 內</text>' % INK)
e.append('  <text x="380" y="74" text-anchor="middle" font-size="9.6" letter-spacing="2" fill="%s">《诗经》周南 · 第七篇　兔罝</text>' % INK2)
e.append('  <defs><marker id="ar7" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % RED)
cells = [(70, "干城", "盾与城", "御外", INK2), (290, "好仇", "仇，匹也", "相匹", RED), (510, "腹心", "心腹", "内信", INK2)]
for (x, big, s1, s2, col) in cells:
    e.append('  <rect x="%d" y="150" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (x, col))
    e.append('  <text x="%d" y="214" text-anchor="middle" font-size="23" letter-spacing="2" fill="%s" font-weight="700">%s</text>' % (x + 75, col, big))
    e.append('  <text x="%d" y="254" text-anchor="middle" font-size="10" fill="#3B352F">%s</text>' % (x + 75, s1))
    e.append('  <text x="%d" y="278" text-anchor="middle" font-size="8" fill="%s">%s</text>' % (x + 75, INK3, s2))
e.append('  <line x1="220" y1="225" x2="288" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar7)"/>' % RED)
e.append('  <line x1="440" y1="225" x2="508" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar7)"/>' % RED)
e.append('  <text x="380" y="330" text-anchor="middle" font-size="8.4" fill="%s">用一个人，三道关：能不能挡、能不能配、能不能托</text>' % INK2)
e.append('  <line x1="120" y1="360" x2="640" y2="360" stroke="%s" stroke-width="0.8"/>' % INK3)
e.append('  <text x="230" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">中逵</text>' % RED)
e.append('  <text x="230" y="414" text-anchor="middle" font-size="7.4" fill="%s">九达之衢：布网在人所共见处</text>' % INK3)
e.append('  <text x="530" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">中林</text>' % RED)
e.append('  <text x="530" y="414" text-anchor="middle" font-size="7.4" fill="%s">深林无人：可托处，正在无人处</text>' % INK3)
e.append('  <text x="380" y="446" text-anchor="middle" font-size="7.4" fill="%s">《诗》三章　·　地愈深，位愈近</text>' % INK3)
e.append('  <text x="120" y="512" font-size="5.6" fill="%s">诗经 · 周南</text>' % INK2)
e.append('  <text x="640" y="512" text-anchor="end" font-size="5.6" fill="%s">图二 · 由外及内 · sj007b</text>' % INK2)
e.append('</svg>')
open(os.path.join(FIG, "sj007b-you-wai-ji-nei.svg"), "w", encoding="utf-8").write("\n".join(e))

import cairosvg
for k in ["sj007a-tu-wang-mu-zhuang", "sj007b-you-wai-ji-nei"]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok")
