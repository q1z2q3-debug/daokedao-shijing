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

def ink_rows(svg):
    """每条填充路径：面积、长边、平均宽、颜色、中心 x。"""
    rows = []
    for m in re.finditer(r'<path[^>]*d="([^"]+)"[^>]*fill="(#[0-9A-Fa-f]{6})"', svg):
        d, col = m.group(1), m.group(2)
        xs, ys = nums(d)
        if len(xs) < 3:
            continue
        a = shoelace(xs, ys)
        P = sum(((xs[i + 1] - xs[i]) ** 2 + (ys[i + 1] - ys[i]) ** 2) ** 0.5
                for i in range(len(xs) - 1))
        if P < 12:
            continue
        rows.append(dict(a=a, L=P, w=2 * a / P, col=col,
                         cx=(min(xs) + max(xs)) / 2, cy=(min(ys) + max(ys)) / 2))
    return rows


def adapt_checks(rows):
    """三项适配的可测部分：线宽比分格、墨阶数、软物闭口。"""
    issues, notes = [], []
    zones = [[], [], []]
    for r in rows:
        x = r['cx']
        z = 0 if x < 313 else (1 if x < 500 else 2)
        if r['a'] > 20:            # 过小的碎笔不计
            zones[z].append(r['w'])
    # 取各格 90 分位宽：读者定调靠最粗的那几笔，不被极细发缕、水纹拉偏
    avg = [sorted(z)[int(0.9 * (len(z) - 1))] if z else None for z in zones]
    named = ['舟/一', '人/二', '水/三']
    txt = '线宽 ' + ' · '.join('%s %.2f' % (n, v) for n, v in zip(named, avg) if v)
    vals = [v for v in avg if v]
    if len(vals) >= 2:
        ratio = max(vals) / min(vals)
        txt += '  比 %.2f' % ratio
        if ratio > 2.0:
            # 口径提示：闭合环带的 2A/P 约为开放带的一半，故比值偏大不可靠，只作提示
            notes.append('适配提示  三格线宽比 %.2f 偏大（含闭合环带口径差，宜人眼复核）' % ratio)
    notes.append(txt)

    # 墨阶：按亮度分桶，墨阶数应在 3–6
    def L(c):
        c = c.lstrip('#')
        return (int(c[0:2], 16) * 0.6 + int(c[2:4], 16) * 0.3 + int(c[4:6], 16) * 0.1)
    buckets = set()
    for r in rows:
        if r['col'] == '#B35142':      # 印泥不计墨阶
            continue
        buckets.add(int(L(r['col']) // 12))
    if len(buckets) > 6:
        issues.append('适配  墨阶 %d 档，超 6（颜色未按层分配）' % len(buckets))
    notes.append('墨阶 %d 档' % len(buckets))

    # 软物闭口：水区（x>500, y>240）不应有闭合大形
    closed_big = [r for r in rows if r['cx'] > 500 and r['cy'] > 240 and r['a'] > 900]
    if closed_big:
        issues.append('适配  水域出现闭合形 %d 个（软物不许有硬边）' % len(closed_big))
    return issues, notes


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
    rows = ink_rows(svg)
    if rows:
        a_iss, a_not = adapt_checks(rows)
        issues += a_iss
        notes += a_not
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
