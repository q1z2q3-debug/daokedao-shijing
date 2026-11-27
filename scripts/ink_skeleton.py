# -*- coding: utf-8 -*-
"""墨形取中线：由底本的墨块抽出「骨」，再以笔压线描出

用意：墨拓（面）与全书的线（骨）不同重量，同页并置便突兀。
取墨形的中线，就既保住底本的形准，又落回同一套线语汇——
得意忘形：要的是「这一叶舟腰身收束、双舷有厚、四梁跨舷」的意，
不是每一像素的黑。
"""
import math

import cv2
import numpy as np
from skimage.morphology import skeletonize


def skeleton_paths(png, crop=0.075, min_len=14, dilate=1):
    img = cv2.imread(png, cv2.IMREAD_GRAYSCALE)
    h, w = img.shape
    cy, cx = int(h * crop), int(w * crop)
    img = img[cy:h - cy, cx:w - cx]
    m = (img < 70).astype(np.uint8)
    if dilate:
        m = cv2.dilate(m, np.ones((dilate * 2 + 1,) * 2, np.uint8))
    sk = skeletonize(m > 0).astype(np.uint8)
    # 8 邻域计数：1 为端点，>2 为分叉，2 为通途
    ker = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]], np.uint8)
    nb = cv2.filter2D(sk, -1, ker, borderType=cv2.BORDER_CONSTANT)
    nb = nb * sk

    pts = np.argwhere(sk > 0)  # (y,x)
    node = {}
    for y, x in pts:
        node[(y, x)] = nb[y, x]

    def walk(y, x, prev):
        """自节点出发沿骨架走，至端或分叉止。"""
        path = [(x, y)]
        cur = (y, x)
        prv = prev
        while True:
            nxt = None
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    if dy == 0 and dx == 0:
                        continue
                    ny, nx = cur[0] + dy, cur[1] + dx
                    if (ny, nx) in node and (ny, nx) != prv and ((ny, nx) not in path_yx):
                        nxt = (ny, nx)
                        break
                if nxt:
                    break
            if nxt is None:
                break
            path.append((nxt[1], nxt[0]))
            path_yx.add(nxt)
            prv, cur = cur, nxt
            if node.get(nxt, 2) != 2:
                break
        return path

    segs = []
    path_yx = set()
    starts = [k for k, v in node.items() if v != 2]
    for s in starts:
        if s in path_yx:
            continue
        path_yx.add(s)
        p = walk(s[0], s[1], None)
        if len(p) >= min_len:
            segs.append(p)
    # 余下的环（无端点闭合）
    for k, v in node.items():
        if k not in path_yx and v == 2:
            path_yx.add(k)
            p = walk(k[0], k[1], None)
            if len(p) >= min_len:
                segs.append(p)

    def rdp(p, eps=1.6):
        if len(p) < 3:
            return p
        a, b = np.array(p[0], float), np.array(p[-1], float)
        ab = b - a
        L = np.linalg.norm(ab)
        if L < 1e-6:
            d = [np.linalg.norm(np.array(q, float) - a) for q in p]
        else:
            d = [abs(ab[0] * (q[1] - a[1]) - ab[1] * (q[0] - a[0])) / L for q in p]
        i = int(np.argmax(d))
        if d[i] > eps:
            return rdp(p[:i + 1], eps)[:-1] + rdp(p[i:], eps)
        return [p[0], p[-1]]

    return [rdp(p) for p in segs], (w - 2 * cx, h - 2 * cy)
