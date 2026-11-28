# -*- coding: utf-8 -*-
"""075 缁衣 · 图一

三格：缁衣（黑而不闷，以密线代色）／馆（门、堂、阶）／粲（簋与饭）。
三物即好贤之三级：养其体、安其居、饱其腹。
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


def zi_yi(cx, cy):
    """缁衣：交领右衽、宽袖、束带、下裳两片。黑以密线出，不以墨块。"""
    out = []
    top, g = cy - 74, cy + 80
    waist = cy + 6
    # 两肩与身廓
    out.append(B.stroke([(cx - 34, top + 10), (cx - 40, cy - 30), (cx - 40, waist),
                         (cx - 40, g)], W * 0.85, W * 0.35, n=26, col=adapt.tone(0.06),
                        taper_end=0.2))
    out.append(B.stroke([(cx + 34, top + 10), (cx + 40, cy - 30), (cx + 40, waist),
                         (cx + 40, g)], W * 0.85, W * 0.35, n=26, col=adapt.tone(0.06),
                        taper_end=0.2))
    # 领：交领为 V，右衽自右肩斜下
    out.append(B.stroke([(cx - 20, top), (cx, top + 22), (cx + 20, top)], W * 0.6, W * 0.3, n=14,
                        col=adapt.tone(0.14)))
    out.append(B.stroke([(cx + 20, top), (cx + 14, cy - 36), (cx - 6, cy - 8)],
                        W * 0.55, W * 0.24, n=16, col=adapt.tone(0.2), taper_end=0.3))
    # 两袖：宽而垂，袖口双线
    for s in (-1, 1):
        out.append(B.stroke([(cx + s * 40, cy - 34), (cx + s * 62, cy - 10), (cx + s * 66, cy + 40),
                             (cx + s * 58, cy + 58)], W * 0.6, W * 0.24, n=24,
                            col=adapt.tone(0.12), taper_end=0.3))
        out.append(B.stroke([(cx + s * 58, cy + 58), (cx + s * 44, cy + 56)],
                            W * 0.4, W * 0.26, n=10, col=adapt.tone(0.26)))
    # 束带：双横
    out.append(B.stroke([(cx - 41, waist), (cx + 41, waist - 2)], W * 0.6, W * 0.5, n=14,
                        col=adapt.tone(0.3)))
    out.append(B.stroke([(cx - 38, waist + 8), (cx + 38, waist + 6)], W * 0.3, W * 0.24, n=12,
                        col=adapt.tone(0.4)))
    # 下裳：中缝一竖，两片
    out.append(B.stroke([(cx, waist + 10), (cx - 2, g)], W * 0.3, W * 0.22, n=14,
                        col=adapt.tone(0.36)))
    # 缁：密线十道，短而不齐（本色最深，非墨块）
    for k in range(10):
        x = cx - 30 + k * 6.6
        y0 = cy - 24 + (k % 3) * 5
        y1 = waist - 6 - (k % 2) * 6
        out.append(B.stroke([(x, y0), (x + (1.2 if k % 2 else -1.2), y1)],
                            W * 0.2, W * 0.11, n=10, col=adapt.tone(0.34), taper_end=0.6))
    return out


def guan(cx, cy):
    """馆：立柱、楣梁、双扇门、两坡屋顶、三级阶。"""
    out = []
    g = cy + 82
    x0, x1 = cx - 58, cx + 58
    eave, base = cy - 40, cy + 56
    for x in (x0, x1):
        out.append(B.stroke([(x, eave), (x, base)], W * 0.7, W * 0.5, n=18, col=adapt.tone(0.1)))
    out.append(B.stroke([(x0 - 8, eave), (x0 + 8, eave), (x1 - 8, eave), (x1 + 8, eave)],
                        W * 0.5, W * 0.36, n=12, col=adapt.tone(0.2)))
    # 屋顶：两坡有脊，檐出
    apex = (cx, cy - 92)
    out.append(B.stroke([(x0 - 16, eave - 4), (cx - 26, cy - 70), apex, (cx + 26, cy - 70),
                         (x1 + 16, eave - 4)], W * 0.6, W * 0.28, n=30,
                        col=adapt.tone(0.08), taper_end=0.25))
    out.append(B.stroke([(x0 - 16, eave - 4), (x1 + 16, eave - 4)], W * 0.4, W * 0.3, n=14,
                        col=adapt.tone(0.28)))
    # 门：双扇，中缝
    out.append(B.stroke([(cx - 22, base), (cx - 22, cy - 6), (cx + 22, cy - 6), (cx + 22, base)],
                        W * 0.55, W * 0.3, n=26, col=adapt.tone(0.14)))
    out.append(B.stroke([(cx, cy - 6), (cx, base)], W * 0.3, W * 0.22, n=12, col=adapt.tone(0.36)))
    for s in (-1, 1):
        out.append(B.oval(cx + s * 6, cy + 22, 1.8, 1.8, w=W * 0.24, col=adapt.tone(0.34), n=10))
    # 阶：三级，向外张
    for k in range(3):
        y = base + 4 + k * 8
        out.append(B.stroke([(cx - 30 - k * 9, y), (cx + 30 + k * 9, y)],
                            W * 0.34, W * 0.24, n=12, col=adapt.tone(0.3)))
    out.append(B.stroke([(cx - 76, g + 6), (cx - 20, g + 4), (cx + 20, g + 4), (cx + 76, g + 6)],
                        W * 0.24, W * 0.18, n=16, col=adapt.tone(0.42)))
    return out


def can(cx, cy):
    """粲：簋——口沿、腹两段收、圈足、双环耳，器中饭作堆弧。"""
    out = []
    g = cy + 72
    ry, rx = 11.0, 44.0
    ct = cy - 6                     # 口沿中心
    # 口沿：上下两道，上实下淡
    out.append(B.stroke(elliptic(cx, ct, rx, ry, 34), W * 0.62, W * 0.26, n=52,
                        col=adapt.tone(0.1)))
    out.append(B.stroke(elliptic(cx, ct + 6, rx - 2, ry, 34), W * 0.3, W * 0.2, n=52,
                        col=adapt.tone(0.36)))
    # 腹：上段缓收至腰，下段急收至足口
    waist_y, waist_r = ct + 30, 34
    foot_y, foot_r = g - 14, 18
    for s in (-1, 1):
        out.append(B.stroke([(cx + s * rx, ct + 2), (cx + s * 41, ct + 14),
                             (cx + s * waist_r, waist_y)], W * 0.55, W * 0.28, n=20,
                            col=adapt.tone(0.12), taper_end=0.3))
        out.append(B.stroke([(cx + s * waist_r, waist_y), (cx + s * 24, foot_y - 8),
                             (cx + s * foot_r, foot_y)], W * 0.5, W * 0.26, n=18,
                            col=adapt.tone(0.16), taper_end=0.3))
    # 腰线：一圈横短弧
    out.append(B.stroke(elliptic(cx, waist_y, waist_r, 5.0, 24), W * 0.28, W * 0.18, n=40,
                        col=adapt.tone(0.4)))
    # 圈足：底沿 + 两侧
    out.append(B.stroke(elliptic(cx, foot_y, foot_r, 5.0, 24), W * 0.5, W * 0.3, n=40,
                        col=adapt.tone(0.14)))
    out.append(B.stroke([(cx - foot_r, foot_y), (cx - foot_r, g), (cx + foot_r, g),
                         (cx + foot_r, foot_y)], W * 0.5, W * 0.3, n=20, col=adapt.tone(0.14)))
    # 双环耳：自口沿侧外上，环双线
    for s in (-1, 1):
        out.append(B.oval(cx + s * (rx + 6), ct + 4, 7.4, 9.4, w=W * 0.3, col=adapt.tone(0.2), n=20))
        out.append(B.oval(cx + s * (rx + 6), ct + 4, 3.8, 5.2, w=W * 0.2, col=adapt.tone(0.42), n=16))
    # 饭：口沿内三弧堆起，中高旁低
    for k, (rr, h) in enumerate(((34, 6), (24, 11), (12, 14))):
        out.append(B.stroke([(cx - rr, ct - 1), (cx - rr * 0.5, ct - 1 - h * 0.8),
                             (cx + rr * 0.5, ct - 1 - h * 0.8), (cx + rr, ct - 1)],
                            W * 0.26, W * 0.14, n=16, col=adapt.tone(0.28 + k * 0.04),
                            taper_end=0.45))
    return out


def elliptic(cx, cy, rx, ry, n=40):
    return [(cx + rx * math.cos(2 * math.pi * k / n), cy + ry * math.sin(2 * math.pi * k / n))
            for k in range(n + 1)]


def main():
    meta = dict(volume='郑 风 · 之一', title='缁　衣', index='诗三百五篇 · 之七五',
                quote='缁衣之宜兮，敝予又改为兮', footer='图一 · 名物 · sj075a')
    draws = [('缁衣', zi_yi), ('馆', guan), ('粲', can)]
    notes = ['卿士正服，黑而密，敝则改之', '门、堂、阶：适子之馆', '簋盛饭：还予授子之粲']
    svg = os.path.join(ROOT, 'assets', 'fig', 'sj075a-zi-yi.svg')
    png = os.path.join(ROOT, 'dist', 'sj075a.png')
    print('svg', P.build(meta, draws, notes, svg, png), 'B')


if __name__ == '__main__':
    main()
