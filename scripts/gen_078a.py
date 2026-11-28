# -*- coding: utf-8 -*-
"""078 大叔于田 · 图一（名物/场景）

一章十句：乘马、执辔、两骖、薮、火、暴虎、献公、戒。
不画马，画四辔与车轮；不画搏虎的人，画公所门外的虎皮。
「执辔如组」是诗眼，「献于公所」是结果。
"""
import math
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import svgbrush as B  # noqa: E402

W, H = 760, 540
PAPER = '#F5F1E8'
RED = '#A63D2F'
GOLD = '#B79A63'
LG = '#6B6259'


def wheel(cx, cy, r):
    out = []
    out.append(B.oval(cx, cy, r, r, 0.62, B.INK, n=48))
    out.append(B.oval(cx, cy, r - 3.4, r - 3.4, 0.28, B.GREY, n=40))
    for k in range(12):
        a = k * math.pi / 6
        out.append(B.hair([(cx + 4 * math.cos(a), cy + 4 * math.sin(a)),
                           (cx + (r - 4) * math.cos(a), cy + (r - 4) * math.sin(a))],
                          0.24, B.INK2))
    out.append(B.oval(cx, cy, 4.6, 4.6, 0.4, B.INK, n=16))
    return out


def rein_bank(x, y):
    """四辔：一结四线，四镳环。"""
    out = []
    # 结
    out.append(B.oval(x, y, 5.2, 3.4, 0.5, B.INK, n=18))
    out.append(B.hair([(x - 5, y), (x + 5, y)], 0.3, B.GREY))
    out.append(B.hair([(x - 3, y - 4), (x + 3, y + 4)], 0.24, B.GREY))
    out.append(B.hair([(x + 3, y - 4), (x - 3, y + 4)], 0.24, B.GREY))
    # 四线：两服在内，两骖在外
    ends = ((x - 26, y + 66), (x - 9, y + 76), (x + 9, y + 76), (x + 26, y + 66))
    for i, (ex, ey) in enumerate(ends):
        mx = x + (ex - x) * 0.45 + (-5 if i % 2 == 0 else 5)
        my = y + (ey - y) * 0.5
        out.append(B.stroke([(x, y + 3), (mx, my), (ex, ey - 4)],
                            0.26, 0.16, n=16, col=B.INK2, taper_end=0.2))
        out.append(B.oval(ex, ey, 3.8, 3.8, 0.4, B.INK, n=14))
        out.append(B.hair([(ex - 2, ey - 2), (ex + 2, ey + 2)], 0.22, B.GREY))
    return out


def reed(x, base, h, seed=False):
    out = []
    out.append(B.stroke([(x, base), (x + 1.5, base - h)], 0.36, 0.2, n=14,
                        col=B.INK2, taper_end=0.5))
    for k in range(3):
        y = base - h * (0.32 + k * 0.2)
        out.append(B.stroke([(x + 1, y), (x + 12 - k * 2, y - 10 + k * 2)],
                            0.22, 0.12, n=8, col=B.GREY, taper_end=0.6))
    if seed:
        out.append(B.oval(x + 1.5, base - h - 5, 2.6, 7.0, 0.3, B.INK2, n=12))
    return out


def torch(x, base, h):
    out = []
    out.append(B.stroke([(x, base), (x + 1, base - h)], 0.34, 0.2, n=10,
                        col=B.INK2, taper_end=0.4))
    # 火焰：三瓣，朱砂只作勾
    out.append(B.stroke([(x, base - h), (x - 7, base - h - 12), (x - 2, base - h - 20),
                         (x + 1, base - h - 11), (x + 4, base - h - 22),
                         (x + 8, base - h - 12), (x, base - h)],
                        0.34, 0.18, n=24, col=RED, taper_end=0.3))
    out.append(B.hair([(x - 3, base - h - 10), (x - 1, base - h - 3)], 0.2, RED))
    return out


