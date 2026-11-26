# -*- coding: utf-8 -*-
"""SJ024《何彼襛矣》两图。图一：唐棣·桃李·丝缗。图二：盛而能敬。"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fig_shelf import *

A = "sj024a-tang-di-tao-li"
B = "sj024b-nong-er-su-yong"


def blossom(d, cx, cy, r, col):
    for k in range(5):
        a = math.tau * k / 5 - math.pi / 2
        x = cx + r * math.cos(a)
        y = cy + r * math.sin(a)
        d.append('  <circle cx="%.1f" cy="%.1f" r="%.1f" fill="#FCFAF6" stroke="%s" stroke-width="0.8"/>' % (x, y, r * 0.62, col))
    d.append('  <circle cx="%d" cy="%d" r="%.1f" fill="%s"/>' % (cx, cy, r * 0.4, col))


def draw(d):
    # 壹 · 唐棣：花簇
    blossom(d, 148, 300, 16, INK2)
    d.append('  <text x="148" y="356" text-anchor="middle" font-size="7.0" fill="%s">唐棣：花繁之木</text>' % RED)
    # 贰 · 桃李：一枝两花
    d.append('  <path d="M340,336 L416,286" stroke="%s" stroke-width="1.1" fill="none"/>' % INK2)
    blossom(d, 356, 318, 11, INK2)
    blossom(d, 404, 296, 11, INK2)
    d.append('  <text x="378" y="356" text-anchor="middle" font-size="7.0" fill="%s">华如桃李</text>' % RED)
    # 叁 · 丝缗：合股之绳
    for off in (0, 6):
        pts = []
        for i in range(7):
            x = 588 + i * 11
            y = 300 + off + (8 if i % 2 == 0 else -8)
            pts.append((x, y))
        dline = "M" + " L".join("%.1f,%.1f" % p for p in pts)
        d.append('  <path d="%s" fill="none" stroke="%s" stroke-width="0.9"/>' % (dline, INK2))
    d.append('  <text x="622" y="356" text-anchor="middle" font-size="7.0" fill="%s">丝缗：合丝成绳</text>' % RED)


name_fig(A, "何彼襛矣", "召南 · 二", "二十四",
         ["壹 唐棣　郁李类繁花", "贰 桃李　颜色之盛", "叁 丝缗　夫妇相配之喻"],
         "何彼襛矣，唐棣之华", "车服盛，而能敬和", A, draw)

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
