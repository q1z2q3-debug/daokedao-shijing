# -*- coding: utf-8 -*-
"""077 叔于田 · 图一（名物/场景）

左：里涂空巷，两扇门开着，人只在门后探头；巷中酒器有酒无人。
中：一张弓、一壶箭、一串蹄迹；不画叔，只画他出巷后的空。
右：郊野，野树与飞禽。
「巷无居人」不是巷空，是人心都跟叔出了巷。
"""
import math
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import svgbrush as B  # noqa: E402

W, H = 760, 540
PAPER = '#F5F1E8'
RED = '#A63D2F'
GOLD = '#B79A63'
LG = '#6B6259'


def house(x0, x1, base, top, door):
    """里居：夯土墙、瓦顶、一扇门；门内留空。"""
    out = []
    out.append(B.stroke([(x0, base), (x0, top), (x1, top), (x1, base)],
                        0.7, 0.38, n=20, col=B.INK, taper_end=0.1))
    # 瓦顶
    for x in range(x0 - 6, x1 + 6, 13):
        out.append(B.hair([(x, top - 6), (x + 7, top + 2)], 0.36, B.INK2))
    out.append(B.stroke([(x0 - 10, top - 6), (x1 + 10, top - 6)], 0.46, 0.28, n=14, col=B.INK))
    # 夯土横线
    for k in range(2):
        yy = top + 22 + k * 18
        out.append(B.hair([(x0 + 7, yy), (x1 - 7, yy + (1 if k % 2 else -1))], 0.24, B.GREY))
    # 门洞
    dc, dw = door
    out.append(B.stroke([(dc - dw, base), (dc - dw, top + 34)], 0.54, 0.3, n=12, col=B.INK))
    out.append(B.stroke([(dc + dw, base), (dc + dw, top + 34)], 0.54, 0.3, n=12, col=B.INK))
    out.append(B.stroke([(dc - dw - 3, top + 34), (dc + dw + 3, top + 34)],
                        0.44, 0.28, n=12, col=B.INK2))
    out.append(B.hair([(dc - dw + 2, base - 2), (dc + dw - 2, base - 2)], 0.24, B.GREY))
    # 半开门扇
    out.append(B.stroke([(dc - dw, base - 2), (dc - dw + 4, top + 42)],
                        0.32, 0.22, n=10, col=B.GREY, taper_end=0.3))
    # 门侧小窗：方格，不填
    wx = x0 + 12
    wy = top + 48
    out.append(B.stroke([(wx, wy), (wx, wy + 22), (wx + 18, wy + 22), (wx + 18, wy)],
                        0.34, 0.2, n=12, col=B.GREY, taper_end=0.2))
    out.append(B.hair([(wx + 9, wy), (wx + 9, wy + 22)], 0.22, B.GREY))
    out.append(B.hair([(wx, wy + 11), (wx + 18, wy + 11)], 0.22, B.GREY))
    return out


def peek(cx, base, scale=0.75):
    """门后探头的人：头、肩、一只手，身体被门框遮住。"""
    out = []
    r = 7.4 * scale
    top = base - 42 * scale
    out.append(B.oval(cx, top + r, r, r * 1.08, 0.6, B.INK2, n=30))
    out.append(B.arcband(cx, top + r, r + 1, r * 1.08 + 1, 3.4, 5.95, 0.32, B.INK, n=16))
    # 肩：短斜，断在门框内
    out.append(B.stroke([(cx - r * 1.6, base), (cx - r * 1.0, top + r * 2.4)],
                        0.38, 0.24, n=10, col=B.INK2, taper_end=0.25))
    out.append(B.stroke([(cx + r * 1.6, base), (cx + r * 1.0, top + r * 2.4)],
                        0.38, 0.24, n=10, col=B.INK2, taper_end=0.25))
    # 手扶门框
    out.append(B.hair([(cx + r * 1.1, top + r * 2.2), (cx + r * 2.2, top + r * 1.5)],
                      0.28, B.INK2))
    return out


