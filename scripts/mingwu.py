# -*- coding: utf-8 -*-
"""mingwu · 诗经名物画具库

目标：060–080px 格心内可辨，每物 8–24 条线，线走三阶墨（轮廓 0.9／结构 0.5／细部 0.3）。
每具函数签名统一为 f(cx, cy, s=1.0, **kw)，cx,cy 是格心锚点，s 是尺度。

收录：水、岸、舟、两髦、墙、蒺藜、帚、笄珈、礼服、菟丝、桑、禽、星、宫、木、竿、狐、兔、黍、竹、瓜、鱼、马、车。
"""
import math
import numpy as np
import svgbrush as B

INK, INK2, GREY, RED = B.INK, B.INK2, B.GREY, B.RED


def _q(p0, p1, p2, w=0.9, w1=None, te=0.0, col=INK, n=18):
    t = np.linspace(0, 1, n)[:, None]
    p0, p1, p2 = (np.asarray(p, float) for p in (p0, p1, p2))
    pts = (1 - t) ** 2 * p0 + 2 * (1 - t) * t * p1 + t ** 2 * p2
    return B.stroke(pts, w, w1, n=n, col=col, taper_end=te)


def _s(p0, p1, w=0.9, w1=None, te=0.0, col=INK):
    return B.stroke([p0, p1], w, w1, n=5, col=col, taper_end=te)


# ---------------------------------------------------------------- 水与岸
def water(cx, cy, w=120, rows=3, gap=13, s=1.0, amp=3.4):
    out = []
    for r in range(rows):
        y = cy + r * gap * s
        hw = w * s * (1 - r * 0.06)
        out.append(_q((cx - hw, y - amp * s), (cx - hw * 0.55, y + amp * s * 1.6), (cx, y), 0.42, col=INK2, n=14))
        out.append(_q((cx, y), (cx + hw * 0.55, y - amp * s * 1.6), (cx + hw, y - amp * s), 0.42, col=INK2, n=14))
    return out


def bank(cx, cy, w=130, h=54, s=1.0, side=1):
    """岸坡：一条折岸 + 坡面排线。"""
    out = [_s((cx - w * s, cy + h * 0.6 * s), (cx - w * 0.3 * s * side, cy - h * 0.1 * s), 0.9, 0.4),
           _s((cx - w * 0.3 * s * side, cy - h * 0.1 * s), (cx + w * 0.9 * s * side, cy + h * 0.45 * s), 0.75, 0.35)]
    for k in range(4):
        x0 = cx - w * 0.7 * s + k * w * 0.42 * s * side
        y0 = cy + h * 0.2 * s + k * 4 * s
        out.append(B.hair([(x0, y0), (x0 + 12 * s * side, y0 + 9 * s)], 0.24, GREY))
    return out


def boat(cx, cy, L=104, s=1.0):
    """舟：船底线一条、左右舷各一弧、三道肋、一桨。"""
    h = 22 * s
    out = [_q((cx - L * 0.5 * s, cy), (cx, cy + h * 1.1), (cx + L * 0.5 * s, cy), 0.95, 0.4),          # 底
           _q((cx - L * 0.5 * s, cy), (cx - L * 0.42 * s, cy - h * 0.55), (cx - L * 0.3 * s, cy - h * 0.7), 0.7),  # 左舷
           _q((cx + L * 0.5 * s, cy), (cx + L * 0.42 * s, cy - h * 0.55), (cx + L * 0.3 * s, cy - h * 0.7), 0.7),
           # 舷口
           _s((cx - L * 0.3 * s, cy - h * 0.7), (cx - L * 0.1 * s, cy - h * 0.62), 0.55, col=INK2),
           _s((cx - L * 0.1 * s, cy - h * 0.62), (cx + L * 0.3 * s, cy - h * 0.7), 0.55, col=INK2)]
    for k in range(3):
        x = cx - L * 0.24 * s + k * L * 0.24 * s
        out.append(_s((x, cy - h * 0.66), (x + 2 * s, cy + h * 0.85), 0.3, col=GREY))
    # 桨
    out.append(_s((cx + L * 0.36 * s, cy - h * 1.2), (cx - L * 0.12 * s, cy + h * 1.6), 0.5, 0.2, col=INK2))
    out.append(_s((cx + L * 0.36 * s, cy - h * 1.2), (cx + L * 0.46 * s, cy - h * 1.4), 0.34, col=INK2))
    return out


# ---------------------------------------------------------------- 人物
def hair_mao(cx, cy, s=1.0, two=True):
    """两髦：侧身人形两名，各垂两缕长发于胸前（周礼「髦」为童子垂发）。"""
    out = []

    def one(x, flip=1):
        o = []
        o.append(_q((x - 5 * s, cy - 34 * s), (x + 4 * s, cy - 38 * s), (x + 6 * s, cy - 30 * s), 0.55))   # 头顶
        o.append(_s((x + 6 * s, cy - 30 * s), (x + 5 * s, cy - 22 * s), 0.5))                              # 面侧
        o.append(_s((x - 5 * s, cy - 24 * s), (x - 4 * s, cy - 8 * s), 0.85, 0.6))                          # 背
        o.append(_s((x + 5 * s, cy - 22 * s), (x + 4 * s, cy - 8 * s), 0.6, 0.4))                           # 胸
        o.append(_s((x - 4 * s, cy - 8 * s), (x - 3 * s, cy + 6 * s), 0.7, 0.5))                            # 下身
        o.append(_s((x + 4 * s, cy - 8 * s), (x + 3 * s, cy + 6 * s), 0.6, 0.4))
        # 两髦（垂发两缕）
        o.append(_q((x - 5 * s, cy - 26 * s), (x - 10 * s, cy - 18 * s), (x - 8 * s, cy + 2 * s), 0.5, 0.16, te=0.5, col=INK2))
        o.append(_q((x + 5 * s, cy - 25 * s), (x + 9 * s, cy - 16 * s), (x + 7 * s, cy + 2 * s), 0.46, 0.14, te=0.5, col=INK2))
        return o

    out += one(cx - 34 * s, 1)
    if two:
        out += one(cx + 34 * s, -1)
    return out


