# -*- coding: utf-8 -*-
"""SJ024《何彼襛矣》两图。图一：唐棣·王姬车·肃雝。图二：盛而能敬。"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fig_shelf import *

A = "sj024a-tang-di-tao-li"
B = "sj024b-nong-er-su-yong"


def draw(d):
    # 壹 · 唐棣：主干分枝有节，五瓣花带蕊，叶簇
    path(d, "M128,352 C132,316 140,276 158,232", INK2, 1.6)
    path(d, "M140,300 C128,286 116,282 104,284", INK2, 1.0)
    path(d, "M148,272 C160,260 172,256 184,258", INK2, 1.0)
    circ(d, 138, 300, 1.6, INK3, INK3, 0.0)  # 枝节疤
    blossom(d, 116, 286, 12, INK2)
    blossom(d, 178, 260, 13, INK2)
    blossom(d, 158, 236, 11, INK2)
    path(d, "M124,320 q10,-6 18,0", INK3, 0.6)
    txt(d, 148, 386, "唐棣：花繁之木", RED, 7.0)

    # 贰 · 王姬之车：轮（辐条）＋舆＋衡轭
    wheel(d, 344, 330, 26, INK2)
    wheel(d, 412, 330, 26, INK2)
    rect(d, 330, 278, 100, 30, INK2, "#FCFAF6", 1.0)
    line(d, 330, 278, 312, 262, INK2, 1.0)   # 衡
    line(d, 430, 278, 448, 262, INK2, 1.0)
    path(d, "M312,262 L312,280", INK2, 0.9)  # 轭
    txt(d, 378, 386, "王姬之车", RED, 7.0)

    # 叁 · 肃雝：车衡銮铃 + 执礼者拱立侧影（非锯齿符号）
    line(d, 560, 250, 640, 250, INK2, 1.0)   # 衡
    for bx in (576, 624):
        line(d, bx, 250, bx, 262, INK3, 0.6)
        circ(d, bx, 270, 6, INK2, "#FCFAF6", 0.9)   # 銮铃
        line(d, bx - 3, 270, bx + 3, 270, INK3, 0.4)
    # 执礼者侧身：冠、肩、宽袖、衣裾
    circ(d, 672, 236, 8, INK2, "#FCFAF6", 1.0)
    line(d, 668, 228, 676, 228, INK2, 0.8)   # 冠
    path(d, "M664,246 C656,262 654,300 658,346 L686,346 C690,300 688,262 680,246", INK2, 1.0, "#FCFAF6")
    path(d, "M664,262 C650,270 646,286 650,300", INK2, 0.9)  # 宽袖
    txt(d, 622, 386, "肃雝：敬而能和", RED, 7.0)


name_fig(A, "何彼襛矣", "召南 · 二", "二十四",
         ["壹 唐棣　郁李类繁花", "贰 车　轮辐舆衡之制", "叁 肃雝　銮铃与执礼者"],
         "何彼襛矣，唐棣之華", "车服盛，而能敬和", A, draw)

logic_fig(B, "盛 · 敬 · 匹", "《诗经》召南 · 第十三篇　何彼襛矣", "ar24",
          [(70, "襛", "王姬之车", "车服繁盛", INK2),
           (290, "肃雝", "曷不肃雝", "敬而且和", RED),
           (510, "匹", "维丝伊缗", "夫妇有配", INK2)],
          "盛是给人看的，敬和是内里；盛而能敬，方是王姬之德",
          ("肃雝", "敬且和，非严肃"),
          ("王孙", "平王之孙，齐侯之子，同一人"),
          "襛为繁盛浓艳；唐棣即棠棣，非棠梨", "召南", "盛而能敬")

import cairosvg
for k in [A, B]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok", audit([A, B]))
