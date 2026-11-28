# -*- coding: utf-8 -*-
"""SJ126–SJ128 秦风前三篇图一/图二，共六张。760×540，纸墨五色，不填面。"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gen_batch_123_125 as B
from gen_batch_123_125 import (t, p, line, circ, rect, person, foot,
                               PAPER, INK, DARK, LIGHT, RED, SEAL, GOLD, ZPAPER, ZINK, ZMID, LINE_L)

ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "assets", "fig")


def headq(vol, title, sub, zh_no, zhuo=False):
    paper = ZPAPER if zhuo else PAPER
    ink = ZINK if zhuo else INK
    mid = ZMID if zhuo else DARK
    border = ZMID if zhuo else LINE_L
    return ['<rect width="760" height="540" fill="%s"/>' % paper,
            '<rect x="10" y="10" width="740" height="520" fill="none" stroke="%s" stroke-width="0.6"/>' % border,
            '<rect x="22" y="28" width="716" height="470" fill="none" stroke="%s" stroke-width="0.8"/>' % border,
            t(38, 62, "秦 风 · 之%s" % vol, 9.5, RED, ls=2),
            t(380, 72, title, 25, ink, "middle", "bold", 1.6),
            t(720, 62, "诗三百五篇 · 之%s" % zh_no, 8.6, mid, "end", ls=1),
            line(38, 100, 722, 100, 0.35, GOLD),
            t(380, 122, sub, 10.2, mid, "middle", ls=1)]


def cart(x, y, wd=90, ht=34, color=INK, horse=False):
    s = [rect(x, y, wd, ht, 0.5, color, 2),
         circ(x + wd*0.28, y + ht + 9, 10, 0.45, color),
         circ(x + wd*0.78, y + ht + 9, 10, 0.45, color),
         line(x + wd*0.5, y, x + wd*0.5, y - 34, 0.4, color),
         line(x + wd*0.5, y - 34, x + wd*1.18, y - 28, 0.4, color)]
    if horse:
        hx, hy = x + wd*1.12, y + 18
        s += [p("M %d %d L %d %d L %d %d L %d %d L %d %d" % (hx, hy-26, hx+34, hy-34, hx+52, hy-27, hx+48, hy+8, hx, hy+10), 0.5, color),
              line(hx+6, hy+8, hx+2, hy+31, 0.4, color), line(hx+42, hy+8, hx+47, hy+31, 0.4, color)]
    return s


def gate(x, y, color=INK, open_=False):
    s = [line(x-40, y, x-40, y-92, 0.7, color), line(x+40, y, x+40, y-92, 0.7, color),
         line(x-58, y-92, x+58, y-92, 0.8, color)]
    if not open_:
        s += [line(x-38, y-86, x-38, y-42, 0.4, color), line(x+38, y-86, x+38, y-42, 0.4, color),
              line(x-38, y-64, x+38, y-64, 0.35, color)]
    return s


def tree(x, y, ht=92, wd=34, color=INK, fruit=False):
    s = [line(x, y, x, y-ht*0.55, 0.6, color),
         p("M %d %d Q %d %d %d %d Q %d %d %d %d Q %d %d %d %d Z" %
           (x-wd*0.7, y-ht*0.55, x-wd, y-ht*0.82, x-wd*0.55, y-ht-6,
            x, y-ht-18, x+wd*0.55, y-ht-6, x+wd, y-ht*0.82, x+wd*0.7, y-ht*0.55), 0.45, color)]
    for dx, dy in [(-18,-ht+8),(4,-ht+16),(22,-ht+4),(-6,-ht*0.6),(16,-ht*0.55)]:
        s.append(line(x, y-ht*0.55, x+dx, y+dy, 0.28, color))
    if fruit:
        for dx, dy in [(-20,-ht+6),(4,-ht+12),(24,-ht+2)]:
            s.append(circ(x+dx, y+dy, 2.2, 0.5, RED))
    return s


def bighorse(x, y, color=INK, white=False, scale=1.0):
    """马侧影：背、颈首、四足、尾；只描轮廓，不画眼、不画全脸。"""
    sc = scale
    d = ("M %d %d C %d %d %d %d %d %d C %d %d %d %d %d %d L %d %d "
         "C %d %d %d %d %d %d C %d %d %d %d %d %d Z") % (
        x - 30 * sc, y - 34 * sc,
        x - 28 * sc, y - 46 * sc, x + 12 * sc, y - 48 * sc, x + 26 * sc, y - 38 * sc,
        x + 30 * sc, y - 52 * sc, x + 38 * sc, y - 58 * sc, x + 44 * sc, y - 54 * sc,
        x + 40 * sc, y - 46 * sc,
        x + 30 * sc, y - 40 * sc, x + 26 * sc, y - 24 * sc, x + 22 * sc, y - 16 * sc,
        x - 26 * sc, y - 16 * sc, x - 30 * sc, y - 24 * sc, x - 30 * sc, y - 34 * sc)
    s = [p(d, 0.5, color)]
    for fx in (-20, -10, 12, 22):
        s.append(line(x + fx * sc, y - 16 * sc, x + (fx - 2) * sc, y, 0.4, color))
    s.append(p("M %d %d C %d %d %d %d %d %d" %
               (x - 30 * sc, y - 36 * sc, x - 42 * sc, y - 30 * sc,
                x - 44 * sc, y - 16 * sc, x - 38 * sc, y - 10 * sc), 0.35, color))
    if white:
        s.append(line(x + 34 * sc, y - 54 * sc, x + 40 * sc, y - 50 * sc, 0.45, color))
    return s


def beast(x, y, color=DARK, scale=1.0):
    """牡兽侧影：身、首、角、四足；不画眼。"""
    sc = scale
    s = [p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f Z" %
               (x - 26 * sc, y - 26 * sc, x - 24 * sc, y - 36 * sc,
                x + 12 * sc, y - 36 * sc, x + 24 * sc, y - 26 * sc,
                x + 24 * sc, y - 16 * sc, x + 10 * sc, y - 12 * sc, x - 26 * sc, y - 26 * sc),
           0.5, color),
         p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
               (x + 22 * sc, y - 28 * sc, x + 30 * sc, y - 34 * sc,
                x + 34 * sc, y - 32 * sc, x + 32 * sc, y - 26 * sc), 0.4, color),
         line(x + 28 * sc, y - 32 * sc, x + 32 * sc, y - 42 * sc, 0.3, color),
         line(x + 25 * sc, y - 32 * sc, x + 26 * sc, y - 42 * sc, 0.3, color)]
    for fx in (-16, -6, 8, 18):
        s.append(line(x + fx * sc, y - 14 * sc, x + fx * sc, y, 0.3, color))
    return s


def dragon_shield(cx, cy, r=34, color=INK):
    s = [circ(cx, cy, r, 0.55, color), p("M %d %d L %d %d L %d %d L %d %d Z" % (cx-24, cy, cx-10, cy-12, cx+10, cy-12, cx+24, cy), 0.4, RED)]
    return s


def f126a():
    s = headq("一", "车邻　门外车马", "车马之盛，先闻其声", "一百二十六")
    s += gate(330, 392)
    s += cart(55, 358, 88, 28, INK, False)
    s += cart(145, 374, 76, 26, DARK, False)
    s += bighorse(150, 358, INK, True, 0.85)
    s += bighorse(244, 374, DARK, False, 0.75)
    s += person(356, 390, 88, 24)
    s += tree(500, 392, 104, 42, DARK, True)
    s += tree(618, 392, 84, 34, LIGHT)
    s += foot("图一 · 车邻　众车、白颠马、寺人传令", "车在马前，令在门内")
    return "".join(s)


def f126b():
    ink = ZINK; mid = ZMID
    s = headq("一", "车邻　未见·既见·不乐", "盛有期限，乐在当下", "一百二十六", True)
    ys = (190, 260, 330)
    for y in ys:
        s.append(line(44, y+22, 716, y+22, 0.3, mid))
    s.append(line(204, 168, 204, 352, 0.55, RED))
    s.append(t(62, 190, "未见", 11, ink, "start", "bold"))
    s += gate(100, 206, ink)
    s.append(t(226, 190, "车在门外，寺人传令；先闻其声，未见其人。", 10.4, ink))
    s.append(t(62, 260, "既见", 11, ink, "start", "bold"))
    s.append(t(226, 260, "阪漆隰栗，并坐鼓瑟；有而能用，才叫乐。", 10.4, ink))
    s.append(line(236, 278, 300, 278, 0.45, ink))
    s.append(circ(320, 274, 7, 0.4, ink))
    s.append(t(352, 278, "瑟", 9.4, mid))
    s.append(t(62, 330, "不乐", 11, ink, "start", "bold"))
    s.append(t(226, 330, "今者不乐，逝者其耋；再一步，就是其亡。", 10.4, ink))
    s.append(line(50, 392, 710, 392, 0.35, GOLD))
    s.append(t(380, 418, "车可邻，乐不可待；今者不乐，逝者其耋。", 11.6, RED, "middle", "bold", 0.6))
    s.append(t(380, 486, "图二 · 义理", 8.6, mid, "middle"))
    s.append('<rect x="676" y="492" width="22" height="22" fill="%s" opacity="0.13"/>' % SEAL)
    s.append(t(687, 507, "润", 8.8, SEAL, "middle"))
    return "".join(s)


def f127a():
    s = headq("二", "驷驖　四马六辔", "马整辔齐，射在有令", "一百二十七")
    for i, x in enumerate((55, 165, 275, 385)):
        s += bighorse(x, 330, INK if i % 2 == 0 else DARK, i == 1)
    for i, x in enumerate((55, 165, 275, 385)):
        s.append(line(x+64, 300, 505, 282 + i*4, 0.3, LIGHT))
    s.append(t(512, 272, "六辔", 8.6, LIGHT, "start"))
    s.append(rect(490, 330, 78, 30, 0.5, DARK, 2))
    s.append(circ(510, 370, 12, 0.45, DARK)); s.append(circ(552, 370, 12, 0.45, DARK))
    s += person(535, 360, 96, 26)
    s += beast(656, 392, DARK, 0.9)
    s.append(line(596, 362, 642, 382, 0.55, RED))
    s.append(line(642, 382, 654, 388, 0.4, RED))
    s += foot("图一 · 驷驖　四马六辔、辰牡、射获", "公曰左之，舍拔则获")
    return "".join(s)


def f127b():
    ink = ZINK; mid = ZMID
    s = headq("二", "驷驖　狩前·狩中·北园", "一张一弛，田狩之礼", "一百二十七", True)
    ys = (190, 260, 330)
    for y in ys:
        s.append(line(44, y+22, 716, y+22, 0.3, mid))
    s.append(line(204, 168, 204, 352, 0.55, RED))
    s.append(t(62, 190, "狩前", 11, ink, "start", "bold"))
    s.append(t(226, 190, "四马六辔在手；媚子从公，车马先整。", 10.4, ink))
    s.append(t(62, 260, "狩中", 11, ink, "start", "bold"))
    s.append(t(226, 260, "奉时辰牡，公曰左之；一舍拔，获在掌握。", 10.4, ink))
    s.append(line(560, 248, 620, 240, 0.45, ink))
    s.append(line(620, 240, 650, 234, 0.35, RED))
    s.append(t(62, 330, "北园", 11, ink, "start", "bold"))
    s.append(t(226, 330, "四马既闲，轻车鸾铃；由张到弛，猎才算完。", 10.4, ink))
    s.append(line(50, 392, 710, 392, 0.35, GOLD))
    s.append(t(380, 418, "马可闲，令不可慢；一舍拔，获在掌握。", 11.6, RED, "middle", "bold", 0.6))
    s.append(t(380, 486, "图二 · 义理", 8.6, mid, "middle"))
    s.append('<rect x="676" y="492" width="22" height="22" fill="%s" opacity="0.13"/>' % SEAL)
    s.append(t(687, 507, "润", 8.8, SEAL, "middle"))
    return "".join(s)


def f128a():
    s = headq("三", "小戎　兵车甲盾", "器有其制，念有其人", "一百二十八")
    s.append(rect(210, 310, 250, 66, 0.6, INK, 2))
    s.append(line(210, 310, 150, 344, 0.6, INK))
    s.append(line(460, 310, 510, 330, 0.5, INK))
    for i in range(5):
        s.append(line(210+i*46, 310, 210+i*46, 376, 0.35, LIGHT))
    s.append(circ(250, 392, 15, 0.5, INK)); s.append(circ(420, 392, 15, 0.5, INK))
    s += bighorse(560, 360, INK, False)
    s += dragon_shield(690, 250, 34, INK)
    s.append(line(620, 310, 700, 214, 0.55, DARK))
    s.append(p("M 700 214 L 708 200 L 712 216 Z", 0.5, DARK))
    s.append(p("M 700 224 L 712 226 L 706 238 Z", 0.45, DARK))
    s.append(rect(80, 330, 26, 64, 0.5, DARK, 3))
    s.append(line(106, 342, 210, 342, 0.55, DARK))
    s += person(120, 392, 96, 26)
    s += foot("图一 · 小戎　兵车、五楘梁辀、龙盾", "驾我骐馵，乱我心曲")
    return "".join(s)


def f128b():
    ink = ZINK; mid = ZMID
    s = headq("三", "小戎　板屋·在邑·德音", "器是公家，念是私室", "一百二十八", True)
    ys = (190, 260, 330)
    for y in ys:
        s.append(line(44, y+22, 716, y+22, 0.3, mid))
    s.append(line(204, 168, 204, 352, 0.55, RED))
    s.append(t(62, 190, "板屋", 11, ink, "start", "bold"))
    s.append(t(226, 190, "西戎板屋，君子在远；车甲越精，心曲越乱。", 10.4, ink))
    s.append(t(62, 260, "在邑", 11, ink, "start", "bold"))
    s.append(t(226, 260, "温其在邑，归期无期；不怨战，只怨无期。", 10.4, ink))
    s.append(t(62, 330, "德音", 11, ink, "start", "bold"))
    s.append(t(226, 330, "载寝载兴，厌厌良人；兵越精，人越可敬。", 10.4, ink))
    s.append(line(50, 392, 710, 392, 0.35, GOLD))
    s.append(t(380, 418, "甲可坚，念不可断；板屋之下，心曲自乱。", 11.6, RED, "middle", "bold", 0.6))
    s.append(t(380, 486, "图二 · 义理", 8.6, mid, "middle"))
    s.append('<rect x="676" y="492" width="22" height="22" fill="%s" opacity="0.13"/>' % SEAL)
    s.append(t(687, 507, "润", 8.8, SEAL, "middle"))
    return "".join(s)


FIGS = {"sj126a-che-lin": f126a, "sj126b-ji-shi": f126b,
        "sj127a-si-tie": f127a, "sj127b-bei-yuan": f127b,
        "sj128a-xiao-rong": f128a, "sj128b-san-nian": f128b}

for k, fn in FIGS.items():
    body = fn()
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 540" width="760" height="540">\n'
           + body + "\n</svg>\n")
    open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8").write(svg)
    print(k)
