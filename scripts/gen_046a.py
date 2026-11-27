# -*- coding: utf-8 -*-
"""046 墙有茨 · 图一

三句要说的话：
 一 墙     —— 一道砖墙，茨长在墙上
 二 茨     —— 蒺藜，五角带刺，伏地而生
 三 埽     —— 束草为帚，欲扫而不能（「不可埽也」）
茨、砖、帚三者皆是几何物，正好不靠底本。
"""
import math
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import svgbrush as B  # noqa: E402
import adapt  # noqa: E402
import fig_page as P  # noqa: E402


def wall(cx, cy, w=196, h=150, course=30, brick=62):
    """砖墙：等距横缝、逐层错半砖、墙脚一线。硬笔等压。"""
    out = []
    y0, y1 = cy - h / 2, cy + h / 2
    x0, x1 = cx - w / 2, cx + w / 2
    # 压顶两道
    out.append(B.stroke([(x0 - 8, y0 - 6), (x1 + 8, y0 - 6)], 0.76, 0.76, n=8, col=adapt.tone(0.04)))
    out.append(B.stroke([(x0 - 8, y0 + 2), (x1 + 8, y0 + 2)], 0.6, 0.6, n=8, col=adapt.tone(0.14)))
    # 横缝
    n_course = int((y1 - y0) // course)
    for k in range(1, n_course):
        yy = y0 + 2 + k * course
        if yy > y1 - 3:
            break
        out.append(B.stroke([(x0, yy), (x1, yy)], 0.6, 0.6, n=10, col=adapt.tone(0.3)))
    # 竖缝：第 k 层起笔偏移 k*半砖，等距推进
    for k in range(n_course):
        ytop = y0 + 2 + k * course
        ybot = min(ytop + course - 2, y1 - 4)
        if ybot - ytop < 6:
            break
        off = (k % 2) * brick / 2
        x = x0 + off
        while x <= x1 + 0.1:
            if x0 + 5 < x < x1 - 5:
                out.append(B.stroke([(x, ytop), (x, ybot)], 0.46, 0.46, n=8, col=adapt.tone(0.36)))
            x += brick
    # 两竖边与墙脚
    for x in (x0, x1):
        out.append(B.stroke([(x, y0 + 2), (x, y1)], 0.7, 0.55, n=12, col=adapt.tone(0.1)))
    out.append(B.stroke([(x0 - 5, y1 + 2), (x0, y1 - 2), (x1, y1 - 2), (x1 + 5, y1 + 2)],
                        0.58, 0.5, n=16, col=adapt.tone(0.32)))
    # 墙上生茨：墙头三丛（缩小的蒺藜，示「墙有茨」）
    for dx, r in ((-58, 0.42), (2, 0.48), (58, 0.40)):
        for seg in ci(cx + dx, y0 - 10 - r * 30, r=34, scale=r):
            out.append(seg)
    return out


def ci(cx, cy, r=34, scale=1.0):
    """蒺藜：五角果实，角出硬刺。刺短而粗，与果体同量级——蒺藜之「刺」不在长，在「硬」。"""
    out = []
    w = adapt.w_of(120 * scale)
    R = r * scale
    # 五角轮廓：角处外张、凹处内收（尖角由 cos 的高次项逼出）
    # 果体为一枚略压扁的圆，刺另出——蒺藜是「刺球」，不是「星」
    ring = [(cx + R * 0.78 * math.cos(math.pi * 2 * k / 40 - math.pi / 2),
             cy + R * 0.7 * math.sin(math.pi * 2 * k / 40 - math.pi / 2)) for k in range(40)]
    out.append(B.stroke_closed(ring, w * 0.95, adapt.tone(0.14), pad=5))
    # 五刺：自角向外，基部宽、末端尖（收敛带）
    for k in range(5):
        a = -math.pi / 2 + math.pi * 2 * k / 5
        bx, by = cx + R * 0.74 * math.cos(a), cy + R * 0.66 * math.sin(a)
        tip = (cx + (R * 0.74 + 29 * scale) * math.cos(a), cy + (R * 0.66 + 26 * scale) * math.sin(a))
        px, py = -math.sin(a) * 7.8 * scale, math.cos(a) * 7.0 * scale
        out.append(B.stroke([(bx + px, by + py), tip, (bx - px, by - py)],
                            w * 0.62, w * 0.16, n=14, col=adapt.tone(0.18), taper_end=0.35))
    # 果面三道弧纹
    for t0 in (-0.6, 0.5, 2.6):
        arc = [(cx + R * 0.56 * math.cos(t0 + 0.28 * j / 6),
                cy + R * 0.5 * math.sin(t0 + 0.28 * j / 6)) for j in range(7)]
        out.append(B.stroke(arc, w * 0.24, w * 0.2, n=12, col=adapt.tone(0.46)))
    # 果心一道小环
    out.append(B.stroke_closed([(cx + 7 * scale * math.cos(math.pi * 2 * k / 12),
                                 cy + 6 * scale * math.sin(math.pi * 2 * k / 12)) for k in range(12)],
                               w * 0.3, adapt.tone(0.42), pad=3))
    if scale >= 0.9:
        # 伏地两枝（只在主格画，缩小的墙头丛不画）
        out.append(B.stroke([(cx - R - 2, cy + R * 0.9), (cx - R - 30, cy + R * 0.9 + 7)],
                            w * 0.42, w * 0.26, n=10, col=adapt.tone(0.52), taper_end=0.5))
        out.append(B.stroke([(cx + R * 0.5, cy + R * 0.95), (cx + R + 26, cy + R * 0.95 + 9)],
                            w * 0.4, w * 0.24, n=10, col=adapt.tone(0.52), taper_end=0.5))
    return out


def sao(cx, cy, h=142):
    """埽（帚）：柄两道，帚身收敛带，束腰两道，草茎六道。软笔。"""
    out = []
    w = adapt.w_of(h)
    top = cy - h / 2
    waist = cy + h * 0.06
    foot = cy + h / 2
    # 柄
    out.append(B.stroke([(cx - 6, top), (cx - 6, waist - 10)], w * 0.78, w * 0.7, n=14, col=adapt.tone(0.16)))
    out.append(B.stroke([(cx + 6, top), (cx + 6, waist - 10)], w * 0.78, w * 0.7, n=14, col=adapt.tone(0.16)))
    out.append(B.stroke([(cx - 6, top), (cx + 6, top)], w * 0.56, n=6, col=adapt.tone(0.28)))
    # 帚身两缘：上窄下宽，末端参差
    for sx in (-1, 1):
        out.append(B.stroke([(cx + sx * 9, waist - 10), (cx + sx * 15, waist + 8),
                             (cx + sx * 27, waist + 34), (cx + sx * 34, foot - 6)],
                            w * 0.62, w * 0.3, n=22, col=adapt.tone(0.12), taper_end=0.28))
    # 帚头一道横线，接住帚身
    out.append(B.stroke([(cx - 15, waist - 8), (cx + 15, waist - 8)],
                        w * 0.44, w * 0.44, n=6, col=adapt.tone(0.22)))
    # 束腰两道
    for dy in (0, 7):
        out.append(B.stroke([(cx - 12, waist + dy), (cx + 12, waist + dy)],
                            w * 0.4, w * 0.4, n=6, col=adapt.tone(0.24)))
    # 草茎：自束腰向下散开，末端略长短不齐
    for i, (dx, dl) in enumerate(((-16, 2), (-9, -4), (-2, 1), (5, -6), (12, 3), (18, -2))):
        out.append(B.stroke([(cx + dx * 0.6, waist + 9), (cx + dx, foot + dl)],
                            w * 0.3, w * 0.12, n=12, col=adapt.tone(0.36), taper_end=0.55))
    return out


def main():
    meta = dict(volume='鄘 风 · 四', title='墙 有 茨', index='诗三百五篇 · 之四六',
                quote='墙有茨，不可埽也', footer='图一 · 名物 · sj046a')
    draws = [('墙', wall), ('茨', ci), ('埽', sao)]
    notes = ['一道砖墙，茨生于墙头', '蒺藜：五瓣出刺，伏地而生', '束草为帚，欲埽而不能']
    svg = os.path.join(ROOT, 'assets', 'fig', 'sj046a-qiang-you-ci.svg')
    png = os.path.join(ROOT, 'dist', 'sj046a.png')
    size = P.build(meta, draws, notes, svg, png)
    print('svg', size, 'B')


if __name__ == '__main__':
    main()
