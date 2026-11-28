# -*- coding: utf-8 -*-
"""078 大叔于田 · 图二（义理）

一戒三才：一章把「暴虎、献公、戒」一次说尽；二章、三章不再提戒，
只把射御与收弓铺开。戒只一句，才铺三章。
"""
import os
import sys

SK = '/home/user/.doubao/agent_mode/workspace/.user_skills/runze-daokedao-yili-fig/scripts'
sys.path.insert(0, SK)
from figkit import Fig, P, INK, OCH, BR, LINE, LG  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    f = Fig('大叔于田　一戒三才', 'sj078b-yi-jie')

    f.t(380, 90, '毛序：叔多才而好勇，不义而得众也', 8.2, OCH, 'middle', 0.4)
    f.t(380, 108, '一章有戒，二章三章不复言', 8.4, LG, 'middle', 0.8)

    rows = (
        ('一章', '乘马 · 如舞 · 火举', '暴虎 · 献公 · 将叔无狃', '戒'),
        ('二章', '乘黄 · 雁行 · 火扬', '善射 · 良御 · 磬控 · 纵送', ''),
        ('三章', '乘鸨 · 如手 · 火阜', '马慢 · 发罕 · 释掤 · 鬯弓', ''),
    )
    ys = (150, 240, 330)

    # 首章红框：先落框，后落字
    f.rect(112, 130, 456, 76, OCH, P, 0.8)

    for i, (chap, line1, line2, mark) in enumerate(rows):
        y = ys[i]
        f.t(78, y + 34, chap, 10, OCH, 'middle', 1.5)
        f.line(100, y + 14, 100, y + 58, LINE, 0.7, '4,3')
        f.t(124, y + 28, line1, 9.0, INK, 'start', 0.6)
        f.t(124, y + 48, line2, 8.6, BR, 'start', 0.5)

    # 一戒：只在首章亮一次
    f.arr(520, 164, 556, 164, OCH, 0.9)
    f.line(570, 172, 570, 376, LINE, 0.8, '4,4')
    f.t(602, 160, '戒', 22, OCH, 'middle', 2)
    f.t(602, 180, '只此一句', 7.6, OCH, 'middle', 0.4)
    f.t(602, 258, '不复言', 7.8, LG, 'middle')
    f.t(602, 348, '不复言', 7.8, LG, 'middle')

    # 三才：左侧一括，收于「才」
    f.line(58, 140, 58, 376, BR, 0.9)
    f.line(58, 140, 70, 140, BR, 0.9)
    f.line(58, 376, 70, 376, BR, 0.9)
    f.t(52, 258, '才', 16, INK, 'middle', 2)

    f.t(380, 404, '戒只一句，才铺三章', 10.5, LG, 'middle', 1)
    f.t(380, 422, '1 句戒　·　29 句才', 8.6, OCH, 'middle', 1)
    f.t(380, 436, '警告被说出，随后被展示淹没', 8.0, LG, 'middle', 0.6)

    f.concl('才可夸，义不可假；爱之而戒，戒而不制。')
    print('ok', f.save(os.path.join(ROOT, 'assets', 'fig')))


if __name__ == '__main__':
    main()
