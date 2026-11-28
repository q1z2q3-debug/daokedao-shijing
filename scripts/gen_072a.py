# -*- coding: utf-8 -*-
"""072 采葛 · 图一

三格：
 一 葛 —— 藤蔓缠绕，三出复叶（絺绤之材，事之小）
 二 萧 —— 直立多枝，叶羽状，顶生穗（祭祀爇香，事之大）
 三 艾 —— 直立，叶深裂，穗细（疗疾之急）

三物皆草，故同一株法：根、茎、枝、叶、穗五层。
差别只在「枝之多寡、叶之裂与否、穗之形」，不另立画法。
"""
import math
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import svgbrush as B  # noqa: E402
import adapt  # noqa: E402
import fig_page as P  # noqa: E402

W = 0.44


def blade(cx, cy, ang, ln, wd, w=0.30, depth=0.2, lobes=1):
    """一叶：披针形，两侧收敛于尖；lobes>1 则叶缘作浅裂（艾）。"""
    ca, sa = math.cos(ang), math.sin(ang)
    nx, ny = -sa * wd, ca * wd
    tip = (cx + ln * ca, cy + ln * sa)
    out = []
    if lobes <= 1:
        mid = (cx + ln * 0.45 * ca, cy + ln * 0.45 * sa)
        out.append(B.stroke([(cx, cy), (mid[0] + nx, mid[1] + ny), tip], w, w * 0.16, n=16,
                            col=adapt.tone(depth), taper_end=0.55))
        out.append(B.stroke([(cx, cy), (mid[0] - nx, mid[1] - ny), tip], w, w * 0.16, n=16,
                            col=adapt.tone(depth), taper_end=0.55))
        out.append(B.stroke([(cx, cy), (cx + ln * 0.92 * ca, cy + ln * 0.92 * sa)], w * 0.45,
                            w * 0.2, n=10, col=adapt.tone(depth + 0.2), taper_end=0.5))
    else:
        # 裂叶：三裂，两侧小叶外张，中央一片
        for k, (f, off) in enumerate(((0.34, 1.0), (0.62, 0.8), (0.9, 0.55))):
            p = (cx + ln * f * ca, cy + ln * f * sa)
            side = wd * off
            out.append(B.stroke([p, (p[0] + nx * side, p[1] + ny * side),
                                 (tip[0] + nx * side * 0.4, tip[1] + ny * side * 0.4)],
                                w * 0.8, w * 0.14, n=14, col=adapt.tone(depth), taper_end=0.5))
            out.append(B.stroke([p, (p[0] - nx * side, p[1] - ny * side),
                                 (tip[0] - nx * side * 0.4, tip[1] - ny * side * 0.4)],
                                w * 0.8, w * 0.14, n=14, col=adapt.tone(depth), taper_end=0.5))
        out.append(B.stroke([(cx, cy), tip], w * 0.5, w * 0.2, n=12,
                            col=adapt.tone(depth + 0.18), taper_end=0.5))
    return out


def stem(cx, base, top, w=W, depth=0.08, sway=0.0):
    out = []
    for sx in (-1.6, 1.6):
        out.append(B.stroke([(cx + sx, base), (cx + sway * 0.5 + sx * 0.9, (base + top) / 2),
                             (cx + sway, top)],
                            w * 0.9, w * 0.35, n=18, col=adapt.tone(depth), taper_end=0.3))
    return out


