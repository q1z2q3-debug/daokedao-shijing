# -*- coding: utf-8 -*-
"""077 叔于田 · 图二（义理）

一图一义：三章三空——居人、饮酒、服马；三空都归到一个「叔」。
左三门，右一柱；三章的空，三章的誉，都落在同一个人身上。
"""
import os
import sys

SK = '/home/user/.doubao/agent_mode/workspace/.user_skills/runze-daokedao-yili-fig/scripts'
sys.path.insert(0, SK)
from figkit import Fig, P, INK, OCH, BR, LINE, LG  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    f = Fig('叔于田　三空', 'sj077b-san-kong')
    rows = (
        ('一章　田', '居人', '仁'),
        ('二章　狩', '饮酒', '好'),
        ('三章　野', '服马', '武'),
    )
    ys = (124, 214, 304)
    x0, w, h = 76, 156, 72
    bx, bw = 500, 82

    # 顶注：毛序的框
    f.t(380, 90, '毛序：刺庄公也——叔处于京，缮甲治兵，以出于田，国人说而归之',
        8.1, OCH, 'middle', 0.3)
    f.t(380, 108, '三章皆曰「洵美」：美不变，所誉者三', 8.4, LG, 'middle', 0.8)

    # 三章三门：门内空
    for i, (chap, empty, praise) in enumerate(rows):
        y = ys[i]
        f.rect(x0, y, w, h, BR, P, 0.9)
        # 门内：抹掉下边一段，作「空门」
        f.gap(x0 + 28, y + h, x0 + w - 28, y + h, 9)
        f.t(x0, y - 7, chap, 8.4, OCH, 'start', 0.6)
        f.t(x0 + w / 2, y + 25, '巷无', 9.4, LG, 'middle', 1.2)
        f.t(x0 + w / 2, y + 49, empty, 15, INK, 'middle', 1.5)
        # 空门内：两道虚线，示「无人」
        f.line(x0 + 18, y + 58, x0 + w - 18, y + 58, LINE, 0.7, '3,3')
        # 指向叔
        f.arr(x0 + w + 6, y + h / 2, bx - 6, y + h / 2, OCH, 0.9)

    # 叔：一柱受三空
    f.rect(bx, 112, bw, 288, OCH, P, 1.2)
    f.t(bx + bw / 2, 238, '叔', 24, INK, 'middle', 3)
    f.t(bx + bw / 2, 258, '共叔段', 8.4, BR, 'middle', 1)
    f.t(bx + bw / 2, 390, '国人说而归之', 8.2, OCH, 'middle', 0.4)

    # 三誉
    f.t(630, 112, '国人誉之', 8.4, LG, 'middle', 1)
    for i, (_, _, praise) in enumerate(rows):
        f.t(630, ys[i] + 42, praise, 18, INK, 'middle', 2)
    f.line(612, 128, 612, 372, LINE, 0.8, '4,4')
    f.t(690, 126, '美', 12, OCH, 'middle', 2)
    f.t(690, 142, '不变', 7.6, LG, 'middle')

    # 三空归一：底部收束
    f.line(bx + bw / 2, 400, bx + bw / 2, 420, BR, 0.9, '3,3')
    f.t(380, 424, '一巷三空，三空一叔', 9.2, LG, 'middle', 1)

    f.concl('巷可空，心不可空；众所归，祸所起。')
    print('ok', f.save(os.path.join(ROOT, 'assets', 'fig')))


if __name__ == '__main__':
    main()
