# -*- coding: utf-8 -*-
"""072 采葛 · 图二 义理图

一图一义：**一日为枢，三时其量。**
诗之全部张力，在「一日」同一个，所量却是三月、三秋、三岁。
三线自枢点辐射，线端三牌为三量，线上标三事——葛之小、萧之大、艾之急。
事愈急，则线愈陡、牌愈高，惧愈深。右侧一竖轴示「惧」。
"""
import os
import sys

SK = '/home/user/.doubao/agent_mode/workspace/.user_skills/runze-daokedao-yili-fig/scripts'
sys.path.insert(0, SK)
from figkit import Fig, P, INK, OCH, BR, LINE, LG  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    f = Fig('采葛　一日为枢', 'sj072b-yi-ri-wei-shu')
    px, py = 148, 366

    # 枢点：一日。赭环只此一处
    f.ring(px, py, 7, color=OCH)
    f.dot(px, py, 2.2)
    f.t(px, py + 26, '一日', 12, INK)

    # 三线三量：三月、三秋、三岁
    rays = ((432, 336, '三月', '葛 · 絺绤', '小'),
            (474, 258, '三秋', '萧 · 祭祀', '大'),
            (516, 172, '三岁', '艾 · 疗疾', '急'))
    for k, (x2, y2, lab, bing, deng) in enumerate(rays):
        f.line(px + 8, py - 2, x2, y2, BR, 1.0)
        # 事标：断线压口，标签落在断处——不断线，标签就无所属
        xm, ym = px + 8 + (x2 - px - 8) * 0.56, py - 2 + (y2 - py + 2) * 0.56
        f.gap(xm - 30, ym, xm + 30, ym, half=9)
        f.t(xm, ym + 4, bing, 9.5, LG)
        # 量牌
        f.rect(x2, y2 - 14, 68, 28, stroke=BR, lw=0.9)
        f.t(x2 + 34, y2 + 4, lab, 12.5, INK)
        # 等第，牌下小字
        f.t(x2 + 34, y2 + 26, deng, 9, LG)

    # 惧轴：右竖，向上为深
    f.line(650, 404, 650, 146, LINE, 1.0, dash='5 4')
    f.arr(650, 190, 650, 152, BR, 1.2)
    f.t(650, 424, '浅', 9.5, LG)
    f.t(650, 128, '深', 9.5, LG)
    f.t(678, 278, '惧', 13, INK)

    f.concl('一日为枢，三时其量；事愈急，则惧愈深')
    print('ok', f.save(os.path.join(ROOT, 'assets', 'fig')))


if __name__ == '__main__':
    main()