def robe(cx, cy, s=1.0):
    """礼服（曲裾深衣）：交领、宽袖、绕襟。"""
    out = [_q((cx - 16 * s, cy - 30 * s), (cx - 22 * s, cy - 6 * s), (cx - 26 * s, cy + 26 * s), 0.85, 0.5),
           _q((cx + 16 * s, cy - 30 * s), (cx + 24 * s, cy - 4 * s), (cx + 30 * s, cy + 26 * s), 0.85, 0.5),
           _s((cx - 26 * s, cy + 26 * s), (cx + 30 * s, cy + 26 * s), 0.8, 0.55),
           # 交领
           _s((cx - 10 * s, cy - 30 * s), (cx + 4 * s, cy - 12 * s), 0.55, col=INK2),
           _s((cx + 10 * s, cy - 30 * s), (cx + 4 * s, cy - 12 * s), 0.55, col=INK2),
           # 宽袖
           _q((cx - 18 * s, cy - 24 * s), (cx - 40 * s, cy - 10 * s), (cx - 34 * s, cy + 6 * s), 0.7),
           _q((cx + 18 * s, cy - 24 * s), (cx + 42 * s, cy - 8 * s), (cx + 36 * s, cy + 8 * s), 0.7)]
    for k in range(3):
        out.append(_s((cx - 14 * s + k * 14 * s, cy + 6 * s), (cx - 8 * s + k * 14 * s, cy + 26 * s), 0.28, col=GREY))
    return out


def hairpin(cx, cy, s=1.0):
    """笄与六珈：一横笄，垂六枚玉饰。"""
    out = [_s((cx - 34 * s, cy - 18 * s), (cx + 34 * s, cy - 18 * s), 1.0, 0.6),
           _q((cx - 34 * s, cy - 18 * s), (cx - 40 * s, cy - 12 * s), (cx - 38 * s, cy - 6 * s), 0.6),
           _q((cx + 34 * s, cy - 18 * s), (cx + 40 * s, cy - 12 * s), (cx + 38 * s, cy - 6 * s), 0.6)]
    for k in range(6):
        x = cx - 25 * s + k * 10 * s
        out.append(_s((x, cy - 17 * s), (x, cy - 10 * s), 0.25, col=INK2))
        out.append(B.oval(x, cy - 4 * s, 3.4 * s, 4.6 * s, 0.5, INK, n=18))
    return out


# ---------------------------------------------------------------- 建筑
def wall(cx, cy, w=150, h=92, s=1.0):
    """城墙：垛口、门洞、砖缝。"""
    out = []
    base = cy + h * 0.5 * s
    top = cy - h * 0.5 * s
    out.append(_s((cx - w * 0.5 * s, base), (cx - w * 0.5 * s, top), 0.95, 0.7))
    out.append(_s((cx + w * 0.5 * s, base), (cx + w * 0.5 * s, top), 0.95, 0.7))
    out.append(_s((cx - w * 0.5 * s, top), (cx + w * 0.5 * s, top), 0.75, 0.5))
    # 垛口
    n = 6
    for k in range(n):
        x0 = cx - w * 0.5 * s + k * w / n * s
        out.append(_s((x0, top), (x0, top - 9 * s), 0.6, 0.4))
        out.append(_s((x0, top - 9 * s), (x0 + w / n * s * 0.62, top - 9 * s), 0.5, col=INK2))
        out.append(_s((x0 + w / n * s * 0.62, top - 9 * s), (x0 + w / n * s * 0.62, top), 0.5, col=INK2))
    # 门洞
    out.append(_q((cx - 16 * s, base), (cx - 16 * s, cy + 6 * s), (cx, cy - 6 * s), 0.7))
    out.append(_q((cx + 16 * s, base), (cx + 16 * s, cy + 6 * s), (cx, cy - 6 * s), 0.7))
    # 砖缝
    for r in range(3):
        y = top + 16 * s + r * 16 * s
        out.append(_s((cx - w * 0.48 * s, y), (cx + w * 0.48 * s, y), 0.2, col=GREY))
    return out


