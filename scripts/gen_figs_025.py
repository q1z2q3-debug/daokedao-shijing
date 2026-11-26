# -*- coding: utf-8 -*-
"""SJ025《驺虞》两图。图一：葭蓬·弓矢·特写。图二：壹发·仁节。"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fig_shelf import *

A = "sj025a-jia-peng-ba-zong"
B = "sj025b-yi-fa-ren-zhi"


def draw(d):
    # 壹 · 葭：芦苇，叶鞘裹茎、穗下垂
    for (x, h, lean) in [(126, 110, -6), (148, 146, 0), (170, 100, 6)]:
        reed(d, x, 360, h, lean)
        # 叶鞘
        path(d, "M%g,%g q6,4 12,0" % (x - 6, 360 - h * 0.35), INK3, 0.5)
    line(d, 104, 360, 192, 360, INK3, 0.7)
    txt(d, 148, 386, "葭：水旁芦苇", RED, 7.0)

    # 贰 · 壹发：弓与矢，一发而中（非放射线）
    path(d, "M330,240 C306,280 306,320 330,360", INK2, 1.6)   # 弓
    line(d, 330, 240, 330, 360, INK3, 0.6)                      # 弦
    line(d, 330, 300, 430, 300, INK2, 1.0)                      # 矢
    line(d, 330, 300, 338, 294, INK2, 0.7)
    line(d, 330, 300, 338, 306, INK2, 0.7)
    path(d, "M430,300 L420,295 L420,305 Z", INK2, 0.8, INK2)   # 镞
    # 中于蓬把
    circ(d, 448, 300, 12, INK3, "#EFEAD6", 0.8)
    for k in range(5):
        line(d, 448, 300, 448 + 12 * math.cos(math.tau * k / 5), 300 + 12 * math.sin(math.tau * k / 5), INK3, 0.4)
    txt(d, 378, 386, "壹发：一发而中", RED, 7.0)

    # 叁 · 驺虞：蹄、耳、斑 三处特写（不画整兽）
    ell(d, 586, 316, 10, 7, INK2, "#FCFAF6", 0.9)
    ell(d, 606, 316, 10, 7, INK2, "#FCFAF6", 0.9)
    path(d, "M634,300 L624,320 L644,320 Z", INK2, 0.9, "#FCFAF6")  # 耳
    for (x, y) in [(662, 306), (674, 314), (658, 322), (676, 324), (666, 330)]:
        circ(d, x, y, 2.0, INK2, INK2, 0.0)                          # 斑
    txt(d, 622, 352, "蹄 · 耳 · 斑 三处特写", RED, 7.0)


name_fig(A, "驺 虞", "召南 · 二", "二十五",
         ["壹 葭　春时水生", "贰 弓矢　一发而中", "叁 豝豵　特写不画整兽"],
         "彼茁者葭，壹發五豝", "仁在节制，不在多杀", A, draw)

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
