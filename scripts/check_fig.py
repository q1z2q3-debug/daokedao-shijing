# -*- coding: utf-8 -*-
"""check_fig · 白描图自动质检

用法：
    python3 check_fig.py a.svg b.svg ...

检查项（任一不过即 exit 1）：
1 出界   —— 任一笔的 bbox 越出画布 2px，判「线条出界」（硬错）
2 面代线 —— 单一填充形面积 > 画布 12%，判「黑块」，即用面代线（硬错）
3 断笔   —— 同一 path 内相邻点跨距 > 画布宽 0.55，判「跨格线」（硬错）
4 无字   —— 名物图应有标题与图题，全图 0 个 text 判「无字」（提示）
5 层级   —— 统计 line/fill 数，给出「线∶面」比，供人工复核
"""
import re, sys, os

def paths(svg):
    return re.findall(r'<path[^>]*d="([^"]+)"[^>]*>', svg)

def nums(d):
    raw = re.findall(r'-?\d+\.?\d*', d)
    v = [float(x) for x in raw]
    return v[0::2], v[1::2]

def shoelace(xs, ys):
    if len(xs) < 3:
        return 0.0
    s = 0.0
    n = len(xs)
    for i in range(n):
        j = (i + 1) % n
        s += xs[i] * ys[j] - xs[j] * ys[i]
    return abs(s) / 2.0

def check(path):
    svg = open(path, encoding='utf-8').read()
    m = re.search(r'viewBox="0 0 (\d+(?:\.\d+)?) (\d+(?:\.\d+)?)"', svg)
    W, H = (float(m.group(1)), float(m.group(2))) if m else (760.0, 540.0)
    fills = len(re.findall(r'fill="(?!none)([^"]+)"', svg))
    txt = len(re.findall(r'<text', svg))
    issues, notes = [], []
    area_canvas = W * H
    for d in paths(svg):
        xs, ys = nums(d)
        if not xs:
            continue
        if min(xs) < -2 or min(ys) < -2 or max(xs) > W + 2 or max(ys) > H + 2:
            issues.append('出界  bbox=(%.0f,%.0f)-(%.0f,%.0f)' % (min(xs), min(ys), max(xs), max(ys)))
        jumps = [(xs[i + 1] - xs[i], ys[i + 1] - ys[i]) for i in range(len(xs) - 1)]
        big = [abs(j[0]) for j in jumps]
        if big and max(big) > W * 0.55:
            issues.append('跨格  x 跨距 %.0fpx' % max(big))
        a = shoelace(xs, ys)
        if a > area_canvas * 0.12:
            issues.append('面代线  填充面积占画布 %.0f%%' % (a / area_canvas * 100))
    if txt == 0:
        notes.append('无字：图题与编号缺失')
    ratio = '路径 %d 条 · 填充块 %d 个' % (len(paths(svg)), fills)
    if len(paths(svg)) < 12:
        notes.append('路径过少：要么图未画完，要么用色块代形')
    return issues, notes, ratio

def main():
    bad = 0
    for p in sys.argv[1:]:
        if not os.path.exists(p):
            print('MISSING', p)
            bad += 1
            continue
        issues, notes, ratio = check(p)
        uniq = sorted(set(issues))
        status = 'PASS' if not uniq else 'FAIL'
        print('%s  %s  %s' % (status, os.path.basename(p), ratio))
        for u in uniq[:6]:
            print('    - ' + u)
        if uniq:
            bad += 1
        for n in notes:
            print('    · ' + n)
    sys.exit(1 if bad else 0)

if __name__ == '__main__':
    main()