def hall(cx, cy, w=150, h=96, s=1.0):
    """宫室：台基、四柱、檐口、脊。"""
    out = []
    base = cy + h * 0.5 * s
    out.append(_s((cx - w * 0.52 * s, base), (cx + w * 0.52 * s, base), 1.0, 0.6))       # 台基
    out.append(_s((cx - w * 0.46 * s, base), (cx - w * 0.46 * s, cy - h * 0.08 * s), 0.7))  # 右柱
    out.append(_s((cx + w * 0.46 * s, base), (cx + w * 0.46 * s, cy - h * 0.08 * s), 0.7))
    out.append(_s((cx - w * 0.16 * s, base), (cx - w * 0.16 * s, cy - h * 0.08 * s), 0.5, col=INK2))
    out.append(_s((cx + w * 0.16 * s, base), (cx + w * 0.16 * s, cy - h * 0.08 * s), 0.5, col=INK2))
    # 檐
    out.append(_q((cx - w * 0.62 * s, cy - h * 0.10 * s), (cx, cy - h * 0.02 * s), (cx + w * 0.62 * s, cy - h * 0.10 * s), 1.15, 0.7))
    # 屋顶
    out.append(_q((cx - w * 0.62 * s, cy - h * 0.10 * s), (cx - w * 0.26 * s, cy - h * 0.46 * s), (cx, cy - h * 0.54 * s), 0.9, 0.5))
    out.append(_q((cx + w * 0.62 * s, cy - h * 0.10 * s), (cx + w * 0.26 * s, cy - h * 0.46 * s), (cx, cy - h * 0.54 * s), 0.9, 0.5))
    # 门窗
    out.append(_s((cx - 8 * s, base), (cx - 8 * s, cy + 8 * s), 0.4, col=INK2))
    out.append(_s((cx + 8 * s, base), (cx + 8 * s, cy + 8 * s), 0.4, col=INK2))
    out.append(_s((cx - 8 * s, cy + 8 * s), (cx + 8 * s, cy + 8 * s), 0.35, col=INK2))
    return out


# ---------------------------------------------------------------- 草木
def mulberry(cx, cy, s=1.0):
    """桑：主干一、三枝、叶七。"""
    out = [_s((cx, cy + 34 * s), (cx + 2 * s, cy - 4 * s), 1.0, 0.6)]
    for k, (bx, by) in enumerate(((-30, -22), (14, -30), (34, -12))):
        out.append(_q((cx + 2 * s, cy - 4 * s), (cx + bx * 0.5 * s, cy + by * 0.4 * s), (cx + bx * s, cy + by * s), 0.7, 0.35))
    leaves = [(-30, -22), (-22, -30), (-8, -34), (4, -38), (16, -32), (30, -16), (36, -8)]
    for lx, ly in leaves:
        x, y = cx + lx * s, cy + ly * s
        out.append(_q((x - 6 * s, y + 2 * s), (x, y - 7 * s), (x + 6 * s, y + 2 * s), 0.5))
        out.append(_q((x - 6 * s, y + 2 * s), (x, y + 8 * s), (x + 6 * s, y + 2 * s), 0.42, col=INK2))
    return out


def tree(cx, cy, s=1.0, kind='zi'):
    """梓／一般乔木：主干、分枝、云头冠。"""
    out = [_s((cx, cy + 36 * s), (cx + 1 * s, cy - 10 * s), 1.05, 0.55)]
    out.append(_q((cx + 1 * s, cy - 10 * s), (cx - 16 * s, cy - 26 * s), (cx - 26 * s, cy - 36 * s), 0.6, 0.3))
    out.append(_q((cx + 1 * s, cy - 10 * s), (cx + 18 * s, cy - 24 * s), (cx + 28 * s, cy - 34 * s), 0.6, 0.3))
    for k, (dx, dy) in enumerate(((-30, -38), (-10, -46), (8, -48), (26, -40), (-2, -34))):
        x, y = cx + dx * s, cy + dy * s
        out.append(_q((x - 13 * s, y + 6 * s), (x, y - 6 * s), (x + 13 * s, y + 6 * s), 0.55, 0.2))
    return out


def vine(cx, cy, s=1.0):
    """菟丝（唐）：缠绕细蔓，无根无叶。"""
    out = []
    for k in range(3):
        x0 = cx - 40 * s + k * 26 * s
        pts = []
        for t in np.linspace(0, 1, 18):
            pts.append((x0 + 22 * s * math.sin(t * 5.0 + k), cy - 26 * s + 60 * s * t))
        out.append(B.stroke(pts, 0.42, 0.16, n=18, col=INK2, taper_end=0.5))
    return out


def bamboo(cx, cy, s=1.0):
    """竹竿：三竿，节三，叶五。"""
    out = []
    for k in range(3):
        x = cx - 24 * s + k * 24 * s
        top = cy - 60 * s + k * 6 * s
        out.append(_s((x, cy + 46 * s), (x + 2 * s, top), 0.85, 0.45))
        for m in range(3):
            y = cy + 20 * s - m * 24 * s
            out.append(_s((x - 2 * s, y), (x + 4 * s, y), 0.3, col=GREY))
            out.append(B.hair([(x + 2 * s, y), (x + 16 * s, y - 8 * s)], 0.24, GREY))
    return out


