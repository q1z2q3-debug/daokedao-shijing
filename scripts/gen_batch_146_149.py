# -*- coding: utf-8 -*-
"""SJ146–SJ149 桧风四篇八图：图一名物，图二义理。760×540，不填面。"""
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
            t(38, 62, "桧 风 · 之%s" % vol, 9.5, RED, ls=2),
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


def robe(x, y, w, h, color=INK, fur=False):
    s = [p("M %d %d L %d %d L %d %d L %d %d L %d %d L %d %d Z" %
           (x-w/2, y, x-w/2+12, y-24, x-6, y-34, x+6, y-34, x+w/2-12, y-24, x+w/2, y),
           0.5, color),
         p("M %d %d Q %d %d %d %d" % (x-w/2+12, y-24, x, y-18, x+w/2-12, y-24), 0.3, LIGHT)]
    if fur:
        s.append(p("M %d %d Q %d %d %d %d" % (x-7, y-34, x, y-42, x+7, y-34), 0.45, color))
        for dx in (-4, 0, 4):
            s.append(line(x+dx, y-34, x+dx, y-27, 0.25, LIGHT))
    s.append(line(x, y-30, x, y-2, 0.25, LIGHT))
    s.append(p("M %d %d Q %d %d %d %d" % (x-w/2+2, y-22, x-w/2-16, y-12, x-w/2-12, y+12), 0.35, color))
    s.append(p("M %d %d Q %d %d %d %d" % (x+w/2-2, y-22, x+w/2+16, y-12, x+w/2+12, y+12), 0.35, color))
    s.append(p("M %d %d L %d %d L %d %d" % (x-6, y-34, x, y-22, x+6, y-34), 0.35, LIGHT))
    return s


def rack(x, y, color=DARK):
    return [line(x-34, y, x-34, y-108, 0.45, color),
            line(x+34, y, x+34, y-108, 0.45, color),
            line(x-40, y-104, x+40, y-104, 0.4, color)]


def cap(x, y, color=INK):
    s = [p("M %d %d Q %d %d %d %d Q %d %d %d %d Z" %
           (x-36, y, x-38, y-26, x, y-34, x+38, y-26, x+36, y), 0.5, color),
         rect(x-30, y, 60, 12, 0.4, color, 2),
         line(x-24, y-4, x+24, y-4, 0.3, LIGHT),
         line(x-18, y-30, x-18, y-8, 0.25, LIGHT),
         line(x+18, y-30, x+18, y-8, 0.25, LIGHT),
         line(x-30, y+2, x-38, y+20, 0.25, LIGHT),
         line(x+30, y+2, x+38, y+20, 0.25, LIGHT)]
    return s


def knee(x, y, color=INK):
    return [rect(x-34, y, 68, 44, 0.45, color, 2),
            p("M %d %d Q %d %d %d %d" % (x-34, y+8, x, y+18, x+34, y+8), 0.3, LIGHT),
            line(x, y, x, y+44, 0.25, LIGHT)]


def f146a():
    s = head("一", "羔裘　服与政", "裘可朝，政不可废", "一百四十六")
    s += rack(150, 392)
    s += robe(150, 360, 92, 118, INK)
    s.append(t(150, 430, "羔裘 · 燕服", 8.0, DARK, "middle"))
    s += rack(300, 392)
    s += robe(300, 360, 92, 118, DARK, True)
    s.append(t(300, 430, "狐裘 · 朝服", 8.0, DARK, "middle"))
    # 堂：两柱一梁
    s.append(line(470, 392, 470, 260, 0.55, DARK))
    s.append(line(610, 392, 610, 260, 0.55, DARK))
    s.append(line(450, 260, 630, 260, 0.6, DARK))
    s.append(p("M 450 260 L 540 210 L 630 260", 0.4, LIGHT))
    s.append(t(540, 300, "在堂", 8.4, DARK, "middle"))
    # 日与曜
    s.append(circ(680, 200, 18, 0.45, RED))
    for ang in range(0, 360, 45):
        s.append(p("M %.0f %.0f L %.0f %.0f" %
                   (680 + 23*math.cos(math.radians(ang)), 200 + 23*math.sin(math.radians(ang)),
                    680 + 30*math.cos(math.radians(ang)), 200 + 30*math.sin(math.radians(ang))), 0.2, RED))
    s += foot("图一 · 羔裘　羔裘逍遥、狐裘在朝、日出有曜", "羔裘逍遥，狐裘以朝。")
    return "".join(s)


