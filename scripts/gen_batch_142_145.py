# -*- coding: utf-8 -*-
"""SJ142–SJ145 陈风四篇八图：图一名物，图二义理。760×540，不填面。"""
import os, sys, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from gen_batch_123_125 import (t, p, line, circ, rect, person, foot,
                               PAPER, INK, DARK, LIGHT, RED, SEAL, GOLD,
                               ZPAPER, ZINK, ZMID, LINE_L)

ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "assets", "fig")


def head(vol, title, sub, zh_no, zhuo=False):
    paper = ZPAPER if zhuo else PAPER
    ink = ZINK if zhuo else INK
    mid = ZMID if zhuo else DARK
    border = ZMID if zhuo else LINE_L
    return ['<rect width="760" height="540" fill="%s"/>' % paper,
            '<rect x="10" y="10" width="740" height="520" fill="none" stroke="%s" stroke-width="0.6"/>' % border,
            '<rect x="22" y="28" width="716" height="470" fill="none" stroke="%s" stroke-width="0.8"/>' % border,
            t(38, 62, "陈 风 · 之%s" % vol, 9.5, RED, ls=2),
            t(380, 72, title, 25, ink, "middle", "bold", 1.6),
            t(720, 62, "诗三百五篇 · 之%s" % zh_no, 8.6, mid, "end", ls=1),
            line(38, 100, 722, 100, 0.35, GOLD),
            t(380, 122, sub, 10.2, mid, "middle", ls=1)]


def bfig(vol, title, sub, rows, conclusion, zh_no):
    s = head(vol, title, sub, zh_no, True)
    ys = (190, 260, 330)
    for i, row in enumerate(rows):
        y = ys[i]
        s.append(line(44, y + 22, 716, y + 22, 0.3, ZMID))
        s.append(t(62, y, row[0], 10.4, ZINK, "start", "bold"))
        s.append(t(226, y, row[1], 10.8, ZINK, "start"))
        s.append(t(566, y, row[2], 9.4, ZMID, "start"))
    s.append(line(204, 168, 204, 352, 0.55, RED))
    s.append(line(50, 392, 710, 392, 0.35, GOLD))
    s.append(t(380, 418, conclusion, 11.2, RED, "middle", "bold", 0.6))
    s.append(t(380, 486, "图二 · 义理", 8.6, ZMID, "middle"))
    s.append('<rect x="676" y="492" width="22" height="22" fill="%s" opacity="0.13"/>' % SEAL)
    s.append(t(687, 507, "润", 8.8, SEAL, "middle"))
    return "".join(s)


def tree(x, y, h=80, color=INK, fruit=False):
    s = [line(x, y, x, y-h*0.5, 0.55, color),
         p("M %d %d Q %d %d %d %d Q %d %d %d %d Q %d %d %d %d Z" %
           (x-22, y-h*0.5, x-30, y-h*0.8, x-14, y-h, x, y-h-10,
            x+16, y-h, x+30, y-h*0.8, x+22, y-h*0.5), 0.4, color)]
    if fruit:
        for dx, dy in [(-10,-h+10),(4,-h+2),(14,-h+12)]:
            s.append(circ(x+dx, y+dy, 2, 0.5, RED))
    return s


def grass(x, y, h=70, color=DARK, leaf=5, flower=False):
    s = [line(x, y, x, y-h, 0.4, color)]
    for i in range(leaf):
        yy = y - 8 - i*12
        s.append(p("M %d %d Q %d %d %d %d" % (x, yy, x-16, yy-14, x-26, yy-4), 0.32, color))
        s.append(p("M %d %d Q %d %d %d %d" % (x, yy, x+16, yy-14, x+26, yy-4), 0.32, color))
    if flower:
        s.append(p("M %d %d L %d %d" % (x, y-h, x+2, y-h-12), 0.3, color))
        s.append(circ(x+3, y-h-14, 3, 0.35, RED))
    return s


