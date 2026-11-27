# -*- coding: utf-8 -*-
"""050 定之方中 · 图一

三句：
 一 宫室 —— 楚宫：台基、五柱等距、庑殿起翘（几何模数）
 二 揆日 —— 立表测影：表一、影两道、晷弧一刻
 三 树   —— 榛栗椅桐梓漆，四株错落（取树干锥度 + 冠形四式）

宫室可由模数算出：柱距 31、柱高 86、檐出 12、脊高 36。
揆日靠角度：影长取表高之 0.9，日高取 52°。
"""
import math
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import svgbrush as B  # noqa: E402
import adapt  # noqa: E402
import fig_page as P  # noqa: E402

W = 0.47


# ── 一 宫室 ─────────────────────────────────────────────
def hall(cx, cy):
    out = []
    w = W
    base = cy + 44          # 台基面
    eave = cy - 44          # 檐口
    ridge = cy - 80         # 屋脊
    # 台基：两层线，下宽上窄（收分）
    out.append(B.stroke([(cx - 76, base + 14), (cx + 76, base + 14)],
                        w * 0.8, w * 0.55, n=20, col=adapt.tone(0.3)))
    out.append(B.stroke([(cx - 70, base + 14), (cx - 70, base),
                         (cx + 70, base), (cx + 70, base + 14)],
                        w * 0.7, w * 0.7, n=26, col=adapt.tone(0.26)))
    out.append(B.stroke([(cx - 74, base), (cx + 74, base)],
                        w * 0.9, w * 0.6, n=20, col=adapt.tone(0.14)))
    # 五柱，等距 31；柱脚落台基、柱头托檐
    xs = [cx - 62, cx - 31, cx, cx + 31, cx + 62]
    for i, x in enumerate(xs):
        vs = w * (0.85 if i in (0, 4) else 0.72)   # 角柱略重
        out.append(B.stroke([(x - 3.2, base), (x - 3.0, base - 40),
                             (x - 2.6, eave)], vs, vs * 0.5, n=18, col=adapt.tone(0.1)))
        out.append(B.stroke([(x + 3.2, base), (x + 3.0, base - 40),
                             (x + 2.6, eave)], vs, vs * 0.5, n=18, col=adapt.tone(0.1)))
        # 柱头斗：一小横
        out.append(B.stroke([(x - 6, eave + 1), (x + 6, eave + 1)],
                            w * 0.55, w * 0.45, n=8, col=adapt.tone(0.24)))
    # 阑额：柱头间一横
    out.append(B.stroke([(cx - 68, eave), (cx + 68, eave)],
                        w * 0.9, w * 0.6, n=24, col=adapt.tone(0.12)))
    # 门窗：当心间一门（左右各一窗，略小）
    out.append(B.stroke([(cx - 9, base), (cx - 9, base - 46), (cx + 9, base - 46), (cx + 9, base)],
                        w * 0.5, w * 0.5, n=20, col=adapt.tone(0.34)))
    for sx in (-1, 1):
        out.append(B.stroke([(cx + sx * 22 - 7, base - 16), (cx + sx * 22 - 7, base - 40),
                             (cx + sx * 22 + 7, base - 40), (cx + sx * 22 + 7, base - 16)],
                            w * 0.42, w * 0.42, n=16, col=adapt.tone(0.4)))
    # 屋顶：两坡切弧，脊横，两端起翘
    for sx in (-1, 1):
        p0 = (cx + sx * 78, eave - 4)          # 檐角（起翘 4）
        p1 = (cx + sx * 40, ridge + 12)
        p2 = (cx + sx * 22, ridge)
        pts = [p0, ((p0[0] + p1[0]) / 2, p0[1] - 16), p1, p2]
        out.append(B.stroke(pts, w * 1.05, w * 0.6, n=30, col=adapt.tone(0.06), taper_end=0.25))
        # 檐口垂线（瓦口）
        out.append(B.stroke([p0, (p0[0], eave + 2)], w * 0.4, w * 0.3, n=8, col=adapt.tone(0.3)))
    out.append(B.stroke([(cx - 22, ridge), (cx + 22, ridge)],
                        w * 1.0, w * 0.8, n=16, col=adapt.tone(0.06)))
    # 鸱尾：脊端两小竖，微内曲
    for sx in (-1, 1):
        out.append(B.stroke([(cx + sx * 22, ridge), (cx + sx * 24, ridge - 9)],
                            w * 0.6, w * 0.25, n=10, col=adapt.tone(0.1), taper_end=0.55))
    # 屋面瓦纹：六道，斜随坡
    for k in range(6):
        f = k / 5.0
        x = cx - 66 + 132 * f
        top = ridge + abs(x - cx) * 0.55
        out.append(B.stroke([(x, top), (x, eave - 3)], w * 0.24, w * 0.2, n=10,
                            col=adapt.tone(0.44), taper_start=0.4, taper_end=0.4))
    return out


