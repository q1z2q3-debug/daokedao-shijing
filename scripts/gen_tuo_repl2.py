# -*- coding: utf-8 -*-
"""印拓式复刻 v2 · 配色定版

色谱（「润泽说」图版专用，全书统一）：
  纸  #F5F1E8  宣纸米（不是灰，也不是纯白）
  焦墨 #1C1917 主体墨形（浓）
  重墨 #4A443C 次层（淡墨区，示墨色渐次）
  淡墨 #6B6259 小注
  朱砂 #A63D2F 题名、编号
  印泥 #B35142 小印
  泥金 #B79A63 只作细分隔线，0.35px，不出现在别处

技法：墨形分两级取（灰度 <70 为焦墨，70–150 为重墨），叠滤镜造毛边；
纸以极淡纤维纹承托（不透明度 0.10），不压纸色。
"""
import os
import cv2
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REF = os.path.join(ROOT, 'assets', 'ref', 'ref-zhou.png')
OUT = os.path.join(ROOT, 'assets', 'fig')
W, H = 760, 540

PAPER = '#F5F1E8'
INK_HEAVY = '#1C1917'
INK_MID = '#4A443C'
INK_LIGHT = '#6B6259'
CINNABAR = '#A63D2F'
SEAL = '#B35142'
GOLD = '#B79A63'