def horse(cx, base):
    """马：侧身，一条外轮廓从左臀经背、颈、头，再回到胸腹。"""
    out = []
    y = base - 80
    # 单条外轮廓：臀—背—颈—头—胸—腹
    body = (f"M {cx-40},{y+30} C {cx-42},{y+14} {cx-30},{y+4} {cx-10},{y+4}"
            f" L {cx+28},{y+8} C {cx+38},{y+8} {cx+44},{y+12} {cx+46},{y+18}"
            f" L {cx+56},{y-6} L {cx+66},{y-20}"
            f" L {cx+80},{y-24} C {cx+92},{y-24} {cx+98},{y-16} {cx+92},{y-8}"
            f" L {cx+82},{y-2}"
            f" L {cx+66},{y+22} C {cx+58},{y+34} {cx+54},{y+44} {cx+50},{y+52}"
            f" C {cx+46},{y+62} {cx+30},{y+68} {cx+10},{y+68}"
            f" C {cx-12},{y+68} {cx-34},{y+60} {cx-38},{y+44} Z")
    out.append(f'<path d="{body}" fill="none" stroke="{B.INK}" stroke-width="0.95"/>')
    # 耳
    out.append(B.stroke([(cx+80, y-24), (cx+82, y-36)], 0.34, 0.18, n=8, col=B.INK2, taper_end=0.6))
    out.append(B.stroke([(cx+86, y-22), (cx+90, y-33)], 0.34, 0.18, n=8, col=B.INK2, taper_end=0.6))
    # 鬃：沿颈背短斜
    for k in range(8):
        t = k / 7
        px = cx + 46 + 30 * t
        py = y + 18 - 38 * t
        out.append(B.hair([(px, py), (px - 7, py + 8)], 0.26, B.INK2))
    # 四腿：两线一腿，膝折
    for tx, hx in ((cx-26, cx-30), (cx-14, cx-17), (cx+22, cx+27), (cx+34, cx+40)):
        out.append(B.stroke([(tx-3, y+60), (hx-2, base-16), (hx, base)],
                            0.4, 0.22, n=12, col=B.INK2, taper_end=0.18))
        out.append(B.stroke([(tx+3, y+60), (hx+3, base-16), (hx+2, base)],
                            0.4, 0.22, n=12, col=B.INK2, taper_end=0.18))
        out.append(B.hair([(hx-5, base-1), (hx+7, base-1)], 0.26, B.INK))
    # 尾
    out.append(B.stroke([(cx-40, y+34), (cx-54, y+50), (cx-56, y+68)],
                        0.5, 0.22, n=16, col=B.INK2, taper_end=0.5))
    return out


def rider(cx, base):
    """叔段：坐于马背，执弓。宽袖、束带、下裳；不画五官。"""
    out = []
    hy = base - 56
    r = 6.2
    out.append(B.oval(cx, hy, r, r * 1.1, 0.56, B.INK2, n=28))
    out.append(B.arcband(cx, hy, r + 1, r * 1.1 + 1, 3.35, 5.95, 0.3, B.INK, n=16))
    # 小冠
    out.append(B.stroke([(cx - 5, hy - 5), (cx, hy - 9), (cx + 5, hy - 5)],
                        0.34, 0.18, n=10, col=B.INK2, taper_end=0.4))
    # 上身：外轮廓，略宽
    torso = (f"M {cx-10},{hy+8} C {cx-14},{hy+20} {cx-13},{base-18} {cx-8},{base-10}"
             f" L {cx+8},{base-10} C {cx+13},{base-18} {cx+14},{hy+20} {cx+10},{hy+8} Z")
    out.append(f'<path d="{torso}" fill="none" stroke="{B.INK2}" stroke-width="0.6"/>')
    # 交领
    out.append(B.stroke([(cx - 7, hy + 10), (cx, hy + 24), (cx + 7, hy + 10)],
                        0.34, 0.2, n=12, col=B.INK2, taper_end=0.3))
    # 腰带
    out.append(B.stroke([(cx - 9, base - 14), (cx + 9, base - 14)], 0.3, 0.18, n=10, col=B.INK2))
    # 右臂执弓
    out.append(B.stroke([(cx + 9, hy + 12), (cx + 26, base - 28), (cx + 34, base - 38)],
                        0.42, 0.22, n=14, col=B.INK2, taper_end=0.2))
    # 左臂控缰
    out.append(B.stroke([(cx - 9, hy + 12), (cx - 20, base - 28), (cx - 22, base - 18)],
                        0.4, 0.22, n=12, col=B.INK2, taper_end=0.2))
    # 两腿跨马
    out.append(B.stroke([(cx - 6, base - 10), (cx - 18, base + 8), (cx - 22, base + 20)],
                        0.4, 0.22, n=12, col=B.INK2, taper_end=0.2))
    out.append(B.stroke([(cx + 6, base - 10), (cx + 18, base + 8), (cx + 22, base + 20)],
                        0.4, 0.22, n=12, col=B.INK2, taper_end=0.2))
    # 弓
    bx, by = cx + 38, base - 42
    out.append(B.arcband(bx, by, 17, 25, -1.45, 1.45, 0.6, B.INK, n=26))
    out.append(B.stroke([(bx + 17 * math.cos(-1.45), by + 25 * math.sin(-1.45)),
                         (bx + 17 * math.cos(1.45), by + 25 * math.sin(1.45))],
                        0.22, 0.12, n=8, col=B.GREY))
    return out