# ── 二 揆日 ─────────────────────────────────────────────
def gnomon(cx, cy):
    out = []
    w = W
    foot = cy + 40
    top = cy - 46
    # 表：一根竖杆，两线成柱（下有础）
    out.append(B.stroke([(cx - 3.4, foot), (cx - 2.6, top)], w * 1.0, w * 0.4, n=18,
                        col=adapt.tone(0.06)))
    out.append(B.stroke([(cx + 3.4, foot), (cx + 2.6, top)], w * 1.0, w * 0.4, n=18,
                        col=adapt.tone(0.06)))
    out.append(B.stroke([(cx - 8, foot), (cx + 8, foot)], w * 0.6, w * 0.4, n=10,
                        col=adapt.tone(0.2)))
    out.append(B.stroke([(cx - 11, foot + 5), (cx + 11, foot + 5)], w * 0.45, w * 0.3, n=10,
                        col=adapt.tone(0.3)))
    # 影：自表底斜出的一道窄楔（起处贴足、尽处收锋），不是一条粗坡
    ang = math.radians(33)
    L = 86
    tip = (cx + L * math.cos(ang), foot + L * math.sin(ang))
    for off in (-1.8, 1.8):
        out.append(B.stroke([(cx + 4, foot + off * 0.6),
                             (cx + L * 0.5 * math.cos(ang), foot + L * 0.5 * math.sin(ang) + off),
                             (tip[0], tip[1] + off * 0.3)],
                            w * 0.44, w * 0.12, n=20, col=adapt.tone(0.3),
                            taper_start=0.25, taper_end=0.75))
    # 晷弧：仍以表底为心，半径收到 66，只取影那一侧（-50°→4°）
    arcs = []
    for k in range(36):
        t = math.radians(-62 + 76 * k / 35)
        arcs.append((cx + 66 * math.cos(t), foot + 66 * math.sin(t)))
    out.append(B.stroke(arcs, w * 0.32, w * 0.3, n=36, col=adapt.tone(0.5),
                        taper_start=0.3, taper_end=0.4))
    # 刻度：六道短垂，贴弧外侧
    for k in range(6):
        t = math.radians(-56 + 13 * k)
        p = (cx + 66 * math.cos(t), foot + 66 * math.sin(t))
        q = (cx + 73 * math.cos(t), foot + 73 * math.sin(t))
        out.append(B.stroke([p, q], w * 0.22, w * 0.18, n=6, col=adapt.tone(0.6)))
    # 日：一淡圆 + 三道光，不在天上画满
    sx, sy = cx - 30, cy - 82
    out.append(B.oval(sx, sy, 9, 9, w=w * 0.34, col=adapt.tone(0.5), n=24))
    for a in (math.radians(150), math.radians(180), math.radians(210)):
        out.append(B.stroke([(sx + 13 * math.cos(a), sy + 13 * math.sin(a)),
                             (sx + 21 * math.cos(a), sy + 21 * math.sin(a))],
                            w * 0.24, w * 0.14, n=6, col=adapt.tone(0.62), taper_end=0.5))
    # 连光：自日到表头的两道短线，示「揆」的指向
    for d in (-1, 1):
        out.append(B.stroke([(sx + 12, sy + 6 * d), (cx - 5, top - 2 + 6 * d)],
                            w * 0.16, w * 0.12, n=14, col=adapt.tone(0.74), taper_end=0.4))
    return out


