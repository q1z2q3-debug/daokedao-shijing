# -*- coding: utf-8 -*-
"""SJ053 三旗 · 笔压白描 v4

v3 的毛病是「画法对了、比例错了」：
- 三杆占画高 306px，旗面只占上部三分之一，下半幅空荡；
- 干旄束身成了球，旄尾只有 26px 宽，不像牛尾；
- 干旌羽长 78 而束距 46，五束叠成棕榈叶（正犯 fails.md 第 4 条）；
- 鸟隼线条二十余根挤在 60px 内，成一团乱麻。

v4 重排：
- 视平线统一 BASE=452，器身在 140–400 之间铺满；
- 旄尾 22 缕，扇面宽 68，束身只留系绳三道，不封口；
- 旌羽长 50、束距 64（≥0.7 羽长），每束三片角度错开；
- 鸟隼改正面展翅的「简形」：头喙、纺锤身、两翅各两折、三尾羽，共十四根线。
"""
import os
import sys
import math
import numpy as np

SK = "/home/user/.doubao/agent_mode/workspace/.user_skills/runze-shijing-figure/scripts"
sys.path.insert(0, SK)
import svgbrush as B  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "fig", "sj053a-san-qi-zai-jun-v8.svg")
W, H = 760, 540
INK, INK2, PAPER, RED, GREY = B.INK, B.INK2, B.PAPER, B.RED, B.GREY

g = [B.svg_open(W, H), B.grid_check((W, H))]


def qb(p0, p1, p2, n=16):
    t = np.linspace(0, 1, n)[:, None]
    p0, p1, p2 = (np.asarray(p, float) for p in (p0, p1, p2))
    return (1 - t) ** 2 * p0 + 2 * (1 - t) * t * p1 + t ** 2 * p2


def q(p0, p1, p2, w=0.9, w1=None, taper_end=0.0, taper_start=0.0, col=INK, n=18):
    return B.stroke(qb(p0, p1, p2, n), w, w1, n=n, col=col, taper_end=taper_end, taper_start=taper_start)


def seg(p0, p1, w=0.9, w1=None, taper_end=0.0, col=INK, n=6):
    return B.stroke([p0, p1], w, w1, n=n, col=col, taper_end=taper_end)


# ---------------------------------------------------------------- 页眉
g.append(B.text(44, 58, '鄘风 · 四', 8.6, RED, ls=2))
g.append(B.text(380, 60, '干 旄', 26, INK, anchor='middle', ls=10, weight=500))
g.append(B.text(716, 58, '诗三百五篇 · 之五十三', 8.2, GREY, anchor='end', ls=1.5))
g.append('<line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.7"/>' % GREY)

TOP, BASE = 138, 452


def pole(cx, base=BASE, top=TOP):
    out = [seg((cx - 2.7, base), (cx - 2.1, top + 10), 0.85, 0.6, n=40),
           seg((cx + 2.7, base), (cx + 2.1, top + 10), 0.85, 0.6, n=40),
           '<path d="M%.2f,%.2f L%.2f,%.2f" stroke="%s" stroke-width="0.26" fill="none"/>'
           % (cx - 2.7, base - 4, cx + 2.7, base - 4, INK2)]
    # 顶端箍与锥
    out.append(seg((cx - 7.0, top + 3), (cx + 7.0, top + 3), 1.3, 0.8, n=8))
    out.append(q((cx - 7.0, top + 3), (cx - 5.6, top - 8), (cx, top - 21), 0.95, 0.16, taper_end=0.55))
    out.append(q((cx + 7.0, top + 3), (cx + 5.6, top - 8), (cx, top - 21), 0.95, 0.16, taper_end=0.55))
    return out


# ---------------------------------------------------------------- 壹 干旄
cx = 152
g += pole(cx)
# 束身：上窄下宽，两条外弧＋三道系绳；不封口
g.append(q((cx - 8.4, 150), (cx - 13.2, 166), (cx - 12.6, 186), 1.0, taper_end=0.15))
g.append(q((cx + 8.4, 150), (cx + 13.2, 166), (cx + 12.6, 186), 1.0, taper_end=0.15))
for k, y in enumerate((156, 166, 178)):
    hw = 9.6 + k * 1.4
    g.append(q((cx - hw, y + 1.4), (cx, y - 1.2), (cx + hw, y + 1.4), 0.32, col=INK2))
# 旄尾：22 缕，根在束内，尾端扇面
rng = np.random.default_rng(17)
N = 18
for i in range(N):
    t = i / (N - 1)
    xr = cx - 10.6 + t * 21.2 + rng.uniform(-0.6, 0.6)
    yr = 190 + rng.uniform(0, 7)
    xend = cx + (t - 0.5) * 88 + rng.uniform(-4, 4)
    yend = 356 - abs(t - 0.5) * 66 + rng.uniform(-12, 12)
    mid = ((xr + xend) / 2 + (xend - xr) * 0.12, 262 + rng.uniform(-6, 8))
    g.append(q((xr, yr), mid, (xend, yend), 0.95 - 0.26 * abs(t - 0.5), 0.10, taper_end=0.66,
               col=INK2 if i % 4 else GREY, n=24))