def deer(cx, base):
    """鹿：侧身，细颈，短角，细腿。躯干与颈各为闭合轮廓。"""
    out = []
    y = base - 52
    body = (f"M {cx-22},{y+26} C {cx-24},{y+12} {cx-14},{y+4} {cx},{y+4}"
            f" C {cx+14},{y+4} {cx+26},{y+12} {cx+26},{y+24}"
            f" C {cx+26},{y+36} {cx+14},{y+44} {cx},{y+44}"
            f" C {cx-14},{y+44} {cx-22},{y+36} {cx-22},{y+26} Z")
    out.append(f'<path d="{body}" fill="none" stroke="{B.INK2}" stroke-width="0.62"/>')
    neck = (f"M {cx+16},{y+14} C {cx+22},{y+2} {cx+26},{y-10} {cx+28},{y-18}"
            f" L {cx+40},{y-22} C {cx+48},{y-22} {cx+52},{y-14} {cx+46},{y-8}"
            f" L {cx+36},{y-2} C {cx+34},{y+8} {cx+32},{y+18} {cx+30},{y+26} Z")
    out.append(f'<path d="{neck}" fill="none" stroke="{B.INK2}" stroke-width="0.48"/>')
    # 角：短而分叉
    for dx in (-2, 3):
        out.append(B.stroke([(cx + 32 + dx, y - 22), (cx + 30 + dx, y - 34),
                             (cx + 36 + dx, y - 40)], 0.28, 0.14, n=10,
                            col=B.INK2, taper_end=0.5))
    # 四腿：两线
    for lx in (-12, -4, 8, 16):
        out.append(B.stroke([(cx + lx - 1, y + 36), (cx + lx - 1, base)], 0.3, 0.16, n=10, col=B.INK2))
        out.append(B.stroke([(cx + lx + 2, y + 36), (cx + lx + 2, base)], 0.3, 0.16, n=10, col=B.INK2))
    # 尾
    out.append(B.hair([(cx - 22, y + 14), (cx - 28, y + 22)], 0.26, B.INK2))
    return out


def tree(cx, base, h=96):
    """野树：干直，枝疏，叶少。"""
    out = []
    top = base - h
    out.append(B.stroke([(cx, base), (cx - 2, base - h * .45), (cx, top)],
                        0.62, 0.28, n=18, col=B.INK2, taper_end=0.2))
    for side, dy, ln in ((-1, 26, 30), (1, 18, 34), (-1, 48, 24), (1, 42, 22)):
        out.append(B.stroke([(cx, top + dy), (cx + side * ln * .55, top + dy - 12),
                             (cx + side * ln, top + dy - 20)], 0.4, 0.2, n=12,
                            col=B.INK2, taper_end=0.5))
    # 叶：短撇，稀疏
    for k in range(34):
        a = k * 2.4
        r = 12 + (k % 5) * 4
        lx = cx + r * math.cos(a) * 1.2
        ly = top + 20 + r * .7 * math.sin(a)
        out.append(B.stroke([(lx, ly), (lx + 2, ly - 5)], 0.26, 0.12, n=8,
                            col=B.GREY, taper_end=0.6))
    return out


