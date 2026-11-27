# -*- coding: utf-8 -*-
"""批量生成图一（名物图）· 045–054

版式取 book/图式.md 定版坐标；三格内容由 SPEC 指定，绘图走 mingwu 画具库，
引句一律从 sjNNN.md 的「二、经文」段首句抽取——不经手改，故一字不改。
"""
import os
import re
import sys
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import svgbrush as B  # noqa: E402
import mingwu as M   # noqa: E402

W, H = 760, 540
OUTDIR = os.path.join(ROOT, 'assets', 'fig')
BMDIR = os.path.join(ROOT, 'book')


def quote_of(num):
    """从 book/SJNNN-*.md 取经文首句，繁转简；一字不改，只改字形。"""
    files = [f for f in os.listdir(BMDIR) if f.startswith('SJ%03d-' % num)]
    if not files:
        return ''
    txt = open(os.path.join(BMDIR, files[0]), encoding='utf-8').read()
    m = re.search(r'##\s*二[　\s]*经文\s*\n+(?:第[一二三四五六七八九十]+章\s*\n+\s*>(.+?)\n)', txt)
    if not m:
        return ''
    line = m.group(1).strip()
    q = re.split(r'[。！？]', line)[0].strip()
    if len(q) > 26:
        q = '，'.join(re.split(r'[，；]', q)[:2])
    try:
        from opencc import OpenCC
        q = OpenCC('t2s').convert(q)
    except Exception:
        pass
    return q.replace('\U0002b7bd', '蝀').replace('𬟽', '蝀')


def layout(key, vol, title, num, cells, quote, cap):
    """图一版式：页眉／界／三格／注文带／引句／图题。"""
    g = [B.svg_open(W, H), B.grid_check((W, H))]
    g.append(B.text(44, 58, vol, 8.6, B.RED, ls=2))
    g.append(B.text(380, 60, title, 26, B.INK, anchor='middle', ls=10, weight=500))
    g.append(B.text(716, 58, '诗三百五篇 · 之%s' % num, 8.2, B.GREY, anchor='end', ls=1.5))
    g.append('<line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.7"/>' % B.GREY)
    cx_list = (148, 378, 622)
    for i, (tag, name, note, draw) in enumerate(cells):
        cx = cx_list[i]
        g.append(B.text(cx - 30, 132, tag, 7.6, B.RED, ls=1))
        g.extend(draw())
    g.append('<line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.7"/>' % B.GREY)
    xs = (44, 264, 486)
    for i, (tag, name, note, _d) in enumerate(cells):
        g.append(B.text(xs[i], 466, '%s %s　%s' % (tag, name, note), 7.8, B.INK2, ls=1))
    g.append(B.text(380, 512, quote, 16, B.INK, anchor='middle', ls=3))
    g.append(B.text(716, 524, cap, 7.4, B.GREY, anchor='end', ls=1))
    g.append('</svg>')
    svg = ''.join(g)
    path = os.path.join(OUTDIR, key + '.svg')
    open(path, 'w', encoding='utf-8').write(svg)
    return path, B.count_bytes(svg)


