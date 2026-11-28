# -*- coding: utf-8 -*-
"""073 大车 · 图二 义理图

一图一义：**生不敢，死乃敢言。**
左境为生：车声、衣色二威，威逼出「畏」，畏成「不敢」。
中一竖界：生｜死。
右境为死：异室而同穴，是把不敢之于生者，托之于死。
皦日压在界上——实者不可改，虚者不可证，诗在虚实之间。
"""
import os
import sys

SK = '/home/user/.doubao/agent_mode/workspace/.user_skills/runze-daokedao-yili-fig/scripts'
sys.path.insert(0, SK)
from figkit import Fig, P, INK, OCH, BR, LINE, LG  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    f = Fig('大车　生畏死誓', 'sj073b-sheng-si')
    # 生境：二威 → 畏 → 不敢
    for k, (txt, sub) in enumerate((('車聲：檻檻·啍啍', '轻而清，重而迟'),
                                    ('服色：如菼·如璊', '青如初荻，赤如赤玉'))):
        y = 150 + k * 62
        f.rect(96, y, 186, 40, stroke=BR, lw=0.9)
        f.t(189, y + 17, txt, 11, INK)
        f.t(189, y + 32, sub, 9, LG)
    f.arr(282, 210, 322, 210, BR, 1.0)
    f.rect(330, 176, 86, 68, stroke=INK, lw=1.4)
    f.t(373, 202, '畏', 15, INK)
    f.t(373, 226, '不敢·不奔', 9.5, LG)

    f.line(420, 210, 448, 210, LINE, 0.9, dash='4 4')
    f.arr(440, 206, 450, 210, LINE, 0.9)

    # 生死界
    f.line(452, 118, 452, 402, LINE, 1.1, dash='6 5')
    f.t(452, 110, '生', 10, LG)
    f.t(452, 418, '死', 10, LG)

    # 死境：异室 → 同穴
    f.rect(492, 150, 168, 40, stroke=BR, lw=0.9, dash='5 4')
    f.t(576, 175, '生则异室（礼）', 11, LG)
    f.line(540, 196, 540, 234, LINE, 0.9, dash='4 4')
    f.arr(536, 226, 540, 238, LINE, 0.9)
    f.rect(492, 244, 168, 52, stroke=INK, lw=1.4)
    f.t(576, 268, '死则同穴', 13, INK)
    f.t(576, 286, '舍礼而合', 9.5, LG)

    # 皦日：压在界上，唯一赭
    f.ring(452, 358, 13, color=OCH, lw=1.2)
    f.dot(452, 358, 3, OCH)
    f.t(452, 394, '皦日', 11, OCH)
    for a in (-1, 1):
        f.line(452 + a * 20, 358, 452 + a * 30, 358, OCH, 0.9)

    f.concl('生不敢，死乃敢言；实者不可改，虚者不可证')
    print('ok', f.save(os.path.join(ROOT, 'assets', 'fig')))


if __name__ == '__main__':
    main()
