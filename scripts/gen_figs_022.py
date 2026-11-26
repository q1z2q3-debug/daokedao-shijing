# -*- coding: utf-8 -*-
"""SJ022《江有汜》两图。图一：汜·渚·沱。图二：悔·处·歌。"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fig_shelf import *

A = "sj022a-si-zhu-tuo"
B = "sj022b-hui-chu-ge"


def draw(d):
    # 壹 · 汜：分出又合回
    d.append('  <path d="M104,300 L192,300" stroke="%s" stroke-width="1.2" fill="none"/>' % INK2)
    d.append('  <path d="M116,300 C116,268 172,268 172,300" stroke="%s" stroke-width="0.9" fill="none"/>' % INK2)
    d.append('  <text x="148" y="336" text-anchor="middle" font-size="7.0" fill="%s">汜：决而复入</text>' % RED)
    # 贰 · 渚：水中洲
    d.append('  <path d="M318,306 L438,306" stroke="%s" stroke-width="1.0" fill="none"/>' % INK3)
    d.append('  <path d="M340,300 C348,284 408,284 416,300 C408,312 348,312 340,300 Z" fill="#EFEAD6" stroke="%s" stroke-width="0.9"/>' % INK2)
    for k in range(4):
        x = 352 + k * 16
        d.append('  <line x1="%d" y1="296" x2="%d" y2="286" stroke="%s" stroke-width="0.5"/>' % (x, x, INK3))
    d.append('  <text x="378" y="336" text-anchor="middle" font-size="7.0" fill="%s">渚：水中之洲</text>' % RED)
    # 叁 · 沱：别出不返
    d.append('  <path d="M560,300 L640,300" stroke="%s" stroke-width="1.2" fill="none"/>' % INK2)
    d.append('  <path d="M596,300 C612,284 640,276 676,276" stroke="%s" stroke-width="0.9" fill="none"/>' % INK2)
    d.append('  <text x="622" y="336" text-anchor="middle" font-size="7.0" fill="%s">沱：别出之流</text>' % RED)


name_fig(A, "江有汜", "召南 · 二", "二十二",
         ["壹 汜　决而复入", "贰 渚　水中沙洲", "叁 沱　别出不返"],
         "江有汜，之子归，不我以", "被弃自宽，逐层收回", A, draw)

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
