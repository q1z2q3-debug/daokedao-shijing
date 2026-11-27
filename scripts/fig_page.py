# -*- coding: utf-8 -*-
"""fig_page · 名物图通用版式（760×540 三格）

一切坐标照 book/图式.md 16.2 表，不许逐篇改。篇目只做三件事：
  1 写三句「这一格要说的话」
  2 提供三个 draw(cx, cy) 函数
  3 填 meta
"""
import os
import math

import svgbrush as B

W, H = 760, 540
PAPER, CIN, GOLD, LIGHT = '#F5F1E8', '#A63D2F', '#B79A63', '#6B6259'

CX = (148, 378, 622)
NUM = ('一', '二', '三')


DEFS = '''<defs>
  <radialGradient id="lg" cx="50%" cy="44%" r="72%">
    <stop offset="0%" stop-color="#FFFBF1" stop-opacity="0.30"/>
    <stop offset="62%" stop-color="#FFFBF1" stop-opacity="0.05"/>
    <stop offset="100%" stop-color="#D9CFB8" stop-opacity="0.22"/>
  </radialGradient>
  <pattern id="fibre" width="62" height="62" patternUnits="userSpaceOnUse">
    <path d="M6,14 L19,9" stroke="#E6DED1" stroke-width="0.26"/>
    <path d="M31,37 L47,31" stroke="#EBE4D8" stroke-width="0.24"/>
    <path d="M12,52 L22,56" stroke="#E9E2D5" stroke-width="0.22"/>
  </pattern>
</defs>'''


def build(meta, draws, notes, out_svg, out_png=None, width=1200):
    """meta: volume,title,index,key,quote,footer
    draws: [(name, fn(cx, cy)), ...] 三格；fn 返回 SVG 片段列表
    notes: 三行注文
    """
    g = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" '
         'font-family="Noto Serif SC,Songti SC,serif">' % (W, H, W, H), DEFS,
         '<rect width="%d" height="%d" fill="%s"/>' % (W, H, PAPER),
         '<rect width="%d" height="%d" fill="url(#fibre)" opacity="0.34"/>' % (W, H),
         '<rect width="%d" height="%d" fill="url(#lg)"/>' % (W, H)]

    for (name, fn), x in zip(draws, CX):
        g += fn(x, 258)

    g.append(B.text(56, 58, meta['volume'], 8.6, CIN, ls=2))
    g.append(B.text(380, 62, meta['title'], 26, B.INK, anchor='middle', ls=10, weight=500))
    g.append(B.text(704, 58, meta['index'], 8.2, LIGHT, anchor='end', ls=1.5))
    for yy in (96, 478):
        g.append('<line x1="44" y1="%d" x2="716" y2="%d" stroke="%s" stroke-width="0.35" opacity="0.6"/>'
                 % (yy, yy, GOLD))
    for x, num, (name, _) in zip(CX, NUM, draws):
        g.append(B.text(x - 26, 130, num, 8.6, CIN, ls=1))
        g.append(B.text(x - 8, 130, name, 9.2, B.INK2, ls=3))
    for x, n in zip((44, 264, 486), notes):
        g.append(B.text(x, 466, n, 7.8, LIGHT, ls=1))
    g.append(B.text(380, 514, meta['quote'], 16, B.INK, anchor='middle', ls=3))
    g.append(B.text(704, 526, meta['footer'], 7.4, LIGHT, anchor='end'))
    g.append('</svg>')

    svg = ''.join(g)
    open(out_svg, 'w', encoding='utf-8').write(svg)
    if out_png:
        import cairosvg
        cairosvg.svg2png(url=out_svg, write_to=out_png, output_width=width, background_color=PAPER)
    return B.count_bytes(svg)


def wave(cx, cy, hw, amp=4, n=23, phase=0.0, w=0.42, col=None, depth=None):
    import adapt
    pts = [(cx - hw + 2 * hw * k / n,
            cy + amp * math.sin(k / n * math.pi * 2.2 + phase)) for k in range(n + 1)]
    if col is None:
        col = adapt.tone(depth if depth is not None else 0.6)
    return B.stroke(pts, w, w * 0.5, n=(n + 1) * 2, col=col, taper_start=0.3, taper_end=0.5)
