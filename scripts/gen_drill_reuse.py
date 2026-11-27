# -*- coding: utf-8 -*-
"""靶场二：复用与镜像。同一件器物，两种写法：逐条独立 path vs defs+use。"""
import os, sys, math
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svgbrush import (svg_open_xlink, def_group, use, feather_module, hair_module,
                      stroke, hair, text, count_bytes, INK, INK2, PAPER, RED, GREY)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "fig", "drill-reuse.svg")
W, H = 1140, 640
g = [svg_open_xlink(W, H), '<rect width="%d" height="%d" fill="%s"/>' % (W, H, PAPER)]

# ---------- defs ----------
feather = feather_module("fw", length=70, width=21, w=0.62, ribs=2)
tuft = hair_module("hair", length=128, bend=7, w=0.5)
g.append('<defs>%s%s</defs>' % (feather, tuft))

g.append(text(44, 46, "复 用 与 镜 像", 22, INK, ls=8, weight=700))
g.append(text(44, 66, "一片母羽、一条母缕；笔画只定义一次，其余靠 transform 复制", 8.4, INK2, ls=1))
g.append('<line x1="44" y1="84" x2="1096" y2="84" stroke="%s" stroke-width="0.8"/>' % GREY)

# ---------- 左：羽毛串（母片 + 镜像 + 逐层缩）----------
g.append(text(44, 136, "叁 干旌　析羽：母片一次，镜像与缩放各六", 7.8, RED, ls=0.4))
cx, top = 186, 410
g.append('<path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="1.4"/>' % (cx - 1.6, 196, cx - 1.6, 516, INK))
g.append('<path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="1.4"/>' % (cx + 1.6, 196, cx + 1.6, 516, INK))
for k in range(4):
    sc = 1.0 - k * 0.05
    yy = top - k * 62
    g.append(use("fw", tx=cx + 2, ty=yy, rot=-8, sx=sc, sy=sc))
    g.append(use("fw", tx=cx - 3, ty=yy - 4, rot=9, sx=-sc, sy=sc))

# ---------- 中：旄尾（母缕 + 旋转扇形）----------
g.append(text(374, 136, "壹 干旄　旄尾：母缕一次，扇形排布十八", 7.8, RED, ls=0.4))
cx2 = 516
g.append('<path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="1.4"/>' % (cx2 - 1.6, 196, cx2 - 1.6, 516, INK))
g.append('<path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="1.4"/>' % (cx2 + 1.6, 196, cx2 + 1.6, 516, INK))
for i in range(18):
    a = -22 + i * 2.6
    sy = 0.84 + (i % 5) * 0.055
    g.append(use("hair", tx=cx2, ty=214, rot=a, sx=1.0, sy=sy))

# ---------- 右：旗帜（对称 + 帘状旒）----------
g.append(text(700, 136, "贰 干旟　旗面：中轴对折，旒以母条复制", 7.8, RED, ls=0.4))
cx3 = 846
g.append('<path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="1.4"/>' % (cx3 - 1.6, 196, cx3 - 1.6, 516, INK))
g.append('<path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="1.4"/>' % (cx3 + 1.6, 196, cx3 + 1.6, 516, INK))
g.append('<path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="2.6"/>' % (cx3 - 56, 236, cx3 + 56, 236, INK))
# 旗面：只画左半，镜像得右半
half = [(cx3, 240), (cx3 - 50, 240), (cx3 - 50, 344), (cx3, 344)]
g.append(stroke(half, 1.0, n=40))
g.append('<g transform="scale(-1,1)"><g transform="translate(%.1f,0)">' % (-2 * cx3))
g.append(stroke(half, 1.0, n=40))
g.append('</g></g>')
# 旒：母条复制 7 次
for i in range(7):
    x = cx3 - 45 + i * 15.0
    ln = 56 + (i % 3) * 12
    g.append(stroke([(x, 344), (x + (1 if i % 2 else -1) * 2.6, 344 + ln * 0.6),
                     (x + (1 if i % 2 else -1) * 3.6, 344 + ln)], 0.85, n=22, col=INK2))

# 页脚数据：同形两种写法的体积
def independent_feathers():
    out = []
    for k in range(6):
        sc = 1.0 - k * 0.075
        for sign in (1, -1):
            ts = np.linspace(0, 1, 15)
            left, right = [], []
            for t in ts:
                wd = 17 * (max(0.0, math.sin(math.pi * (0.06 + t * 0.9))) ** 0.5) * 0.5 * sc
                left.append((sign * -wd, -80 * sc * t))
                right.append((sign * wd, -80 * sc * t))
            out.append(stroke(left, 0.62, n=20))
            out.append(stroke(right, 0.62, n=20))
    return ''.join(out)


def independent_hairs():
    out = []
    for i in range(18):
        a = math.radians(-17 + i * 2.0)
        sy = 0.82 + (i % 5) * 0.05
        pts = [(7 * (t ** 2), 128 * t) for t in np.linspace(0, 1, 12)]
        c, sn = math.cos(a), math.sin(a)
        out.append(stroke([(x * c - (y * sy) * sn + 516, x * sn + (y * sy) * c + 186) for x, y in pts], 0.5, n=16))
    return ''.join(out)


ind = count_bytes(independent_feathers()) + count_bytes(independent_hairs())
reuse = (count_bytes(feather) + count_bytes(tuft)
         + count_bytes(''.join(use('fw', tx=0, ty=0, rot=0, sx=1, sy=1) for _ in range(12)))
         + count_bytes(''.join(use('hair', tx=0, ty=0, rot=0, sx=1, sy=1) for _ in range(18))))
ratio = int(ind / max(1, reuse) * 10) / 10

g.append('<line x1="44" y1="556" x2="1096" y2="556" stroke="%s" stroke-width="0.8"/>' % GREY)
g.append(text(44, 578, "靶场二 · 复用与镜像　｜　独立 path %d B → defs+use %d B，压缩 %.1fx" % (ind, reuse, ratio), 7.4, GREY, ls=0.6))
g.append(text(1096, 578, "润泽说 道可道之诗经 · 图法", 7.4, GREY, anchor='end', ls=1))
g.append('</svg>')
open(OUT, 'w', encoding='utf-8').write('\n'.join(g))

import cairosvg
cairosvg.svg2png(url=OUT, write_to=os.path.join(ROOT, 'dist', 'drill-reuse.png'), output_width=1140)
print('independent=%d reuse=%d ratio=%.1f file=%d' % (ind, reuse, ratio, os.path.getsize(OUT)))
