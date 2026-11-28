# -*- coding: utf-8 -*-
"""076 将仲子 · 图一（名物/场景）

一图一景：里门—墙门—园门，三重由外而内；杞—桑—檀，三树由柔而坚。
仲子在门外，我在园内；三道门各打一个「×」，是「无逾」。
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


def tree_willow(cx, base, h=112):
    """杞柳：干斜，枝垂，叶细长。"""
    out = []
    top = base - h
    out.append(B.stroke([(cx, base), (cx - 4, base - h * .42), (cx - 12, base - h * .7),
                         (cx - 8, top)], 0.9, 0.34, n=26, col=B.INK, taper_end=0.22))
    # 主枝：先上扬，再下垂
    for k in range(12):
        ang = -2.6 + k * 0.47
        sx = cx - 8 + 3 * math.cos(ang)
        sy = top + 2 + 10 * math.sin(ang * .4)
        ex = sx + 30 * math.cos(ang)
        ey = sy + 38 + 34 * abs(math.sin(ang * .5))
        midx = sx + (ex - sx) * .55
        midy = sy - 10 + (ey - sy) * .30
        out.append(B.stroke([(sx, sy), (midx, midy), (ex, ey)],
                            0.55, 0.22, n=20, col=B.INK2, taper_end=0.55))
        # 叶：沿枝三节，细长斜出
        for j in range(5):
            t = .3 + j * .16
            lx = sx + (ex - sx) * t
            ly = sy + (ey - sy) * t + 4
            out.append(B.stroke([(lx, ly), (lx + 2.2, ly + 11)], 0.26, 0.12, n=8,
                                col=B.GREY, taper_end=0.6))
    return out


def tree_mulberry(cx, base, h=102):
    """桑：干直，枝展，叶厚而阔。"""
    out = []
    top = base - h
    out.append(B.stroke([(cx, base), (cx + 2, base - h * .42), (cx - 2, top)],
                        0.95, 0.36, n=24, col=B.INK, taper_end=0.18))
    # 主枝三出，再分小枝
    for s, dx, dy in ((-1, 46, 30), (0, 8, 44), (1, 42, 24)):
        p0 = (cx - 2, top + 16)
        p1 = (cx + s * dx * .42, top - dy * .45)
        p2 = (cx + s * dx, top - dy)
        out.append(B.stroke([p0, p1, p2], 0.62, 0.26, n=20, col=B.INK2, taper_end=0.4))
        # 二级枝
        for q in (-1, 1):
            out.append(B.stroke([p1, (p1[0] + q * 16, p1[1] - 10),
                                 (p1[0] + q * 22, p1[1] - 2)], 0.34, 0.2, n=12,
                                col=B.INK2, taper_end=0.5))
    # 叶：椭圆小叶，按冠幅铺开，不填面
    for k in range(48):
        a = k * 2.399
        r = 22 + (k % 7) * 5.2
        lx = cx + r * math.cos(a) * 1.15
        ly = top + 6 + r * .62 * math.sin(a)
        if base - 40 < ly:
            continue
        # 桑叶：三出脉，不闭合
        out.append(B.hair([(lx, ly - 4), (lx, ly + 5)], 0.22, B.GREY))
        out.append(B.stroke([(lx, ly + 2), (lx - 4.2, ly - 1), (lx - 5, ly - 4)], 0.22, 0.12, n=8,
                            col=B.GREY, taper_end=0.5))
        out.append(B.stroke([(lx, ly + 2), (lx + 4.2, ly - 1), (lx + 5, ly - 4)], 0.22, 0.12, n=8,
                            col=B.GREY, taper_end=0.5))
    return out


def tree_hard(cx, base, h=118):
    """檀：干直，枝劲，叶疏而硬。"""
    out = []
    top = base - h
    out.append(B.stroke([(cx, base), (cx + 1, base - h * .5), (cx, top)],
                        1.0, 0.4, n=24, col=B.INK, taper_end=0.15))
    # 劲枝：折而不断，左右各三
    branches = (
        (-1, [(cx, top + 24), (cx - 20, top + 2), (cx - 36, top + 4), (cx - 46, top - 10)]),
        (1, [(cx, top + 32), (cx + 24, top + 6), (cx + 38, top + 10), (cx + 50, top - 2)]),
        (-1, [(cx - 4, top + 42), (cx - 28, top + 28), (cx - 40, top + 36)]),
        (1, [(cx + 2, top + 50), (cx + 22, top + 40), (cx + 32, top + 46)]),
        (-1, [(cx - 2, top + 56), (cx - 12, top + 42), (cx - 22, top + 46)]),
        (1, [(cx + 4, top + 62), (cx + 14, top + 50), (cx + 24, top + 56)]),
    )
    for s, pts in branches:
        out.append(B.stroke(pts, 0.6, 0.26, n=18, col=B.INK2, taper_end=0.5))
    # 叶：少而硬，短撇，集中在枝端
    for dx, dy in ((-36, -10), (-46, -4), (-28, 2), (30, -2), (42, 4), (52, -2),
                   (-22, 10), (18, 12), (-8, 18), (10, 20), (-2, 26), (24, 26)):
        lx, ly = cx + dx, top + dy
        out.append(B.stroke([(lx, ly), (lx + (4 if dx > 0 else -4), ly - 9)],
                            0.34, 0.18, n=10, col=B.GREY, taper_end=0.55))
    return out


def person(cx, base, scale=1.0, male=True, facing=1):
    """剪影：不画五官。宽袖、束带、下裳。"""
    out = []
    h = 76 * scale
    top = base - h
    head_r = 7.2 * scale
    # 头
    out.append(B.oval(cx, top + head_r + 2, head_r, head_r * 1.12, 0.78, B.INK2, n=40))
    # 发：顶上一弧；女加髻
    out.append(B.arcband(cx, top + head_r + 2, head_r + 1.2, head_r * 1.12 + 1.2, 3.45, 5.9, 0.45, B.INK, n=22))
    if not male:
        out.append(B.oval(cx, top - 1, 3.4, 3.0, 0.5, B.INK, n=24))
    # 肩与身
    neck = top + head_r * 2.1
    out.append(B.stroke([(cx - 8 * scale, neck), (cx - 12 * scale, base - 34 * scale),
                         (cx - 15 * scale, base)], 0.6, 0.32, n=18, col=B.INK2, taper_end=0.18))
    out.append(B.stroke([(cx + 8 * scale, neck), (cx + 12 * scale, base - 34 * scale),
                         (cx + 15 * scale, base)], 0.6, 0.32, n=18, col=B.INK2, taper_end=0.18))
    out.append(B.stroke([(cx - 8 * scale, neck), (cx, neck + 4), (cx + 8 * scale, neck)],
                        0.4, 0.24, n=12, col=B.INK2))
    # 交领：V
    out.append(B.stroke([(cx - 7 * scale, neck + 2), (cx, neck + 18 * scale),
                         (cx + 7 * scale, neck + 2)], 0.42, 0.22, n=14, col=B.INK2, taper_end=0.3))
    # 两袖：一袖前伸，一袖垂
    out.append(B.stroke([(cx + 8 * scale, neck + 6), (cx + 22 * scale * facing, base - 44 * scale),
                         (cx + 20 * scale * facing, base - 32 * scale), (cx + 10 * scale, base - 36 * scale)],
                        0.5, 0.26, n=18, col=B.INK2, taper_end=0.25))
    out.append(B.stroke([(cx - 8 * scale, neck + 6), (cx - 16 * scale, base - 44 * scale),
                         (cx - 12 * scale, base - 32 * scale)],
                        0.46, 0.24, n=14, col=B.INK2, taper_end=0.3))
    # 腰带
    out.append(B.stroke([(cx - 10 * scale, base - 34 * scale), (cx + 10 * scale, base - 34 * scale)],
                        0.34, 0.22, n=10, col=B.INK2))
    # 下裳：中缝、下摆
    out.append(B.stroke([(cx, base - 32 * scale), (cx + (2 if male else -2), base - 4)],
                        0.3, 0.2, n=12, col=B.GREY))
    out.append(B.stroke([(cx - 15 * scale, base), (cx - 8 * scale, base - 2),
                         (cx + 8 * scale, base - 2), (cx + 15 * scale, base)],
                        0.36, 0.24, n=14, col=B.INK2))
    return out


def gate(cx, base, half=24, h=96, roof=True):
    """门：两柱一楣，门内断口。"""
    out = []
    left, right = cx - half, cx + half
    top = base - h
    for x in (left, right):
        out.append(B.stroke([(x, top), (x, base)], 0.72, 0.4, n=18, col=B.INK, taper_end=0.12))
    out.append(B.stroke([(left - 6, top), (right + 6, top)], 0.52, 0.36, n=16, col=B.INK2))
    if roof:
        out.append(B.stroke([(left - 18, top - 2), (cx - 10, top - 18), (cx + 10, top - 18),
                             (right + 18, top - 2)], 0.55, 0.28, n=22, col=B.INK2, taper_end=0.2))
        out.append(B.stroke([(left - 18, top - 2), (right + 18, top - 2)],
                            0.3, 0.2, n=14, col=B.GREY))
    # 门扇：只画一门，半开
    out.append(B.stroke([(left + 3, base - 2), (left + 3, top + 16), (cx + 2, top + 16),
                         (cx + 2, base - 2)], 0.4, 0.24, n=18, col=B.INK2, taper_end=0.3))
    return out


def wall(x0, x1, base, h=74, door=(364, 28)):
    """墙：夯土，瓦顶；中留一门。"""
    out = []
    top = base - h
    dc, dh = door
    # 墙身两段，中间门洞
    for a, b in ((x0, dc - dh), (dc + dh, x1)):
        out.append(B.stroke([(a, base), (a, top), (b, top), (b, base)],
                            0.7, 0.32, n=22, col=B.INK2, taper_end=0.12))
        # 夯土层：横线三道，短而不齐
        for k in range(3):
            yy = top + 16 + k * 18
            out.append(B.hair([(a + 5, yy), (b - 5, yy + (1 if k % 2 else -1))], 0.28, B.GREY))
    # 瓦顶：连续短斜
    for x in range(x0, x1, 18):
        if dc - dh - 8 < x < dc + dh + 8:
            continue
        out.append(B.hair([(x, top - 6), (x + 9, top + 4)], 0.4, B.INK2))
    out.append(B.stroke([(x0 - 8, top - 6), (dc - dh - 4, top - 6)], 0.45, 0.32, n=12, col=B.INK))
    out.append(B.stroke([(dc + dh + 4, top - 6), (x1 + 8, top - 6)], 0.45, 0.32, n=12, col=B.INK))
    # 门洞两侧门柱
    for x in (dc - dh, dc + dh):
        out.append(B.stroke([(x, base), (x, top + 6)], 0.6, 0.36, n=14, col=B.INK))
    # 门楣
    out.append(B.stroke([(dc - dh, top + 6), (dc + dh, top + 6)], 0.48, 0.32, n=14, col=B.INK2))
    # 门内空：只画门槛
    out.append(B.hair([(dc - dh + 4, base - 3), (dc + dh - 4, base - 3)], 0.3, B.GREY))
    return out


def fence(x0, x1, base, h=56):
    """园篱：木栅，留门。"""
    out = []
    top = base - h
    for x in range(x0, x1, 17):
        if x0 + 56 < x < x0 + 86:
            continue
        out.append(B.stroke([(x, base), (x + (2 if x % 2 else -2), top)],
                            0.34, 0.22, n=12, col=B.INK2, taper_end=0.25))
    for y in (top + 8, base - 18):
        out.append(B.stroke([(x0, y), (x1, y)], 0.36, 0.24, n=20, col=B.GREY))
    # 园门：两柱一横
    out.append(B.stroke([(x0 + 52, base), (x0 + 52, top + 4)], 0.5, 0.3, n=12, col=B.INK))
    out.append(B.stroke([(x0 + 90, base), (x0 + 90, top + 4)], 0.5, 0.3, n=12, col=B.INK))
    out.append(B.stroke([(x0 + 46, top + 4), (x0 + 96, top + 4)], 0.42, 0.28, n=12, col=B.INK2))
    return out


def xmark(cx, cy, s=7):
    return [B.stroke([(cx - s, cy - s), (cx + s, cy + s)], 0.9, 0.6, n=8, col=RED),
            B.stroke([(cx - s, cy + s), (cx + s, cy - s)], 0.9, 0.6, n=8, col=RED)]


def main():
    g = [B.svg_open(W, H), B.grid_check((W, H))]
    # 外框
    g.append('<rect x="10" y="16" width="740" height="508" fill="none" stroke="%s" stroke-width="1.0"/>' % B.GREY)
    g.append('<rect x="22" y="28" width="716" height="484" fill="none" stroke="%s" stroke-width="0.8"/>' % '#DCD5C8')
    # 页眉
    g.append(B.text(44, 58, '郑 风 · 之二', 8.6, RED, ls=2))
    g.append(B.text(380, 62, '将仲子　里墙园', 24, B.INK, anchor='middle', ls=8, weight=500))
    g.append(B.text(704, 58, '诗三百五篇 · 之七六', 8.2, LG, anchor='end', ls=1.5))
    g.append('<line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.35"/>' % GOLD)

    base = 404
    # 地面
    g.append(B.hair([(58, base), (704, base)], 0.5, B.GREY))
    for k in range(15):
        x = 76 + k * 42
        g.append(B.hair([(x, base + 4), (x + 10, base + 4 + (k % 3) * 2)], 0.22, B.GREY))

    # 三树
    g += tree_willow(122, base, 112)
    g += tree_mulberry(430, base, 102)
    g += tree_hard(640, base, 118)

    # 三界
    g += gate(194, base, 26, 96)
    g += wall(252, 474, base, 74, door=(364, 28))
    g += fence(474, 704, base, 56)

    # 人
    g += person(84, base, scale=1.0, male=True, facing=1)
    g += person(590, base, scale=1.0, male=False, facing=-1)

    # 无逾：虚线由仲子至我，三道门各断一次
    for x0, x1 in ((92, 168), (220, 334), (394, 516), (570, 588)):
        g.append('<line x1="%d" y1="372" x2="%d" y2="372" stroke="%s" stroke-width="0.55" '
                 'stroke-dasharray="5 5" opacity="0.55"/>' % (x0, x1, B.GREY))
    g += xmark(194, 372, 8)
    g += xmark(364, 372, 8)
    g += xmark(545, 372, 8)

    # 标题语
    g.append(B.text(380, 140, '无　逾', 18, RED, anchor='middle', ls=8, weight=500))
    g.append(B.text(380, 160, '三章三境，皆曰无逾', 9.2, LG, anchor='middle', ls=2))

    # 小标注
    g.append(B.text(194, 262, '里', 11, B.INK, anchor='middle', ls=2))
    g.append(B.text(194, 278, '二十五家', 7.4, LG, anchor='middle'))
    g.append(B.text(364, 312, '墙', 11, B.INK, anchor='middle', ls=2))
    g.append(B.text(364, 326, '垣', 7.4, LG, anchor='middle'))
    g.append(B.text(545, 326, '园', 11, B.INK, anchor='middle', ls=2))
    g.append(B.text(545, 340, '圃之藩', 7.4, LG, anchor='middle'))

    g.append(B.text(122, 438, '杞（杞柳）', 7.6, B.INK2, anchor='middle'))
    g.append(B.text(430, 438, '桑', 7.6, B.INK2, anchor='middle'))
    g.append(B.text(640, 438, '檀（强韧之木）', 7.6, B.INK2, anchor='middle'))
    g.append(B.text(68, 452, '仲子', 8, B.INK2, anchor='middle'))
    g.append(B.text(604, 452, '我', 8, B.INK2, anchor='middle'))

    # 注文带
    g.append('<line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.35"/>' % GOLD)
    g.append(B.text(44, 466, '里·墙·园：三重界，由外而内', 7.8, LG))
    g.append(B.text(380, 466, '杞·桑·檀：三树由柔而坚', 7.8, LG))
    # 引句
    g.append(B.text(380, 514, '将仲子兮，无逾我里，无折我树杞', 16, B.INK, anchor='middle', ls=3))
    g.append(B.text(704, 526, '图一 · 名物 · sj076a', 7.4, LG, anchor='end'))
    g.append('</svg>')

    out = os.path.join(ROOT, 'assets', 'fig', 'sj076a-jiang-zhong-zi.svg')
    open(out, 'w', encoding='utf-8').write('\n'.join(g))
    import cairosvg
    cairosvg.svg2png(url=out, write_to=os.path.join(ROOT, 'dist', 'sj076a.png'),
                    output_width=1200, background_color=PAPER)
    print('wrote', out, len(''.join(g)))


if __name__ == '__main__':
    main()