# ---------------------------------------------------------------- 贰 干旟
cx = 380
g += pole(cx)
# 旗面：上边略上弧，下边略下弧，右边下摆外飘
g.append(B.stroke([(cx - 76, 174), (cx - 8, 166), (cx + 76, 174)], 1.2, 0.72, n=48))         # 上边
g.append(B.stroke([(cx - 76, 174), (cx - 79, 258), (cx - 76, 344)], 0.6, col=INK2, n=34))  # 左边
g.append(B.stroke([(cx + 76, 174), (cx + 81, 258), (cx + 84, 346)], 0.6, col=INK2, n=34))  # 右边
g.append(B.stroke([(cx - 76, 344), (cx - 4, 352), (cx + 84, 346)], 0.95, 0.55, n=48))        # 下边
for y in (184, 334):
    g.append(B.stroke([(cx - 72, y), (cx + 74, y + 2)], 0.26, col=GREY))


def bird(cx0, cy0, s=1.0):
    """侧身隼（头朝右）：圆头短喙、背弧腹弧、单翅向后上展、三根尾羽、一足。

    为什么放弃正面展翅：正面两翼的上下缘近乎平行，中间必然读成一层膜，
    无论怎么加飞羽都像蝙蝠。侧面单翅的翼弦由肩向尖收窄，才是鸟。
    """
    o = []
    # 头、喙、眼
    o.append(B.oval(cx0 + 20 * s, cy0 - 7 * s, 5.2 * s, 5.4 * s, 0.62, INK, n=26))
    o.append(seg((cx0 + 24.4 * s, cy0 - 8.4 * s), (cx0 + 31.5 * s, cy0 - 6.2 * s), 0.48, 0.04, taper_end=0.7))
    o.append(B.hair([(cx0 + 18.4 * s, cy0 - 8.6 * s), (cx0 + 19.6 * s, cy0 - 7.8 * s)], 0.26, INK))
    # 背弧（颈 → 背 → 尾根）
    o.append(q((cx0 + 16 * s, cy0 - 12 * s), (cx0, cy0 - 17 * s), (cx0 - 14 * s, cy0 - 8 * s), 0.82, n=28))
    # 腹弧（颈下 → 胸 → 腹 → 尾根）
    o.append(q((cx0 + 17 * s, cy0 - 2 * s), (cx0 + 4 * s, cy0 + 9 * s), (cx0 - 9 * s, cy0 + 7 * s), 0.7, col=INK2, n=26))
    # 三根尾羽（向后，略下）
    for k, d in enumerate((0, 5, 10)):
        o.append(seg((cx0 - 13 * s, cy0 - (8 - k * 3) * s),
                     (cx0 - (31 + k * 4) * s, cy0 - (12 - k * 7) * s), 0.44, 0.06, taper_end=0.6, col=INK2))
    # 翅：肩 (-1,-13) → 外上 (-16,-27) → 翅尖 (-36,-24)
    o.append(q((cx0 - 1 * s, cy0 - 13 * s), (cx0 - 16 * s, cy0 - 29 * s), (cx0 - 36 * s, cy0 - 24 * s), 0.86, 0.3, taper_end=0.28, n=36))
    o.append(q((cx0 - 3 * s, cy0 - 3 * s), (cx0 - 20 * s, cy0 - 12 * s), (cx0 - 35 * s, cy0 - 22.5 * s), 0.5, col=INK2, n=32))
    # 初级飞羽四根：自翅尖向后下分离
    for j in range(4):
        t = j / 3.0
        bx = cx0 - (36 - 5 * t) * s
        by = cy0 - (23 + 1.2 * t) * s
        o.append(seg((bx, by), (bx - (9 - 3 * t) * s, by + (8 + 3 * t) * s),
                     0.44 - 0.05 * j, 0.04, taper_end=0.75, col=INK if j < 2 else INK2))
    # 覆羽三道（沿翼展方向）
    for m in range(3):
        t = 0.2 + m * 0.22
        x0 = cx0 - (4 + 30 * t) * s
        y0 = cy0 - (13 + 11 * t) * s
        o.append(B.hair([(x0, y0), (x0 - 3 * s, y0 + 7 * s)], 0.24, GREY))
    # 一足与爪
    o.append(seg((cx0 + 5 * s, cy0 + 8 * s), (cx0 + 6 * s, cy0 + 20 * s), 0.4, 0.16, col=INK2))
    o.append(seg((cx0 + 6 * s, cy0 + 20 * s), (cx0 + 12 * s, cy0 + 24 * s), 0.3, 0.08, col=INK2))
    o.append(seg((cx0 + 6 * s, cy0 + 20 * s), (cx0 + 2 * s, cy0 + 25 * s), 0.3, 0.08, col=INK2))
    return o


