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
OUT = os.path.join(ROOT, "assets", "fig", "sj053a-san-qi-zai-jun-v6.svg")
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
g.append(q((cx - 7.6, 146), (cx - 13.0, 168), (cx - 12.4, 196), 1.0, taper_end=0.2))
g.append(q((cx + 7.6, 146), (cx + 13.0, 168), (cx + 12.4, 196), 1.0, taper_end=0.2))
for k, y in enumerate((153, 164, 176)):
    hw = 9.0 + k * 1.7
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
    """正面展翅的隼：头喙、纺锤身、两翅两折、三尾羽、双爪。"""
    o = []
    # 头 + 喙（头朝左上，喙向右）
    o.append(B.oval(cx0, cy0 - 30 * s, 6.2 * s, 6.8 * s, 0.62, INK, n=26))
    o.append(seg((cx0 + 4.6 * s, cy0 - 31 * s), (cx0 + 11.5 * s, cy0 - 28 * s), 0.5, 0.06, taper_end=0.62))
    # 身：纺锤（颈 → 腹 → 尾根）
    o.append(q((cx0 - 3.2 * s, cy0 - 24 * s), (cx0 - 8.5 * s, cy0 - 10 * s), (cx0 - 7.0 * s, cy0 + 4 * s), 0.72, n=26))
    o.append(q((cx0 + 3.2 * s, cy0 - 24 * s), (cx0 + 8.5 * s, cy0 - 10 * s), (cx0 + 7.0 * s, cy0 + 4 * s), 0.72, n=26))
    o.append(q((cx0 - 7.0 * s, cy0 + 4 * s), (cx0, cy0 + 10 * s), (cx0 + 7.0 * s, cy0 + 4 * s), 0.6, n=20))
    # 翅：上缘（肩 → 外 → 尖），下缘（腹 → 尖）
    for sgn in (1, -1):
        o.append(q((cx0 + sgn * 5 * s, cy0 - 18 * s), (cx0 + sgn * 30 * s, cy0 - 33 * s),
                   (cx0 + sgn * 56 * s, cy0 - 21 * s), 0.82, 0.22, taper_end=0.35, n=34))
        for j in range(3):
            o.append(seg((cx0 + sgn * (50 + j * 3) * s, cy0 - (22 - j * 3) * s),
                         (cx0 + sgn * (58 + j * 2) * s, cy0 - (14 - j * 4) * s), 0.4, 0.05, taper_end=0.6, col=INK2))
        o.append(q((cx0 + sgn * 6 * s, cy0 - 6 * s), (cx0 + sgn * 30 * s, cy0 - 12 * s),
                   (cx0 + sgn * 54 * s, cy0 - 20 * s), 0.5, col=INK2, n=30))
        # 翅内两折（结构线，短）
        for k in range(2):
            tx = 0.34 + k * 0.24
            o.append(B.hair([(cx0 + sgn * (8 + 44 * tx) * s, cy0 - 21 * s - 2 * s * k),
                             (cx0 + sgn * (12 + 40 * tx) * s, cy0 - 14 * s - 2 * s * k)], 0.24, GREY))
    # 三尾羽
    for k, dx in enumerate((-5.4, 0, 5.4)):
        o.append(B.stroke([(cx0 + dx * 0.4 * s, cy0 + 9 * s), (cx0 + dx * s, cy0 + 26 * s),
                           (cx0 + dx * 1.7 * s, cy0 + 40 * s)], 0.44, 0.08, taper_end=0.5, col=INK2, n=16))
    # 双爪
    for sgn in (1, -1):
        o.append(seg((cx0 + sgn * 4.6 * s, cy0 + 16 * s), (cx0 + sgn * 6.4 * s, cy0 + 28 * s), 0.38, 0.16, col=INK2))
    return o


g += bird(400, 242, 1.16)
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
    by = 198 + k * 66
    tilt = 0.38 if k % 2 == 0 else -0.42
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
g.append(B.text(716, 524, '图一 · 名物 · sj053a-v6', 7.4, GREY, anchor='end', ls=1))
g.append('</svg>')

os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, 'w', encoding='utf-8').write(''.join(g))
print('svg', os.path.basename(OUT), B.count_bytes(''.join(g)), 'B')
import cairosvg  # noqa: E402
png = os.path.join(ROOT, 'dist', 'sj053a-v6.png')
cairosvg.svg2png(url=OUT, write_to=png, output_width=1200)
print('png', os.path.basename(png))
