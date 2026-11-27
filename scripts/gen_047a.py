# -*- coding: utf-8 -*-
"""047 君子偕老 · 图一

三句：
 一 副笄 —— 笄横贯发，两端垂瑱
 二 六珈 —— 笄上垂玉六枚，等距为列
 三 象服 —— 交领右衽，衣缘有文（「象服是宜」）
三物皆礼器与衣冠，几何可成，不待底本。
"""
import math
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import svgbrush as B  # noqa: E402
import adapt  # noqa: E402
import fig_page as P  # noqa: E402


def fu_ji(cx, cy, h=180):
    """副笄：髻上一道横笄贯之，两端垂瑱。笄是主角，髻是它的承。"""
    out = []
    w = adapt.w_of(h)
    # 发髻（覆发之「副」）：椭圆，内三道发缕
    ring = [(cx + 27 * math.cos(math.pi * 2 * k / 32),
             cy + 6 + 19 * math.sin(math.pi * 2 * k / 32)) for k in range(32)]
    out.append(B.stroke_closed(ring, w * 0.68, adapt.tone(0.12), pad=4))
    for dx in (-13, 0, 13):
        out.append(B.stroke([(cx + dx, cy - 8), (cx + dx * 1.15, cy + 20)],
                            w * 0.26, w * 0.16, n=8, col=adapt.tone(0.46), taper_end=0.5))
    # 横笄：贯髻而过，两端出尖
    out.append(B.stroke([(cx - 74, cy + 2), (cx - 34, cy + 0), (cx, cy - 1),
                         (cx + 34, cy + 0), (cx + 74, cy + 2)],
                        w * 0.9, w * 0.22, n=44, col=adapt.tone(0.04), taper_end=0.45))
    # 两端垂瑱：绳 + 水滴玉
    for sx in (-1, 1):
        x = cx + sx * 72
        out.append(B.stroke([(x, cy + 4), (x, cy + 32)], w * 0.28, w * 0.26, n=10, col=adapt.tone(0.28)))
        out.append(B.stroke_closed([(x - 7, cy + 38), (x + 7, cy + 38), (x + 5, cy + 50),
                                    (x, cy + 58), (x - 5, cy + 50)],
                                   w * 0.52, adapt.tone(0.1), pad=3))
        out.append(B.stroke([(x - 5, cy + 43), (x + 5, cy + 43)], w * 0.18, n=6, col=adapt.tone(0.44)))
    return out


def liu_jia(cx, cy, h=150):
    """六珈：六枚圭形玉，三列两行，每枚上系一绳。等距为列，不为美观而错落。"""
    out = []
    w = adapt.w_of(h)
    dx, dy = 52, 62
    for r in range(2):
        for c in range(3):
            gx = cx + (c - 1) * dx
            gy = cy - dy / 2 + r * dy
            # 系绳
            out.append(B.stroke([(gx, gy - 34), (gx, gy - 14)], w * 0.22, w * 0.18, n=6,
                                col=adapt.tone(0.44)))
            # 圭形：上窄下宽，下端一尖
            out.append(B.stroke_closed([(gx - 5, gy - 12), (gx + 5, gy - 12),
                                        (gx + 8, gy + 6), (gx, gy + 16), (gx - 8, gy + 6)],
                                       w * 0.62, adapt.tone(0.11), pad=3))
            # 玉上一道横纹
            out.append(B.stroke([(gx - 6, gy - 4), (gx + 6, gy - 4)], w * 0.2, w * 0.2, n=6,
                                col=adapt.tone(0.42)))
    return out


def xiang_fu(cx, cy, h=176):
    """象服：交领右衽，宽袖，下裳。衣缘一路纹（等距小回文）。软笔。"""
    out = []
    w = adapt.w_of(h)
    # 肩与领
    out.append(B.stroke([(cx - 46, cy - 72), (cx - 20, cy - 80), (cx + 20, cy - 80), (cx + 46, cy - 72)],
                        w * 0.62, w * 0.55, n=22, col=adapt.tone(0.12)))
    # 交领 V（右衽：左片压右片，故左线在上）
    out.append(B.stroke([(cx - 20, cy - 78), (cx - 2, cy - 26), (cx + 18, cy - 78)],
                        w * 0.55, w * 0.45, n=22, col=adapt.tone(0.1)))
    out.append(B.stroke([(cx - 18, cy - 76), (cx + 6, cy - 24), (cx + 24, cy - 74)],
                        w * 0.4, w * 0.34, n=20, col=adapt.tone(0.3)))
    # 右衽掩襟：左片向右掩，自领口斜下
    out.append(B.stroke([(cx + 4, cy - 24), (cx + 14, cy + 4), (cx + 2, cy + 30)],
                        w * 0.42, 0.3, n=14, col=adapt.tone(0.18)))
    # 两袖
    for sx in (-1, 1):
        out.append(B.stroke([(cx + sx * 46, cy - 72), (cx + sx * 66, cy - 30),
                             (cx + sx * 62, cy + 6)], w * 0.58, w * 0.4, n=22, col=adapt.tone(0.12)))
        # 袖口
        out.append(B.stroke([(cx + sx * 66, cy - 30), (cx + sx * 60, cy - 8),
                             (cx + sx * 62, cy + 4)], w * 0.42, w * 0.34, n=14, col=adapt.tone(0.3)))
    # 裳（下摆）：两缘外张
    for sx in (-1, 1):
        out.append(B.stroke([(cx + sx * 46, cy - 8), (cx + sx * 34, cy + 40), (cx + sx * 50, cy + 66)],
                            w * 0.6, w * 0.45, n=20, col=adapt.tone(0.14)))
    out.append(B.stroke([(cx - 50, cy + 66), (cx, cy + 62), (cx + 50, cy + 66)],
                        w * 0.6, 0.5, n=18, col=adapt.tone(0.06)))
    # 衣缘：下摆内侧一道平行线
    out.append(B.stroke([(cx - 44, cy + 58), (cx, cy + 55), (cx + 44, cy + 58)],
                        w * 0.34, w * 0.3, n=16, col=adapt.tone(0.34)))
    # 缘上小回文六枚（等距）
    for i in range(5):
        gx = cx - 40 + i * 20
        gy = cy + 57
        out.append(B.stroke([(gx, gy - 4), (gx + 7, gy - 4), (gx + 7, gy + 2),
                             (gx, gy + 2), (gx, gy - 4)],
                            w * 0.24, w * 0.2, n=12, col=adapt.tone(0.38)))
    return out


def main():
    meta = dict(volume='鄘 风 · 四', title='君 子 偕 老', index='诗三百五篇 · 之四七',
                quote='副笄六珈，象服是宜', footer='图一 · 名物 · sj047a')
    draws = [('副笄', fu_ji), ('六珈', liu_jia), ('象服', xiang_fu)]
    notes = ['笄横贯发，两端垂瑱', '六玉为列，系以丝绳', '交领右衽，缘上回文']
    svg = os.path.join(ROOT, 'assets', 'fig', 'sj047a-jun-zi-xie-lao.svg')
    png = os.path.join(ROOT, 'dist', 'sj047a.png')
    print('svg', P.build(meta, draws, notes, svg, png), 'B')


if __name__ == '__main__':
    main()
