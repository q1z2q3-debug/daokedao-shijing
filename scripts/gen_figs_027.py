# -*- coding: utf-8 -*-
"""SJ027《绿衣》两图。图一：绿衣·黄里·絺绤。图二：见衣思人。"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fig_shelf import *

A = "sj027a-lv-yi-huang-li"
B = "sj027b-jian-yi-si-ren"


def garment(d, cx, top, bottom, inner):
    # 衣形：肩、袖、身
    d.append('  <path d="M%d,%d L%d,%d L%d,%d L%d,%d Z" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' %
             (cx - 26, top, cx + 26, top, cx + 20, bottom, cx - 20, bottom, INK2))
    if inner:
        d.append('  <path d="M%d,%d L%d,%d L%d,%d L%d,%d Z" fill="#EFEAD6" stroke="%s" stroke-width="0.7"/>' %
                 (cx - 16, top + 8, cx + 16, top + 8, cx + 12, bottom - 6, cx - 12, bottom - 6, INK3))


def draw(d):
    # 壹 · 绿衣黄里
    garment(d, 148, 280, 352, True)
    d.append('  <text x="148" y="384" text-anchor="middle" font-size="7.0" fill="%s">绿外黄里，色失常度</text>' % RED)
    # 贰 · 绿衣黄裳
    d.append('  <rect x="356" y="278" width="44" height="26" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % INK2)
    d.append('  <path d="M352,304 L404,304 L410,350 L346,350 Z" fill="#EFEAD6" stroke="%s" stroke-width="1.1"/>' % INK2)
    d.append('  <text x="378" y="384" text-anchor="middle" font-size="7.0" fill="%s">绿上黄裳，上下易位</text>' % RED)
    # 叁 · 絺（密）绤（疏）
    d.append('  <rect x="576" y="286" width="44" height="56" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % INK2)
    for gx in range(582, 618, 5):
        d.append('  <line x1="%d" y1="286" x2="%d" y2="342" stroke="%s" stroke-width="0.4"/>' % (gx, gx, INK3))
    d.append('  <rect x="632" y="286" width="44" height="56" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % INK2)
    for gx in range(640, 672, 10):
        d.append('  <line x1="%d" y1="286" x2="%d" y2="342" stroke="%s" stroke-width="0.4"/>' % (gx, gx, INK3))
    d.append('  <text x="598" y="360" text-anchor="middle" font-size="7.0" fill="%s">絺（密）</text>' % RED)
    d.append('  <text x="654" y="360" text-anchor="middle" font-size="7.0" fill="%s">绤（疏）</text>' % RED)


name_fig(A, "绿 衣", "邶风 · 三", "二十七",
         ["壹 衣里　间色外，正色内", "贰 衣裳　上衣下裳倒置", "叁 絺绤　粗细葛布"],
         "绿兮衣兮，绿衣黄里", "见衣而思人，一针一缕", A, draw)

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
