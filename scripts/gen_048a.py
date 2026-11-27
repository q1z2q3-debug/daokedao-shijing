# -*- coding: utf-8 -*-
"""048 桑中 · 图一

三句：
 一 桑      —— 一株桑，三歧枝，叶簇生在枝端
 二 唐      —— 菟丝：无根之丝，缠枝而生（「爰采唐矣」）
 三 淇      —— 淇水，送别之处
桑是树，唐是丝，淇是水——树硬、丝软、水更软，正好一页三档。
"""
import math
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import svgbrush as B  # noqa: E402
import adapt  # noqa: E402
import fig_page as P  # noqa: E402


def leaf(cx, cy, ang, ln=26, wd=9, w=0.4, depth=0.16):
    """一叶：两线自叶柄出，收于叶尖（收敛带）。"""
    ca, sa = math.cos(ang), math.sin(ang)
    p0 = (cx, cy)
    tip = (cx + ln * ca, cy + ln * sa)
    side = (-sa * wd, ca * wd)
    mid = (cx + ln * 0.45 * ca, cy + ln * 0.45 * sa)
    out = []
    out.append(B.stroke([p0, (mid[0] + side[0], mid[1] + side[1]), tip],
                        w, w * 0.25, n=16, col=adapt.tone(depth), taper_end=0.5))
    out.append(B.stroke([p0, (mid[0] - side[0], mid[1] - side[1]), tip],
                        w, w * 0.25, n=16, col=adapt.tone(depth), taper_end=0.5))
    out.append(B.stroke([p0, (mid[0] * 1.3 - cx * 0.3, mid[1] * 1.3 - cy * 0.3),
                         (cx + ln * 0.9 * ca, cy + ln * 0.9 * sa)],
                        w * 0.5, w * 0.2, n=10, col=adapt.tone(depth + 0.22), taper_end=0.5))
    return out


def cluster(cx, cy, w=0.4, depth=0.16, ln=30):
    out = []
    for a in (-2.9, -2.35, -1.8, -1.25, -0.7):
        out += leaf(cx, cy, a, ln, 9, w, depth)
    return out


def mulberry(cx, cy, h=200):
    """桑：主干下粗上细（双线锥度 16→6），三主枝抬至树冠，枝端各一叶簇。"""
    out = []
    w = adapt.w_of(h)
    base = cy + h / 2
    top = cy - h / 2 + 26
    # 主干：左右两线，间距自 16 收到 6
    for sx in (-1, 1):
        out.append(B.stroke([(cx + sx * 8, base), (cx + sx * 7, cy + 40),
                             (cx + sx * 4, cy - 20), (cx + sx * 3, top)],
                            w * 0.95, w * 0.5, n=26, col=adapt.tone(0.06), taper_end=0.25))
    # 三主枝：左、右、中，皆自主干上部出，斜上
    branches = ((-1, (cx - 3, cy - 30), (cx - 26, cy - 54), (cx - 46, cy - 70), (cx - 58, cy - 78)),
                (1, (cx + 3, cy - 34), (cx + 24, cy - 56), (cx + 44, cy - 72), (cx + 56, cy - 80)),
                (0, (cx, cy - 40), (cx - 4, cy - 62), (cx + 2, cy - 80), (cx + 4, cy - 92)))
    for _, p0, p1, p2, p3 in branches:
        out.append(B.stroke([p0, p1, p2, p3], w * 0.62, w * 0.26, n=24,
                            col=adapt.tone(0.12), taper_end=0.35))
        out += cluster(p3[0], p3[1] - 4, w * 0.5, 0.18, ln=28)
        # 枝上一小分杈
        out.append(B.stroke([p2, (p2[0] + (8 if p2[0] > cx else -8), p2[1] - 12)],
                            w * 0.3, w * 0.16, n=10, col=adapt.tone(0.26), taper_end=0.4))
    # 树根
    out.append(B.stroke([(cx - 24, base + 2), (cx - 8, base - 4), (cx + 8, base - 4), (cx + 24, base + 2)],
                        w * 0.5, w * 0.34, n=16, col=adapt.tone(0.32)))
    return out


def tang(cx, cy, h=170):
    """唐（菟丝）：借一根枯枝为承，丝自枝上盘旋而下，无根，末端飘散。"""
    out = []
    w = adapt.w_of(h)
    # 承枝
    for sx in (-1, 1):
        out.append(B.stroke([(cx + sx * 6, cy - h / 2), (cx + sx * 5, cy - 20),
                             (cx + sx * 4, cy + h / 2 - 10)],
                            w * 0.62, w * 0.34, n=18, col=adapt.tone(0.36), taper_end=0.35))
    for sx, dy in ((-1, -46), (1, -30), (-1, 26), (1, 40)):
        out.append(B.stroke([(cx + sx * 4, cy + dy), (cx + sx * 32, cy + dy * 1.35)],
                            w * 0.4, w * 0.2, n=10, col=adapt.tone(0.42), taper_end=0.5))
    # 丝：绕枝 3.4 圈，半径随下渐大，末端散成三缕
    t0, t1 = 0.0, math.pi * 2 * 4.2
    pts = []
    for k in range(90):
        t = t0 + (t1 - t0) * k / 89
        rr = 13 + 8 * (t / t1)
        pts.append((cx + rr * math.cos(t - math.pi / 2), cy - h / 2 + 18 + (h - 26) * k / 89)
                   )
    out.append(B.stroke(pts, w * 0.26, w * 0.2, n=90, col=adapt.tone(0.2), taper_start=0.15))
    # 第二股：同绕而相位差，丝有两股才像「缠」
    pts2 = []
    for k in range(90):
        t = t0 + (t1 - t0) * k / 89
        rr = 12 + 7 * (t / t1)
        pts2.append((cx + rr * math.cos(t - math.pi / 2 + 1.15),
                     cy - h / 2 + 22 + (h - 30) * k / 89))
    out.append(B.stroke(pts2, w * 0.2, w * 0.16, n=90, col=adapt.tone(0.3), taper_start=0.15))
    # 末端三缕飘散
    end = pts[-1]
    for dy, dx in ((14, -22), (20, 4), (13, 26)):
        out.append(B.stroke([end, (end[0] + dx * 0.5, end[1] + dy * 0.5), (end[0] + dx, end[1] + dy)],
                            w * 0.22, w * 0.08, n=12, col=adapt.tone(0.42), taper_end=0.6))
    return out


def qi(cx, cy):
    out = []
    for i, (hw, amp, yy) in enumerate(((88, 9, cy + 34), (70, 7, cy + 8), (52, 5, cy - 18))):
        out.append(P.wave(cx, yy, hw, amp=amp, n=26, phase=i * 1.1,
                          w=0.5 if i == 0 else 0.4, depth=0.52 + i * 0.07))
    return out


def main():
    meta = dict(volume='鄘 风 · 四', title='桑 中', index='诗三百五篇 · 之四八',
                quote='期我乎桑中，送我乎淇之上矣', footer='图一 · 名物 · sj048a')
    draws = [('桑', mulberry), ('唐', tang), ('淇', qi)]
    notes = ['三歧枝，叶簇生枝端', '菟丝无根，缠枝而下', '淇水，送别之处']
    svg = os.path.join(ROOT, 'assets', 'fig', 'sj048a-sang-zhong.svg')
    png = os.path.join(ROOT, 'dist', 'sj048a.png')
    print('svg', P.build(meta, draws, notes, svg, png), 'B')


if __name__ == '__main__':
    main()