def ge(cx, cy):
    """葛：藤本缠绕。藤一线盘旋而上，三出复叶生于节。"""
    out = []
    base = cy + 78
    top = cy - 66
    w = W
    # 藤：s 形盘旋，一圈半
    pts = []
    for k in range(60):
        t = k / 59.0
        y = base - (base - top) * t
        x = cx + 26 * math.sin(t * math.pi * 3.0)
        pts.append((x, y))
    out.append(B.stroke(pts, w * 0.9, w * 0.4, n=60, col=adapt.tone(0.06), taper_end=0.35))
    # 节上三出复叶：每节三小叶
    for k in range(5):
        t = 0.12 + 0.19 * k
        x = cx + 26 * math.sin(t * math.pi * 3.0)
        y = base - (base - top) * t
        side = 1 if k % 2 == 0 else -1
        for da in (-0.55, 0, 0.55):
            a = (-1.35 if side > 0 else -1.85) + da * side
            out += blade(x + side * 8, y, a, 30, 7.5, w * 0.72, 0.18)
    # 根
    out.append(B.stroke([(cx - 20, base + 2), (cx - 4, base - 6), (cx + 6, base - 6),
                         (cx + 20, base + 2)], w * 0.5, w * 0.3, n=14, col=adapt.tone(0.3)))
    return out


def xiao(cx, cy):
    """萧：直立茎，上部多枝，叶羽状，顶生穗（灰白小点）。"""
    out = []
    base = cy + 78
    top = cy - 74
    w = W
    out += stem(cx, base, top, w)
    for k in range(4):
        y = top + 34 + k * 22
        for side in (-1, 1):
            tip = (cx + side * (26 - k * 3), y - 16)
            out.append(B.stroke([(cx, y), (cx + side * 12, y - 6), tip], w * 0.5, w * 0.16, n=12,
                                col=adapt.tone(0.16), taper_end=0.5))
            for da in (-22, 10):
                out += blade(tip[0], tip[1], math.pi / 2 + side * (1.1 + da / 60), 22, 3.2,
                             w * 0.5, 0.24)
    # 顶穗：小点六
    for i, (dx, dy) in enumerate(((0, -2), (-6, 4), (6, 4), (-3, 12), (3, 12), (0, 20))):
        out.append(B.oval(cx + dx, top + dy, 2.4, 3.2, w=w * 0.2, col=adapt.tone(0.34), n=12))
    out.append(B.stroke([(cx - 14, base + 2), (cx - 3, base - 5), (cx + 3, base - 5),
                         (cx + 14, base + 2)], w * 0.45, w * 0.28, n=12, col=adapt.tone(0.3)))
    return out


def ai(cx, cy):
    """艾：直立、叶深裂、穗细而长。"""
    out = []
    base = cy + 78
    top = cy - 72
    w = W
    out += stem(cx, base, top, w)
    for k in range(4):
        y = base - 22 - k * 26
        for side in (-1, 1):
            out += blade(cx + side * 2, y, -1.9 if side < 0 else -1.24, 34, 11, w * 0.62,
                         0.16, lobes=3)
    # 穗：一束细长，五笔
    for dx in (-5, -2.5, 0, 2.5, 5):
        out.append(B.stroke([(cx + dx, top + 6), (cx + dx * 1.15, top - 12)],
                            w * 0.3, w * 0.1, n=8, col=adapt.tone(0.3), taper_end=0.6))
    out.append(B.stroke([(cx - 13, base + 2), (cx - 3, base - 5), (cx + 3, base - 5),
                         (cx + 13, base + 2)], w * 0.45, w * 0.28, n=12, col=adapt.tone(0.3)))
    return out


def main():
    meta = dict(volume='王 风 · 之八', title='采 葛', index='诗三百五篇 · 之七二',
                quote='一日不见，如三秋兮', footer='图一 · 名物 · sj072a')
    draws = [('葛', ge), ('萧', xiao), ('艾', ai)]
    notes = ['藤蔓缠绕，三出复叶，絺绤之材', '直立多枝，叶羽状，祭祀爇香', '叶深裂，穗细长，疗疾之草']
    svg = os.path.join(ROOT, 'assets', 'fig', 'sj072a-cai-ge.svg')
    png = os.path.join(ROOT, 'dist', 'sj072a.png')
    print('svg', P.build(meta, draws, notes, svg, png), 'B')


if __name__ == '__main__':
    main()
