# -*- coding: utf-8 -*-
"""带笔压的白描工具：沿折线生成变宽笔触轮廓。"""
import numpy as np
from shapely.geometry import LineString, Polygon


def _norm(pts):
    return [(float(x), float(y)) for x, y in pts]


def taper(pts, w_mid, w_end=0.35, n=48, power=0.55, cap_round=True):
    """沿折线取等距点，宽度按 sin^power 分布：中间 w_mid，两端 w_end。"""
    ls = LineString(_norm(pts))
    L = ls.length
    if L < 0.5:
        return ''
    left, right = [], []
    for i in range(n + 1):
        t = i / n
        p = ls.interpolate(t * L)
        q = ls.interpolate(min(t * L + 0.8, L))
        r = ls.interpolate(max(t * L - 0.8, 0.0))
        dx, dy = q.x - r.x, q.y - r.y
        ln = (dx * dx + dy * dy) ** 0.5 or 1.0
        nx, ny = -dy / ln, dx / ln
        w = w_end + (w_mid - w_end) * (np.sin(np.pi * t) ** power)
        h = w / 2.0
        left.append((p.x + nx * h, p.y + ny * h))
        right.append((p.x - nx * h, p.y - ny * h))
    d = ['M%.2f,%.2f' % left[0]]
    for x, y in left[1:]:
        d.append('L%.2f,%.2f' % (x, y))
    for x, y in reversed(right):
        d.append('L%.2f,%.2f' % (x, y))
    d.append('Z')
    return ' '.join(d)


def ribbon(pts, w, **kw):
    """等宽带（杆、梁），两端可收。"""
    return taper(pts, w, w_end=kw.pop('w_end', w * 0.82), power=0.3, **kw)


def leafshape(cx, cy, length, width, tilt=0.0, tip=0.55):
    """一片羽/叶的闭合轮廓，带中轴。"""
    cos, sin = np.cos(tilt), np.sin(tilt)
    x0, y0 = 0.0, -length * 0.5
    x1, y1 = 0.0, length * 0.5
    pts = []
    for t in np.linspace(0, 1, 26):
        yy = y0 + (y1 - y0) * t
        xx = width * (np.sin(np.pi * t) ** tip) * 0.5
        pts.append((xx, yy))
    for t in np.linspace(1, 0, 26):
        yy = y0 + (y1 - y0) * t
        xx = -width * (np.sin(np.pi * t) ** tip) * 0.5
        pts.append((xx, yy))
    out = []
    for x, y in pts:
        out.append((cx + x * cos - y * sin, cy + x * sin + y * cos))
    d = 'M%.2f,%.2f' % out[0]
    for x, y in out[1:]:
        d.append('L%.2f,%.2f' % (x, y))
    d.append('Z')
    axis = 'M%.2f,%.2f L%.2f,%.2f' % (
        cx - (length * 0.5) * sin, cy - (length * 0.5) * cos,
        cx + (length * 0.5) * sin, cy + (length * 0.5) * cos)
    return ' '.join(d), axis


def qbez(p0, p1, p2, n=24):
    pts = []
    for t in np.linspace(0, 1, n + 1):
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts
