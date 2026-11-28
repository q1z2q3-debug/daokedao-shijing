# -*- coding: utf-8 -*-
"""074 丘中有麻 · 图一

三格：麻（掌状叶，可绩布）／麦（丛生，穗有芒）／李（小树，果圆）。
三物是「地不荒」的三证：麻为初植、麦为可食、李已成树。
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


def leaf_ell(cx, cy, ang, ln, wd, w=0.3, depth=0.2):
    """一枚闭合椭圆叶 + 中脉。ang 为叶尖方向（弧度）。"""
    out = []
    # 以 (cx,cy) 为叶基，沿 ang 方向展开
    n, pts = 26, []
    ca, sa = math.cos(ang), math.sin(ang)
    for k in range(n + 1):
        t = math.pi * k / n
        u = ln * (1 - math.cos(t)) / 2            # 0..ln
        v = wd * math.sin(t) / 2
        pts.append((cx + u * ca - v * sa, cy + u * sa + v * ca))
    for k in range(n):
        t = math.pi * (n - k) / n
        u = ln * (1 - math.cos(t)) / 2
        v = -wd * math.sin(t) / 2
        pts.append((cx + u * ca - v * sa, cy + u * sa + v * ca))
    out.append(B.stroke(pts + [pts[0]], w, w * 0.3, n=60, col=adapt.tone(depth)))
    out.append(B.stroke([(cx, cy), (cx + ln * ca, cy + ln * sa)], w * 0.45, w * 0.1, n=8,
                        col=adapt.tone(depth + 0.14), taper_end=0.3))
    return out


def ma(cx, cy):
    """麻：茎粗、叶大、掌状五裂各有主脉。"""
    out = []
    base, top = cy + 80, cy - 74
    for sx in (-3.2, 3.2):
        out.append(B.stroke([(cx + sx, base), (cx + sx * 0.75, (base + top) / 2), (cx + sx * 0.25, top)],
                            W * 1.15, W * 0.4, n=20, col=adapt.tone(0.05), taper_end=0.25))
    for k in range(5):
        y = base - 26 - k * 30
        side = -1 if k % 2 == 0 else 1
        out += leaf_ell(cx + side * 3, y, -2.05 if side < 0 else -1.09, 48 - k * 4, 15 - k, W * 0.5, 0.14)
    # 顶穗：束状，六根
    for i in range(6):
        dx = -13 + i * 5.2
        out.append(B.stroke([(cx + dx * 0.6, top + 12), (cx + dx, top - 12)],
                            W * 0.3, W * 0.12, n=8, col=adapt.tone(0.3), taper_end=0.5))
    out.append(B.stroke([(cx - 16, base + 2), (cx - 4, base - 5), (cx + 4, base - 5),
                         (cx + 16, base + 2)], W * 0.5, W * 0.3, n=12, col=adapt.tone(0.3)))
    return out


def mai(cx, cy):
    """麦：四茎丛生，叶作下垂弧，穗为一串小粒、粒上有芒。"""
    out = []
    base = cy + 80
    for dx, h, lean in ((-22, 118, -7), (-9, 140, -2), (7, 134, 3), (22, 112, 8)):
        top = (cx + dx + lean, base - h)
        for sx in (-2.0, 1.6):
            out.append(B.stroke([(cx + dx + sx, base), (cx + dx + sx * 0.8 + lean * 0.5, base - h * 0.5),
                                 (top[0] + sx * 0.3, top[1])],
                                W * 0.8, W * 0.24, n=18, col=adapt.tone(0.09), taper_end=0.25))
        # 叶：自节点向外下弯（弧，不是直线）
        for t, s in ((0.38, -1), (0.62, 1)):
            p = (cx + dx + lean * t * 0.5, base - h * t)
            out += leaf_ell(p[0], p[1], (1.22 if s > 0 else 1.92), 36,
                            7.0, W * 0.4, 0.26)
        # 穗：一串六粒
        for i in range(6):
            yy = top[1] + 4 - i * 7
            out.append(B.oval(cx + dx * 0.9 + lean * 0.9 + i * 0.4, yy, 2.4, 3.4,
                              w=W * 0.24, col=adapt.tone(0.24), n=12))
            for s in (-1, 1):
                out.append(B.stroke([(cx + dx * 0.9 + lean * 0.9 + i * 0.4, yy),
                                     (cx + dx * 0.9 + lean * 0.9 + i * 0.4 + s * 9, yy - 8)],
                                    W * 0.16, W * 0.07, n=6, col=adapt.tone(0.44), taper_end=0.65))
    out.append(B.stroke([(cx - 28, base + 2), (cx - 6, base - 4), (cx + 6, base - 4),
                         (cx + 28, base + 2)], W * 0.45, W * 0.26, n=14, col=adapt.tone(0.34)))
    return out


def li(cx, cy):
    """李：树干有粗、三主枝、枝梢叶簇、果挂枝下（不悬空）。"""
    out = []
    base, top = cy + 80, cy - 50
    for sx in (-5.0, 5.0):
        out.append(B.stroke([(cx + sx, base), (cx + sx * 0.62, base - 66), (cx + sx * 0.2, top)],
                            W * 1.0, W * 0.42, n=20, col=adapt.tone(0.07), taper_end=0.25))
    for a in (math.radians(-148), math.radians(-90), math.radians(-32)):
        ln = 52
        tip = (cx + ln * math.cos(a), top + ln * math.sin(a))
        out.append(B.stroke([(cx, top), (cx + ln * 0.5 * math.cos(a), top + ln * 0.5 * math.sin(a)),
                             tip], W * 0.6, W * 0.18, n=12, col=adapt.tone(0.13), taper_end=0.35))
        # 枝梢叶簇：三叶
        for da in (-0.55, 0.0, 0.55):
            out += leaf_ell(tip[0] - 6 * math.cos(a), tip[1] - 6 * math.sin(a),
                            a + da, 24, 9.0, W * 0.4, 0.24)
        # 果：挂枝梢内侧
        out.append(B.oval(tip[0] - 12 * math.cos(a), tip[1] - 10 * math.sin(a), 5.4, 5.0,
                          w=W * 0.42, col=adapt.tone(0.28), n=16))
    out.append(B.stroke([(cx - 18, base + 2), (cx - 5, base - 6), (cx + 5, base - 6),
                         (cx + 18, base + 2)], W * 0.5, W * 0.3, n=12, col=adapt.tone(0.34)))
    return out


def main():
    meta = dict(volume='王 风 · 之十', title='丘 中 有 麻', index='诗三百五篇 · 之七四',
                quote='丘中有麻，彼留子嗟', footer='图一 · 名物 · sj074a')
    draws = [('麻', ma), ('麦', mai), ('李', li)]
    notes = ['直立茎，叶对生，皮可绩布', '丛生，叶细长，穗有芒', '小树三枝，果圆']
    svg = os.path.join(ROOT, 'assets', 'fig', 'sj074a-qiu-zhong.svg')
    png = os.path.join(ROOT, 'dist', 'sj074a.png')
    print('svg', P.build(meta, draws, notes, svg, png), 'B')


if __name__ == '__main__':
    main()
