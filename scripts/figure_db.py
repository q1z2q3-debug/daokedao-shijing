# -*- coding: utf-8 -*-
"""几何构建人形骨架（figure_db）

思路：人形的可辨性不靠手感，靠五个可算的量——
  1 头：椭圆（rx, ry 两个参数）
  2 颈：从头下缘截取的等宽带（布尔相减）
  3 肩：自颈端外斜的切线，角度固定 32°
  4 发际：头椭圆上一段等角弧（起止角可调）
  5 垂束：两条向同一尖点收敛的曲线，束根另加两道「结」
全部点由参数与镜像生成，左右严格对称；换视角只换角区间，不改手工锚点。

用法：
    from figure_db import head, shoulder, hair_cap, two_mao, build_liangmao
    strokes = build_liangmao(cx, cy, scale=1.0, view='back')
"""
import math

import svgbrush as B

DEFAULTS = dict(
    rx=40.0,          # 头半宽
    ry=46.0,          # 头半高
    neck_hw=13.5,     # 颈半宽
    neck_len=20.0,    # 颈长
    shoulder_hw=40.0,  # 肩端半距
    shoulder_drop=15.0,
    bundle_hw_root=17.0,   # 束根宽
    bundle_len=88.0,       # 束长（自束根下垂）
    bundle_flare=4.0,      # 束中段外扩
)


def _mirror(pts, sx):
    return [(sx * x, y) for x, y in pts]


def ellipse(cx, cy, rx, ry, a0=0.0, a1=360.0, n=64, cx_off=0.0):
    """角度自正上方计（-90° 为顶），顺时针为正。"""
    out = []
    for k in range(n + 1):
        a = math.radians(a0 + (a1 - a0) * k / n - 90.0)
        out.append((cx + rx * math.cos(a) + cx_off, cy + ry * math.sin(a)))
    return out


def head_shape(cx, cy, rx, ry, n=150, taper=0.20):
    """蛋形：上半为正椭圆，下半按 taper 收窄——人颅骨前宽后窄，正圆即呆。"""
    pts = []
    for k in range(n):
        t = 2 * math.pi * k / n - math.pi / 2
        c, s = math.cos(t), math.sin(t)
        fx = 1.0 if s <= 0 else 1.0 - taper * (s ** 1.4)
        pts.append((cx + rx * fx * c, cy + ry * s))
    return pts


def head(cx, cy, rx, ry, n=150):
    return B.stroke_closed(head_shape(cx, cy, rx, ry, n=n), 0.95, B.INK, n=300, pad=12)


def shoulder(cx, cy, p):
    """颈两条 + 肩两条斜线（切线角度由 p 决定，不用眼定）。"""
    out = []
    ty = cy + p['ry'] * 0.95            # 颈起点：头下缘
    for sx in (-1, 1):
        out.append(B.stroke([(cx + sx * p['neck_hw'], ty - 4),
                             (cx + sx * p['neck_hw'], ty + p['neck_len'])], 0.34, n=12, col=B.INK2))
        out.append(B.stroke([(cx + sx * p['neck_hw'], ty + p['neck_len']),
                             (cx + sx * (p['neck_hw'] + 12), ty + p['neck_len'] + 6),
                             (cx + sx * p['shoulder_hw'], ty + p['neck_len'] + p['shoulder_drop'])],
                            0.58, 0.3, n=24))
    return out


def hair_cap(cx, cy, p, a_span=(-58, 58), step=16):
    """发际：头椭圆上的一段等角弧，半径外扩 1.03（发在皮外）。"""
    out = []
    for d in range(step, int(a_span[1]), step):
        pass
    out.append(B.stroke(ellipse(cx, cy, p['rx'] * 1.03, p['ry'] * 1.03,
                                a_span[0], a_span[1], n=48), 0.8, 0.75, n=54))
    return out


def hair_strands(cx, cy, p, angles=(18, 36, 54), ratio=0.9):
    """发缕：沿头椭圆的等角弧，自顶向下，长度到中分线下端。"""
    out = []
    for a in angles:
        for sx in (-1, 1):
            arc = []
            for k in range(12):
                t = a * k / 11
                rad = math.radians(t * sx - 90 + 0)
                rx, ry = p['rx'] * ratio, p['ry'] * ratio
                arc.append((cx + rx * math.cos(rad), cy + ry * math.sin(rad)))
            out.append(B.hair(arc, 0.26, B.GREY))
    return out


def two_mao(cx, cy, p, root_y=None):
    """两束垂发：束根贴头两侧，中段外扩，两线收敛于同一尖点。

    这是几何构建的要害——束不是「画一条辫子」，而是
    「一条外缘曲线与一条内缘曲线求交于尖点」，宽度便由两者之差自动成立。
    """
    out = []
    ry = p['ry']
    root_y = cy - ry * 0.42 if root_y is None else cy + root_y
    len_ = p['bundle_len']
    flare = p['bundle_flare']
    # 束根落在头椭圆上该 y 处的横坐标，束外缘再外 4px（发的厚度）
    rel = max(-0.98, min(0.98, (root_y - cy) / ry))
    x_at = p['rx'] * math.sqrt(max(0.0, 1 - rel ** 2))
    for sx in (-1, 1):
        x_out = cx + sx * (x_at + 4.0)
        x_in = cx + sx * (x_at - p['bundle_hw_root'] * 0.62)
        tip = (cx + sx * (x_at - p['bundle_hw_root'] * 0.30), root_y + len_)
        outer = [(x_out, root_y),
                 (cx + sx * (x_at + 4.0 + flare), root_y + len_ * 0.42),
                 (cx + sx * (x_at + 6.0 + flare * 0.7), root_y + len_ * 0.76),
                 tip]
        inner = [(x_in, root_y),
                 (cx + sx * (x_at - p['bundle_hw_root'] * 0.20), root_y + len_ * 0.42),
                 (cx + sx * (x_at - p['bundle_hw_root'] * 0.28), root_y + len_ * 0.74),
                 tip]
        out.append(B.stroke(outer, 0.85, 0.3, n=46, taper_end=0.5))
        out.append(B.stroke(inner, 0.62, 0.22, n=44, taper_end=0.5, col=B.INK2))
        # 束内发缕：按两缘插值取中线，不手摆
        mid = [(outer[i][0] * 0.6 + inner[i][0] * 0.4,
                outer[i][1] * 0.6 + inner[i][1] * 0.4) for i in range(4)]
        out.append(B.hair(mid, 0.24, B.GREY))
        # 束结：一道短弧，只在束宽之内
        out.append(B.stroke([(x_in, root_y + 4), ((x_in + x_out) / 2, root_y + 2),
                             (x_out, root_y + 1)], 0.34, n=14, col=B.INK2))

    return out


def build_liangmao(cx, cy, scale=1.0, view='back', **kw):
    p = dict(DEFAULTS)
    p.update(kw)
    for k in ('rx', 'ry', 'neck_hw', 'neck_len', 'shoulder_hw', 'shoulder_drop',
              'bundle_hw_root', 'bundle_len', 'bundle_flare'):
        p[k] *= scale
    out = []
    out.append(head(cx, cy, p['rx'], p['ry']))
    out += shoulder(cx, cy, p)
    if view == 'back':
        out.append(B.stroke([(cx, cy - p['ry'] * 0.96), (cx, cy - p['ry'] * 0.45),
                             (cx, cy + p['ry'] * 0.05), (cx, cy + p['ry'] * 0.42)],
                            0.5, n=36, col=B.INK2))
        out += hair_strands(cx, cy, p)
    else:
        out += hair_cap(cx, cy, p)
    out += two_mao(cx, cy, p)
    return out
