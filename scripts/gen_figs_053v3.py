# -*- coding: utf-8 -*-
"""SJ053 三旗 · 笔压白描 v3

相对 v2 的三处整改（v2 的问题都是「线」的问题，不是构图的问题）：
1) 全图画等宽线（0.85/0.55），所以像铁丝。v3 每一笔都走 svgbrush 的变宽笔触：
   起笔重、行笔匀、收笔出锋。三阶墨：轮廓 0.9 / 结构 0.5 / 细部 0.28。
2) 旄尾「过散」：v2 的缕根从束外起、尾端随机落。v3 缕根压在束身内 12px，
   尾端按锥形下摆分布（中间长、两侧短），缕身带一次侧弯。
3) 羽「偏叶形」：v2 用对称 sin 宽度，成梭形。v3 改「弯刀」——宽度偏前段、
   后端骤收成尖，外缘凸、内缘凹，羽轴出尖，羽枝向后斜三分段。
4) 旗内鸟隼改用实形：头、喙、背、两折翅、三根尾羽，不再是三条弧。
"""
import os
import sys
import math
import numpy as np

SK = "/home/user/.doubao/agent_mode/workspace/.user_skills/runze-shijing-figure/scripts"
sys.path.insert(0, SK)
import svgbrush as B  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "fig", "sj053a-san-qi-zai-jun-v3.svg")
W, H = 760, 540
INK, INK2, PAPER, RED, GREY = B.INK, B.INK2, B.PAPER, B.RED, B.GREY

g = [B.svg_open(W, H), B.grid_check((W, H))]


def qb(p0, p1, p2, n=16):
    t = np.linspace(0, 1, n)[:, None]
    p0, p1, p2 = (np.asarray(p, float) for p in (p0, p1, p2))
    return (1 - t) ** 2 * p0 + 2 * (1 - t) * t * p1 + t ** 2 * p2


def q(p0, p1, p2, w=0.9, w1=None, taper_end=0.0, taper_start=0.0, col=INK, n=18):
    return B.stroke(qb(p0, p1, p2, n), w, w1, n=n, col=col, taper_end=taper_end, taper_start=taper_start)


# ---------------------------------------------------------------- 页眉
g.append(B.text(44, 58, '鄘风 · 四', 8.6, RED, ls=2))
g.append(B.text(380, 60, '干 旄', 26, INK, anchor='middle', ls=10, weight=500))
g.append(B.text(716, 58, '诗三百五篇 · 之五十三', 8.2, GREY, anchor='end', ls=1.5))
g.append('<line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.7"/>' % GREY)

TOP, BASE = 124, 430


def pole(cx):
    """杆：双线，上段略收；顶端小箍＋锥。"""
    out = [B.stroke([(cx - 1.7, BASE), (cx - 1.55, 260), (cx - 1.35, TOP - 4)], 0.62, 0.44, n=60),
           B.stroke([(cx + 1.7, BASE), (cx + 1.55, 260), (cx + 1.35, TOP - 4)], 0.62, 0.44, n=60)]
    out.append('<path d="M%.2f,%.2f L%.2f,%.2f" stroke="%s" stroke-width="0.28" fill="none"/>'
               % (cx - 1.7, BASE - 3, cx + 1.7, BASE - 3, INK2))
    out.append(B.stroke([(cx - 5.4, TOP - 1), (cx - 4.6, TOP - 6), (cx - 2.6, TOP - 12),
                         (cx, TOP - 16)], 0.7, 0.25, taper_end=0.5))
    out.append(B.stroke([(cx + 5.4, TOP - 1), (cx + 4.6, TOP - 6), (cx + 2.6, TOP - 12),
                         (cx, TOP - 16)], 0.7, 0.25, taper_end=0.5))
    out.append(B.stroke([(cx - 5.4, TOP - 1), (cx + 5.4, TOP - 1)], 1.1, 0.7, n=8))
    return out


# ---------------------------------------------------------------- 壹 干旄
cx = 152
g += pole(cx)
# 束身：上窄下宽，两侧外弧，不封口（封口即「柱＋一堆线」）
g.append(q((cx - 3.0, 134), (cx - 9.5, 150), (cx - 8.0, 176), 0.9, taper_end=0.25))
g.append(q((cx + 3.0, 134), (cx + 9.5, 150), (cx + 8.0, 176), 0.9, taper_end=0.25))
for y, w in ((142, 9.2), (150, 9.0), (158, 8.6)):
    g.append(q((cx - w, y + 1.2), (cx, y - 1.4), (cx + w, y + 1.2), 0.34, col=INK2))