# ── 三 树 ─────────────────────────────────────────────
def leaf(cx, cy, ang, ln=20, wd=7, w=0.3, depth=0.2):
    ca, sa = math.cos(ang), math.sin(ang)
    side = (-sa * wd, ca * wd)
    mid = (cx + ln * 0.45 * ca, cy + ln * 0.45 * sa)
    tip = (cx + ln * ca, cy + ln * sa)
    out = [B.stroke([(cx, cy), (mid[0] + side[0], mid[1] + side[1]), tip],
                    w, w * 0.2, n=14, col=adapt.tone(depth), taper_end=0.55),
           B.stroke([(cx, cy), (mid[0] - side[0], mid[1] - side[1]), tip],
                    w, w * 0.2, n=14, col=adapt.tone(depth), taper_end=0.55)]
    return out


def crown(cx, cy, r, style, n=7, w=0.3, depth=0.2):
    """冠四式：round 圆冠／cone 锥冠／umbrella 伞冠／droop 垂冠。"""
    out = []
    if style == 'cone':
        angs = [math.radians(a) for a in (-118, -102, -88, -74, -58)]
        for a, ln in zip(angs, (r * 0.75, r * 0.95, r * 1.1, r * 0.95, r * 0.75)):
            out += leaf(cx, cy, a, ln, 3.4, w * 0.9, depth)
    elif style == 'umbrella':
        for k in range(7):
            a = math.radians(184 + 172 * k / 6)
            tip = (cx + r * math.cos(a), cy + r * 0.46 * math.sin(a))
            out.append(B.stroke([(cx, cy), (cx + r * 0.5 * math.cos(a), cy + r * 0.2 * math.sin(a)), tip],
                                w * 0.55, w * 0.16, n=14, col=adapt.tone(depth), taper_end=0.5))
            out += leaf(tip[0], tip[1], a + math.radians(18), 11, 3.2, w * 0.8, depth + 0.16)
            out += leaf(tip[0], tip[1], a - math.radians(22), 10, 3.2, w * 0.8, depth + 0.16)
    elif style == 'droop':
        for k in range(7):
            a = math.radians(-152 + 124 * k / 6)
            ln = r * (1.0 + 0.2 * math.sin(k))
            tip = (cx + ln * math.cos(a), cy + ln * 0.9 * math.sin(a) + r * 0.42)
            out.append(B.stroke([(cx, cy),
                                 (cx + ln * 0.66 * math.cos(a), cy + ln * 0.34 * math.sin(a) - 3),
                                 tip],
                                w * 0.5, w * 0.1, n=16, col=adapt.tone(depth), taper_end=0.7))
            out += leaf(tip[0], tip[1], math.radians(78), 9, 2.6, w * 0.7, depth + 0.24)
    else:
        # round：四主枝，各枝梢再三叶（枝是骨，叶是纹——同点发散必成星芒）
        for a in (math.radians(-150), math.radians(-112), math.radians(-74), math.radians(-36)):
            tip = (cx + r * 0.82 * math.cos(a), cy + r * 0.82 * math.sin(a))
            out.append(B.stroke([(cx, cy), (cx + r * 0.45 * math.cos(a), cy + r * 0.45 * math.sin(a)), tip],
                                w * 0.6, w * 0.16, n=14, col=adapt.tone(depth), taper_end=0.5))
            for da in (-26, 2, 30):
                out += leaf(tip[0], tip[1], a + math.radians(da), 15, 3.6, w * 0.8, depth + 0.14)
            # 次枝：一枝再分两梢
            mid = (cx + r * 0.5 * math.cos(a), cy + r * 0.5 * math.sin(a))
            for da in (-38, 34):
                t2 = (mid[0] + r * 0.34 * math.cos(a + math.radians(da)),
                      mid[1] + r * 0.34 * math.sin(a + math.radians(da)))
                out.append(B.stroke([mid, t2], w * 0.4, w * 0.14, n=8,
                                    col=adapt.tone(depth + 0.12), taper_end=0.5))
                out += leaf(t2[0], t2[1], a + math.radians(da), 11, 3.2, w * 0.75, depth + 0.2)
    return out


