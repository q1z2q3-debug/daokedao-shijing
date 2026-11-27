# -*- coding: utf-8 -*-
"""045 柏舟 · 图一（名物）· 成套第一张

三格：舟（印拓取形）／两髦（白描写生）／中河（画具水岸）
一路一法，不锁一种：有的格取墨形，有的格走线。判据只有一条——这一格里
什么最容易认、最不容易错。
"""
import os
import sys
import math

import cv2
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import svgbrush as B  # noqa: E402
import figure_db as F  # noqa: E402
from ink_skeleton import skeleton_paths  # noqa: E402
import adapt  # noqa: E402

W, H = 760, 540
PAPER, CIN, GOLD, LIGHT = '#F5F1E8', '#A63D2F', '#B79A63', '#6B6259'
REF = os.path.join(ROOT, 'assets', 'ref', 'ref-zhou.png')


# ---------------- 一 舟：底本取骨 ----------------
def zhou_bone(cx, cy, h=250, min_len=16):
    """不画墨块，只取底本的骨：墨形骨架化后的中线，按同一线重描出。
    得意忘形——要的是腰身收束、双舷有厚、四梁跨舷的那个「意」。"""
    segs, size = skeleton_paths(REF, dilate=2)
    sc = h / size[1]
    out = []
    for seg in segs:
        if sum(math.dist(seg[k], seg[k + 1]) for k in range(len(seg) - 1)) < min_len:
            continue
        pts = [(cx - size[0] * sc / 2 + x * sc, cy - h / 2 + y * sc) for x, y in seg]
        out.append(adapt.stroke(B.stroke, pts, h, kind='hard', depth=0.0))
    return out


# ---------------- 二 两髦：白描写生 ----------------
def liangmao(cx, cy, s=1.0):
    """两髦：几何构建（figure_db）。
    头＝蛋形椭圆；颈＝截取自头下缘的等宽带；肩＝自颈端外斜的切线；
    发＝沿椭圆的等角中分与发缕；两束＝两缘收敛于同一尖点，束根落在椭圆上该 y 处的横坐标外 4px。
    参数一改，形即随之改，不靠手感。
    """
    return F.build_liangmao(cx, cy, scale=s, view='back')


def zhonghe(cx, cy, w=170):
    """中河：只写水，不设岸。三道波，近宽远窄、起伏相间。"""
    out = []
    for i, (hw, amp, yy) in enumerate(((w / 2, 9, cy + 34), (w / 2 - 22, 7, cy + 8), (w / 2 - 44, 5, cy - 18))):
        pts = [(cx - hw + 2 * hw * k / 30,
                yy + amp * math.sin(k / 30 * math.pi * 2.1 + i * 1.1)) for k in range(31)]
        out.append(adapt.stroke(B.stroke, pts, 110 - i * 14, kind='soft',
                                depth=0.50 + i * 0.08))
    # 波间水纹：两段极短细线，示水动
    for a, b in (((cx - 46, cy + 20), (cx - 24, cy + 18)),
                 ((cx + 16, cy + 44), (cx + 40, cy + 42)),
                 ((cx - 12, cy - 6), (cx + 8, cy - 7))):
        out.append(B.hair([a, b], adapt.w_of(70) * 0.52, adapt.tone(0.78)))
    return out