# 旄尾：18 缕，根在束内（y 168..176），尾端锥形下摆
rng = np.random.default_rng(11)
N = 18
for i in range(N):
    t = i / (N - 1)                      # 0..1 横向
    xr = cx - 6.6 + t * 13.2 + rng.uniform(-0.7, 0.7)
    yr = 170 + rng.uniform(-2, 3)
    spread = (t - 0.5) * 38 + rng.uniform(-3, 3)
    yend = 286 - abs(t - 0.5) * 44 + rng.uniform(-9, 9)
    xend = cx + spread
    mid = ((xr + xend) / 2 + rng.uniform(-4, 4), (yr + yend) / 2 + 12)
    g.append(q((xr, yr), mid, (xend, yend), 0.62 - 0.2 * abs(t - 0.5), 0.18, taper_end=0.55,
               col=INK2 if i % 5 else GREY, n=22))

# ---------------------------------------------------------------- 贰 干旟
cx = 380
g += pole(cx)
# 旗面：上下边带弧、右边飘（不是矩形）
g.append(B.stroke([(cx - 50, 150), (cx, 146), (cx + 50, 150)], 1.15, 0.75, n=40))          # 上边
g.append(B.stroke([(cx + 50, 150), (cx + 53, 200), (cx + 50, 262)], 0.6, col=INK2, n=30))   # 右边
g.append(B.stroke([(cx - 50, 150), (cx - 51, 200), (cx - 50, 258)], 0.6, col=INK2, n=30))   # 左边
g.append(B.stroke([(cx - 50, 258), (cx, 265), (cx + 50, 262)], 0.85, 0.5, n=40))            # 下边
# 旗面内的横繃（二道）
for y in (158, 250):
    g.append(B.stroke([(cx - 48, y), (cx + 48, y + 1.5)], 0.26, col=GREY))


def bird_hui(cx0, cy0, s=1.0, flip=1):
    """侧身展翅的隼：头喙、背线、两折翅、三尾羽。线分三阶。"""
    o = []
    f = flip * s
    # 头
    o.append(B.stroke([(cx0 - 9 * s * f, cy0 - 6 * s), (cx0 - 2 * s * f, cy0 - 13 * s),
                       (cx0 + 5 * s * f, cy0 - 9 * s)], 0.72, col=INK, n=20))
    # 喙（尖，向 flip 方向）
    o.append(B.stroke([(cx0 + 5 * s * f, cy0 - 9 * s), (cx0 + 12 * s * f, cy0 - 7 * s)],
                      0.6, 0.1, taper_end=0.7))
    # 背到腹
    o.append(B.stroke([(cx0 - 9 * s * f, cy0 - 6 * s), (cx0 - 16 * s * f, cy0 + 4 * s),
                       (cx0 - 12 * s * f, cy0 + 14 * s)], 0.78, 0.5, n=24))
    # 翅上缘（展）
    o.append(B.stroke([(cx0 - 4 * s * f, cy0 - 8 * s), (cx0 - 22 * s * f, cy0 - 22 * s),
                       (cx0 - 44 * s * f, cy0 - 20 * s)], 0.82, 0.3, taper_end=0.45))
    # 翅下缘
    o.append(B.stroke([(cx0 - 10 * s * f, cy0 + 2 * s), (cx0 - 18 * s * f, cy0 - 8 * s),
                       (cx0 - 40 * s * f, cy0 - 12 * s)], 0.55, col=INK2))
    # 翅羽两折（结构线）
    for k in range(2):
        t = 0.45 + k * 0.22
        o.append(B.hair([(cx0 - 4 * s * f - 38 * s * f * t, cy0 - 20 * s + 2 * s * k),
                         (cx0 - 4 * s * f - 34 * s * f * t, cy0 - 12 * s + 2 * s * k)], 0.26, GREY))
    # 三尾羽
    for k in range(3):
        o.append(B.stroke([(cx0 - 12 * s * f, cy0 + 14 * s),
                           (cx0 - 22 * s * f - k * 2 * s, cy0 + 22 * s + k * 5 * s),
                           (cx0 - 34 * s * f - k * 3 * s, cy0 + 30 * s + k * 6 * s)],
                          0.48, 0.12, taper_end=0.5, col=INK2))
    # 爪
    o.append(B.stroke([(cx0 + 2 * s * f, cy0 + 8 * s), (cx0 + 4 * s * f, cy0 + 18 * s)],
                      0.4, 0.2, col=INK2))
    o.append(B.stroke([(cx0 - 8 * s * f, cy0 + 6 * s), (cx0 - 10 * s * f, cy0 + 16 * s)],
                      0.4, 0.2, col=INK2))
    return o


