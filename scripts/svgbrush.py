# -*- coding: utf-8 -*-
"""svgbrush · 白描笔法库

设计原则：
1) 一切皆线。线 = 中心折线 + 宽度函数 → 生成闭合轮廓，填充墨色即为「笔压」。
2) 三阶笔宽：轮廓 0.9 / 结构 0.5 / 细部 0.3。
3) 收锋：宽度收敛至 0，末端成尖；宽线用斜切。
4) 器物先骨后皮：先给轴线/椭圆口沿/束点，再包轮廓。
"""
import math
import numpy as np

INK, INK2, PAPER, RED, GREY = "#1F1B17", "#5C544A", "#F7F4EE", "#994433", "#9A9186"

# ---------- 基础 ----------

def _resample(pts, n=40):
    pts = np.asarray(pts, dtype=float)
    if len(pts) == 2:
        t = np.linspace(0, 1, n)[:, None]
        return pts[0] + (pts[1] - pts[0]) * t
    seg = np.linalg.norm(np.diff(pts, axis=0), axis=1)
    s = np.concatenate([[0], np.cumsum(seg)])
    total = s[-1]
    if total < 1e-6:
        return np.repeat(pts[:1], n, axis=0)
    tt = np.linspace(0, total, n)
    x = np.interp(tt, s, pts[:, 0])
    y = np.interp(tt, s, pts[:, 1])
    return np.stack([x, y], axis=1)


def _normals(P):
    d = np.gradient(P, axis=0)
    ln = np.linalg.norm(d, axis=1)
    ln[ln < 1e-9] = 1.0
    return np.stack([-d[:, 1] / ln, d[:, 0] / ln], axis=1)


def d_of_poly(pts):
    d = 'M%.2f,%.2f' % (pts[0][0], pts[0][1])
    for x, y in pts[1:]:
        d += ' L%.2f,%.2f' % (x, y)
    return d + ' Z'


def stroke(pts, w=0.9, w1=None, n=44, col=INK, taper_end=0.0, taper_start=0.0):
    """变宽笔触（填充轮廓）。taper_end>0 表示末端收锋的比例长度。"""
    P = _resample(pts, n)
    N = _normals(P)
    t = np.linspace(0, 1, n)
    w0 = float(w)
    w1 = w0 if w1 is None else float(w1)
    W = w0 + (w1 - w0) * t
    if taper_start:
        W = W * np.clip(t / taper_start, 0, 1) ** 0.7
    if taper_end:
        W = W * np.clip((1 - t) / taper_end, 0, 1) ** 0.7
    left = P + N * (W[:, None] / 2)
    right = P - N * (W[:, None] / 2)
    poly = np.vstack([left, right[::-1]])
    return '<path d="%s" fill="%s" stroke="none"/>' % (d_of_poly(poly), col)


def chaikin(pts, it=2, closed=True):
    """Chaikin 细分：折线变顺，但尖端保留（与傅里叶不同，不产生圆谐波化）。"""
    P = np.asarray(pts, float)
    for _ in range(it):
        if closed:
            nxt = np.roll(P, -1, axis=0)
            q = 0.75 * P + 0.25 * nxt
            r = 0.25 * P + 0.75 * nxt
            P = np.vstack([q, r]).reshape(2, -1, 2).transpose(1, 0, 2).reshape(-1, 2)
        else:
            Q = [P[0]]
            for i in range(len(P) - 1):
                Q.append(0.75 * P[i] + 0.25 * P[i + 1])
                Q.append(0.25 * P[i] + 0.75 * P[i + 1])
            Q.append(P[-1])
            P = np.asarray(Q)
    return P