def main():
    g = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 540" width="760" height="540" '
         'font-family="Noto Serif SC,Songti SC,serif">',
         '<defs><radialGradient id="lg" cx="50%" cy="44%" r="72%">'
         '<stop offset="0%" stop-color="#FFFBF1" stop-opacity="0.30"/>'
         '<stop offset="62%" stop-color="#FFFBF1" stop-opacity="0.05"/>'
         '<stop offset="100%" stop-color="#D9CFB8" stop-opacity="0.22"/>'
         '</radialGradient>'
         '<filter id="edge" x="-10%" y="-10%" width="120%" height="120%">'
         '<feTurbulence type="fractalNoise" baseFrequency="0.062" numOctaves="3" seed="7" result="n"/>'
         '<feDisplacementMap in="SourceGraphic" in2="n" scale="2.4" xChannelSelector="R" yChannelSelector="G"/>'
         '<feGaussianBlur stdDeviation="0.16"/></filter>'
         '<mask id="speck"><rect width="760" height="540" fill="white"/>'
         '<rect width="760" height="540" fill="black" filter="url(#mott)"/></mask>'
         '<filter id="mott" x="0" y="0" width="100%" height="100%">'
         '<feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="4" seed="5" result="t"/>'
         '<feColorMatrix in="t" type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0.9 0.6 0.3 0 -0.22"/>'
         '</filter>'
         '<pattern id="fibre" width="62" height="62" patternUnits="userSpaceOnUse">'
         '<path d="M6,14 L19,9" stroke="#E6DED1" stroke-width="0.26"/>'
         '<path d="M31,37 L47,31" stroke="#EBE4D8" stroke-width="0.24"/>'
         '<path d="M12,52 L22,56" stroke="#E9E2D5" stroke-width="0.22"/></pattern>'
         '</defs>',
         '<rect width="760" height="540" fill="%s"/>' % PAPER,
         '<rect width="760" height="540" fill="url(#fibre)" opacity="0.34"/>',
         '<rect width="760" height="540" fill="url(#lg)"/>']

    # 一 舟（骨线）与舟下之波
    g += zhou_bone(152, 256, h=208)
    for i, (yy, hw, amp) in enumerate(((376, 58, 4), (390, 40, 3))):
        pts = [(148 - hw + 2 * hw * k / 22,
                yy + amp * math.sin(k / 22 * math.pi * 2.2 + i * 1.3)) for k in range(23)]
        g.append(adapt.stroke(B.stroke, pts, 96, kind='soft', depth=0.60))

    # 二 两髦 / 三 中河
    F.MUL = 0.66
    g += liangmao(378, 244, 1.1)
    g += zhonghe(622, 262, 190)

    # 页眉
    g.append(B.text(56, 58, '鄘 风 · 四', 8.6, CIN, ls=2))
    g.append(B.text(380, 62, '柏 舟', 26, B.INK, anchor='middle', ls=10, weight=500))
    g.append(B.text(704, 58, '诗三百五篇 · 之四五', 8.2, LIGHT, anchor='end', ls=1.5))
    g.append('<line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.35" opacity="0.6"/>' % GOLD)
    g.append('<line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.35" opacity="0.6"/>' % GOLD)

    # 三格编号
    for x, num, name in ((148, '一', '舟'), (378, '二', '两髦'), (622, '三', '河')):
        g.append(B.text(x - 26, 130, num, 8.6, CIN, ls=1))
        g.append(B.text(x - 8, 130, name, 9.2, B.INK2, ls=3))

    # 注文三条
    g.append(B.text(44, 466, '一叶柏舟，双舷有厚', 7.8, LIGHT, ls=1))
    g.append(B.text(264, 466, '垂发少年，中分两束', 7.8, LIGHT, ls=1))
    g.append(B.text(486, 466, '中河，舟所行处', 7.8, LIGHT, ls=1))

    # 引句
    g.append(B.text(380, 514, '汎彼柏舟，在彼中河', 16, B.INK, anchor='middle', ls=3))
    g.append(B.text(704, 526, '图一 · 名物 · sj045a', 7.4, LIGHT, anchor='end'))
    g.append('</svg>')

    svg = ''.join(g)
    p = os.path.join(ROOT, 'assets', 'fig', 'sj045a-bo-zhou.svg')
    open(p, 'w', encoding='utf-8').write(svg)
    print('svg', B.count_bytes(svg), 'B')
    import cairosvg
    png = os.path.join(ROOT, 'dist', 'sj045a.png')
    cairosvg.svg2png(url=p, write_to=png, output_width=1200, background_color=PAPER)
    print('png', png)


if __name__ == '__main__':
    main()
