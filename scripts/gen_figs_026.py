# -*- coding: utf-8 -*-
"""SJ026《柏舟》两图。图一：柏舟·鉴·石席。图二：匪石匪席。"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fig_shelf import *

A = "sj026a-bai-zhou-jian"
B = "sj026b-fei-shi-fei-xi"


def draw(d):
    # 壹 · 柏舟：一叶孤舟，不系缆
    d.append('  <path d="M112,320 L184,320 L172,344 L124,344 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % INK2)
    d.append('  <line x1="148" y1="320" x2="148" y2="282" stroke="%s" stroke-width="1.0"/>' % INK2)
    d.append('  <path d="M148,282 L176,316" fill="none" stroke="%s" stroke-width="0.8"/>' % INK3)
    d.append('  <path d="M108,356 C124,350 140,362 156,356 C172,350 188,362 200,356" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
    d.append('  <text x="148" y="384" text-anchor="middle" font-size="7.0" fill="%s">汎流之舟，无所系泊</text>' % RED)
    # 贰 · 鉴：铜镜
    d.append('  <circle cx="378" cy="312" r="26" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % INK2)
    d.append('  <circle cx="378" cy="312" r="20" fill="none" stroke="%s" stroke-width="0.5"/>' % INK3)
    d.append('  <line x1="378" y1="338" x2="378" y2="356" stroke="%s" stroke-width="1.1"/>' % INK2)
    d.append('  <text x="378" y="384" text-anchor="middle" font-size="7.0" fill="%s">鉴：镜可纳众形</text>' % RED)
    # 叁 · 石与席
    d.append('  <path d="M576,336 C576,322 596,318 606,326 C616,334 608,346 592,346 C580,346 576,344 576,336 Z" fill="#EFEAD6" stroke="%s" stroke-width="0.9"/>' % INK2)
    d.append('  <rect x="624" y="318" width="56" height="30" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % INK2)
    for gx in (638, 652, 666):
        d.append('  <line x1="%d" y1="318" x2="%d" y2="348" stroke="%s" stroke-width="0.4"/>' % (gx, gx, INK3))
    d.append('  <line x1="624" y1="328" x2="680" y2="328" stroke="%s" stroke-width="0.4"/>' % INK3)
    d.append('  <text x="592" y="364" text-anchor="middle" font-size="7.0" fill="%s">石（平置）</text>' % RED)
    d.append('  <text x="652" y="364" text-anchor="middle" font-size="7.0" fill="%s">席（舒展）</text>' % RED)


name_fig(A, "柏 舟", "邶风 · 三", "二十六",
         ["壹 柏舟　浮流无泊", "贰 鉴　铜镜可纳", "叁 石席　不可转卷"],
         "汎彼柏舟，亦汎其流", "邶风开卷：忧之不可转", A, draw)

logic_fig(B, "匪石 · 匪席", "《诗经》邶风 · 第一篇　柏舟", "ar26",
          [(70, "汎流", "耿耿不寐", "如有隐忧", INK2),
           (290, "匪石", "不可转也", "心非石，不可转", RED),
           (510, "匪席", "不可卷也", "心非席，不可卷", INK2)],
          "忧之深而志不可转：石可转，席可卷，心则不然",
          ("鉴", "镜可纳，心不可茹"),
          ("选", "通「巽」，屈退；不可选"),
          "威仪棣棣，不可屈退；静言思之，不能奋飞", "邶风", "匪石匪席")

import cairosvg
for k in [A, B]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok", audit([A, B]))