def bird(cx, cy, s=1.0):
    """飞鸟：两翼一背，不画头眼。"""
    out = []
    out.append(B.stroke([(cx - 14 * s, cy), (cx - 4 * s, cy - 8 * s), (cx, cy - 2 * s)],
                        0.4, 0.2, n=12, col=B.INK2, taper_end=0.5))
    out.append(B.stroke([(cx, cy - 2 * s), (cx + 6 * s, cy - 9 * s), (cx + 16 * s, cy - 2 * s)],
                        0.4, 0.2, n=12, col=B.INK2, taper_end=0.5))
    out.append(B.hair([(cx - 2 * s, cy - 1 * s), (cx + 4 * s, cy + 3 * s)], 0.28, B.INK2))
    return out


def main():
    g = [B.svg_open(W, H), B.grid_check((W, H))]
    g.append('<rect x="10" y="16" width="740" height="508" fill="none" stroke="%s" stroke-width="1.0"/>' % B.GREY)
    g.append('<rect x="22" y="28" width="716" height="484" fill="none" stroke="%s" stroke-width="0.8"/>' % '#DCD5C8')
    # 页眉
    g.append(B.text(44, 58, '郑 风 · 之三', 8.6, RED, ls=2))
    g.append(B.text(380, 62, '叔于田　空巷', 24, B.INK, anchor='middle', ls=8, weight=500))
    g.append(B.text(704, 58, '诗三百五篇 · 之七七', 8.2, LG, anchor='end', ls=1.5))
    g.append('<line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.35"/>' % GOLD)

    base = 404
    # 地面
    g.append(B.hair([(54, base), (704, base)], 0.5, B.GREY))
    for k in range(14):
        x = 70 + k * 45
        g.append(B.hair([(x, base + 4), (x + 10, base + 4 + (k % 3) * 2)], 0.22, B.GREY))
    # 里涂：两道边线，由巷口向野收
    g.append(B.hair([(250, base - 12), (560, base - 8)], 0.3, B.GREY))
    g.append(B.hair([(250, base + 2), (560, base + 6)], 0.3, B.GREY))
    for x in range(270, 560, 38):
        g.append(B.hair([(x, base - 12), (x + 2, base + 2)], 0.22, B.GREY))

    # 左：两座里居，一条巷
    g += house(58, 150, base, 330, (104, 18))
    g += house(166, 248, base, 340, (204, 18))
    g += peek(104, base, 0.78)
    g += peek(204, base, 0.72)
    # 巷中酒器：有酒无人
    jx, jy = 282, base - 2
    jar = (f"M {jx-12},{jy-24} C {jx-18},{jy-16} {jx-16},{jy-4} {jx-10},{jy-2}"
           f" L {jx+10},{jy-2} C {jx+16},{jy-4} {jx+18},{jy-16} {jx+12},{jy-24}"
           f" L {jx+8},{jy-30} L {jx-8},{jy-30} Z")
    g.append(f'<path d="{jar}" fill="none" stroke="{B.INK2}" stroke-width="0.5"/>')
    g.append(B.oval(jx, jy-30, 9, 2.4, 0.34, B.INK2, n=24))
    for dx in (-24, 24):
        g.append(B.arcband(jx + dx, jy - 4, 5.5, 2.4, 0, 3.14, 0.32, B.GREY, n=12))
        g.append(B.hair([(jx + dx - 5, jy - 4), (jx + dx + 5, jy - 4)], 0.24, B.GREY))

    # 叔已出巷：一张弓、一壶箭，斜倚门柱
    bx, by = 336, base - 44
    g.append(B.arcband(bx, by, 16, 40, -1.25, 1.25, 0.62, B.INK, n=28))
    g.append(B.stroke([(bx + 16 * math.cos(-1.25), by + 40 * math.sin(-1.25)),
                       (bx + 16 * math.cos(1.25), by + 40 * math.sin(1.25))],
                      0.24, 0.14, n=10, col=B.GREY))
    # 箭壶
    qx, qy = 360, base - 2
    g.append(B.stroke([(qx - 7, qy), (qx - 5, qy - 26), (qx + 5, qy - 26), (qx + 7, qy)],
                      0.42, 0.24, n=12, col=B.INK2, taper_end=0.2))
    g.append(B.hair([(qx - 7, qy - 8), (qx + 7, qy - 8)], 0.26, B.GREY))
    for k in range(3):
        ax = qx - 5 + k * 5
        g.append(B.stroke([(ax, qy - 24), (ax + 1, qy - 42)], 0.24, 0.12, n=8, col=B.INK2, taper_end=0.5))
        g.append(B.stroke([(ax + 1, qy - 42), (ax - 2, qy - 46)], 0.2, 0.1, n=6, col=B.GREY))
    # 蹄迹：两列，由巷入野
    for k in range(7):
        x = 380 + k * 27
        y = base - 4 - k * 1.8
        g.append(B.oval(x, y - 3, 2.3, 4.0, 0.62, B.GREY, n=14, rot=-0.55))
        g.append(B.oval(x + 6, y + 3, 2.3, 4.0, 0.62, B.GREY, n=14, rot=-0.55))

    # 中：叔已出巷，只留弓矢与蹄迹

    # 右：郊野，树与飞禽
    g += tree(690, base, 96)
    g += bird(596, 330, 1.25)
    g += bird(632, 300, 0.9)
    g += bird(664, 324, 0.62)
    for x in range(560, 710, 12):
        g.append(B.hair([(x, base), (x + 2, base - 8 - (x % 3) * 2)], 0.22, B.GREY))

    # 门后之人望出巷口：虚线向野
    for x0, y0 in ((108, 354), (208, 356)):
        g.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="0.5" '
                 'stroke-dasharray="4 5" opacity="0.55"/>' % (x0, y0, 560, 330, B.GREY))

    # 题语
    g.append(B.text(380, 138, '巷 无 居 人', 18, RED, anchor='middle', ls=8, weight=500))
    g.append(B.text(380, 158, '非无居人，不如叔也；国人注心于叔，似如无人处', 9.0, LG, anchor='middle', ls=1))
    # 小标注
    g.append(B.text(150, 292, '巷', 11, B.INK, anchor='middle', ls=2))
    g.append(B.text(150, 306, '里涂', 7.2, LG, anchor='middle'))
    g.append(B.text(282, 438, '饮酒（燕饮）', 7.4, B.INK2, anchor='middle'))
    g.append(B.text(336, 438, '弓矢', 7.4, B.INK2, anchor='middle'))
    g.append(B.text(500, 438, '蹄迹', 7.4, B.INK2, anchor='middle'))

    g.append(B.text(600, 360, '禽', 7.4, B.INK2, anchor='middle'))
    g.append(B.text(660, 438, '野（郊外）', 7.4, B.INK2, anchor='middle'))

    # 注文带
    g.append('<line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.35"/>' % GOLD)
    g.append(B.text(44, 466, '巷：里涂，二十五家所居', 7.8, LG))
    g.append(B.text(380, 466, '田：取禽；狩：冬猎；野：郊外', 7.8, LG))
    # 引句
    g.append(B.text(380, 514, '叔于田，巷无居人。岂无居人？不如叔也，洵美且仁。', 16, B.INK, anchor='middle', ls=2))
    g.append(B.text(704, 526, '图一 · 名物 · sj077a', 7.4, LG, anchor='end'))
    g.append('</svg>')

    out = os.path.join(ROOT, 'assets', 'fig', 'sj077a-shu-yu-tian.svg')
    open(out, 'w', encoding='utf-8').write('\n'.join(g))
    import cairosvg
    cairosvg.svg2png(url=out, write_to=os.path.join(ROOT, 'dist', 'sj077a.png'),
                    output_width=1200, background_color=PAPER)
    print('wrote', out, len(''.join(g)))


if __name__ == '__main__':
    main()