def horse(x, y, sc=0.8, color=INK):
    d = ("M %d %d C %d %d %d %d %d %d C %d %d %d %d %d %d L %d %d "
         "C %d %d %d %d %d %d C %d %d %d %d %d %d Z") % (
        x-30*sc, y-34*sc, x-28*sc, y-46*sc, x+12*sc, y-48*sc, x+26*sc, y-38*sc,
        x+30*sc, y-52*sc, x+38*sc, y-58*sc, x+44*sc, y-54*sc, x+40*sc, y-46*sc,
        x+30*sc, y-40*sc, x+26*sc, y-24*sc, x+22*sc, y-16*sc,
        x-26*sc, y-16*sc, x-30*sc, y-24*sc, x-30*sc, y-34*sc)
    s = [p(d, 0.5, color)]
    for fx in (-20, -10, 12, 22):
        s.append(line(x+fx*sc, y-16*sc, x+(fx-2)*sc, y, 0.4, color))
    return s


def nest(x, y, color=INK):
    s = [p("M %d %d Q %d %d %d %d Q %d %d %d %d" %
           (x-26, y, x-26, y-20, x, y-24, x+26, y-20, x+26, y), 0.45, color),
         p("M %d %d Q %d %d %d %d" % (x-24, y-6, x, y-20, x+24, y-6), 0.3, DARK)]
    for dx in (-16, -8, 0, 8, 16):
        s.append(line(x+dx, y-4, x+dx*0.6, y-14, 0.25, LIGHT))
    return s


def f142a():
    s = head("四", "防有鹊巢　物失其所", "物有定所，言无定形", "一百四十二")
    # 防：捍水堤岸，斜线双层
    s.append(p("M 40 392 L 190 300 L 330 392", 0.6, INK))
    s.append(p("M 54 392 L 190 316 L 316 392", 0.35, DARK))
    s += nest(180, 296)
    s.append(t(120, 430, "防 · 堤岸", 8.0, DARK, "middle"))
    # 邛：低丘，旨苕
    s.append(p("M 350 392 Q 440 286 540 392", 0.55, DARK))
    s += grass(450, 330, 64, INK, 4, True)
    s += grass(478, 340, 50, LIGHT, 3, True)
    s.append(t(452, 430, "邛 · 土丘／旨苕", 8.0, DARK, "middle"))
    # 中唐：庭中通道，甓砖
    s.append(line(560, 392, 700, 392, 0.5, INK))
    s.append(line(560, 376, 700, 376, 0.35, DARK))
    for i in range(6):
        x = 566 + i*22
        s.append(rect(x, 378, 16, 12, 0.3, LIGHT, 1))
    s.append(t(630, 414, "中唐 · 甓", 8.0, DARK, "middle"))
    # 旨鷊：绶草，花作小穗
    s += grass(700, 330, 56, DARK, 3, False)
    for yy in (292, 284, 276):
        s.append(circ(701, yy, 2.5, 0.3, RED))
    s.append(t(690, 430, "旨鷊 · 绶草", 8.0, DARK, "middle"))
    s += foot("图一 · 防有鹊巢　防巢、邛苕、中唐甓、旨鷊", "防有鹊巢，邛有旨苕。")
    return "".join(s)


def f142b():
    return bfig("四", "防有鹊巢　谁侜予美", "物失其所，心失其宁",
                [("防巢", "鹊巢在防，非其木；苕在邛，非其地", "失所"),
                 ("中唐", "甓铺中唐，鷊在邛；物各有位而皆错", "错置"),
                 ("忉忉·惕惕", "谁侜予美？心焉忉忉／惕惕", "忧间")],
                "物有定所，言无定形；谁侜予美，心焉不宁。", "一百四十二")


