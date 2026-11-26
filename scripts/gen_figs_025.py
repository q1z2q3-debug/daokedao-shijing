# -*- coding: utf-8 -*-
"""SJ025《驺虞》两图。图一：葭蓬·豝豵特写。图二：壹发·仁节。"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fig_shelf import *

A = "sj025a-jia-peng-ba-zong"
B = "sj025b-yi-fa-ren-zhi"


def draw(d):
    # 壹 · 葭（芦苇，水旁）
    d.append('  <path d="M104,360 L192,360" stroke="%s" stroke-width="0.9" fill="none"/>' % INK3)
    for (x, h) in [(124, 120), (146, 148), (168, 110)]:
        d.append('  <line x1="%d" y1="360" x2="%d" y2="%d" stroke="%s" stroke-width="1.0"/>' % (x, x, 360 - h, INK2))
        d.append('  <path d="M%d,%d C%d,%d %d,%d %d,%d" fill="none" stroke="%s" stroke-width="0.7"/>' %
                 (x, 360 - h + 20, x - 14, 360 - h + 10, x - 16, 360 - h - 6, x - 10, 360 - h - 14, INK3))
    d.append('  <text x="148" y="384" text-anchor="middle" font-size="7.0" fill="%s">葭：水旁芦苇</text>' % RED)
    # 贰 · 蓬（旱地丛草）
    for k in range(9):
        a = -math.pi / 2 + (k - 4) * 0.28
        x0, y0 = 378, 360
        x1 = x0 + 30 * math.cos(a)
        y1 = y0 + 30 * math.sin(a)
        d.append('  <line x1="%d" y1="%d" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="0.8"/>' % (x0, y0, x1, y1, INK2))
    d.append('  <text x="378" y="384" text-anchor="middle" font-size="7.0" fill="%s">蓬：旱地蒿丛</text>' % RED)
    # 叁 · 豕三处特写：蹄、耳、斑纹（不画整兽）
    d.append('  <ellipse cx="592" cy="330" rx="9" ry="6" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % INK2)
    d.append('  <ellipse cx="610" cy="330" rx="9" ry="6" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % INK2)
    d.append('  <path d="M636,312 L628,330 L644,330 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % INK2)
    for (x, y) in [(660, 324), (670, 332), (656, 336), (672, 318)]:
        d.append('  <circle cx="%d" cy="%d" r="1.8" fill="%s"/>' % (x, y, INK2))
    d.append('  <text x="622" y="364" text-anchor="middle" font-size="7.0" fill="%s">蹄 · 耳 · 斑 三处特写</text>' % RED)


name_fig(A, "驺 虞", "召南 · 二", "二十五",
         ["壹 葭　春时水生", "贰 蓬　旱地草盛", "叁 豝豵　特写不画整兽"],
         "彼茁者葭，壹发五豝", "仁在节制，不在多杀", A, draw)

logic_fig(B, "壹发 · 仁节", "《诗经》召南 · 第十四篇　驺虞", "ar25",
          [(70, "茁", "彼茁者葭蓬", "草木方盛于春", INK2),
           (290, "壹发", "壹发五豝", "一发而中，不乱发", RED),
           (510, "仁", "于嗟乎驺虞", "取之以节，不贪", INK2)],
          "仁不在射中什么，在不乱发、不贪取；蒐田以时",
          ("驺虞", "虞人 / 仁兽，两说并列"),
          ("豝豵", "豝牝豕，豵幼豕"),
          "草木方茁，禽兽方蕃；猎以其时、取以有节", "召南", "壹发仁节")

import cairosvg
for k in [A, B]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok", audit([A, B]))
