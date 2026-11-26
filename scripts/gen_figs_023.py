# -*- coding: utf-8 -*-
"""SJ023《野有死麕》两图。图一：麕·白茅·帨犬。图二：野礼·如玉。"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fig_shelf import *

A = "sj023a-jun-mao-shui"
B = "sj023b-ye-li-hun-yue"


def draw(d):
    # 壹 · 麕：无角小獐，短尾、后腿长，侧视朝右
    ell(d, 140, 300, 30, 13, INK2, "#FCFAF6", 1.0)
    line(d, 130, 312, 126, 352, INK2, 0.9)   # 前腿
    line(d, 138, 312, 138, 352, INK2, 0.9)
    line(d, 154, 312, 160, 352, INK2, 0.9)   # 后腿较长
    line(d, 162, 312, 168, 352, INK2, 0.9)
    line(d, 112, 296, 104, 286, INK2, 0.9)    # 短尾
    path(d, "M164,294 L176,284", INK2, 1.0)   # 颈
    circ(d, 178, 280, 8, INK2, "#FCFAF6", 1.0)
    path(d, "M174,274 L170,264 L178,270 Z", INK2, 0.8, "#FCFAF6")  # 耳
    circ(d, 180, 278, 1.3, INK, "#1F1B17", 0.0)
    txt(d, 148, 386, "麕：无角小獐", RED, 7.0)

    # 贰 · 白茅：叶束带根，束绳一道
    for (x, lean) in [(354, -10), (366, -4), (378, 0), (390, 4), (402, 10)]:
        path(d, "M%g,330 C%g,308 %g,278 %g,256" % (x, x + lean, x + lean, x + lean * 1.3), INK2, 0.9)
    line(d, 350, 330, 406, 330, RED, 0.8)
    for x in (362, 378, 394):
        line(d, x, 330, x - 3, 350, INK3, 0.5)  # 根
    txt(d, 378, 386, "白茅：束物取洁", RED, 7.0)

    # 叁 · 帨（佩巾：系带 + 垂角）与尨（犬：耳、尾、爪）
    line(d, 576, 250, 576, 270, INK3, 0.7)
    path(d, "M568,270 L584,270 L580,302 L572,302 Z", INK2, 1.0, "#FCFAF6")
    line(d, 572, 302, 570, 312, INK3, 0.5)
    line(d, 580, 302, 582, 312, INK3, 0.5)
    txt(d, 576, 330, "帨", RED, 7.0)
    # 犬
    ell(d, 636, 300, 20, 10, INK2, "#FCFAF6", 1.0)
    for lx in (622, 632, 646, 654):
        line(d, lx, 308, lx, 330, INK2, 0.9)
    line(d, 656, 296, 664, 286, INK2, 0.9)   # 尾上卷
    circ(d, 658, 296, 7, INK2, "#FCFAF6", 1.0)
    path(d, "M656,290 L654,282 L660,287 Z", INK2, 0.8, "#FCFAF6")  # 耳
    circ(d, 660, 295, 1.2, INK, "#1F1B17", 0.0)
    txt(d, 636, 352, "尨：多毛犬", RED, 7.0)


name_fig(A, "野有死麕", "召南 · 二", "二十三",
         ["壹 麕　小獐，非麋", "贰 白茅　包束之洁", "叁 帨尨　佩巾与犬"],
         "野有死麕，白茅包之", "婚媾之礼见于野", A, draw)

logic_fig(B, "野礼 · 如玉", "《诗经》召南 · 第十二篇　野有死麕", "ar23",
          [(70, "怀春", "有女怀春", "当春动心", INK2),
           (290, "引导", "吉士诱之", "通「道」，以礼相导", RED),
           (510, "如玉", "有女如玉", "洁白温润", INK2)],
          "事可以成，步必须缓；礼在男女相接的分寸里",
          ("诱", "通道／导，非诱骗"),
          ("脱脱", "舒缓安重之貌"),
          "末章三句是女子之辞：慢些、轻些、别惊动犬吠", "召南", "野礼如玉")

import cairosvg
for k in [A, B]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok", audit([A, B]))
