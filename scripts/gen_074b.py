# -*- coding: utf-8 -*-
"""074 丘中有麻 · 图二 义理图

一图一义：**物在地中，思在地中。**
丘为地，三物在地（麻初植、麦可食、李成树——时间的三层）。
人则不在：留氏之名作虚框，无实。三条虚线自物指框，是「思」的形状。
地不荒而人不归，故王风以思贤终。
"""
import os
import sys

SK = '/home/user/.doubao/agent_mode/workspace/.user_skills/runze-daokedao-yili-fig/scripts'
sys.path.insert(0, SK)
from figkit import Fig, P, INK, OCH, BR, LINE, LG  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    f = Fig('丘中有麻　物在人不在', 'sj074b-wu-zai-di')
    # 丘：两斜一弧，作「地」的界
    f.path('M 380 152 L 96 392 Q 380 430 664 392 L 380 152', stroke=BR, fill='none', lw=1.3)

    # 三物：沿丘内一线排开，高低不齐是「递长」
    items = ((176, 348, '麻', '初植，绩布'), (380, 318, '麥', '可食'), (584, 348, '李', '成树'))
    _ = items
    for x, y, name, sub in items:
        f.dot(x, y, 3.4)
        f.t(x, y - 16, name, 13, INK)
        f.t(x, y + 20, sub, 9, LG)

    # 虚框：留氏之名，无实
    f.rect(322, 190, 116, 46, stroke=OCH, lw=1.2, dash='6 4')
    f.t(380, 210, '留氏', 14, OCH)
    f.t(380, 227, '子嗟 · 子国 · 之子', 8.5, LG)

    # 三条虚线：物 → 人（思的形状）
    for x, y, _, _ in (items[0], items[2]):
        f.line(x, y - 24, 380 + (x - 380) * 0.30, 240, LINE, 0.9, dash='5 5')
    # 中物一线，须断于「麦」字，否则字压线
    f.line(380, 302, 380, 246, LINE, 0.9, dash='5 5')

    # 丘上标「地」
    f.t(380, 404, '地', 11, BR)

    f.concl('物在地中，思在地中；地不荒，而人不归')
    print('ok', f.save(os.path.join(ROOT, 'assets', 'fig')))


if __name__ == '__main__':
    main()