def gate(x0, x1, base, top):
    out = []
    out.append(B.stroke([(x0, base), (x0, top), (x1, top), (x1, base)],
                        0.62, 0.32, n=24, col=B.INK, taper_end=0.12))
    # 屋檐
    out.append(B.stroke([(x0 - 14, top), (x0 + 18, top - 16), (x1 - 18, top - 16),
                         (x1 + 14, top)], 0.55, 0.3, n=20, col=B.INK, taper_end=0.2))
    for x in range(x0 - 4, x1 + 4, 12):
        out.append(B.hair([(x, top - 8), (x + 5, top + 1)], 0.26, B.GREY))
    # 门内两扇
    out.append(B.stroke([(x0 + 10, base), (x0 + 10, top + 22)], 0.3, 0.16, n=8, col=B.GREY))
    out.append(B.stroke([(x1 - 10, base), (x1 - 10, top + 22)], 0.3, 0.16, n=8, col=B.GREY))
    # 门柱础
    out.append(B.stroke([(x0, base), (x0 - 4, base + 4)], 0.3, 0.18, n=6, col=B.GREY))
    out.append(B.stroke([(x1, base), (x1 + 4, base + 4)], 0.3, 0.18, n=6, col=B.GREY))
    return out


def tiger_pelt(x, y, s=1.0):
    """虎皮：一张挂着的皮，不画虎身。"""
    out = []
    # 挂杆
    out.append(B.stroke([(x - 4, y - 58), (x + 4, y - 58)], 0.28, 0.16, n=8, col=B.GREY))
    out.append(B.stroke([(x, y - 58), (x - 12, y - 30)], 0.22, 0.12, n=8, col=B.GREY))
    out.append(B.stroke([(x, y - 58), (x + 12, y - 30)], 0.22, 0.12, n=8, col=B.GREY))
    pts = [(x - 26, y - 24), (x - 32, y - 2), (x - 22, y + 22), (x - 4, y + 30),
           (x + 16, y + 26), (x + 30, y + 6), (x + 26, y - 18), (x + 8, y - 28)]
    out.append(B.stroke_closed(pts, 0.5, B.INK, n=120, pad=6))
    # 四足残端
    out.append(B.stroke([(x - 22, y + 22), (x - 28, y + 34)], 0.28, 0.14, n=8, col=B.GREY))
    out.append(B.stroke([(x + 16, y + 26), (x + 22, y + 36)], 0.28, 0.14, n=8, col=B.GREY))
    # 尾
    out.append(B.stroke([(x + 30, y + 6), (x + 42, y + 16), (x + 46, y + 30)],
                        0.3, 0.16, n=12, col=B.INK2, taper_end=0.4))
    # 虎斑
    for k in range(4):
        yy = y - 14 + k * 10
        out.append(B.hair([(x - 18 + k * 2, yy), (x - 2 + k * 2, yy + 4)], 0.28, B.INK2))
        out.append(B.hair([(x + 4 + k * 2, yy), (x + 18 + k * 2, yy + 3)], 0.28, B.INK2))
    # 眼窝两笔，示头
    out.append(B.oval(x - 8, y - 18, 3.0, 2.2, 0.24, B.GREY, n=12))
    out.append(B.oval(x + 6, y - 18, 3.0, 2.2, 0.24, B.GREY, n=12))
    return out


