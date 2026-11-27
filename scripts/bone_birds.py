# -*- coding: utf-8 -*-
"""禽鸟取骨：底本墨形 → 中线 → 归一段列（供图版按格心缩放复用）

049 鹑、鹊两只鸟无底本不可成，故取骨而不复制像素：
 要的是「鹑伏地、尾短、颈细」「鹊长尾、翅上扬」的形，不是底本的每一笔。
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
from ink_skeleton import skeleton_paths  # noqa: E402

JOBS = {
    'quail': dict(png='assets/ref/ref-quail.png', crop=0.03, min_len=16, dilate=1),
    'magpie': dict(png='assets/ref/ref-magpie-inv.png', crop=0.06, min_len=22, dilate=2),
}


def normalize(segs):
    """像素 → 以 bbox 中心为原点、长边归一为 1 的坐标。"""
    xs = [p[0] for s in segs for p in s]
    ys = [p[1] for s in segs for p in s]
    x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
    w, h = x1 - x0, y1 - y0
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    sc = 1.0 / max(w, h)
    return [[[round((p[0] - cx) * sc, 5), round((p[1] - cy) * sc, 5)] for p in s]
            for s in segs], (round(w * sc, 4), round(h * sc, 4))


def main():
    out = os.path.join(ROOT, 'assets', 'fig', '_bone')
    os.makedirs(out, exist_ok=True)
    for name, j in JOBS.items():
        segs, size = skeleton_paths(os.path.join(ROOT, j['png']), crop=j['crop'],
                                    min_len=j['min_len'], dilate=j['dilate'])
        ns, wh = normalize(segs)
        path = os.path.join(out, name + '.json')
        with open(path, 'w', encoding='utf-8') as f:
            json.dump({'wh': wh, 'segs': ns}, f)
        print(name, 'segs', len(ns), 'wh', wh, '->', path)


if __name__ == '__main__':
    main()
