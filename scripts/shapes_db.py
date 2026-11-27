# -*- coding: utf-8 -*-
"""shapes_db · 器形系数库（傅里叶母本）

为什么要有它：每次出图都手工算器物轮廓，同一只鼎画十遍就是十种鼎。
本库把「器形」存成傅里叶系数母本，出图只做三件事：
  取系数 → 定尺寸位置 → 反变换成点列。
于是「形」可复用、可插值（豆→鼎的中间态）、可概括（k=6 得势、k=12 形备）。

数据模型
  SHAPES[name] = {
     vol:  卷/类（礼器·兵器·陶器）
     cn:   中文名
     mode: 'mirror'（给半边，镜像成闭合）| 'closed'（给整圈）
     body: 主轮廓半边或整圈，归一化：x∈[0,0.6] 为半径方向，y∈[0,1] 顶→底
     parts:[(kind, 点列)]  配件（足、耳、流、鋬、援），同坐标系
  }
归一化约定：原点在顶口中点，y 向下为正，器高 = 1。

用法
  python3 shapes_db.py build            # 写 npz 母本 + 器物总表 SVG
  python3 shapes_db.py list             # 列已收器形
  from shapes_db import place
  place('ding', cx=380, cy_top=180, h=200, k=12)  -> (body_pts, [part_pts...])
"""
import os
import sys
import json
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))
                if os.path.dirname(os.path.abspath(__file__)) else '.')
from fourier_shape import resample_closed, fd_coeff, fd_rebuild  # noqa: E402
import svgbrush as B  # noqa: E402

K_ORDER = 20          # 母本存 20 阶，够复刻这些器形的手工折角

# ---------------------------------------------------------------- 器形定义
# 半边（mirror）：从顶口中点 (0,0) 沿右侧下行到底部中点 (0, y_bottom)
SHAPES = {}

SHAPES['dou'] = dict(vol='礼器', cn='豆', mode='mirror', body=[
    (0.00, 0.00), (0.44, 0.00), (0.47, 0.05), (0.43, 0.11), (0.34, 0.16),
    (0.22, 0.20), (0.11, 0.24), (0.085, 0.48), (0.10, 0.55), (0.24, 0.60),
    (0.28, 0.66), (0.26, 0.72), (0.14, 0.745), (0.00, 0.75)], parts=[])

SHAPES['ding'] = dict(vol='礼器', cn='鼎', mode='mirror', body=[
    (0.00, 0.00), (0.40, 0.00), (0.45, 0.06), (0.47, 0.15), (0.43, 0.25),
    (0.33, 0.34), (0.20, 0.40), (0.09, 0.42), (0.00, 0.42)],
    parts=[('ear', [(0.30, -0.02), (0.30, -0.13), (0.38, -0.15)]),
           ('leg', [(0.00, 0.42), (0.01, 0.52), (0.00, 0.62)]),
           ('leg', [(0.22, 0.40), (0.27, 0.50), (0.25, 0.60)])])

SHAPES['gui'] = dict(vol='礼器', cn='簋', mode='mirror', body=[
    (0.00, 0.00), (0.38, 0.00), (0.42, 0.06), (0.44, 0.16), (0.40, 0.28),
    (0.30, 0.38), (0.18, 0.44), (0.07, 0.46), (0.00, 0.46)],
    parts=[('ring', [(0.16, 0.53), (0.15, 0.60), (0.24, 0.62)]),
           ('ear', [(0.40, 0.04), (0.48, 0.10), (0.46, 0.20)])])

SHAPES['hu'] = dict(vol='礼器', cn='壶', mode='mirror', body=[
    (0.00, 0.00), (0.14, 0.00), (0.15, 0.04), (0.13, 0.10), (0.13, 0.22),
    (0.18, 0.32), (0.30, 0.44), (0.34, 0.56), (0.30, 0.68), (0.20, 0.76),
    (0.14, 0.80), (0.13, 0.86), (0.18, 0.92), (0.19, 0.97), (0.10, 0.995),
    (0.00, 1.00)], parts=[('ear', [(0.17, 0.16), (0.26, 0.22), (0.27, 0.30)])])

SHAPES['yu'] = dict(vol='礼器', cn='盂', mode='mirror', body=[
    (0.00, 0.00), (0.46, 0.00), (0.50, 0.07), (0.50, 0.20), (0.44, 0.34),
    (0.34, 0.44), (0.22, 0.50), (0.10, 0.52), (0.00, 0.53)],
    parts=[('ring', [(0.11, 0.58), (0.10, 0.64), (0.17, 0.66)])])

