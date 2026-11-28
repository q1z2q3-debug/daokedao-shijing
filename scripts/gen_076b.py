# -*- coding: utf-8 -*-
"""076 将仲子 · 图二（义理）

一图一义：三章换境、换树、换说话的人；不换的是「仲可怀也」与「亦可畏也」。
三柱：父母低，诸兄中，人言高——畏一层高过一层。
一横线：仲可怀也，三级都穿，位置不动——怀不改。
"""
import os
import sys

SK = '/home/user/.doubao/agent_mode/workspace/.user_skills/runze-daokedao-yili-fig/scripts'
sys.path.insert(0, SK)
from figkit import Fig, P, INK, OCH, BR, LINE, LG  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    f = Fig('将仲子　三畏', 'sj076b-san-wei')
    base = 392
    x = (165, 380, 595)
    w = 104
    top = (300, 230, 150)
    big = ('父母', '诸兄', '人言')
    jing = ('里', '墙', '园')
    tree = ('杞', '桑', '檀')
    chap = ('一章', '二章', '三章')

    # 三柱：高度即畏之递进
    for i in range(3):
        f.rect(x[i] - w / 2, top[i], w, base - top[i], stroke=OCH if i == 2 else BR, lw=1.1 if i == 2 else 0.9)
        # 柱内横纹：土石层，不作面
        for k in range(4):
            yy = top[i] + 18 + k * 18
            if yy < base - 14:
                f.line(x[i] - w / 2 + 8, yy, x[i] + w / 2 - 8, yy, LINE, 0.4)
        f.t(x[i], top[i] - 10, chap[i], 8.6, LG, spacing=1)
        f.t(x[i], top[i] + 26, jing[i], 15, INK, spacing=2)
        f.t(x[i], top[i] + 42, tree[i], 8.5, BR)
        f.t(x[i], base - 20, big[i], 15, INK, spacing=2)
        f.t(x[i], base - 4, ('近', '中', '远')[i], 7.4, LG)

    # 基线
    f.line(90, base, 670, base, BR, 1.1)
    f.t(88, base + 16, '三章换境换树，不换怀畏', 9, LG, anchor='start')

    # 畏之递进：从低柱顶到高柱顶
    f.arr(x[0] + w / 2 + 6, top[0] - 2, x[1] - w / 2 - 8, top[1] - 2, OCH, 1.0)
    f.arr(x[1] + w / 2 + 6, top[1] - 2, x[2] - w / 2 - 8, top[2] - 2, OCH, 1.0)
    f.t(500, 126, '畏之递进', 9.5, OCH, spacing=1)

    # 仲可怀也：横线穿三级，位置不动
    f.line(92, 330, 668, 330, OCH, 1.2, '6 4')
    f.t(380, 112, '横线：仲可怀也——三级都穿，位置不动', 9.5, OCH, spacing=0.5)

    # 三条注
    f.t(165, 428, '父母：最近之言', 8.8, LG)
    f.t(380, 428, '诸兄：公族之言', 8.8, LG)
    f.t(595, 428, '人言：众人之口', 8.8, LG)

    f.concl('墙可三重，言只一句；爱在畏中，畏在言中。')
    print('ok', f.save(os.path.join(ROOT, 'assets', 'fig')))


if __name__ == '__main__':
    main()