g += bird(392, 240, 1.28)
# 旒：七条，根在旗面下缘，垂过杆底
for i in range(9):
    x0 = cx - 68 + i * 19.0
    ln = 40 + (4 - abs(i - 4)) * 16 + (i % 2) * 6
    sgn = 1 if i % 2 else -1
    g.append(q((x0, 333), (x0 + sgn * 4.4, 333 + ln * 0.5), (x0 + sgn * 6.4, 333 + ln),
               0.88, 0.18, taper_end=0.6, col=INK2, n=20))

# ---------------------------------------------------------------- 叁 干旌
cx = 608
g += pole(cx)


def blade(bx, by, length, width, ang, bend=0.0, w=0.66):
    """弯刀羽：外缘凸、内缘凹，后端骤收出尖，羽轴出尖，羽枝向后斜。"""
    dx, dy = math.sin(ang), -math.cos(ang)
    nx, ny = -dy, dx
    ts = np.linspace(0, 1, 20)
    left, right = [], []
    for t in ts:
        px = bx + dx * length * t + nx * bend * (t ** 2)
        py = by + dy * length * t + ny * bend * (t ** 2)
        prof = max(0.0, math.sin(math.pi * (t ** 0.76))) ** 0.6
        wl = width * prof * (0.60 + 0.40 * t)
        wr = width * prof * (0.36 + 0.20 * t)
        left.append((px + nx * wl, py + ny * wl))
        right.append((px - nx * wr, py - ny * wr))
    out = [B.stroke(left, w, 0.2, taper_end=0.6, n=26), B.stroke(right, w * 0.84, 0.16, taper_end=0.66, n=26)]
    out.append(B.stroke([(bx, by), (bx + dx * length * 0.92, by + dy * length * 0.92)],
                        0.26, 0.05, taper_end=0.7, col=INK2, n=18))
    for k in range(2):
        t = 0.24 + k * 0.3
        px = bx + dx * length * t + nx * bend * (t ** 2)
        py = by + dy * length * t + ny * bend * (t ** 2)
        prof = max(0.0, math.sin(math.pi * (t ** 0.76))) ** 0.6
        for sgn in (1, -1):
            wd = width * prof * (0.5 if sgn > 0 else 0.32)
            out.append(B.hair([(px, py), (px + sgn * nx * wd * 0.88 + dx * 3.0,
                                         py + sgn * ny * wd * 0.88 + dy * 3.0)], 0.2, GREY))
    return out


for k in range(4):
    by = 200 + k * 70
    tilt = 0.30 if k % 2 == 0 else -0.34
    g += blade(cx + (2 if k % 2 == 0 else -2), by, 66, 12.5, tilt, bend=2.6 if k % 2 == 0 else -2.6)
    g += blade(cx + (-3 if k % 2 == 0 else 3), by + 9, 47, 9.6, tilt * 2.0, bend=-1.6)
    g += blade(cx + 4, by + 15, 37, 7.8, -tilt * 0.55, bend=1.9)
    g.append(seg((cx - 4.0, by - 2), (cx + 4.0, by - 2), 0.7, 0.42, n=6))
    g.append(seg((cx - 3.4, by + 3.6), (cx + 3.4, by + 3.6), 0.4, col=INK2, n=6))

# ---------------------------------------------------------------- 版式注记
for (x, t) in [(118, '壹'), (348, '贰'), (588, '叁')]:
    g.append(B.text(x, 132, t, 7.6, RED, ls=1))
g.append(B.text(44, 466, '壹 干旄　旄牛尾注杆首', 7.8, INK2, ls=1))
g.append(B.text(264, 466, '贰 干旟　鸟隼为饰', 7.8, INK2, ls=1))
g.append(B.text(486, 466, '叁 干旌　析羽为饰', 7.8, INK2, ls=1))
g.append('<line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.7"/>' % GREY)
g.append(B.text(380, 512, '孑孑干旄，在浚之郊', 16, INK, anchor='middle', ls=3))
g.append(B.text(44, 524, '三旗三制，礼愈近', 7.4, GREY, ls=1))
g.append(B.text(716, 524, '图一 · 名物 · sj053a-v8', 7.4, GREY, anchor='end', ls=1))
g.append('</svg>')

os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, 'w', encoding='utf-8').write(''.join(g))
print('svg', os.path.basename(OUT), B.count_bytes(''.join(g)), 'B')
import cairosvg  # noqa: E402
png = os.path.join(ROOT, 'dist', 'sj053a-v8.png')
cairosvg.svg2png(url=OUT, write_to=png, output_width=1200)
print('png', os.path.basename(png))