SHAPES['wei'] = dict(vol='礼器', cn='爵', mode='closed', body=[
    (0.42, 0.00), (0.30, 0.06), (0.14, 0.16), (0.05, 0.28), (0.03, 0.40),
    (0.10, 0.48), (0.22, 0.50), (0.10, 0.56), (0.00, 0.62), (-0.10, 0.56),
    (-0.22, 0.50), (-0.30, 0.44), (-0.30, 0.34), (-0.24, 0.24),
    (-0.16, 0.14), (-0.12, 0.06), (-0.20, 0.00), (-0.06, 0.02), (0.20, 0.02)],
    parts=[('leg', [(0.06, 0.50), (0.05, 0.62), (0.02, 0.72)]),
           ('leg', [(-0.06, 0.50), (-0.05, 0.62), (-0.02, 0.72)]),
           ('handle', [(0.26, 0.20), (0.38, 0.26), (0.34, 0.34)])])

SHAPES['yi'] = dict(vol='礼器', cn='匜', mode='closed', body=[
    (0.40, 0.10), (0.34, 0.04), (0.22, 0.06), (0.10, 0.14), (0.02, 0.26),
    (-0.04, 0.40), (-0.10, 0.52), (-0.20, 0.54), (-0.26, 0.44),
    (-0.24, 0.30), (-0.26, 0.20), (-0.34, 0.14), (-0.30, 0.06),
    (-0.14, 0.06), (0.06, 0.14), (0.22, 0.16), (0.34, 0.16)],
    parts=[('leg', [(-0.16, 0.54), (-0.15, 0.64), (-0.12, 0.70)]),
           ('leg', [(0.10, 0.18), (0.12, 0.52), (0.10, 0.60)]),
           ('leg', [(-0.24, 0.55), (-0.26, 0.64), (-0.22, 0.70)])])

SHAPES['zhi'] = dict(vol='礼器', cn='卮', mode='mirror', body=[
    (0.00, 0.00), (0.30, 0.00), (0.32, 0.05), (0.31, 0.34), (0.29, 0.58),
    (0.30, 0.64), (0.26, 0.70), (0.16, 0.72), (0.00, 0.72)],
    parts=[('leg', [(0.14, 0.72), (0.15, 0.78), (0.12, 0.82)]),
           ('handle', [(0.30, 0.18), (0.40, 0.26), (0.38, 0.36)])])

SHAPES['fou'] = dict(vol='陶器', cn='缶', mode='mirror', body=[
    (0.00, 0.00), (0.10, 0.00), (0.11, 0.05), (0.10, 0.12), (0.14, 0.20),
    (0.26, 0.32), (0.33, 0.48), (0.30, 0.64), (0.18, 0.76), (0.10, 0.82),
    (0.12, 0.90), (0.10, 0.96), (0.00, 0.98)], parts=[])

SHAPES['fu'] = dict(vol='陶器', cn='釜', mode='mirror', body=[
    (0.00, 0.00), (0.30, 0.00), (0.36, 0.04), (0.44, 0.16), (0.48, 0.34),
    (0.42, 0.52), (0.28, 0.64), (0.14, 0.70), (0.04, 0.72), (0.00, 0.72)],
    parts=[])

SHAPES['ge'] = dict(vol='兵器', cn='戈', mode='closed', body=[
    (-0.52, 0.03), (-0.40, 0.00), (0.10, 0.00), (0.32, -0.04), (0.40, 0.00),
    (0.30, 0.06), (0.10, 0.08), (-0.10, 0.09), (-0.30, 0.12), (-0.40, 0.16),
    (-0.46, 0.12), (-0.52, 0.10)], parts=[('edge', [(-0.20, 0.10), (-0.24, 0.22)])])

SHAPES['gong'] = dict(vol='兵器', cn='弓', mode='closed', body=[
    (0.00, -0.50), (0.14, -0.34), (0.20, -0.10), (0.20, 0.16), (0.12, 0.36),
    (0.00, 0.46), (-0.02, 0.44), (-0.10, 0.36), (-0.16, 0.16), (-0.16, -0.10),
    (-0.12, -0.32), (-0.02, -0.48)], parts=[])