def f143a():
    s = head("五", "月出　月皎人远", "月皎而人远，姿好而难即", "一百四十三")
    # 三阶月：皎、皓、照
    for i, (x, r) in enumerate(((110, 26), (190, 30), (270, 34))):
        s.append(circ(x, 200, r, 0.55, INK if i < 2 else DARK))
        s.append(circ(x, 200, r-7, 0.25, LIGHT))
        s.append(circ(x, 200, r+8, 0.18, LIGHT))
        for ang in range(0, 360, 45):
            s.append(p("M %.0f %.0f L %.0f %.0f" %
                       (x + (r+11)*math.cos(math.radians(ang)),
                        200 + (r+11)*math.sin(math.radians(ang)),
                        x + (r+17)*math.cos(math.radians(ang)),
                        200 + (r+17)*math.sin(math.radians(ang))), 0.2, LIGHT))
    s.append(line(80, 250, 300, 250, 0.3, GOLD))
    s.append(t(190, 272, "月出：皎 · 皓 · 照", 8.0, DARK, "middle"))
    # 佼人剪影：长袖、舒窈纠，不画脸
    s += person(500, 392, 168, 40, DARK, 0.9)
    s.append(p("M 462 330 Q 430 300 414 340", 0.35, DARK))
    s.append(p("M 538 330 Q 570 300 586 340", 0.35, DARK))
    s.append(t(500, 430, "佼人 · 舒窈纠", 8.0, DARK, "middle"))
    # 月下地线
    s.append(line(60, 392, 700, 392, 0.3, LIGHT))
    s += foot("图一 · 月出　月出皎皓照，佼人舒窈纠", "月出皎兮，佼人僚兮。")
    return "".join(s)


def f143b():
    return bfig("五", "月出　劳心三叠", "月愈明，人愈远",
                [("悄", "月出皎兮，佼人僚兮；劳心悄兮", "初念"),
                 ("慅", "月出皓兮，佼人懰兮；劳心慅兮", "再念"),
                 ("惨", "月出照兮，佼人燎兮；劳心惨兮", "极念")],
                "月皎而人远，姿好而难即；劳心三叠，皆为不可见之一念。", "一百四十三")


def f144a():
    s = head("六", "株林　朝夕驰驱", "托言从子，实淫其母", "一百四十四")
    # 株林：丛树三株
    for x, h, col in ((90, 80, INK), (150, 96, DARK), (210, 84, LIGHT)):
        s += tree(x, 392, h, col)
    s.append(t(150, 430, "株林", 8.2, DARK, "middle"))
    # 株野：方田
    s.append(rect(290, 310, 150, 82, 0.4, DARK, 2))
    for x in (330, 370, 410):
        s.append(line(x, 310, x, 392, 0.3, LIGHT))
    s.append(t(365, 430, "株野", 8.2, DARK, "middle"))
    # 乘马、乘驹：车箱、双轮、四辔、蹄迹；不画马身
    s += rect(560, 322, 82, 34, 0.5, INK, 2)
    s.append(circ(580, 368, 12, 0.4, INK))
    s.append(circ(622, 368, 12, 0.4, INK))
    s.append(line(560, 340, 500, 328, 0.4, DARK))
    for yy in (310, 318, 326, 334):
        s.append(p("M 505 %d Q 540 %d 575 %d" % (yy, yy-4, yy), 0.28, LIGHT))
    for x in (500, 520, 540, 560):
        s.append(line(x, 386, x+6, 378, 0.25, LIGHT))
        s.append(line(x+8, 386, x+14, 378, 0.25, LIGHT))
    s.append(t(600, 430, "乘马 · 乘驹", 8.2, DARK, "middle"))
    # 朝食：日与食器
    s.append(circ(690, 210, 18, 0.4, RED))
    s.append(p("M 700 230 L 704 250", 0.3, RED))
    s += foot("图一 · 株林　株林株野，乘马乘驹", "胡为乎株林？从夏南。")
    return "".join(s)


def f144b():
    return bfig("六", "株林　只问不答", "问在从子，实在从母",
                [("一问", "胡为乎株林？从夏南", "诘问"),
                 ("二问", "匪适株林，从夏南", "掩迹"),
                 ("驰驱", "说于株野，朝食于株；朝夕不息", "实迹")],
                "托言从子，实淫其母；朝夕驰驱，朝食于株。", "一百四十四")


