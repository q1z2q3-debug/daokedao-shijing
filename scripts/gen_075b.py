# -*- coding: utf-8 -*-
"""075 缁衣 · 图二 义理图

一图一义：**好贤不是一个字，是三个动作。**
一件衣在最左（敝）——不弃其旧；一「改」随之——不惜其力；
「适子之馆」——不惮其往；「授子之粲」——不吝其食。
三章所换者（宜、好、席），皆衣之评，画作虚；三章不换者（适馆、授粲），皆待人之实，画作实。
"""
import os
import sys

SK = '/home/user/.doubao/agent_mode/workspace/.user_skills/runze-daokedao-yili-fig/scripts'
sys.path.insert(0, SK)
from figkit import Fig, P, INK, OCH, BR, LINE, LG  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    f = Fig('缁衣　好贤三级', 'sj075b-hao-xian')
    y, h = 190, 50
    # 主链：敝衣 → 改 → 适馆 → 授粲
    f.rect(60, y, 122, h, stroke=BR, lw=0.9)
    f.t(121, y + 20, '缁衣之敝', 11, INK)
    f.t(121, y + 37, '卿士正服，旧', 9, LG)

    f.rect(214, y, 92, h, stroke=BR, lw=0.9)
    f.t(260, y + 20, '改', 12, INK)
    f.t(260, y + 37, '改·改造·改作', 8.5, LG)

    f.rect(344, y, 118, h, stroke=BR, lw=0.9)
    f.t(403, y + 20, '适子之馆', 11, INK)
    f.t(403, y + 37, '不惮其往', 9, LG)

    f.rect(500, y, 130, h, stroke=OCH, lw=1.3)
    f.t(565, y + 20, '授子之粲', 11, OCH)
    f.t(565, y + 37, '不吝其食', 9, LG)

    for x1, x2 in ((182, 212), (306, 342), (462, 498)):
        f.arr(x1, y + h / 2, x2, y + h / 2, BR, 1.0)

    # 上：三章所换，衣之评，虚
    f.t(121, 132, '宜　好　席', 11, LG, spacing=2)
    f.line(121, 140, 121, y - 6, LINE, 0.8, dash='4 4')
    f.t(232, 132, '三章所换者——衣之评', 9, LG)

    # 下：三章不换，诗之骨，实
    f.line(403, y + h + 10, 403, 296, INK, 0.9)
    f.line(565, y + h + 10, 565, 296, INK, 0.9)
    f.line(400, 300, 568, 300, INK, 1.1)
    f.t(484, 320, '三章不换者——诗之骨', 10, INK)

    # 三级注
    for x, txt in ((121, '衣之：养其体'), (403, '馆之：安其居'), (565, '粲之：饱其腹')):
        f.t(x, 366, txt, 9.5, BR)

    f.concl('衣可敝，礼不可废；物可旧，人不可弃')
    print('ok', f.save(os.path.join(ROOT, 'assets', 'fig')))


if __name__ == '__main__':
    main()