# ---------------------------------------------------------------- 动物
def bird_s(cx, cy, s=1.0, kind='chun'):
    """小禽：鹑（矮圆）／鹊（长尾）。纹样化，不作写实。"""
    out = []
    body_rx, body_ry = (14, 11) if kind == 'chun' else (11, 9)
    out.append(B.oval(cx, cy, body_rx * s, body_ry * s, 0.7, INK, n=26))
    out.append(B.oval(cx + 11 * s, cy - 9 * s, 4.6 * s, 4.4 * s, 0.6, INK, n=18))     # 头
    out.append(_s((cx + 14 * s, cy - 9 * s), (cx + 21 * s, cy - 7 * s), 0.42, 0.06, te=0.7))  # 喙
    out.append(_s((cx - 2 * s, cy + 6 * s), (cx - 2 * s, cy + 18 * s), 0.4, 0.18, col=INK2))
    out.append(_s((cx + 4 * s, cy + 6 * s), (cx + 4 * s, cy + 18 * s), 0.4, 0.18, col=INK2))
    if kind == 'que':
        out.append(_s((cx - body_rx * s, cy + 2 * s), (cx - 30 * s, cy - 6 * s), 0.55, 0.1, te=0.5, col=INK2))
    else:
        for k in range(3):
            out.append(_s((cx - 10 * s, cy + 6 * s + k * 3 * s), (cx - 22 * s, cy + 10 * s + k * 4 * s), 0.32, 0.08, col=INK2))
    for k in range(2):
        out.append(B.hair([(cx - 6 * s + k * 7 * s, cy - 6 * s), (cx - 3 * s + k * 7 * s, cy + 2 * s)], 0.24, GREY))
    return out


def fox(cx, cy, s=1.0):
    """狐：侧影，长身，大尾。"""
    out = [_q((cx + 20 * s, cy - 6 * s), (cx - 6 * s, cy + 2 * s), (cx - 26 * s, cy - 2 * s), 0.85, 0.5),   # 背
           _q((cx + 20 * s, cy - 6 * s), (cx + 2 * s, cy + 14 * s), (cx - 22 * s, cy + 8 * s), 0.6, col=INK2),  # 腹
           B.oval(cx + 24 * s, cy - 12 * s, 7 * s, 6 * s, 0.65, INK, n=20),                                  # 头
           _s((cx + 30 * s, cy - 12 * s), (cx + 37 * s, cy - 8 * s), 0.42, 0.06, te=0.7),                   # 吻
           _s((cx + 24 * s, cy - 16 * s), (cx + 21 * s, cy - 26 * s), 0.5, 0.16, te=0.5),                   # 耳
           _s((cx + 28 * s, cy - 16 * s), (cx + 26 * s, cy - 26 * s), 0.5, 0.16, te=0.5)]
    # 大尾
    out.append(_q((cx - 24 * s, cy), (cx - 46 * s, cy + 6 * s), (cx - 50 * s, cy + 22 * s), 0.9, 0.3, te=0.4))
    out.append(_q((cx - 24 * s, cy + 8 * s), (cx - 42 * s, cy + 16 * s), (cx - 44 * s, cy + 30 * s), 0.55, col=INK2))
    # 足
    for dx in (-10, 8):
        out.append(_s((cx + dx * s, cy + 10 * s), (cx + dx * s, cy + 26 * s), 0.42, 0.2, col=INK2))
    return out


def rabbit(cx, cy, s=1.0):
    """兔：侧影蹲踞，长耳。"""
    out = [B.oval(cx, cy, 22 * s, 15 * s, 0.8, INK, n=30),
           B.oval(cx + 20 * s, cy - 10 * s, 7 * s, 6 * s, 0.6, INK, n=18),
           _s((cx + 22 * s, cy - 17 * s), (cx + 18 * s, cy - 34 * s), 0.5, 0.16, te=0.5),
           _s((cx + 26 * s, cy - 17 * s), (cx + 25 * s, cy - 33 * s), 0.48, 0.14, te=0.5),
           _s((cx - 20 * s, cy + 2 * s), (cx - 30 * s, cy - 2 * s), 0.45, 0.12, col=INK2),
           _s((cx + 4 * s, cy + 13 * s), (cx + 2 * s, cy + 24 * s), 0.42, 0.2, col=INK2),
           _s((cx + 13 * s, cy + 13 * s), (cx + 12 * s, cy + 24 * s), 0.42, 0.2, col=INK2)]
    return out


def fish(cx, cy, s=1.0):
    out = [_q((cx - 22 * s, cy), (cx, cy - 13 * s), (cx + 22 * s, cy), 0.75, 0.4),
           _q((cx - 22 * s, cy), (cx, cy + 13 * s), (cx + 22 * s, cy), 0.75, 0.4),
           _s((cx - 22 * s, cy), (cx - 34 * s, cy - 10 * s), 0.5, 0.14, te=0.5),
           _s((cx - 22 * s, cy), (cx - 34 * s, cy + 10 * s), 0.5, 0.14, te=0.5),
           _s((cx + 12 * s, cy - 8 * s), (cx + 12 * s, cy + 8 * s), 0.3, col=INK2),
           B.hair([(cx + 12 * s, cy - 2 * s), (cx + 16 * s, cy - 3 * s)], 0.26, INK)]
    return out


# ---------------------------------------------------------------- 器物
def staff(cx, cy, h=96, s=1.0):
    out = [_s((cx - 1.8 * s, cy + h * 0.5 * s), (cx - 1.4 * s, cy - h * 0.5 * s), 0.6, 0.4),
           _s((cx + 1.8 * s, cy + h * 0.5 * s), (cx + 1.4 * s, cy - h * 0.5 * s), 0.6, 0.4)]
    return out


