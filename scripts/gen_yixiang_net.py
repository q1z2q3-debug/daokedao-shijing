# -*- coding: utf-8 -*-
"""意象之网：风七十篇，18 名物的分卷分布。数据来自 book/SJ0*.md 经文段实测。"""
import os, sys, json, math
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svgbrush import svg_open_xlink, def_group, use, text, hair, INK, INK2, PAPER, RED, GREY

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = json.load(open(os.path.join(ROOT, "assets", "data", "yixiang-freq.json"), encoding="utf-8"))
OUT = os.path.join(ROOT, "assets", "fig", "yixiang-net.svg")
W, H = 900, 700
CX, CY = 450, 356
R_VOL, R_IMG = 122, 216

g = [svg_open_xlink(W, H), '<rect width="%d" height="%d" fill="%s"/>' % (W, H, PAPER)]


g.append(text(44, 46, "意 象 之 网", 22, INK, ls=8, weight=700))
g.append(text(44, 68, "风七十篇 · 十八名物的分卷分布 · 线粗为该卷篇数 · 取自本库经文段实测", 8.2, INK2, ls=0.6))
g.append('<line x1="44" y1="84" x2="856" y2="84" stroke="%s" stroke-width="0.8"/>' % GREY)


# 中心
g.append('<circle cx="%d" cy="%d" r="50" fill="%s" stroke="%s" stroke-width="0.9"/>' % (CX, CY, "#FBFAF6", INK))
g.append(text(CX, CY - 3, "风", 24, INK, anchor='middle', weight=700))
g.append(text(CX, CY + 20, "七十篇", 8.4, GREY, anchor='middle', ls=2))

# 卷节点
VOLS = DATA["vols"]
vol_pos = {}
for j, v in enumerate(VOLS):
    a = math.radians(-90 + j * 60)
    x, y = CX + R_VOL * math.cos(a), CY + R_VOL * math.sin(a)
    vol_pos[v["v"]] = (x, y)
    g.append('<circle cx="%.1f" cy="%.1f" r="23" fill="%s" stroke="%s" stroke-width="0.7"/>' % (x, y, "#FBFAF6", INK2))
    g.append(text(round(x), round(y) - 2, v["v"], 11, INK, anchor='middle'))
    g.append(text(round(x), round(y) + 12, "%d篇" % (v["b"] - v["a"] + 1), 7.2, GREY, anchor='middle'))

# 意象节点与连线
nodes = DATA["nodes"]
n = len(nodes)
img_pos = []
for i, o in enumerate(nodes):
    a = math.radians(-90 + i * (360.0 / n))
    x, y = CX + R_IMG * math.cos(a), CY + R_IMG * math.sin(a)
    img_pos.append((x, y))
    r = 4.2 + o["p"] * 0.85
    col = RED if o["p"] >= 9 else INK
    g.append('<circle cx="%.1f" cy="%.1f" r="%.2f" fill="none" stroke="%s" stroke-width="%s"/>'
             % (x, y, r, col, 0.9 if o["p"] >= 9 else 0.6))
    if o["p"] >= 9:
        g.append('<circle cx="%.1f" cy="%.1f" r="%.2f" fill="%s" opacity="0.10"/>' % (x, y, r, col))
    lx, ly = CX + (R_IMG + 26) * math.cos(a), CY + (R_IMG + 26) * math.sin(a)
    lab = "%s %d" % (o["w"], o["p"])
    g.append(text(round(lx), round(ly) + 3, lab, 9.4 if o["p"] >= 9 else 8.2, col, anchor='middle', ls=0.8))

for i, o in enumerate(nodes):
    x0, y0 = img_pos[i]
    for vol, cnt in o["vol"].items():
        x1, y1 = vol_pos[vol]
        w = 0.5 + cnt * 0.72
        mx, my = (x0 + x1) / 2, (y0 + y1) / 2
        ax, ay = (x1 - x0), (y1 - y0)
        ln = math.hypot(ax, ay) or 1
        bend = 10 + cnt * 2.2
        px, py = mx + (-ay / ln) * bend, my + (ax / ln) * bend
        d = 'M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f' % (x0, y0, px, py, x1, y1)
        col = RED if o["p"] >= 9 else "#6E6459"
        op = 0.85 if cnt >= 3 else (0.6 if cnt == 2 else 0.32)
        g.append('<path d="%s" fill="none" stroke="%s" stroke-width="%.2f" opacity="%.2f"/>' % (d, col, w, op))

# 注
g.append('<line x1="44" y1="612" x2="856" y2="560" stroke="%s" stroke-width="0.8"/>' % GREY)
g.append(text(44, 634, "读法：桑七篇、六在鄘风——《桑中》《定之方中》之地；马十一篇而周南占四，皆行役与迎送", 7.4, INK2, ls=0.4))
g.append(text(856, 664, "数据 assets/data/yixiang-freq.json　·　靶场三 · 意象之网", 6.8, GREY, anchor='end', ls=0.4))
g.append('<text x="44" y="664" font-size="6.8" fill="%s" letter-spacing="0.4">口径：经文段内篇频；篇题同字不计；「马」含叠句重复，故篇频看，次频不作据</text>' % GREY)
g.append('</svg>')
open(OUT, 'w', encoding='utf-8').write('\n'.join(g))

import cairosvg
cairosvg.svg2png(url=OUT, write_to=os.path.join(ROOT, 'dist', 'yixiang-net.png'), output_width=900)
print('ok')