def f145a():
    s = head("七", "泽陂　蒲荷在泽", "蒲荷在泽，美人在念", "一百四十五")
    # 泽陂：水与堤
    s.append(line(60, 392, 700, 392, 0.35, DARK))
    for y in (330, 362):
        s.append(p("M 70 %d Q 200 %d 330 %d Q 460 %d 590 %d Q 650 %d 700 %d" %
                   (y, y-10, y, y+10, y, y-6, y), 0.35, LIGHT))
    # 蒲：长茎、穗
    s += grass(150, 330, 92, INK, 4, False)
    s.append(p("M 150 238 L 150 218", 0.3, DARK))
    s.append(circ(150, 216, 4, 0.35, DARK))
    s.append(t(150, 430, "蒲", 8.0, DARK, "middle"))
    # 荷：圆叶、叶脉、花
    for x, y in ((300, 316), (350, 300)):
        s.append(p("M %d %d C %d %d %d %d %d %d C %d %d %d %d %d %d" %
                   (x-34, y, x-30, y-20, x-10, y-26, x, y-24,
                    x+10, y-26, x+30, y-20, x+34, y), 0.45, DARK))
        s.append(p("M %d %d Q %d %d %d %d" % (x-34, y, x, y+6, x+34, y), 0.3, DARK))
        for ang in (-0.75, -0.35, 0, 0.35, 0.75):
            s.append(p("M %d %d Q %d %d %d %d" %
                       (x, y-2, x+ang*22, y-2, x+ang*34, y-2), 0.22, LIGHT))
        s.append(line(x, y-4, x, 360, 0.3, LIGHT))
    s.append(p("M 350 292 L 354 264", 0.35, DARK))
    for dx, dy in ((-10,-2),(10,-2),(0,-12),(-6,-18),(6,-18)):
        s.append(p("M 354 266 Q %d %d %d %d" % (354+dx*2, 266+dy*2, 354+dx, 266+dy), 0.3, RED))
    s.append(t(325, 430, "荷", 8.0, DARK, "middle"))
    # 蕳：兰草
    s += grass(500, 360, 70, DARK, 5, True)
    s.append(t(500, 430, "蕳 · 兰", 8.0, DARK, "middle"))
    # 菡萏：莲苞
    s.append(p("M 620 360 Q 600 300 620 270 Q 640 300 620 360 Z", 0.45, RED))
    s.append(line(620, 360, 620, 380, 0.3, DARK))
    s.append(t(620, 430, "菡萏", 8.0, DARK, "middle"))
    s += foot("图一 · 泽陂　泽陂蒲荷，蕳与菡萏", "彼泽之陂，有蒲与荷。")
    return "".join(s)


def f145b():
    return bfig("七", "泽陂　寤寐无为", "临泽而思，终夜不寐",
                [("蒲荷", "有蒲与荷／与蕳／菡萏；泽有所生", "见"),
                 ("美人", "有美一人，伤如之何；思有所伤", "念"),
                 ("伏枕", "寤寐无为，涕泗滂沱；辗转伏枕", "夜")],
                "蒲荷在泽，美人在念；涕泗于心，辗转于枕。", "一百四十五")


FIGS = {
 "sj142a-fang-you-que-chao": f142a,
 "sj142b-you-chian": f142b,
 "sj143a-yue-chu": f143a,
 "sj143b-lao-xin": f143b,
 "sj144a-zhu-lin": f144a,
 "sj144b-wen-xia-nan": f144b,
 "sj145a-ze-bei": f145a,
 "sj145b-zhuan-fu-zhen": f145b,
}

for k, fn in FIGS.items():
    body = fn()
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 540" width="760" height="540">\n'
           + body + "\n</svg>\n")
    open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8").write(svg)
    print(k)
