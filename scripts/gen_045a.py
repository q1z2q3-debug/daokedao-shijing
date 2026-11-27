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

W, H = 760, 540
PAPER, CIN, GOLD, LIGHT = '#F5F1E8', '#A63D2F', '#B79A63', '#6B6259'
REF = os.path.join(ROOT, 'assets', 'ref', 'ref-zhou.png')


# ---------------- 一 舟：印拓取形 ----------------
def zhou_ink(box_x, box_y, box_w, box_h):
    img = cv2.imread(REF, cv2.IMREAD_GRAYSCALE)
    h, w = img.shape
    cy, cx = int(h * 0.075), int(w * 0.075)
    img = img[cy:h - cy, cx:w - cx]
    m = (img < 70).astype(np.uint8) * 255
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((2, 2), np.uint8))
    cnts, _ = cv2.findContours(m, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    polys = [c for c in cnts if cv2.contourArea(c) >= 16]
    allp = np.vstack(polys).reshape(-1, 2)
    x0, y0 = allp.min(0)
    x1, y1 = allp.max(0)
    pw, ph = x1 - x0, y1 - y0
    s = min(box_w / pw, box_h / ph)
    ox = box_x - (x0 + pw / 2) * s + (box_w / 2) - box_w / 2
    oy = box_y - (y0 + ph / 2) * s + (box_h / 2) - box_h / 2
    segs = []
    for c in polys:
        ap = cv2.approxPolyDP(c, 1.4, True).reshape(-1, 2)
        if len(ap) < 3:
            continue
        segs.append('M' + ' L'.join('%.1f,%.1f' % (ox + px * s, oy + py * s) for px, py in ap) + ' Z')
    return ' '.join(segs)


# ---------------- 二 两髦：白描写生 ----------------
def liangmao(cx, cy, s=1.0):
    """发式图解：不画头。额线一道、中分一道、两束各系一结而垂。"""
    out = []

    def P(p):
        return [(cx + x * s, cy + y * s) for x, y in p]

    # 额线：自左鬓拱过额顶至右鬓
    arc = []
    for k in range(25):
        t = math.pi * k / 24
        arc.append((cx - 74 * math.cos(t) * s, cy - 34 * s + 30 * math.sin(t) * s))
    out.append(B.stroke(arc, 0.85, 0.8, n=50))

    # 中分：自额线顶点下行
    out.append(B.stroke(P([(0, -34), (0, -8), (0, 8)]), 0.55, n=20, col=B.INK2))

    # 两束：束根贴鬓，往下垂；内外双线夹束，末端收尖
    for sx in (-1, 1):
        outer = P([(sx * 68, -12), (sx * 73, 22), (sx * 74, 50), (sx * 70, 68), (sx * 68, 78)])
        inner = P([(sx * 50, -16), (sx * 55, 20), (sx * 56, 48), (sx * 52, 66), (sx * 50, 76)])
        out.append(B.stroke(outer, 0.82, 0.3, n=44, taper_end=0.55))
        out.append(B.stroke(inner, 0.62, 0.22, n=42, taper_end=0.55, col=B.INK2))
        # 束结：两道短横跨在束根
        for yy in (-6, 2):
            out.append(B.hair(P([(sx * 50, yy), (sx * 70, yy)]), 0.34, B.INK2))
        # 束内两道发缕
        out.append(B.hair(P([(sx * 68, 8), (sx * 64, 44), (sx * 56, 68)]), 0.24, B.GREY))
        out.append(B.hair(P([(sx * 60, 12), (sx * 58, 44)]), 0.22, B.GREY))
    return out


def zhonghe(cx, cy, w=170):
    """中河：只写水，不设岸。三道波，近宽远窄、起伏相间。"""
    out = []
    for i, (hw, amp, yy) in enumerate(((w / 2, 9, cy + 34), (w / 2 - 22, 7, cy + 8), (w / 2 - 44, 5, cy - 18))):
        pts = [(cx - hw + 2 * hw * k / 30,
                yy + amp * math.sin(k / 30 * math.pi * 2.1 + i * 1.1)) for k in range(31)]
        out.append(B.stroke(pts, 0.72 if i == 0 else 0.52, 0.3, n=64,
                            col=B.INK if i == 0 else B.INK2))
    # 波间水纹：两段极短细线，示水动
    out.append(B.hair([(cx - 46, cy + 20), (cx - 24, cy + 18)], 0.22, B.GREY))
    out.append(B.hair([(cx + 16, cy + 44), (cx + 40, cy + 42)], 0.22, B.GREY))
    out.append(B.hair([(cx - 12, cy - 6), (cx + 8, cy - 7)], 0.22, B.GREY))
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

    # 一 舟（墨形）
    d = zhou_ink(148, 272, 196, 300)
    g.append('<g mask="url(#speck)" filter="url(#edge)" fill="#1C1917" fill-rule="evenodd" opacity="0.94">'
             '<path d="%s"/></g>' % d)

    # 二 两髦 / 三 中河
    g += liangmao(378, 262, 1.0)
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
    g.append(B.text(44, 466, '斜俯视取墨形；双舷有厚', 7.8, LIGHT, ls=1))
    g.append(B.text(264, 466, '髧彼两髦：中分，束根系结，两束垂', 7.8, LIGHT, ls=1))
    g.append(B.text(486, 466, '中河：舟所行处，波未起', 7.8, LIGHT, ls=1))

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
