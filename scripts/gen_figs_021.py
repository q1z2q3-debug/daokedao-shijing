# -*- coding: utf-8 -*-
"""SJ021《小星》两图。图一：小星·参昴·衾裯。图二：宵征·命分。"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fig_shelf import *

A = "sj021a-xiao-xing-can-mao"
B = "sj021b-ye-xing-zi-chu"


def draw(d):
    # 壹 · 稀疏小星
    for (x, y, r) in [(120, 210, 2.2), (150, 250, 1.6), (132, 300, 1.8), (168, 232, 1.4), (156, 330, 1.6)]:
        d.append('  <circle cx="%d" cy="%d" r="%.1f" fill="%s"/>' % (x, y, r, INK2))
    d.append('  <text x="148" y="372" text-anchor="middle" font-size="7.0" fill="%s">嘒，微光</text>' % RED)
    # 贰 · 参（三星斜列）与昴（一簇）
    for (x, y) in [(350, 224), (368, 250), (386, 276)]:
        d.append('  <circle cx="%d" cy="%d" r="2.4" fill="%s"/>' % (x, y, INK))
    d.append('  <line x1="350" y1="224" x2="386" y2="276" stroke="%s" stroke-width="0.5"/>' % INK3)
    for (x, y) in [(402, 226), (414, 236), (404, 246), (416, 250), (398, 258), (410, 262)]:
        d.append('  <circle cx="%d" cy="%d" r="1.5" fill="%s"/>' % (x, y, INK2))
    d.append('  <text x="350" y="214" font-size="7.0" fill="%s">参</text>' % RED)
    d.append('  <text x="402" y="214" font-size="7.0" fill="%s">昴</text>' % RED)
    # 叁 · 衾（被）与裯（帐）
    d.append('  <rect x="588" y="286" width="44" height="26" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % INK2)
    d.append('  <line x1="588" y1="299" x2="632" y2="299" stroke="%s" stroke-width="0.5"/>' % INK3)
    d.append('  <path d="M650,250 L650,312 L684,312 L684,250" fill="none" stroke="%s" stroke-width="0.9"/>' % INK2)
    d.append('  <path d="M650,250 Q667,236 684,250" fill="none" stroke="%s" stroke-width="0.9"/>' % INK2)
    d.append('  <text x="588" y="330" font-size="7.0" fill="%s">衾（被）</text>' % RED)
    d.append('  <text x="650" y="330" font-size="7.0" fill="%s">裯（帐）</text>' % RED)


name_fig(A, "小 星", "召南 · 二", "二十一",
         ["壹 小星　微光，三三五五", "贰 参昴　西方两宿", "叁 衾裯　被与床帐"],
         "嘒彼小星，三五在东", "夜行者，怨在命不在人", A, draw)

logic_fig(B, "宵征 · 命分", "《诗经》召南 · 第十篇　小星", "ar21",
          [(70, "宵征", "肃肃宵征", "夙夜在公", INK2),
           (290, "命同", "寔命不同", "怨在命，不在人", RED),
           (510, "不犹", "寔命不犹", "其分不如人", INK2)],
          "夜行自处：不谤上位，不妒同辈，把差距归于命",
          ("寔", "同「实」，即「是」"),
          ("不犹", "犹，若也；不如"),
          "嘒为微小之光，非明亮；肃肃为疾行整齐，非严肃", "召南", "宵征命分")

import cairosvg
for k in [A, B]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok", audit([A, B]))
