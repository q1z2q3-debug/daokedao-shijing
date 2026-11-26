# -*- coding: utf-8 -*-
"""SJ023《野有死麕》两图。图一：麕·白茅·帨犬。图二：野礼·如玉。"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fig_shelf import *

A = "sj023a-jun-mao-shui"
B = "sj023b-ye-li-hun-yue"


def draw(d):
    # 壹 · 麕（小獐，侧视朝右）
    d.append('  <ellipse cx="146" cy="332" rx="30" ry="12" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
    d.append('  <circle cx="176" cy="316" r="8" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
    d.append('  <path d="M172,310 L168,300 L176,306 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.8"/>' % INK2)
    for lx in (126, 138, 156, 168):
        d.append('  <line x1="%d" y1="340" x2="%d" y2="358" stroke="%s" stroke-width="0.9"/>' % (lx, lx, INK2))
    d.append('  <line x1="116" y1="328" x2="106" y2="322" stroke="%s" stroke-width="0.8"/>' % INK2)
    d.append('  <text x="148" y="384" text-anchor="middle" font-size="7.0" fill="%s">麕：无角小獐</text>' % RED)
    # 贰 · 白茅
    for (x, lean) in [(362, -8), (378, 0), (394, 8)]:
        d.append('  <path d="M%d,372 C%d,340 %d,312 %d,292" fill="none" stroke="%s" stroke-width="0.9"/>' % (x, x + lean, x + lean, x + lean * 1.4, INK2))
    d.append('  <line x1="356" y1="344" x2="400" y2="344" stroke="%s" stroke-width="0.8"/>' % RED)
    d.append('  <text x="378" y="384" text-anchor="middle" font-size="7.0" fill="%s">白茅：束物取洁</text>' % RED)
    # 叁 · 帨（佩巾）与尨（犬）
    d.append('  <line x1="596" y1="300" x2="596" y2="320" stroke="%s" stroke-width="0.7"/>' % INK3)
    d.append('  <path d="M588,320 L604,320 L600,344 L592,344 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % INK2)
    d.append('  <ellipse cx="652" cy="350" rx="18" ry="8" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
    d.append('  <circle cx="670" cy="342" r="6" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
    d.append('  <path d="M668,338 L666,330 L672,335 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.7"/>' % INK2)
    d.append('  <line x1="634" y1="348" x2="626" y2="340" stroke="%s" stroke-width="0.8"/>' % INK2)
    d.append('  <text x="596" y="364" text-anchor="middle" font-size="7.0" fill="%s">帨</text>' % RED)
    d.append('  <text x="652" y="378" text-anchor="middle" font-size="7.0" fill="%s">尨：多毛犬</text>' % RED)


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