def stroke_closed(pts, w=0.9, col=INK, n=256, pad=10):
    """闭合轮廓的变宽笔触。

    开放 stroke 在首尾接缝处法线由单侧差分给出，会突然反向，左右边界交叉成
    一根长刺（表现为横贯画布的斜线，面积小、bbox 正常，肉眼才看得出）。
    这里把头尾各接一段再算梯度，接完裁掉——接缝处的法线连续，刺消失。
    """
    P = _resample(np.vstack([np.asarray(pts, float), np.asarray(pts, float)[:1]]), n)
    P = P[:-1]
    m = len(P)
    pd = min(pad, max(1, m // 8))
    ext = np.vstack([P[-pd:], P, P[:pd]])
    N = _normals(ext)
    t = np.linspace(0, 1, len(ext))
    W = np.full(len(ext), float(w))
    left = ext + N * (W[:, None] / 2)
    right = ext - N * (W[:, None] / 2)
    poly = np.vstack([left, right[::-1]])
    # 裁掉接缝段后再闭合，避免重复的 padding 边
    keep = poly[(poly.shape[0] - pd - m):]
    return '<path d="%s" fill="%s" stroke="none"/>' % (d_of_poly(poly), col) if False else \
        '<path d="%s" fill="%s" stroke="none"/>' % (d_of_poly(np.vstack([left[pd:pd + m], right[pd:pd + m][::-1]])), col)


def hair(pts, w=0.35, col=INK2):
    """细线：直接 stroke，无笔压。"""
    return stroke(pts, w, w, col=col, n=26)


def wedge(pts, w=2.4, col=INK, n=30):
    """起笔重、收笔出尖的「撇」。"""
    return stroke(pts, w, 0.15, col=col, n=n, taper_start=0.12, taper_end=0.72)


def oval(cx, cy, rx, ry, w=0.9, col=INK, n=64, rot=0.0):
    t = np.linspace(0, 2 * math.pi, n)
    x = rx * np.cos(t)
    y = ry * np.sin(t)
    if rot:
        c, s = math.cos(rot), math.sin(rot)
        x, y = x * c - y * s, x * s + y * c
    pts = np.stack([cx + x, cy + y], axis=1)
    return stroke(pts, w, w, col=col, n=n)


def arcband(cx, cy, rx, ry, a0, a1, w=0.9, col=INK, n=40):
    t = np.linspace(a0, a1, n)
    pts = np.stack([cx + rx * np.cos(t), cy + ry * np.sin(t)], axis=1)
    return stroke(pts, w, w, col=col, n=n)


def hatch(p0, p1, count=6, length=8.0, angle=0.0, w=0.28, col=GREY, shrink=0.0):
    """一排短排线：沿 p0→p1 等距，向 angle 方向出短线。"""
    out = []
    for i in range(count):
        t = 0.0 if count == 1 else i / (count - 1)
        bx = p0[0] + (p1[0] - p0[0]) * t
        by = p0[1] + (p1[1] - p0[1]) * t
        L = length * (1 - shrink * t)
        out.append(hair([(bx, by), (bx + L * math.cos(angle), by + L * math.sin(angle))], w, col))
    return out


def shade(p0, p1, n=5, spacing=1.6, angle=math.pi / 2, length=10, w=0.26, col=GREY):
    """沿一条线段并排多根短虚线，模拟受光/背光的密集。"""
    out = []
    nx, ny = math.cos(angle), math.sin(angle)
    for i in range(n):
        t = i / max(1, n - 1)
        bx = p0[0] + (p1[0] - p0[0]) * t
        by = p0[1] + (p1[1] - p0[1]) * t
        out.append(hair([(bx, by), (bx + nx * length, by + ny * length)], w, col))
    return out


def text(x, y, s, size=7.8, col=INK2, anchor='start', ls=0, weight=400):
    a = {'start': 'start', 'middle': 'middle', 'end': 'end'}[anchor]
    return ('<text x="%d" y="%d" font-size="%s" fill="%s" text-anchor="%s" '
            'letter-spacing="%s" font-weight="%s">%s</text>' % (x, y, size, col, a, ls, weight, s))


def grid_check(canvas=(760, 540)):
    return '<rect width="%d" height="%d" fill="%s"/>' % (canvas[0], canvas[1], PAPER)


def svg_open(w, h, font='Noto Serif SC,Songti SC,serif'):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" '
            'font-family="%s" stroke-linejoin="round" stroke-linecap="round">' % (w, h, w, h, font))


# ---------- 复用层：defs + use ----------

def svg_open_xlink(w, h, font='Noto Serif SC,Songti SC,serif'):
    return ('<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
            'viewBox="0 0 %d %d" width="%d" height="%d" font-family="%s" '
            'stroke-linejoin="round" stroke-linecap="round">' % (w, h, w, h, font))


def def_group(gid, body):
    return '<g id="%s">%s</g>' % (gid, ''.join(body))


def use(gid, tx=0.0, ty=0.0, rot=0.0, sx=1.0, sy=1.0, extra=''):
    tr = 'translate(%.2f,%.2f)' % (tx, ty)
    if rot:
        tr += ' rotate(%.2f)' % rot
    if sx != 1.0 or sy != 1.0:
        tr += ' scale(%.3f,%.3f)' % (sx, sy)
    return '<use xlink:href="#%s" transform="%s"%s/>' % (gid, tr, (' ' + extra if extra else ''))


def feather_module(gid, length=1.0, width=0.34, w=0.7, ribs=2, col=INK, ribcol=GREY):
    """以 (0,0) 为羽根、羽尖朝 -y 的母片；length=1 表示单位长度。"""
    body = []
    ts = np.linspace(0, 1, 15)
    left, right = [], []
    for t in ts:
        wd = width * (max(0.0, math.sin(math.pi * (0.06 + t * 0.9))) ** 0.5) * 0.5
        left.append((-wd, -length * t))
        right.append((wd, -length * t))
    body.append(stroke(left, w, col=col, n=20))
    body.append(stroke(right, w, col=col, n=20))
    body.append(hair([(0, 0), (0, -length * 0.94)], 0.3, ribcol))
    for m in range(ribs):
        t = 0.3 + m * 0.26
        wd = width * (max(0.0, math.sin(math.pi * (0.06 + t * 0.9))) ** 0.5) * 0.42
        body.append(hair([(0, -length * t), (-wd, -length * t - 4)], 0.25, ribcol))
        body.append(hair([(0, -length * t), (wd, -length * t - 4)], 0.25, ribcol))
    return def_group(gid, body)


def hair_module(gid, length=1.0, bend=0.35, w=0.55, col=INK2):
    """一条母「缕」，从 (0,0) 下垂并于末端偏折 bend。"""
    pts = []
    for t in np.linspace(0, 1, 12):
        pts.append((bend * (t ** 2), length * t))
    return def_group(gid, [stroke(pts, w, col=col, n=16)])


def count_bytes(s):
    return len(s.encode('utf-8'))