def broom(cx, cy, s=1.0):
    """帚：柄一，穗七，束箍一。"""
    out = [_s((cx + 14 * s, cy - 40 * s), (cx - 2 * s, cy - 4 * s), 0.75, 0.45)]
    for k in range(7):
        a = -0.5 + k * 0.17
        out.append(_s((cx - 2 * s, cy - 4 * s), (cx - 2 * s + 34 * s * math.sin(a), cy + 30 * s * math.cos(a)), 0.42, 0.1, te=0.5, col=INK2))
    out.append(_s((cx - 6 * s, cy - 6 * s), (cx + 4 * s, cy - 1 * s), 0.6, 0.4))
    return out


def star(cx, cy, s=1.0, n=4):
    """定星：四星连作一方（定之方中）。"""
    out = []
    pos = [(-22, 10), (6, -18), (28, 8), (-2, 26)]
    for i, (dx, dy) in enumerate(pos[:n]):
        x, y = cx + dx * s, cy + dy * s
        out.append(B.hair([(x - 4 * s, y), (x + 4 * s, y)], 0.34, INK))
        out.append(B.hair([(x, y - 4 * s), (x, y + 4 * s)], 0.34, INK))
        j = (i + 1) % min(n, 4)
        if i < n - 1:
            x2, y2 = cx + pos[j][0] * s, cy + pos[j][1] * s
            out.append(B.hair([(x, y), (x2, y2)], 0.2, GREY))
    return out


def thorns(cx, cy, s=1.0):
    """蒺藜：一条藤，八片带刺叶。"""
    out = []
    pts = [(cx - 40 * s, cy + 20 * s), (cx - 16 * s, cy + 4 * s), (cx + 10 * s, cy - 6 * s), (cx + 38 * s, cy + 12 * s)]
    out.append(B.stroke(pts, 0.55, 0.3, n=16))
    for k in range(5):
        x = cx - 34 * s + k * 18 * s
        y = cy + 16 * s - k * 5 * s
        out.append(_q((x - 7 * s, y - 2 * s), (x, y - 12 * s), (x + 7 * s, y - 2 * s), 0.48))
        out.append(_q((x - 7 * s, y - 2 * s), (x, y + 6 * s), (x + 7 * s, y - 2 * s), 0.42, col=INK2))
        for d in (-3, 0, 3):
            out.append(_s((x + d * s, y - 10 * s), (x + d * s * 1.4, y - 16 * s), 0.22, col=GREY))
    return out


# ---------------------------------------------------------------- 续补
def rat(cx, cy, s=1.0):
    """鼠：侧影，尖吻，长尾。"""
    out = [_q((cx + 18 * s, cy - 4 * s), (cx - 4 * s, cy - 12 * s), (cx - 26 * s, cy - 6 * s), 0.8, 0.45),
           _q((cx + 18 * s, cy - 4 * s), (cx - 4 * s, cy + 12 * s), (cx - 26 * s, cy + 4 * s), 0.6, col=INK2),
           _q((cx + 18 * s, cy - 6 * s), (cx + 26 * s, cy - 2 * s), (cx + 33 * s, cy + 1 * s), 0.55, 0.2, te=0.5),
           B.oval(cx + 22 * s, cy - 4 * s, 3.2 * s, 2.6 * s, 0.4, INK, n=14),
           _s((cx + 16 * s, cy - 11 * s), (cx + 14 * s, cy - 20 * s), 0.4, 0.12, te=0.5),
           # 长尾
           _q((cx - 26 * s, cy - 3 * s), (cx - 48 * s, cy - 10 * s), (cx - 56 * s, cy + 6 * s), 0.42, 0.12, te=0.6, col=INK2),
           _s((cx - 6 * s, cy + 11 * s), (cx - 8 * s, cy + 22 * s), 0.3, col=INK2)]
    # 齿（相鼠「无牙」之反）
    for k in range(3):
        out.append(B.hair([(cx + 28 * s + k * 3 * s, cy + 2 * s), (cx + 28 * s + k * 3 * s, cy + 6 * s)], 0.24, GREY))
    return out


def hill(cx, cy, w=140, h=64, s=1.0):
    """谷／丘：双峰夹谷。"""
    out = [_q((cx - w * 0.5 * s, cy + h * 0.4 * s), (cx - w * 0.20 * s, cy - h * 0.55 * s), (cx - 6 * s, cy + h * 0.1 * s), 0.9, 0.5),
           _q((cx + 6 * s, cy + h * 0.1 * s), (cx + w * 0.20 * s, cy - h * 0.55 * s), (cx + w * 0.5 * s, cy + h * 0.4 * s), 0.9, 0.5),
           _s((cx - w * 0.5 * s, cy + h * 0.4 * s), (cx + w * 0.5 * s, cy + h * 0.4 * s), 0.3, col=GREY)]
    for k in range(4):
        x = cx - 20 * s + k * 13 * s
        out.append(B.hair([(x, cy + h * 0.15 * s - k * 2 * s), (x + 8 * s, cy + h * 0.32 * s)], 0.22, GREY))
    return out


def rainbow(cx, cy, s=1.0):
    """蝃蝀（虹）：三层同心弧＋两端云气。"""
    out = []
    for k, r in enumerate((62, 52, 42)):
        out.append(B.arcband(cx, cy + 40 * s, r * s, r * 0.62 * s, 3.34, 6.08, 0.7 - k * 0.14, INK if k < 2 else INK2, n=42))
    for sgn in (1, -1):
        out.append(_q((cx + sgn * 62 * s, cy + 40 * s), (cx + sgn * 62 * s, cy + 10 * s), (cx + sgn * 66 * s, cy - 2 * s), 0.42, 0.12, te=0.6, col=INK2))
    return out


