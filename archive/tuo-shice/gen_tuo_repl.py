# -*- coding: utf-8 -*-
"""印拓式复刻：底本墨形 → 矢量化墨块 → 毛边滤镜 → 拓本样式

语汇与白描不同，须先说清：
- 白描：线是骨，一笔一笔写出来；不填而描。
- 拓本：墨是面，从原刻剥下来；不描而取形。

故本脚本不画任何一笔，只做四件事：
1 二值化取墨形；2 轮廓简化成多边形；3 交 SVG 的实心 path；
4 以 feTurbulence + feDisplacementMap 造毛边、以低透明噪声造纸纹。

两版：墨拓（墨色 #1F1B17）与朱拓（赭 #994433）。
"""
import os
import sys
import numpy as np
import cv2

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REF = os.path.join(ROOT, 'assets', 'ref', 'ref-zhou.png')
OUT = os.path.join(ROOT, 'assets', 'fig')
W, H = 760, 540


def ink_polygons(path, crop=0.075, eps=1.6, min_area=18):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    h, w = img.shape
    cy, cx = int(h * crop), int(w * crop)
    img = img[cy:h - cy, cx:w - cx]
    # Otsu 二值：墨为前景
    inv = 255 - img
    _, bw = cv2.threshold(inv, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    bw = cv2.morphologyEx(bw, cv2.MORPH_OPEN, np.ones((2, 2), np.uint8))
    cnts, hier = cv2.findContours(bw, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    polys = []
    for i, c in enumerate(cnts):
        if cv2.contourArea(c) < min_area:
            continue
        ap = cv2.approxPolyDP(c, eps, True)
        if len(ap) < 3:
            continue
        polys.append((i, ap.reshape(-1, 2), hier[0][i][3]))
    return polys, (w - 2 * cx, h - 2 * cy)


def build(mode='mo'):
    polys, (pw, ph) = ink_polygons(REF)
    target_h = 372
    s = target_h / ph
    ox = 380 - pw * s / 2
    oy = 118

    color = '#1F1B17' if mode == 'mo' else '#994433'
    paper = '#F7F4EE' if mode == 'mo' else '#F6EFE6'

    g = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" '
         'font-family="Noto Serif SC,Songti SC,serif">' % (W, H, W, H)]
    g.append('''<defs>
  <filter id="ink" x="-12%%" y="-12%%" width="124%%" height="124%%">
    <feTurbulence type="fractalNoise" baseFrequency="0.055" numOctaves="3" seed="7" result="n"/>
    <feDisplacementMap in="SourceGraphic" in2="n" scale="2.4" xChannelSelector="R" yChannelSelector="G"/>
    <feGaussianBlur stdDeviation="0.22"/>
  </filter>
  <filter id="paper" x="0" y="0" width="100%%" height="100%%">
    <feTurbulence type="fractalNoise" baseFrequency="0.72" numOctaves="4" seed="11" result="p"/>
    <feColorMatrix in="p" type="matrix"
      values="0 0 0 0 0.62  0 0 0 0 0.56  0 0 0 0 0.46  0.55 0.45 0.4 0 -0.28"/>
  </filter>
  <filter id="grain" x="0" y="0" width="100%%" height="100%%">
    <feTurbulence type="turbulence" baseFrequency="0.03" numOctaves="2" seed="3" result="t"/>
    <feColorMatrix in="t" type="matrix"
      values="0 0 0 0 0.80  0 0 0 0 0.77  0 0 0 0 0.71  0.06 0.05 0.04 0 0.01"/>
  </filter>
</defs>''')
    g.append('<rect width="%d" height="%d" fill="%s"/>' % (W, H, paper))
    g.append('<rect width="%d" height="%d" filter="url(#paper)" opacity="0.42"/>' % (W, H))
    g.append('<rect width="%d" height="%d" filter="url(#grain)" opacity="0.30"/>' % (W, H))

    paths = []
    for _i, pts, parent in polys:
        d = 'M' + ' L'.join('%.1f,%.1f' % (ox + x * s, oy + y * s) for x, y in pts)
        paths.append(d + ' Z')
    g.append('<g filter="url(#ink)" fill="%s" fill-rule="evenodd" stroke="none" opacity="0.94">' % color)
    g.append('<path d="%s"/>' % ' '.join(paths))
    g.append('</g>')

    # 款识：拓本惯例，题名在上，出处与年月在下
    tcol = '#3A342C' if mode == 'mo' else '#7A3527'
    g.append('<text x="58" y="96" font-size="30" letter-spacing="10" fill="%s" font-weight="700">舟</text>' % tcol)
    g.append('<text x="58" y="122" font-size="8.4" letter-spacing="3" fill="%s">诗 经 · 柏 舟 名 物</text>' % tcol)
    g.append('<text x="716" y="86" text-anchor="end" font-size="8" letter-spacing="1.5" fill="%s">%s</text>'
             % (tcol, '墨 拓' if mode == 'mo' else '朱 拓'))
    g.append('<text x="716" y="104" text-anchor="end" font-size="7.6" letter-spacing="1" fill="%s">'
             '依 名物图《舟》取 墨 形 · 非 摹 线</text>' % tcol)
    g.append('<line x1="44" y1="470" x2="716" y2="470" stroke="%s" stroke-width="0.7" opacity="0.45"/>' % tcol)
    g.append('<text x="44" y="492" font-size="8.2" letter-spacing="1" fill="%s">'
             '墨形取底本，轮廓以多边形简化；毛边、纸纹皆由滤镜生，非手绘</text>' % tcol)
    g.append('<text x="380" y="518" text-anchor="middle" font-size="15" letter-spacing="3" fill="%s">'
             '泛彼柏舟，在彼中河</text>' % tcol)
    g.append('</svg>')

    svg = ''.join(g)
    p = os.path.join(OUT, 'zhou-tuo-%s.svg' % mode)
    open(p, 'w', encoding='utf-8').write(svg)
    print(mode, 'svg', len(svg.encode('utf-8')), 'B', 'paths', len(paths))
    import cairosvg
    png = os.path.join(ROOT, 'dist', 'zhou-tuo-%s.png' % mode)
    cairosvg.svg2png(url=p, write_to=png, output_width=1100, background_color=paper)
    print('png', png)


if __name__ == '__main__':
    build('mo')
    build('zhu')