def contours(binary, eps=1.5, min_area=16):
    cnts, hier = cv2.findContours(binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    out = []
    for i, c in enumerate(cnts):
        if cv2.contourArea(c) < min_area:
            continue
        ap = cv2.approxPolyDP(c, eps, True)
        if len(ap) >= 3:
            out.append(ap.reshape(-1, 2))
    return out


def ink_layers(path, crop=0.075):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    h, w = img.shape
    cy, cx = int(h * crop), int(w * crop)
    img = img[cy:h - cy, cx:w - cx]
    heavy = (img < 70).astype(np.uint8) * 255
    mid = ((img >= 70) & (img < 152)).astype(np.uint8) * 255
    heavy = cv2.morphologyEx(heavy, cv2.MORPH_OPEN, np.ones((2, 2), np.uint8))
    mid = cv2.morphologyEx(mid, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    return contours(heavy, 1.4), contours(mid, 2.0), (w - 2 * cx, h - 2 * cy)


def seal(x, y, s=36, text=('润', '泽')):
    """朱文方印：赭底，纸色字，外细边。"""
    o = ['<g>',
         '<rect x="%d" y="%d" width="%d" height="%d" fill="%s" opacity="0.92"/>' % (x, y, s, s, SEAL),
         '<rect x="%d" y="%d" width="%d" height="%d" fill="none" stroke="%s" stroke-width="1.2" opacity="0.75"/>'
         % (x + 2.5, y + 2.5, s - 5, s - 5, PAPER)]
    for i, ch in enumerate(text):
        o.append('<text x="%d" y="%d" font-size="%d" fill="%s" text-anchor="middle" letter-spacing="0">%s</text>'
                 % (x + s / 2, y + s * 0.46 + i * s * 0.42, int(s * 0.36), PAPER, ch))
    o.append('</g>')
    return ''.join(o)


def build(mode='mo'):
    heavy, mid, (pw, ph) = ink_layers(REF)
    target_h = 376
    s = target_h / ph
    ox = 372 - pw * s / 2
    oy = 112

    paper = PAPER if mode == 'mo' else '#F6EFE4'
    main = INK_HEAVY if mode == 'mo' else '#7A2F26'
    second = INK_MID if mode == 'mo' else '#A0604F'

    def d_of(polys):
        segs = []
        for pts in polys:
            segs.append('M' + ' L'.join('%.1f,%.1f' % (ox + x * s, oy + y * s) for x, y in pts) + ' Z')
        return ' '.join(segs)

    g = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" '
         'font-family="Noto Serif SC,Songti SC,serif">' % (W, H, W, H)]
    g.append('''<defs>
  <filter id="edge" x="-10%" y="-10%" width="120%" height="120%">
    <feTurbulence type="fractalNoise" baseFrequency="0.062" numOctaves="3" seed="7" result="n"/>
    <feDisplacementMap in="SourceGraphic" in2="n" scale="3.1" xChannelSelector="R" yChannelSelector="G"/>
    <feGaussianBlur stdDeviation="0.18"/>
  </filter>
  <filter id="bleed" x="-8%" y="-8%" width="116%" height="116%">
    <feGaussianBlur stdDeviation="2.6"/>
  </filter>
  <filter id="mott" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="4" seed="5" result="t"/>
    <feColorMatrix in="t" type="matrix"
      values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0.9 0.6 0.3 0 -0.22"/>
  </filter>
  <mask id="speck">
    <rect width="760" height="540" fill="white"/>
    <rect width="760" height="540" filter="url(#mott)" fill="black"/>
  </mask>
  <pattern id="fibre" width="62" height="62" patternUnits="userSpaceOnUse">
    <rect width="62" height="62" fill="none"/>
    <path d="M6,14 L19,9" stroke="#E6DED1" stroke-width="0.26"/>
    <path d="M31,37 L47,31" stroke="#EBE4D8" stroke-width="0.24"/>
    <path d="M12,52 L22,56" stroke="#E9E2D5" stroke-width="0.22"/>
  </pattern>
  <radialGradient id="light" cx="50%" cy="44%" r="72%">
    <stop offset="0%" stop-color="#FFFBF1" stop-opacity="0.30"/>
    <stop offset="62%" stop-color="#FFFBF1" stop-opacity="0.05"/>
    <stop offset="100%" stop-color="#D9CFB8" stop-opacity="0.22"/>
  </radialGradient>
</defs>''')
    g.append('<rect width="%d" height="%d" fill="%s"/>' % (W, H, paper))
    g.append('<rect width="%d" height="%d" fill="url(#fibre)" opacity="0.34"/>' % (W, H))
    g.append('<rect width="%d" height="%d" fill="url(#light)"/>' % (W, H))

    # 墨：先淡后浓，淡在外、浓在内，得墨分两层
    g.append('<g filter="url(#edge)" fill="%s" fill-rule="evenodd" opacity="0.55">' % second)
    g.append('<path d="%s"/></g>' % d_of(mid))
    g.append('<g filter="url(#bleed)" fill="%s" fill-rule="evenodd" opacity="0.16">' % second)
    g.append('<path d="%s"/></g>' % d_of(heavy))
    g.append('<g mask="url(#speck)" filter="url(#edge)" fill="%s" fill-rule="evenodd" opacity="0.94">' % main)
    g.append('<path d="%s"/></g>' % d_of(heavy))

    # 题名与印
    tcol = CINNABAR if mode == 'mo' else '#8E3A2B'
    g.append('<text x="56" y="104" font-size="34" letter-spacing="12" fill="%s" font-weight="700">舟</text>' % tcol)
    g.append('<text x="58" y="132" font-size="8.6" letter-spacing="3.4" fill="%s">诗 经 · 柏 舟 名 物</text>' % INK_LIGHT)
    g.append(seal(56, 146, 36, ('润', '泽')))
    # 右上款
    g.append('<text x="716" y="88" text-anchor="end" font-size="8" letter-spacing="2" fill="%s">%s</text>'
             % (INK_LIGHT, '墨 拓' if mode == 'mo' else '朱 拓'))
    g.append('<text x="716" y="106" text-anchor="end" font-size="7.6" letter-spacing="1.2" fill="%s">'
             '依 名 物 图 《 舟 》 取 墨 形</text>' % INK_LIGHT)

    # 泥金细分隔线
    g.append('<line x1="56" y1="474" x2="704" y2="474" stroke="%s" stroke-width="0.35" opacity="0.55"/>' % GOLD)
    g.append('<text x="56" y="494" font-size="8.2" letter-spacing="1.2" fill="%s">'
             '墨形两级取，浓淡由灰度分；毛边、纸纹皆滤镜所生，不曾手描一笔</text>' % INK_LIGHT)
    g.append('<text x="380" y="518" text-anchor="middle" font-size="15" letter-spacing="4.5" fill="%s">'
             '泛彼柏舟，在彼中河</text>' % (INK_HEAVY if mode == 'mo' else '#7A2F26'))
    g.append('</svg>')

    svg = ''.join(g)
    p = os.path.join(OUT, 'zhou-tuo%d-%s.svg' % (2, mode))
    open(p, 'w', encoding='utf-8').write(svg)
    print(mode, len(svg.encode('utf-8')), 'B  heavy', len(heavy), 'mid', len(mid))
    import cairosvg
    png = os.path.join(ROOT, 'dist', 'zhou-tuo2-%s.png' % mode)
    cairosvg.svg2png(url=p, write_to=png, output_width=1200, background_color=paper)
    print('png', png)


if __name__ == '__main__':
    build('mo')
    build('zhu')