def jade(cx, cy, s=1.0, n=3):
    """玉佩／琼琚：环形佩，系绳。"""
    out = [_q((cx, cy - 40 * s), (cx, cy - 24 * s), (cx, cy - 16 * s), 0.4, 0.16, col=INK2)]
    for k in range(n):
        y = cy - 8 * s + k * 20 * s
        rx = (13 - k * 2) * s
        out.append(B.oval(cx, y, rx, rx * 0.62, 0.7 - k * 0.1, INK, n=26))
        out.append(B.oval(cx, y, rx * 0.42, rx * 0.26, 0.4, INK2, n=18))
    return out


def car(cx, cy, w=120, s=1.0):
    """车：双轮、舆、轴、辕。"""
    out = []
    for sgn in (1, -1):
        out.append(B.oval(cx + sgn * 34 * s, cy + 16 * s, 19 * s, 19 * s, 0.8, INK, n=30))
        for k in range(4):
            a = k * math.pi / 4
            out.append(_s((cx + sgn * 34 * s - 19 * s * math.cos(a), cy + 16 * s - 19 * s * math.sin(a)),
                          (cx + sgn * 34 * s + 19 * s * math.cos(a), cy + 16 * s + 19 * s * math.sin(a)), 0.22, col=GREY))
    out.append(_s((cx - w * 0.42 * s, cy + 8 * s), (cx + w * 0.42 * s, cy + 8 * s), 1.0, 0.6))       # 舆底
    out.append(_s((cx - w * 0.34 * s, cy + 8 * s), (cx - w * 0.34 * s, cy - 18 * s), 0.65))          # 舆侧
    out.append(_s((cx + w * 0.34 * s, cy + 8 * s), (cx + w * 0.34 * s, cy - 18 * s), 0.65))
    out.append(_q((cx - w * 0.34 * s, cy - 18 * s), (cx, cy - 26 * s), (cx + w * 0.34 * s, cy - 18 * s), 0.6))
    out.append(_s((cx, cy + 8 * s), (cx + w * 0.62 * s, cy + 26 * s), 0.7, 0.4))                     # 辕
    return out


def horse(cx, cy, s=1.0):
    """马：侧影，鬃、四足、尾。"""
    out = [_q((cx + 28 * s, cy - 8 * s), (cx + 4 * s, cy - 14 * s), (cx - 22 * s, cy - 6 * s), 0.9, 0.5),
           _q((cx + 28 * s, cy - 8 * s), (cx + 6 * s, cy + 10 * s), (cx - 20 * s, cy + 4 * s), 0.6, col=INK2),
           _q((cx + 30 * s, cy - 12 * s), (cx + 36 * s, cy - 30 * s), (cx + 40 * s, cy - 36 * s), 0.75, 0.2, te=0.4),
           _s((cx + 40 * s, cy - 34 * s), (cx + 46 * s, cy - 30 * s), 0.4, 0.1, te=0.6, col=INK2),
           _s((cx + 34 * s, cy - 22 * s), (cx + 28 * s, cy - 34 * s), 0.45, 0.14, te=0.5)]
    for dx in (14, 22, -12, -20):
        out.append(_s((cx + dx * s, cy + 8 * s), (cx + dx * s, cy + 34 * s), 0.45, 0.24, col=INK2))
        out.append(_s((cx + dx * s, cy + 34 * s), (cx + dx * s + 4 * s, cy + 38 * s), 0.3, 0.1, col=INK2))
    out.append(_q((cx - 22 * s, cy - 4 * s), (cx - 36 * s, cy + 6 * s), (cx - 38 * s, cy + 32 * s), 0.55, 0.15, te=0.55, col=INK2))
    return out


def millet(cx, cy, s=1.0):
    """黍：三穗，穗下垂。"""
    out = []
    for k in range(3):
        x = cx - 26 * s + k * 26 * s
        out.append(_s((x, cy + 40 * s), (x + 2 * s, cy - 22 * s), 0.6, 0.34))
        for m in range(3):
            out.append(B.hair([(x + 1 * s, cy - 8 * s + m * 8 * s), (x - 12 * s, cy - 14 * s + m * 9 * s)], 0.26, GREY))
            out.append(B.hair([(x + 2 * s, cy - 8 * s + m * 8 * s), (x + 14 * s, cy - 13 * s + m * 9 * s)], 0.26, GREY))
        # 穗
        for m in range(4):
            out.append(_s((x + 2 * s - m * 2 * s, cy - 22 * s - m * 5 * s), (x - 4 * s - m * 3 * s, cy - 34 * s - m * 3 * s), 0.32, 0.08, col=INK2))
    return out


def sun(cx, cy, r=18, s=1.0, rays=6):
    out = [B.oval(cx, cy, r * s, r * s, 0.7, INK, n=28)]
    for k in range(rays):
        a = k * (2 * math.pi / rays)
        out.append(_s((cx + (r + 6) * s * math.cos(a), cy + (r + 6) * s * math.sin(a)),
                      (cx + (r + 16) * s * math.cos(a), cy + (r + 16) * s * math.sin(a)), 0.32, col=INK2))
    return out