# ---------------------------------------------------------------- 九篇规格
SPEC = [
    # (key, 卷, 标题, 篇序, 三格, 图题后缀)
    ('sj045a-bai-zhou-liang-mao', '鄘风 · 四', '柏 舟', '四十五',
     [('壹', '柏舟', '柏木为舟，汎于中河', lambda: M.boat(148, 302, L=114, s=1.35) + M.water(148, 372, w=96, rows=2, gap=12, amp=4)),
      ('贰', '两髦', '童子垂发，齐眉为髦', lambda: M.hair_mao(378, 300, 1.75)),
      ('叁', '河上', '中河、河侧，舟所往来', lambda: M.water(622, 286, w=98, rows=4, gap=16, amp=5) + M.bank(622, 360, w=98))],
     'sj045a'),
    ('sj046a-qiang-ci-zhong-gou', '鄘风 · 四', '墙有茨', '四十六',
     [('壹', '墙', '卫宫之墙，茨生其上', lambda: M.wall(148, 296, w=140, h=104, s=1.0)),
      ('贰', '茨', '蒺藜，不可扫除', lambda: M.thorns(378, 296, 1.4)),
      ('叁', '帚', '欲扫而不能尽', lambda: M.broom(622, 292, 1.4))],
     'sj046a'),
    ('sj047a-fu-ji-liu-jia', '鄘风 · 四', '君子偕老', '四十七',
     [('壹', '副笄六珈', '笄横于发，六玉为饰', lambda: M.hairpin(148, 286, 1.35)),
      ('贰', '象服', '翟衣裼袆，礼服之盛', lambda: M.robe(378, 300, 1.3)),
      ('叁', '两髦', '发垂至眉，少时之容', lambda: M.hair_mao(622, 300, 1.75))],
     'sj047a'),
    ('sj048a-cai-tang-san-di', '鄘风 · 四', '桑中', '四十八',
     [('壹', '唐', '菟丝无根，蔓延于野', lambda: M.vine(148, 296, 1.4)),
      ('贰', '桑中', '桑林之中，期会之所', lambda: M.mulberry(378, 300, 1.3)),
      ('叁', '淇上', '淇水之上，送别之地', lambda: M.water(622, 292, w=96, rows=4, gap=16, amp=5))],
     'sj048a'),
    ('sj049a-chun-que-chang-pi', '鄘风 · 四', '鹑之奔奔', '四十九',
     [('壹', '鹑', '鹑居有常匹，奔而从之', lambda: M.bird_s(148, 300, 2.0, 'chun')),
      ('贰', '鹊', '鹊疆疆然，有定偶', lambda: M.bird_s(378, 300, 1.85, 'que')),
      ('叁', '匹', '禽有定匹，人以刺之', lambda: M.bird_s(596, 306, 1.25, 'chun') + M.bird_s(648, 294, 1.35, 'que'))],
     'sj049a'),
    ('sj050a-ding-xing-chu-gong', '鄘风 · 四', '定之方中', '五十',
     [('壹', '定星', '定星昏中，营室之时', lambda: M.star(148, 296, 2.2, 4)),
      ('贰', '楚宫', '楚丘之宫，宗庙既成', lambda: M.hall(378, 300, w=136, h=104, s=0.95)),
      ('叁', '梓', '梓材为棺，择木而用', lambda: M.tree(622, 300, 1.35))],
     'sj050a'),
    ('sj051a-di-dong-zhao-xi', '鄘风 · 四', '蝃蝀', '五十一',
     [('壹', '蝃蝀', '虹见于东，莫之敢指', lambda: M.rainbow(148, 288, 1.4)),
      ('贰', '朝隮', '云气上升于西', lambda: M.water(378, 280, w=96, rows=4, gap=20, amp=8)),
      ('叁', '女子', '有行之人，远父母兄弟', lambda: M.hair_mao(622, 300, 1.75))],
     'sj051a'),
    ('sj052a-xiang-shu-san-you', '鄘风 · 四', '相鼠', '五十二',
     [('壹', '鼠', '鼠有皮，人而无仪', lambda: M.rat(148, 300, 1.75)),
      ('贰', '齿', '鼠有齿，人而无止', lambda: M.rat(378, 300, 1.75)),
      ('叁', '礼', '人而无礼，胡不遄死', lambda: M.robe(622, 300, 1.3))],
     'sj052a'),
    ('sj054a-chi-qu-gui-yan', '鄘风 · 四', '载驰', '五十四',
     [('壹', '驰', '驱马而归，唁卫侯', lambda: M.horse(148, 268, 1.25) + M.car(148, 356, 104, 0.9)),
      ('贰', '归', '归唁卫侯，谁因谁极', lambda: M.bank(378, 356, w=100) + M.water(378, 280, w=96, rows=4, gap=18, amp=6)),
      ('叁', '麦', '行其野，芃芃其麦', lambda: M.millet(622, 300, 1.4))],
     'sj054a'),
]

if __name__ == '__main__':
    only = sys.argv[1:] or None
    bad = 0
    for (key, vol, title, num, cells, cap) in SPEC:
        if only and key.split('-')[0] not in only:
            continue
        q = quote_of({'四十五': 45, '四十六': 46, '四十七': 47, '四十八': 48, '四十九': 49,
                      '五十': 50, '五十一': 51, '五十二': 52, '五十四': 54}[num])
        p, b = layout(key, vol, title, num, cells, q, '图一 · 名物 · ' + cap)
        print('%-34s %6d B  « %s' % (key, b, q))
    try:
        import cairosvg
        for (key, *_rest) in SPEC:
            if only and key.split('-')[0] not in only:
                continue
            cairosvg.svg2png(url=os.path.join(OUTDIR, key + '.svg'),
                             write_to=os.path.join(ROOT, 'dist', key + '-new.png'), output_width=1000)
        print('png done')
    except Exception as e:
        print('png fail', e)