def tree(cx, base_y, h, style, w=W, depth=0.1):
    out = []
    out.append(B.stroke([(cx - 4, base_y), (cx - 3, base_y - h * 0.5), (cx - 1.5, base_y - h * 0.9)],
                        w * 0.9, w * 0.4, n=20, col=adapt.tone(depth), taper_end=0.3))
    out.append(B.stroke([(cx + 4, base_y), (cx + 3, base_y - h * 0.5), (cx + 1.5, base_y - h * 0.9)],
                        w * 0.9, w * 0.4, n=20, col=adapt.tone(depth), taper_end=0.3))
    top = (cx, base_y - h * 0.9)
    r = h * 0.42
    if style == 'droop':
        out.append(B.stroke([top, (cx - 2, top[1] - 6), (cx + 2, top[1] - 10)],
                            w * 0.6, w * 0.3, n=10, col=adapt.tone(depth), taper_end=0.4))
    out += crown(top[0], top[1] - (6 if style == 'droop' else 0), r, style, w=w * 0.6, depth=depth + 0.14)
    out.append(B.stroke([(cx - 14, base_y), (cx - 5, base_y - 2), (cx + 5, base_y - 2), (cx + 14, base_y)],
                        w * 0.4, w * 0.26, n=12, col=adapt.tone(depth + 0.2)))
    return out


def sapling(cx, base_y, h, w=W, depth=0.1):
    """幼树一式：干三层、三枝、枝梢两叶。同式成行，高矮微差。"""
    out = []
    for sx in (-1, 1):
        out.append(B.stroke([(cx + sx * 3.2, base_y), (cx + sx * 2.6, base_y - h * 0.45),
                             (cx + sx * 1.4, base_y - h * 0.88)],
                            w * 0.78, w * 0.34, n=18, col=adapt.tone(depth), taper_end=0.3))
    top = (cx, base_y - h * 0.88)
    for a, ln in ((math.radians(-142), 0.46), (math.radians(-90), 0.56), (math.radians(-38), 0.46)):
        tip = (top[0] + h * ln * math.cos(a), top[1] + h * ln * math.sin(a))
        out.append(B.stroke([top, (top[0] + h * ln * 0.5 * math.cos(a), top[1] + h * ln * 0.5 * math.sin(a)),
                             tip],
                            w * 0.5, w * 0.16, n=14, col=adapt.tone(depth + 0.1), taper_end=0.45))
        for da in (-24, 22):
            out += leaf(tip[0], tip[1], a + math.radians(da), h * 0.2, 3.0, w * 0.7, depth + 0.24)
        out += leaf(tip[0], tip[1], a, h * 0.22, 3.2, w * 0.7, depth + 0.2)
    # 根：两笔外撇，示「新植未深」
    out.append(B.stroke([(cx - 12, base_y + 4), (cx - 4, base_y), (cx + 4, base_y), (cx + 12, base_y + 4)],
                        w * 0.34, w * 0.22, n=12, col=adapt.tone(depth + 0.28)))
    return out


def grove(cx, cy):
    """一行五株新植：同式、等距 34、高矮 66..88 微差。诗在「树之」，不在辨种。"""
    out = []
    base = cy + 76
    for k in range(5):
        x = cx - 68 + 34 * k
        h = 68 + (10 if k % 2 == 0 else 0) + (6 if k == 2 else 0)
        out += sapling(x, base, h)
    out.append(B.stroke([(cx - 86, base + 4), (cx + 86, base + 4)],
                        W * 0.32, W * 0.2, n=28, col=adapt.tone(0.56),
                        taper_start=0.35, taper_end=0.35))
    return out


def main():
    meta = dict(volume='鄘 风 · 四', title='定 之 方 中', index='诗三百五篇 · 之五十',
                quote='定之方中，作于楚宫', footer='图一 · 名物 · sj050a')
    draws = [('宫室', hall), ('揆日', gnomon), ('树', grove)]
    notes = ['台基五柱，庑殿起翘', '立表测影，以正方位', '榛栗椅桐梓漆，同式成行']
    svg = os.path.join(ROOT, 'assets', 'fig', 'sj050a-ding-zhi-fang-zhong.svg')
    png = os.path.join(ROOT, 'dist', 'sj050a.png')
    print('svg', P.build(meta, draws, notes, svg, png), 'B')


if __name__ == '__main__':
    main()
