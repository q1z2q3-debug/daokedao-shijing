# -*- coding: utf-8 -*-
"""073 大车 · 图一

三格：大车（轮、箱、辕、衡）／毳衣（交领右衽、宽袖、束带）／璊（赤玉璧）。
三物是「威仪」的三个可见处：车之声、衣之色、玉之赤。
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
OCH = adapt.tone(0.78)


def ring(cx, cy, r, w, n=70, depth=0.1):
    pts = [(cx + r * math.cos(2 * math.pi * k / n), cy + r * math.sin(2 * math.pi * k / n))
           for k in range(n)]
    return B.stroke(pts + [pts[0]], w, w * 0.22, n=n * 2, col=adapt.tone(depth))


def che(cx, cy):
    """大车：一轮侧视，轮上为箱，箱前出辕，辕端横衡。"""
    out = []
    g = cy + 82                     # 地平
    wx, wy, R = cx - 40, g - 46, 44
    out.append(ring(wx, wy, R, W * 0.9, 72, 0.05))
    out.append(ring(wx, wy, R - 4, W * 0.3, 72, 0.24))
    out.append(ring(wx, wy, 9, W * 0.45, 26, 0.16))
    for k in range(8):
        a = math.pi * k / 8
        out.append(B.stroke([(wx + 9 * math.cos(a), wy + 9 * math.sin(a)),
                             (wx + (R - 5) * math.cos(a), wy + (R - 5) * math.sin(a))],
                            W * 0.34, W * 0.16, n=10, col=adapt.tone(0.2), taper_end=0.3))
    # 箱：矩形，上下沿加重，内有横档两道
    x0, y0, x1, y1 = cx - 24, g - 108, cx + 62, g - 34
    out.append(B.stroke([(x0, y1), (x0, y0), (x1, y0), (x1, y1)], W * 0.85, W * 0.28, n=40,
                        col=adapt.tone(0.06)))
    out.append(B.stroke([(x0, y0 - 6), (x1, y0 - 6)], W * 0.55, W * 0.4, n=14, col=adapt.tone(0.2)))
    for yy in (y0 + 24, y0 + 46):
        out.append(B.stroke([(x0 + 4, yy), (x1 - 4, yy)], W * 0.36, W * 0.2, n=14, col=adapt.tone(0.26)))
    # 轴：自轮心向右接箱底
    out.append(B.stroke([(wx, wy), (x1, y1 + 6)], W * 0.6, W * 0.34, n=14, col=adapt.tone(0.18)))
    # 辕：箱前斜下，衡横于端
    out.append(B.stroke([(x0 + 2, y0 + 16), (x0 - 30, y0 + 40), (x0 - 44, y0 + 64)],
                        W * 0.6, W * 0.3, n=16, col=adapt.tone(0.14), taper_end=0.3))
    out.append(B.stroke([(x0 - 56, y0 + 64), (x0 - 32, y0 + 62)], W * 0.45, W * 0.3, n=12,
                        col=adapt.tone(0.2)))
    # 地平
    out.append(B.stroke([(cx - 92, g + 4), (cx - 10, g + 2), (cx + 74, g + 4)],
                        W * 0.24, W * 0.18, n=16, col=adapt.tone(0.42)))
    return out


def yi(cx, cy):
    """毳衣：交领右衽、宽袖、束带，无人着之，只挂其形。"""
    out = []
    t = cy - 76                                 # 领口
    out.append(B.stroke([(cx - 16, t), (cx, t + 10), (cx + 18, t)], W * 0.5, W * 0.26, n=14,
                        col=adapt.tone(0.16)))
    # 右衽：左襟压右襟，自领向右下斜
    out.append(B.stroke([(cx - 16, t), (cx - 22, cy + 26), (cx - 24, cy + 64)],
                        W * 0.95, W * 0.42, n=22, col=adapt.tone(0.06), taper_end=0.2))
    out.append(B.stroke([(cx + 18, t), (cx + 22, cy + 22), (cx + 24, cy + 64)],
                        W * 0.85, W * 0.4, n=22, col=adapt.tone(0.09), taper_end=0.2))
    # 右衽之压：左襟自右肩斜下，至左腰——交领压襟只此一斜，不设中轴
    out.append(B.stroke([(cx + 18, t), (cx + 6, cy + 10), (cx - 14, cy + 30),
                         (cx - 18, cy + 46)], W * 0.62, W * 0.2, n=20,
                        col=adapt.tone(0.2), taper_end=0.3))
    # 两袖：宽，向外下垂
    for s in (-1, 1):
        out.append(B.stroke([(cx + s * 20, t + 6), (cx + s * 52, t + 22), (cx + s * 62, t + 58),
                             (cx + s * 56, t + 76)], W * 0.6, W * 0.2, n=26,
                            col=adapt.tone(0.14), taper_end=0.3))
        out.append(B.stroke([(cx + s * 56, t + 76), (cx + s * 30, t + 70)],
                            W * 0.4, W * 0.24, n=10, col=adapt.tone(0.3)))
    # 束带
    out.append(B.stroke([(cx - 26, cy + 18), (cx + 26, cy + 16)], W * 0.55, W * 0.48, n=14,
                        col=adapt.tone(0.3)))
    # 下摆：弧
    out.append(B.stroke([(cx - 24, cy + 64), (cx - 10, cy + 78), (cx + 10, cy + 78),
                         (cx + 24, cy + 64)], W * 0.7, W * 0.5, n=18, col=adapt.tone(0.12)))
    return out


def yue(cx, cy):
    """璊：赤玉璧。外圆内好，双线；玉色一 accent。"""
    out = []
    out.append(ring(cx, cy + 6, 48, W * 0.9, 80, 0.06))
    out.append(ring(cx, cy + 6, 43, W * 0.34, 80, 0.26))
    out.append(ring(cx, cy + 6, 14, W * 0.55, 30, 0.16))
    out.append(ring(cx, cy + 6, 11, W * 0.24, 30, 0.4))
    # 谷纹：外圈内一圈短弧
    for k in range(8):
        a = 2 * math.pi * k / 8 + math.pi / 8
        p = (cx + 30 * math.cos(a), cy + 6 + 30 * math.sin(a))
        out.append(B.stroke([(p[0] - 5 * math.sin(a), p[1] + 5 * math.cos(a)),
                             (p[0] + 3 * math.cos(a), p[1] + 3 * math.sin(a)),
                             (p[0] + 5 * math.sin(a), p[1] - 5 * math.cos(a))],
                            W * 0.24, W * 0.12, n=8, col=adapt.tone(0.34), taper_end=0.4))
    return out


def main():
    meta = dict(volume='王 风 · 之九', title='大　车', index='诗三百五篇 · 之七三',
                quote='大车槛槛，毳衣如菼', footer='图一 · 名物 · sj073a')
    draws = [('大车', che), ('毳衣', yi), ('璊', yue)]
    notes = ['一轮为侧，箱、辕、衡具', '交领右衽，宽袖束带', '赤玉为璧，外圈内好']
    svg = os.path.join(ROOT, 'assets', 'fig', 'sj073a-da-che.svg')
    png = os.path.join(ROOT, 'dist', 'sj073a.png')
    print('svg', P.build(meta, draws, notes, svg, png), 'B')


if __name__ == '__main__':
    main()
