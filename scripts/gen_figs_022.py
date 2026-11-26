# -*- coding: utf-8 -*-
"""SJ022《江有汜》两图。图一：汜·渚·沱。图二：悔·处·歌。"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fig_shelf import *

A = "sj022a-si-zhu-tuo"
B = "sj022b-hui-chu-ge"


def banks(d, x0, x1, yu, yl, col=INK3):
    line(d, x0, yu, x1, yu, INK2, 1.0)
    line(d, x0, yl, x1, yl, INK2, 1.0)
    for x in range(x0 + 8, x1 - 4, 16):
        line(d, x, yu, x - 5, yu - 8, col, 0.5)
        line(d, x, yl, x - 5, yl + 8, col, 0.5)


def draw(d):
    # 壹 · 汜：分出一支，绕回再合入
    banks(d, 76, 220, 248, 352)
    path(d, "M108,300 C108,268 184,268 184,300", INK2, 1.0)
    path(d, "M108,300 C108,332 184,332 184,300", INK2, 1.0)
    path(d, "M120,300 C140,292 164,292 176,300", INK3, 0.5)
    txt(d, 148, 386, "汜：决而复入", RED, 7.0)

    # 贰 · 渚：洲上三茎芦苇，水线环洲
    path(d, "M312,308 C320,286 436,286 444,308 C436,326 320,326 312,308 Z", INK2, 1.0, "#EFEAD6")
    for x in (344, 378, 412):
        reed(d, x, 300, 78, (x - 378) * 0.12)
    for y in (336, 348):
        path(d, "M316,%g C336,%g 356,%g 376,%g C396,%g 416,%g 436,%g" % (y, y - 5, y + 5, y - 5, y + 5, y - 5, y), INK3, 0.5)
    txt(d, 378, 386, "渚：水中之洲", RED, 7.0)

    # 叁 · 沱：别出之流，岸线转折，不返
    line(d, 548, 262, 700, 262, INK2, 1.0)
    path(d, "M548,300 C590,300 620,318 650,344 C666,358 684,362 700,362", INK2, 1.0)
    path(d, "M548,300 C584,304 600,316 616,332", INK3, 0.6)
    for x in (560, 588):
        line(d, x, 262, x - 5, 254, INK3, 0.5)
    txt(d, 622, 386, "沱：别出之流", RED, 7.0)


name_fig(A, "江有汜", "召南 · 二", "二十二",
         ["壹 汜　决而复入", "贰 渚　水中沙洲", "叁 沱　别出不返"],
         "江有汜，之子歸，不我以", "被弃自宽，逐层收回", A, draw)

logic_fig(B, "悔 · 处 · 歌", "《诗经》召南 · 第十一篇　江有汜", "ar22",
          [(70, "悔", "其后也悔", "望对方回心", INK2),
           (290, "处", "其后也处", "把自己安住", RED),
           (510, "歌", "其啸也歌", "蹙口成声自遣", INK2)],
          "自宽三级：望其悔 → 求自处 → 化为歌",
          ("汜", "决而复入，分支再合"),
          ("啸", "蹙口出声，非长啸"),
          "水有分流终复于江；人虽暂弃，情系未绝", "召南", "悔处歌")

import cairosvg
for k in [A, B]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok", audit([A, B]))
