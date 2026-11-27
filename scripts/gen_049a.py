# -*- coding: utf-8 -*-
"""049 鹑之奔奔 · 图一

三句：
 一 鹑   —— 头细尾短（骨自底本，取形不取像素）
 二 鹊   —— 长尾舒举
 三 常匹 —— 一鹑一鹊，同向而随（诗眼：鸟尚常匹，人非匹耦）

画法：取骨线。禽鸟无底本不得成，极坐标与 chaikin 两路皆已试败——
      鸟形不在一条闭合曲线上，而在「头颈背翅尾」诸段的相对关系上。
      取骨即取此关系，形准由底本承担，线语汇由本页统一。
铁律：不画五官。
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import svgbrush as B  # noqa: E402
import adapt  # noqa: E402
import fig_page as P  # noqa: E402

W = 0.47  # 一页一档笔：三格同宽，不按物体大小各自为政

BONE = {}
for _n in ('quail', 'magpie'):
    with open(os.path.join(ROOT, 'assets', 'fig', '_bone', _n + '.json'), encoding='utf-8') as _f:
        BONE[_n] = json.load(_f)


def bone(name, cx, cy, s, depth):
    segs = BONE[name]['segs']
    out = []
    for sg in segs:
        if len(sg) < 2:
            continue
        pts = [(cx + p[0] * s, cy + p[1] * s) for p in sg]
        # 长段是骨（体廓、长尾），短段是羽纹——同色同宽必糊，须分两档
        if len(sg) >= 4:
            w, d, te = W, depth, 0.3
        else:
            w, d, te = W * 0.62, depth + 0.22, 0.45
        out.append(B.stroke(pts, w, w * 0.55, n=max(5, min(len(pts), 26)),
                            col=adapt.tone(d), taper_end=te))
    return out


def quail(cx, cy):
    return bone('quail', cx, cy - 6, 132, 0.08)


def magpie(cx, cy):
    return bone('magpie', cx - 6, cy - 4, 158, 0.12)


def pair(cx, cy):
    """常匹：鹊在上、鹑在下，同向朝右，一飞一走。"""
    out = []
    out += bone('magpie', cx + 6, cy - 44, 96, 0.16)
    out += bone('quail', cx - 18, cy + 58, 84, 0.24)
    for i, yy in enumerate((cy + 104, cy + 116)):
        out.append(P.wave(cx, yy, 56 + i * 8, amp=3, n=22, phase=i * 0.9,
                          w=0.26, depth=0.56))
    return out


def main():
    meta = dict(volume='鄘 风 · 四', title='鹑 之 奔 奔', index='诗三百五篇 · 之四九',
                quote='鹑之奔奔，鹊之彊彊', footer='图一 · 名物 · sj049a')
    draws = [('鹑', quail), ('鹊', magpie), ('常匹', pair)]
    notes = ['头细尾短，伏而奔走', '长尾舒举，翩翩而飞', '鸟有常匹，人非匹耦']
    svg = os.path.join(ROOT, 'assets', 'fig', 'sj049a-chun-zhi-ben-ben.svg')
    png = os.path.join(ROOT, 'dist', 'sj049a.png')
    print('svg', P.build(meta, draws, notes, svg, png), 'B')


if __name__ == '__main__':
    main()