def main():
    g = [B.svg_open(W, H), B.grid_check((W, H))]
    g.append('<rect x="10" y="16" width="740" height="508" fill="none" stroke="%s" stroke-width="1.0"/>' % B.GREY)
    g.append('<rect x="22" y="28" width="716" height="484" fill="none" stroke="%s" stroke-width="0.8"/>' % '#DCD5C8')
    # 页眉
    g.append(B.text(44, 58, '郑 风 · 之四', 8.6, RED, ls=2))
    g.append(B.text(380, 62, '大叔于田　火烈', 24, B.INK, anchor='middle', ls=8, weight=500))
    g.append(B.text(704, 58, '诗三百五篇 · 之七八', 8.2, LG, anchor='end', ls=1.5))
    g.append('<line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.35"/>' % GOLD)

    base = 404
    # 地面
    g.append(B.hair([(54, base), (704, base)], 0.5, B.GREY))
    for k in range(14):
        x = 70 + k * 45
        g.append(B.hair([(x, base + 4), (x + 10, base + 4 + (k % 3) * 2)], 0.22, B.GREY))

    # 左：车轮与四辔
    g += wheel(92, 350, 27)
    g.append(B.stroke([(62, 330), (62, 370)], 0.3, 0.18, n=8, col=B.GREY))
    g.append(B.stroke([(122, 330), (122, 370)], 0.3, 0.18, n=8, col=B.GREY))
    g.append(B.hair([(62, 330), (122, 330)], 0.26, B.GREY))
    g.append(B.hair([(62, 370), (122, 370)], 0.26, B.GREY))
    g += rein_bank(176, 296)
    g.append(B.text(176, 280, '四辔', 8.4, B.INK2, anchor='middle', ls=1))
    g.append(B.text(150, 388, '骖', 7.4, LG, anchor='middle'))
    g.append(B.text(168, 396, '服', 7.4, LG, anchor='middle'))
    g.append(B.text(186, 396, '服', 7.4, LG, anchor='middle'))
    g.append(B.text(204, 388, '骖', 7.4, LG, anchor='middle'))
    g.append(B.text(92, 424, '乘：一乘四马', 7.4, LG, anchor='middle'))
    g.append(B.text(176, 424, '执辔如组', 7.4, LG, anchor='middle'))

    # 中：薮与火
    for x, h in ((252, 86), (272, 106), (292, 78), (312, 98), (334, 90),
                 (356, 108), (378, 84), (400, 96), (422, 80), (444, 100)):
        g += reed(x, base, h, seed=(x % 3 == 0))
    for x in (270, 306, 342, 378, 414):
        g += torch(x, base, 92 + (x % 7) * 2)
    # 火线
    for x in range(250, 450, 12):
        g.append(B.hair([(x, base - 3), (x + 6, base - 10 - (x % 4) * 2)], 0.22, RED))
    g.append(B.text(250, 300, '薮', 11, B.INK, anchor='middle', ls=2))
    g.append(B.text(250, 314, '泽，禽之府', 7.2, LG, anchor='middle'))
    g.append(B.text(350, 438, '火烈具举', 7.6, B.INK2, anchor='middle'))
    g.append(B.text(350, 452, '列人持火', 7.0, LG, anchor='middle'))

    # 右：公所与虎皮
    g += gate(548, 700, base, 316)
    g.append(B.text(624, 296, '公所', 9.0, B.INK, anchor='middle', ls=2))
    g += tiger_pelt(620, 342, 1.0)
    g.append(B.text(620, 424, '虎皮：暴虎', 7.4, B.INK2, anchor='middle'))
    g.append(B.text(620, 438, '献于公所', 7.6, B.INK2, anchor='middle'))
    # 献：虎皮向门
    g.append(B.stroke([(662, 350), (690, 330)], 0.26, 0.14, n=8, col=RED, taper_end=0.4))
    g.append(B.stroke([(690, 330), (684, 336)], 0.22, 0.12, n=6, col=RED))
    g.append(B.stroke([(690, 330), (684, 324)], 0.22, 0.12, n=6, col=RED))
    # 门内小旗
    g.append(B.stroke([(660, 316), (660, 286)], 0.24, 0.14, n=8, col=B.GREY))
    g.append(B.stroke([(660, 286), (680, 292), (660, 298)], 0.24, 0.14, n=8, col=RED))

    # 题语
    g.append(B.text(380, 138, '叔 在 薮　火 烈 具 举', 16, RED, anchor='middle', ls=6, weight=500))
    g.append(B.text(380, 158, '一章：乘马、执辔、暴虎、献公、戒', 8.8, LG, anchor='middle', ls=0.8))

    # 注文带
    g.append('<line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.35"/>' % GOLD)
    g.append(B.text(44, 466, '乘：上 chéng，下 shèng；一乘四马', 7.4, LG))
    g.append(B.text(290, 466, '薮：泽，禽之府；火：列人持火', 7.4, LG))
    g.append(B.text(548, 466, '公所：庄公所在；献：进于君', 7.4, LG))
    # 引句
    g.append(B.text(380, 514, '叔在薮，火烈具举。襢裼暴虎，献于公所。', 15.5, B.INK, anchor='middle', ls=1.5))
    g.append(B.text(704, 526, '图一 · 名物 · sj078a', 7.4, LG, anchor='end'))
    g.append('</svg>')

    out = os.path.join(ROOT, 'assets', 'fig', 'sj078a-huo-lie.svg')
    open(out, 'w', encoding='utf-8').write('\n'.join(g))
    import cairosvg
    cairosvg.svg2png(url=out, write_to=os.path.join(ROOT, 'dist', 'sj078a.png'),
                    output_width=1200, background_color=PAPER)
    print('wrote', out, len(''.join(g)))


if __name__ == '__main__':
    main()