def _closed_from(half, ry=0.07):
    """半边 → 闭合。顶边不吃直线，吃一段下凸的口沿弧（透视口沿）。

    白描器物的「像」，一半靠口沿。顶边若是直线，就成了被切开的碗。
    """
    h = np.asarray(half, float)
    if abs(h[0, 0]) < 1e-9 and abs(h[0, 1]) < 1e-9 and len(h) > 3:
        h = h[1:]                                  # 丢掉顶口中点，改用口沿端点
    rx = h[0, 0]
    ryv = ry * (h[:, 1].max() - h[:, 1].min())
    m = h[::-1].copy()
    m[:, 0] = -m[:, 0]
    u = np.linspace(0, np.pi, 26)
    arc = np.stack([-rx * np.cos(u), ryv * np.sin(u)], 1)   # (-rx,0) → 下凸 → (rx,0)
    return np.vstack([h, m[:-1], arc[1:-1]])


def _poly(name):
    s = SHAPES[name]
    if s['mode'] == 'mirror':
        return _closed_from(s['body'], s.get('ry', 0.07))
    return np.asarray(s['body'], float)


def _unit(name):
    """把器形归一到「总高恰好 1、顶口中点为原点」。

    总高必须含配件（耳、足、提梁）——只按腹体算，鼎的半径会被放大到 1.1，
    于是横向溢出、与邻格器相压。
    """
    poly = _poly(name)
    h = poly[:, 1].max() - poly[:, 1].min()
    for kind, pts in SHAPES[name]['parts']:
        q = np.asarray(pts, float)
        h = max(h, q[:, 1].max() - min(poly[:, 1].min(), q[:, 1].min()))
    if h <= 0:
        h = 1.0
    poly = poly / h
    poly[:, 1] -= poly[:, 1].min()
    parts = []
    for kind, pts in SHAPES[name]['parts']:
        p = np.asarray(pts, float) / h
        p[:, 1] -= 0.0
        parts.append((kind, p))
    return poly, parts


def coeffs(name, k=K_ORDER):
    poly, parts = _unit(name)
    return fd_coeff(poly, k), parts


# ---------------------------------------------------------------- 运行时
def place(name, cx, cy_top, h=200.0, k=None, keep_full=False):
    """取器形 → 定尺寸位置 → 点列。cy_top 是顶口中点的 y。

    默认走 Chaikin 保特征（尖角、折边不丢）；给 k 则走傅里叶概括，
    k=3 得势、k=6 足柄生、k=12 形备、k>=20 近原——但那会把爵的流、戈的援磨圆，
    所以只用于「同族变形」与概括度对照，不用于正式器物。
    """
    if k is None:
        poly, parts = _unit(name)
        body = B.chaikin(poly, 2, closed=True)
        scale0 = 1.0 / max(1e-6, (poly[:, 1].max() - poly[:, 1].min()))
        body = body * h
        out = [(np.asarray(pd, float) * h, kind) for kind, pd in parts]
    else:
        c, parts = coeffs(name, max(k, 4))
        body = fd_rebuild(c, n=256 if not keep_full else 512) * h
        out = [(np.asarray(pd, float) * h, kind) for kind, pd in parts]
    body = body.copy()
    body[:, 0] += cx
    body[:, 1] += cy_top
    parts_out = []
    for pd, kind in out:
        pd = pd.copy()
        pd[:, 0] += cx
        pd[:, 1] += cy_top
        parts_out.append((kind, pd))
    return body, parts_out


def fit(name, cx, cy_mid, box_w=110.0, box_h=110.0, k=None):
    """按框适配：整器（含配件）等比缩放进 box，居中于 (cx, cy_mid)。

    为什么不用「器高=1」硬归一：戈、弓是横长器，按高归一会被放大成六格宽。
    器物各有其真实长宽比，缩放只能按框限制，不能按单一维度。
    """
    body, parts = place(name, 0.0, 0.0, h=1.0, k=k)
    xs = [body[:, 0]]
    ys = [body[:, 1]]
    for _, p in parts:
        xs.append(p[:, 0]); ys.append(p[:, 1])
    x0, x1 = min(a.min() for a in xs), max(a.max() for a in xs)
    y0, y1 = min(a.min() for a in ys), max(a.max() for a in ys)
    w, hh = max(x1 - x0, 1e-6), max(y1 - y0, 1e-6)
    s = min(box_w / w, box_h / hh)
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    body2 = (body - [mx, my]) * s + [cx, cy_mid]
    parts2 = [((p - [mx, my]) * s + [cx, cy_mid]) for _, p in parts]
    return body2, parts2, s