def net(cx, cy, w=96, h=76, s=1.0):
    """罝（兔网）：框一，网目九。"""
    out = [_s((cx - w * 0.5 * s, cy + h * 0.5 * s), (cx - w * 0.5 * s, cy - h * 0.5 * s), 0.8, 0.5),
           _s((cx + w * 0.5 * s, cy + h * 0.5 * s), (cx + w * 0.5 * s, cy - h * 0.5 * s), 0.8, 0.5),
           _s((cx - w * 0.5 * s, cy - h * 0.5 * s), (cx + w * 0.5 * s, cy - h * 0.5 * s), 0.7, 0.4),
           _s((cx - w * 0.5 * s, cy + h * 0.5 * s), (cx + w * 0.5 * s, cy + h * 0.5 * s), 0.6, 0.3)]
    for k in range(3):
        x = cx - w * 0.25 * s + k * w * 0.25 * s
        out.append(_s((x, cy - h * 0.5 * s), (x, cy + h * 0.5 * s), 0.2, col=GREY))
    for k in range(2):
        y = cy - h * 0.2 * s + k * h * 0.35 * s
        out.append(_s((cx - w * 0.5 * s, y), (cx + w * 0.5 * s, y), 0.2, col=GREY))
    return out


# ---------------------------------------------------------------- 精修三具（覆盖前版）
def water(cx, cy, w=120, rows=3, gap=13, s=1.0, amp=3.4):
    """水：波纹弧 + 断线，层层下压。"""
    out = []
    for r in range(rows):
        y = cy + r * gap * s
        hw = w * s * (1 - r * 0.05)
        sw = amp * s * (1 - r * 0.12)
        out.append(_q((cx - hw, y - sw * 0.8), (cx - hw * 0.5, y + sw * 1.5), (cx - hw * 0.08, y), 0.4, col=INK2, n=14))
        out.append(_q((cx - hw * 0.08, y), (cx + hw * 0.42, y - sw * 1.5), (cx + hw * 0.9, y - sw * 0.6), 0.4, col=INK2, n=14))
        if r % 2 == 0:
            out.append(B.hair([(cx + hw * 0.24, y + sw * 0.9), (cx + hw * 0.52, y + sw * 0.9)], 0.22, GREY))
    return out


def bank(cx, cy, w=130, h=54, s=1.0, side=1):
    """岸坡：折岸、坡面、草簇、碎石。"""
    out = [_q((cx - w * s, cy + h * 0.7 * s), (cx - w * 0.5 * s * side, cy + h * 0.18 * s), (cx - w * 0.34 * s * side, cy - h * 0.06 * s), 0.95, 0.45),
           _q((cx - w * 0.34 * s * side, cy - h * 0.06 * s), (cx + w * 0.2 * s * side, cy + h * 0.24 * s), (cx + w * 0.9 * s * side, cy + h * 0.52 * s), 0.8, 0.35),
           _s((cx - w * s, cy + h * 0.7 * s), (cx + w * 0.9 * s * side, cy + h * 0.52 * s), 0.28, col=GREY)]
    for k in range(5):
        x0 = cx - w * 0.62 * s + k * w * 0.34 * s * side
        y0 = cy + h * 0.22 * s + (k % 2) * 5 * s
        for m in range(3):
            out.append(B.hair([(x0, y0), (x0 + (2 + m * 2) * s * side, y0 - (7 - m * 2) * s)], 0.2, GREY))
    out.append(B.oval(cx + w * 0.3 * s, cy + h * 0.34 * s, 6 * s, 3.6 * s, 0.4, INK2, n=16))
    return out