g += bird_hui(392, 200, 0.96, 1)
# 旒：七条，根在旗面下缘，走弧
rng2 = np.random.default_rng(3)
for i in range(7):
    x0 = cx - 42 + i * 14
    ln = 46 + (i % 3) * 11
    sgn = 1 if i % 2 else -1
    g.append(q((x0, 262), (x0 + sgn * 3.4, 262 + ln * 0.55), (x0 + sgn * 4.2, 262 + ln),
               0.75, 0.25, taper_end=0.5, col=INK2, n=18))

# ---------------------------------------------------------------- 叁 干旌
cx = 608
g += pole(cx)


def blade(bx, by, length, width, ang, bend=0.0, w=0.72):
    """一片「弯刀」羽：宽度偏前段、后端骤收；外凸内凹；羽轴出尖。"""
    dx, dy = math.sin(ang), -math.cos(ang)
    nx, ny = -dy, dx
    ts = np.linspace(0, 1, 18)
    left, right = [], []
    for t in ts:
        # 中线随 bend 侧弯
        px = bx + dx * length * t + nx * bend * (t ** 2)
        py = by + dy * length * t + ny * bend * (t ** 2)
        prof = max(0.0, math.sin(math.pi * (t ** 0.78))) ** 0.62
        wl = width * prof * (0.62 + 0.38 * t)      # 外缘（凸）
        wr = width * prof * (0.40 + 0.22 * t)      # 内缘（凹），不对称
        left.append((px + nx * wl, py + ny * wl))
        right.append((px - nx * wr, py - ny * wr))
    out = [B.stroke(left, w, 0.22, taper_end=0.62, n=26), B.stroke(right, w * 0.86, 0.18, taper_end=0.68, n=26)]
    # 羽轴，末端出尖
    out.append(B.stroke([(bx, by), (bx + dx * length * 0.90, by + dy * length * 0.90)],
                        0.30, 0.05, taper_end=0.7, col=INK2, n=16))
    # 羽枝：向后斜，两段
    for k in range(3):
        t = 0.16 + k * 0.26
        px = bx + dx * length * t + nx * bend * (t ** 2)
        py = by + dy * length * t + ny * bend * (t ** 2)
        prof = max(0.0, math.sin(math.pi * (t ** 0.78))) ** 0.62
        for sgn in (1, -1):
            wd = width * prof * (0.52 if sgn > 0 else 0.34)
            out.append(B.hair([(px, py), (px + sgn * nx * wd * 0.9 + dx * 3.2,
                                         py + sgn * ny * wd * 0.9 + dy * 3.2)], 0.22, GREY))
    return out


for k in range(5):
    by = 176 + k * 46
    tilt = 0.26 if k % 2 == 0 else -0.30
    g += blade(cx + (2 if k % 2 == 0 else -2), by, 78, 13.5, tilt, bend=3.2 if k % 2 == 0 else -3.2)
    g += blade(cx + (-3 if k % 2 == 0 else 3), by + 9, 64, 11.0, tilt * 1.9, bend=-2.0)
    g += blade(cx + 4, by + 14, 52, 9.0, -tilt * 0.6, bend=2.4)
    # 束箍
    g.append(B.stroke([(cx - 3.8, by - 3), (cx + 3.8, by - 3)], 0.75, 0.45, n=8))
    g.append(B.stroke([(cx - 3.2, by + 3.4), (cx + 3.2, by + 3.4)], 0.45, col=INK2, n=8))

# ---------------------------------------------------------------- 版式注记
for (x, t) in [(118, '壹'), (348, '贰'), (588, '叁')]:
    g.append(B.text(x, 132, t, 7.6, RED, ls=1))
g.append(B.text(44, 466, '壹 干旄　旄牛尾注杆首', 7.8, INK2, ls=1))
g.append(B.text(264, 466, '贰 干旟　鸟隼为饰', 7.8, INK2, ls=1))
g.append(B.text(486, 466, '叁 干旌　析羽为饰', 7.8, INK2, ls=1))
g.append('<line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.7"/>' % GREY)
g.append(B.text(380, 512, '孑孑干旄，在浚之郊', 16, INK, anchor='middle', ls=3))
g.append(B.text(44, 524, '三旗三制，礼愈近', 7.4, GREY, ls=1))
g.append(B.text(716, 524, '图一 · 名物 · sj053a-v3', 7.4, GREY, anchor='end', ls=1))
g.append('</svg>')

os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, 'w', encoding='utf-8').write(''.join(g))
print('svg', OUT, B.count_bytes(''.join(g)), 'B')
try:
    import cairosvg
    png = os.path.join(ROOT, 'dist', 'sj053a-v3.png')
    os.makedirs(os.path.dirname(png), exist_ok=True)
    cairosvg.svg2png(url=OUT, write_to=png, output_width=1200)
    print('png', png)
except Exception as e:
    print('png-fail', e)