def mouth(name):
    """口沿：返回 (半宽, 底 y) 于归一单位坐标，供画椭圆口沿。"""
    poly, _ = _unit(name)
    ymin = poly[:, 1].min()
    near = poly[np.abs(poly[:, 1] - ymin) < 0.06]
    return float(np.abs(near[:, 0]).max()), ymin


def blend(a, b, t, k=12):
    """同族插值：豆 ↔ 鼎 的中间态。t=0 全 a，t=1 全 b。"""
    ca, _ = coeffs(a, k)
    cb, _ = coeffs(b, k)
    return fd_rebuild(ca * (1 - t) + cb * t, n=256)


def build(outdir=None):
    """写母本 npz；返回路径。"""
    import svgbrush as B  # noqa: F811
    outdir = outdir or os.path.join(os.getcwd(), 'data')
    os.makedirs(outdir, exist_ok=True)
    pack = {}
    for name in SHAPES:
        pack['%s/body' % name] = np.asarray(coeffs(name)[0], dtype=complex)
    npz = os.path.join(outdir, 'shapes.npz')
    np.savez_compressed(npz, **pack)
    return npz


# ---------------------------------------------------------------- 总表图
def sheet_svg(path=None, canvas=(760, 540)):
    """器物总表：12 器母本 + 阶数对照。"""
    W, H = canvas
    g = [B.grid_check(canvas)]
    # 页眉
    g.append(B.text(44, 58, '礼 器 · 兵 器 · 陶 器', 8.6, B.RED, ls=2))
    g.append(B.text(380, 60, '器 形 母 本', 26, B.INK, anchor='middle', ls=10, weight=500))
    g.append(B.text(716, 58, '图法靶场 · 之三', 8.2, B.GREY, anchor='end', ls=1))
    g.append('<line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.6"/>' % B.GREY)

    order = ['dou', 'ding', 'gui', 'hu', 'yu', 'wei',
             'yi', 'fou', 'fu', 'ge', 'gong', 'zhi']
    order = [n for n in order if n in SHAPES]
    cols, rows = 6, 2
    cell_w, cell_h = 112, 168
    x0, y0 = 78, 132
    for i, name in enumerate(order):
        cx = x0 + (i % cols) * cell_w
        cy_top = y0 + (i // cols) * cell_h
        body, parts, s = fit(name, cx, cy_top + 58, box_w=96, box_h=104)
        g.append(B.stroke_closed(body, 0.85, col=B.INK, n=180))
        for p in parts:
            g.append(B.stroke(p, 0.52, col=B.INK2, n=26))
        # 口沿：器物若无口沿线，只是剪影
        g.append(B.text(cx, cy_top + 148, SHAPES[name]['cn'], 13, B.INK, anchor='middle', ls=3))
        g.append(B.text(cx, cy_top + 164, SHAPES[name]['vol'], 7.4, B.GREY, anchor='middle', ls=1))

    g.append('<line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.6"/>' % B.GREY)
    g.append(B.text(44, 498, 'k=3 得势 · k=6 足柄生 · k=12 形备 · k≥20 近原', 9.2, B.INK2, ls=1))
    g.append(B.text(716, 498, 'shapes_db · %d 器' % len(SHAPES), 8.2, B.GREY, anchor='end', ls=1))
    g.append(B.text(380, 522, '一器一系数，出图只取形、不重画形', 15, B.INK, anchor='middle', ls=3))

    svg = B.svg_open(W, H) + ''.join(g) + '</svg>'
    if path:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, 'w', encoding='utf-8').write(svg)
    return svg


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'list'
    if cmd == 'list':
        for k, v in SHAPES.items():
            print('%-6s %-4s %-6s %d 点 %d 件' % (k, v['cn'], v['vol'], len(v['body']), len(v['parts'])))
        print('共 %d 器' % len(SHAPES))
    elif cmd == 'build':
        out = build(sys.argv[2] if len(sys.argv) > 2 else None)
        print('母本 →', out, B.count_bytes(open(out, 'rb').read()) if False else '')
        p = sys.argv[3] if len(sys.argv) > 3 else os.path.join(os.getcwd(), 'out', 'shape-db.svg')
        svg = sheet_svg(p)
        print('总表 →', p, '%d B' % B.count_bytes(svg))