def boat(cx, cy, L=104, s=1.0):
    """舟：底弧、内外双舷、首尾起翘、四肋、舱篷、双桨、水线。"""
    h = 26 * s
    half = L * 0.5 * s
    out = []
    # 船底（长弧）
    out.append(_q((cx - half, cy - 2 * s), (cx, cy + h * 1.25), (cx + half, cy - 2 * s), 0.95, 0.5, te=0.3))
    # 外舷
    out.append(_q((cx - half, cy - 2 * s), (cx - half * 0.86, cy - h * 0.9), (cx - half * 0.66, cy - h * 1.15), 0.75, 0.4))
    out.append(_q((cx + half, cy - 2 * s), (cx + half * 0.86, cy - h * 0.9), (cx + half * 0.66, cy - h * 1.15), 0.75, 0.4))
    # 内舷（厚度）
    out.append(_q((cx - half * 0.94, cy + 1.0 * s), (cx - half * 0.80, cy - h * 0.62), (cx - half * 0.62, cy - h * 0.86), 0.3, col=INK2))
    out.append(_q((cx + half * 0.94, cy + 1.0 * s), (cx + half * 0.80, cy - h * 0.62), (cx + half * 0.62, cy - h * 0.86), 0.3, col=INK2))
    # 舷口：首尾起翘 + 上缘
    out.append(_s((cx - half * 0.66, cy - h * 1.15), (cx - half * 0.34, cy - h * 1.02), 0.7, 0.45))
    out.append(_s((cx - half * 0.34, cy - h * 1.02), (cx + half * 0.30, cy - h * 1.02), 0.55, 0.4, col=INK2))
    out.append(_s((cx + half * 0.30, cy - h * 1.02), (cx + half * 0.66, cy - h * 1.15), 0.7, 0.45))
    out.append(_q((cx - half * 0.66, cy - h * 1.15), (cx - half * 0.86, cy - h * 1.4), (cx - half * 0.92, cy - h * 1.72), 0.5, 0.12, te=0.55))
    out.append(_q((cx + half * 0.66, cy - h * 1.15), (cx + half * 0.88, cy - h * 1.4), (cx + half * 0.94, cy - h * 1.72), 0.5, 0.12, te=0.55))
    # 四肋
    for k in range(4):
        t = -0.42 + k * 0.28
        x = cx + t * half
        out.append(_s((x, cy - h * 0.98), (x + 1.5 * s, cy + h * 1.05), 0.26, col=GREY))
    # 舱篷（拱形，两道）
    for k, r in enumerate((0.42, 0.30)):
        out.append(_q((cx - half * 0.30, cy - h * 1.03), (cx, cy - h * (1.55 + k * 0.18)), (cx + half * 0.30, cy - h * 1.03), 0.55, 0.3, col=INK))
        break
    out.append(_q((cx - half * 0.22, cy - h * 1.03), (cx, cy - h * 1.5), (cx + half * 0.22, cy - h * 1.03), 0.28, col=INK2))
    # 双桨
    for sgn in (1, -1):
        out.append(_s((cx + sgn * half * 0.42, cy - h * 1.55), (cx + sgn * half * 0.92, cy + h * 1.62), 0.46, 0.2, col=INK2))
        out.append(_s((cx + sgn * half * 0.42, cy - h * 1.55), (cx + sgn * half * 0.56, cy - h * 1.78), 0.3, 0.1, col=INK2))
    # 水线
    for k in range(2):
        out.append(B.hair([(cx - half * 1.1, cy + h * 1.42 + k * 7 * s), (cx + half * 1.1, cy + h * 1.42 + k * 7 * s)], 0.24, GREY))
    return out


def hair_mao(cx, cy, s=1.0, two=True):
    """两髦：侧身二人，头、颈、交领衣、腰、双足，各垂两缕髦至胸。"""
    out = []

    def one(x, flip=1):
        o = []
        hh = 52 * s   # 半身高
        # 头（椭圆）与发
        o.append(B.oval(x, cy - hh * 0.96, 8.6 * s, 9.6 * s, 0.65, INK, n=26))
        o.append(_q((x - 8.6 * s, cy - hh * 1.02), (x, cy - hh * 1.2), (x + 8.6 * s, cy - hh * 1.0), 0.5, 0.2, te=0.5))  # 发顶
        # 颈
        o.append(_s((x + flip * 1.6 * s, cy - hh * 0.72), (x + flip * 1.0 * s, cy - hh * 0.60), 0.45, col=INK2))
        # 肩线（左右肩）
        o.append(_s((x - 13.5 * s, cy - hh * 0.62), (x + 13.0 * s, cy - hh * 0.62), 0.8, 0.45))
        # 交领
        o.append(_s((x - 8.0 * s, cy - hh * 0.62), (x + 2.0 * s, cy - hh * 0.22), 0.5, col=INK2))
        o.append(_s((x + 7.5 * s, cy - hh * 0.62), (x + 2.0 * s, cy - hh * 0.22), 0.5, col=INK2))
        # 身（两侧下收）
        o.append(_q((x - 13.5 * s, cy - hh * 0.62), (x - 19.0 * s, cy - hh * 0.14), (x - 14.5 * s, cy + hh * 0.28), 0.7, 0.4))
        o.append(_q((x + 13.0 * s, cy - hh * 0.62), (x + 18.5 * s, cy - hh * 0.14), (x + 14.0 * s, cy + hh * 0.28), 0.7, 0.4))
        # 腰带
        o.append(_s((x - 18.2 * s, cy - hh * 0.10), (x + 17.6 * s, cy - hh * 0.10), 0.62, 0.42))
        # 下摆
        o.append(_q((x - 13.0 * s, cy + hh * 0.26), (x - 2.0 * s, cy + hh * 0.36), (x + 12.5 * s, cy + hh * 0.26), 0.75, 0.45))
        # 两足
        o.append(_s((x - 5.0 * s, cy + hh * 0.36), (x - 6.0 * s, cy + hh * 0.62), 0.45, 0.28, col=INK2))
        o.append(_s((x + 5.0 * s, cy + hh * 0.36), (x + 6.5 * s, cy + hh * 0.62), 0.45, 0.28, col=INK2))
        o.append(_s((x - 11.0 * s, cy + hh * 0.62), (x + 2.0 * s, cy + hh * 0.62), 0.28, col=GREY))
        # 两髦（垂发两缕，至胸）
        o.append(_q((x - 8.2 * s, cy - hh * 0.94), (x - 12.6 * s, cy - hh * 0.52), (x - 12.2 * s, cy + hh * 0.04), 0.66, 0.12, te=0.6, col=INK2))
        o.append(_q((x + 8.0 * s, cy - hh * 0.94), (x + 12.2 * s, cy - hh * 0.50), (x + 11.6 * s, cy + hh * 0.04), 0.6, 0.1, te=0.6, col=INK2))
        return o

    out += one(cx - 40 * s, 1)
    if two:
        out += one(cx + 40 * s, -1)
    return out