def f146b():
    return bfig("一", "羔裘　服其服而不事", "衣可章身，政不可空",
                [("逍遥", "羔裘逍遥；燕服在身，朝事不在心", "燕"),
                 ("在堂", "狐裘在堂；朝服坐堂，政不坐堂", "朝"),
                 ("如膏", "羔裘如膏，日出有曜；服愈亮，政愈空", "曜")],
                "裘可朝，政不可废；服其服而不事，劳心忉忉。", "一百四十六")


def f147a():
    s = head("二", "素冠　三素与棘人", "冠可素，礼不可废", "一百四十七")
    s += rack(150, 330)
    s += cap(150, 300)
    s.append(t(150, 360, "素冠 · 练冠", 8.0, DARK, "middle"))
    s += rack(320, 392)
    s += robe(320, 360, 104, 140, DARK)
    s.append(t(320, 430, "素衣", 8.0, DARK, "middle"))
    s += knee(460, 300)
    s.append(t(460, 360, "素𫖒 · 蔽膝", 8.0, DARK, "middle"))
    # 棘人：瘠瘦剪影，持棘杖
    s += person(600, 392, 150, 26, INK, 0.8)
    s.append(line(568, 300, 550, 392, 0.35, DARK))
    s.append(line(550, 392, 544, 404, 0.25, DARK))
    s.append(line(550, 392, 556, 404, 0.25, DARK))
    s.append(t(600, 430, "棘人 · 栾栾", 8.0, DARK, "middle"))
    s += foot("图一 · 素冠　素冠、素衣、素𫖒、棘人栾栾", "庶见素冠兮，棘人栾栾兮。")
    return "".join(s)


def f147b():
    return bfig("二", "素冠　三年之丧", "礼废则守礼者异",
                [("素冠", "练冠在首；丧服之始", "冠"),
                 ("素衣", "素衣在身；衰裳之次", "衣"),
                 ("素𫖒", "素𫖒在膝；服备礼全", "𫖒")],
                "冠可素，礼不可废；庶见素冠，聊与同归。", "一百四十七")


def changchu(x, y, stage, color=INK):
    s = [line(x, y, x, y-84, 0.5, color)]
    for i in range(3):
        yy = y - 18 - i*20
        s.append(p("M %d %d Q %d %d %d %d" % (x, yy, x-18, yy-14, x-30, yy-4), 0.32, color))
        s.append(p("M %d %d Q %d %d %d %d" % (x, yy, x+18, yy-14, x+30, yy-4), 0.32, color))
    if stage >= 1:
        for dx, dy in ((-8, -78), (6, -86), (16, -72)):
            s.append(circ(x+dx, y+dy, 3, 0.3, RED))
    if stage >= 2:
        for dx, dy in ((-12, -58), (2, -64), (14, -54)):
            s.append(circ(x+dx, y+dy, 4, 0.35, DARK))
            s.append(line(x+dx, y+dy-4, x+dx, y+dy-8, 0.2, LIGHT))
    return s


def f148a():
    s = head("三", "隰有苌楚　枝华实", "草木无知，人独有知", "一百四十八")
    s.append(line(60, 392, 700, 392, 0.35, DARK))
    for y in (360, 376):
        s.append(p("M 70 %d Q 200 %d 340 %d Q 480 %d 620 %d Q 660 %d 700 %d" %
                   (y, y+8, y, y-8, y, y+4, y), 0.3, LIGHT))
    for x, st, lab in ((150, 0, "枝"), (330, 1, "华"), (510, 2, "实")):
        s += changchu(x, 380, st, INK if st < 2 else DARK)
        s.append(t(x, 430, "猗傩其%s" % lab, 8.0, DARK, "middle"))
    s.append(t(650, 300, "隰 · 低湿之地", 8.0, LIGHT, "middle"))
    s += foot("图一 · 隰有苌楚　枝、华、实与隰地", "隰有苌楚，猗傩其枝。")
    return "".join(s)


