# -*- coding: utf-8 -*-
"""复刻示范：依名物图底本《舟》重画为笔压白描

底本：assets/ref/ref-zhou.png（斜俯视小舟线描）
形制要点（不照像素，照结构）：
1 斜俯视：看到船内，故须画内舷；
2 双舷有厚度：外舷与内舷各一线，间距自上而下渐收；
3 四道横梁：跨于两内舷之间，中段略下垂；
4 船底：底端收窄，三道横向底板线；
5 舷外阴影：左舷外侧短排线，示背光；
6 上端口沿：两端微微外翻。
"""
import os
import sys
import math
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import svgbrush as B  # noqa: E402

W, H = 760, 540


def zhou(cx, cy, s=1.0):
    """锚点 (cx, cy) 为船尾口沿中点；s=1 时船长约 340、宽约 130。"""
    out = []

    def P(pts):
        return [(cx + x * s, cy + y * s) for x, y in pts]

    # ---- 外舷：左、右各一条长弧（自船尾沿舷壁到底端）
    L_out = P([(-56, 4), (-64, 60), (-66, 140), (-58, 226), (-38, 292), (-12, 330), (0, 338)])
    R_out = P([(56, 4), (66, 60), (68, 140), (60, 226), (40, 290), (14, 328), (0, 338)])
    out.append(B.stroke(L_out, 1.55, 0.72, n=60, taper_end=0.18))
    out.append(B.stroke(R_out, 1.55, 0.72, n=60, taper_end=0.18))

    # ---- 内舷：与外舷平行，间距 9→4（厚度渐变）
    L_in = P([(-47, 16), (-54, 70), (-56, 140), (-48, 220), (-30, 276), (-9, 312)])
    R_in = P([(47, 16), (56, 70), (58, 140), (50, 220), (32, 274), (10, 310)])
    out.append(B.stroke(L_in, 0.62, n=54, col=B.INK2))
    out.append(B.stroke(R_in, 0.62, n=54, col=B.INK2))

    # ---- 上端口沿：船尾两端微外翻
    out.append(B.stroke(P([(-56, 4), (-50, -2), (-38, -4)]), 0.8, 0.3, n=16))
    out.append(B.stroke(P([(56, 4), (50, -2), (38, -4)]), 0.8, 0.3, n=16))
    out.append(B.stroke(P([(-38, -4), (0, -8), (38, -4)]), 0.7, 0.4, n=24, col=B.INK2))

    # ---- 四道横梁：跨两内舷，中段下垂
    for yy, sag in ((34, 7), (96, 8), (248, 7), (292, 6)):
        lx = np.interp(yy, [p[1] - cy for p in L_in], [p[0] - cx for p in L_in])
        rx = np.interp(yy, [p[1] - cy for p in R_in], [p[0] - cx for p in R_in])
        mid = ((lx + rx) / 2, yy + sag)
        out.append(B.stroke(P([(lx + 3, yy), mid, (rx - 3, yy)]), 0.72, 0.46, n=26))

    # ---- 船底：三道横向板线，收在底端
    for i, (yy, hw) in enumerate(((316, 34), (326, 26), (334, 16))):
        out.append(B.stroke(P([(-hw, yy), (0, yy + 5), (hw, yy)]), 0.44 - i * 0.06, n=22, col=B.INK2))

    # ---- 左舷外侧阴影排线（背光）
    for i in range(9):
        t = 0.10 + i * 0.095
        yy = 20 + t * 290
        lx = np.interp(yy, [p[1] - cy for p in L_out], [p[0] - cx for p in L_out])
        out.append(B.hair(P([(lx + 4, yy), (lx + 9, yy + 13)]), 0.22, B.GREY))
    return out


def main():
    PAPER, CIN, GOLD = '#F5F1E8', '#A63D2F', '#B79A63'
    g = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 540" width="760" height="540" '
         'font-family="Noto Serif SC,Songti SC,serif">',
         '<defs><radialGradient id="lg" cx="50%" cy="44%" r="72%">'
         '<stop offset="0%" stop-color="#FFFBF1" stop-opacity="0.30"/>'
         '<stop offset="62%" stop-color="#FFFBF1" stop-opacity="0.05"/>'
         '<stop offset="100%" stop-color="#D9CFB8" stop-opacity="0.22"/>'
         '</radialGradient></defs>',
         '<rect width="760" height="540" fill="%s"/>' % PAPER,
         '<rect width="760" height="540" fill="url(#lg)"/>']
    g += zhou(380, 120, 1.06)
    # 页眉与注记：单件示范，不套三格版式
    g.append(B.text(56, 104, '舟', 34, CIN, ls=12, weight=700))
    g.append(B.text(58, 132, '诗 经 · 柏 舟 名 物', 8.6, '#6B6259', ls=3.4))
    g.append('<g><rect x="56" y="146" width="36" height="36" fill="#B35142" opacity="0.92"/>'
             '<rect x="58.5" y="148.5" width="31" height="31" fill="none" stroke="%s" stroke-width="1.2" opacity="0.75"/>'
             '<text x="74" y="166" font-size="13" fill="%s" text-anchor="middle">润</text>'
             '<text x="74" y="181" font-size="13" fill="%s" text-anchor="middle">泽</text></g>'
             % (PAPER, PAPER, PAPER))
    g.append(B.text(44, 58, '复 刻 示 范', 8.6, CIN, ls=2))
    g.append(B.text(716, 58, '白 描 · 照 结 构 重 画', 8.2, '#6B6259', anchor='end', ls=1.5))
    g.append('<line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.35" opacity="0.55"/>' % GOLD)
    g.append(B.text(56, 472, '斜俯视，见船内；双舷有厚、四梁跨舷、底端收窄', 8.4, B.INK2, ls=1))
    g.append(B.text(704, 472, '照结构不照像素', 8.4, B.GREY, anchor='end', ls=1))

    g.append(B.text(380, 518, '汎彼柏舟，在彼中河', 15, B.INK, anchor='middle', ls=4.5))
    g.append('</svg>')
    p = os.path.join(ROOT, 'assets', 'fig', 'zhou-repl.svg')
    open(p, 'w', encoding='utf-8').write(''.join(g))
    print('svg', p, B.count_bytes(''.join(g)), 'B')
    import cairosvg
    png = os.path.join(ROOT, 'dist', 'zhou-repl.png')
    cairosvg.svg2png(url=p, write_to=png, output_width=1200, background_color='#F5F1E8')
    print('png', png)


if __name__ == '__main__':
    main()
