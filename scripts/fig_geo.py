# -*- coding: utf-8 -*-
"""几何合成 → 轮廓 path。用 shapely 把椭圆/圆/多边形并集，Chaikin 平滑后输出 SVG path。
用于写生线描的形体：先按真实比例摆构造块，再取外沿。"""
from shapely.geometry import Polygon, Point, LineString, MultiPolygon
from shapely.ops import unary_union
from shapely import affinity
import math


def ell(cx, cy, rx, ry, rot=0.0):
    p = affinity.rotate(Point(cx, cy).buffer(1, resolution=48), 0, origin=(cx, cy))
    # 用参数化生成椭圆
    pts = [(cx + rx * math.cos(t), cy + ry * math.sin(t)) for t in [i * math.tau / 64 for i in range(64)]]
    g = Polygon(pts)
    if rot:
        g = affinity.rotate(g, rot, origin=(cx, cy))
    return g


def circle(cx, cy, r):
    return Point(cx, cy).buffer(r, resolution=32)


def poly(pts):
    return Polygon(pts)


def capsule(x1, y1, x2, y2, w):
    return LineString([(x1, y1), (x2, y2)]).buffer(w / 2, resolution=16)


def comb(*g):
    return unary_union(list(g))


def chaikin(pts, iters=3, closed=True):
    out = list(pts)
    for _ in range(iters):
        if len(out) < 3:
            break
        new = []
        n = len(out)
        rng = range(n) if closed else range(n - 1)
        for i in rng:
            p, q = out[i], out[(i + 1) % n]
            new.append((0.75 * p[0] + 0.25 * q[0], 0.75 * p[1] + 0.25 * q[1]))
            new.append((0.25 * p[0] + 0.75 * q[0], 0.25 * p[1] + 0.75 * q[1]))
        out = new
    return out


def to_path(g, step=1.0, iters=3, holes=False):
    """返回 (外轮廓 path d, 内洞 path d 列表)"""
    if isinstance(g, MultiPolygon):
        g = max(g.geoms, key=lambda p: p.area)
    ext = list(g.exterior.coords)[:-1]
    # 先按弧长重采样，避免 Chaikin 把细节削平
    ext = chaikin(ext, iters=iters)
    d = "M" + " L".join("%.2f,%.2f" % (x, y) for x, y in ext[::max(1, len(ext) // 400)]) + " Z"
    hs = []
    if holes:
        for r in g.interiors:
            hp = chaikin(list(r.coords)[:-1], iters=2)
            hs.append("M" + " L".join("%.2f,%.2f" % (x, y) for x, y in hp) + " Z")
    return d, hs


def stroke_pts(pts, w, iters=2):
    """开放折线平滑（用于翅、水纹）"""
    return chaikin(pts, iters=iters, closed=False)


# ---------- 形体：水鸟（侧视，朝右，脚底 y=100） ----------
def waterbird(scale=1.0, flip=False):
    body = ell(54, 66, 40, 14.5, rot=-6)
    chest = ell(88, 62, 15, 16)
    head = circle(100, 36, 9.5)
    neck = capsule(88, 52, 97, 44, 14)
    beak = poly([(107, 33), (126, 37), (107, 43)])
    tail = poly([(18, 55), (1, 47), (5, 66), (22, 72)])
    g = comb(body, chest, head, neck, beak, tail)
    d, _ = to_path(g, iters=3)
    return g, d


if __name__ == "__main__":
    g, d = waterbird()
    print(len(d))