def f148b():
    return bfig("三", "隰有苌楚　三无", "乐其无，正痛其有",
                [("无知", "枝之柔顺；草木无知识牵挂", "枝"),
                 ("无家", "华之柔顺；草木无家室之累", "华"),
                 ("无室", "实之柔顺；草木无室家之累", "实")],
                "草木无知，人独有知；有知则苦，无家则羡。", "一百四十八")


def f149a():
    s = head("四", "匪风　风车周道", "风可疾，道不可回", "一百四十九")
    # 风：三组疾线
    for y in (200, 230, 260):
        s.append(p("M 70 %d Q 160 %d 250 %d" % (y, y-14, y+6), 0.3, LIGHT))
        s.append(p("M 90 %d Q 170 %d 240 %d" % (y+8, y-8, y+10), 0.22, LIGHT))
    s.append(t(160, 300, "匪风发兮", 8.0, DARK, "middle"))
    # 车：箱、双轮、衡
    s.append(rect(280, 300, 100, 34, 0.5, INK, 2))
    s.append(circ(300, 354, 14, 0.4, INK))
    s.append(circ(360, 354, 14, 0.4, INK))
    s.append(line(280, 316, 230, 306, 0.4, DARK))
    s.append(t(330, 392, "匪车偈兮", 8.0, DARK, "middle"))
    # 周道：透视线
    s.append(p("M 430 392 L 540 250", 0.45, DARK))
    s.append(p("M 540 392 L 620 250", 0.45, DARK))
    s.append(line(540, 250, 620, 250, 0.35, DARK))
    for t0 in (0.3, 0.55, 0.78):
        x1 = 430 + (540-430)*t0; y1 = 392 + (250-392)*t0
        x2 = 540 + (620-540)*t0; y2 = 392 + (250-392)*t0
        s.append(line(x1, y1, x2, y2, 0.25, LIGHT))
    s.append(t(590, 300, "周道", 8.2, DARK, "middle"))
    # 釜鬵与鱼
    s.append(p("M 500 380 Q 500 350 530 346 Q 560 350 560 380 Z", 0.45, INK))
    s.append(line(498, 350, 562, 350, 0.3, DARK))
    s.append(p("M 590 340 Q 570 320 590 300 Q 610 320 590 340 Z", 0.4, DARK))
    s.append(line(590, 340, 590, 356, 0.25, LIGHT))
    for i in range(3):
        s.append(p("M %d 330 Q %d 316 %d 306" % (610+i*10, 618+i*10, 626+i*10), 0.22, LIGHT))
    s += foot("图一 · 匪风　风车周道、釜鬵", "顾瞻周道，中心怛兮。")
    return "".join(s)


def f149b():
    return bfig("四", "匪风　西归好音", "道思寄于家常",
                [("风车", "风发车偈；顾瞻周道，中心怛", "道废"),
                 ("亨鱼", "谁能亨鱼，溉之釜鬵；家常之器", "家"),
                 ("西归", "谁将西归，怀之好音；周京之望", "望")],
                "风可疾，道不可回；西归好音，寄于釜鬵。", "一百四十九")


FIGS = {
 "sj146a-gao-qiu": f146a,
 "sj146b-fu-yu-zheng": f146b,
 "sj147a-su-guan": f147a,
 "sj147b-san-nian": f147b,
 "sj148a-chang-chu": f148a,
 "sj148b-wu-zhi": f148b,
 "sj149a-fei-feng": f149a,
 "sj149b-xi-gui": f149b,
}

for k, fn in FIGS.items():
    body = fn()
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 540" width="760" height="540">\n'
           + body + "\n</svg>\n")
    open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8").write(svg)
    print(k)
