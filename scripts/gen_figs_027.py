# -*- coding: utf-8 -*-
"""SJ027《绿衣》两图。图一：绿衣·黄里·絺绤。图二：见衣思人。"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fig_shelf import *

A = "sj027a-lv-yi-huang-li"
B = "sj027b-jian-yi-si-ren"


def draw(d):
    # 壹 · 绿衣：交领右衽、宽袖、缘边
    path(d, "M124,220 L172,220 L188,248 L178,270 L172,352 L124,352 L118,270 L108,248 Z", INK2, 1.1, "#FCFAF6")
    path(d, "M124,220 L148,252 L172,220", INK2, 0.9)       # 交领
    path(d, "M148,252 L148,352", INK3, 0.6)                  # 中缝
    path(d, "M108,248 C96,262 94,284 104,296", INK2, 0.9)   # 左宽袖
    path(d, "M188,248 C200,262 202,284 192,296", INK2, 0.9) # 右宽袖
    path(d, "M124,352 L172,352", RED, 0.8)                   # 缘边
    txt(d, 148, 386, "绿外黄里，色失常度", RED, 7.0)

    # 贰 · 黄里：里襟翻转露里；裳幅褶裥
    path(d, "M352,224 L404,224 L410,286 L346,286 Z", INK2, 1.1, "#FCFAF6")
    path(d, "M380,224 L368,286 L352,286", INK3, 0.8, "#EFEAD6")  # 翻露之里
    path(d, "M346,286 L410,286 L416,350 L340,350 Z", INK2, 1.1, "#EFEAD6")  # 裳
    for px in (356, 372, 388, 404):
        line(d, px, 290, px - 3, 348, INK3, 0.5)             # 褶裥
    txt(d, 378, 386, "绿上黄裳，上下易位", RED, 7.0)

    # 叁 · 絺（密）绤（疏）：葛布编织纹
    rect(d, 572, 264, 44, 60, INK2, "#FCFAF6", 0.9)
    for gx in range(578, 614, 4):
        line(d, gx, 264, gx, 324, INK3, 0.4)
    for gy in range(270, 324, 6):
        line(d, 572, gy, 616, gy, INK3, 0.4)
    rect(d, 632, 264, 44, 60, INK2, "#FCFAF6", 0.9)
    for gx in range(640, 672, 9):
        line(d, gx, 264, gx, 324, INK3, 0.4)
    for gy in range(274, 324, 10):
        line(d, 632, gy, 676, gy, INK3, 0.4)
    txt(d, 594, 344, "絺（密）", RED, 7.0)
    txt(d, 654, 344, "绤（疏）", RED, 7.0)


name_fig(A, "绿 衣", "邶风 · 三", "二十七",
         ["壹 衣里　间色外，正色内", "贰 衣裳　上衣下裳倒置", "叁 絺绤　粗细葛布"],
         "綠兮衣兮，綠衣黃里", "见衣而思人，一针一缕", A, draw)

logic_fig(B, "见衣 · 思人", "《诗经》邶风 · 第二篇　绿衣", "ar27",
          [(70, "倒置", "绿衣黄里裳", "间色居外上", INK2),
           (290, "所治", "女所治兮", "追想制衣之人", RED),
           (510, "获心", "实获我心", "所思远，心已相合", INK2)],
          "由衣及人，由色及心；衣在，人不在",
          ("古人", "通「故」，故人，非古时人"),
          ("訧", "过失；俾无訧，使我无过"),
          "绿为间色，黄为正色；凄其以风，思之不已", "邶风", "见衣思人")

import cairosvg
for k in [A, B]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok", audit([A, B]))
