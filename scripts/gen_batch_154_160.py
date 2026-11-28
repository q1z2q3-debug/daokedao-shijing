# -*- coding: utf-8 -*-
"""SJ154–SJ160 豳风七篇十四图：图一名物，图二义理。760×540，不填面。"""
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
            t(38, 62, "豳 风 · 之%s" % vol, 9.5, RED, ls=2),
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


def robe(x, y, w=96, h=128, color=INK, pattern=False):
    s = [p(f"M {x-w/2+6} {y-92} L {x-10} {y-104} L {x+10} {y-104} L {x+w/2-6} {y-92} L {x+w/2+14} {y-6} L {x+w/2-2} {y+4} L {x+w/2-8} {y} L {x-w/2+8} {y} L {x-w/2+2} {y+4} L {x-w/2-14} {y-6} Z", 0.45, color),
         p(f"M {x-w/2+6} {y-92} Q {x} {y-82} {x+w/2-6} {y-92}", 0.3, LIGHT),
         p(f"M {x-10} {y-104} L {x} {y-74} L {x+10} {y-104}", 0.3, LIGHT),
         line(x-w/2+8, y-42, x+w/2-8, y-42, 0.3, LIGHT),
         line(x, y-74, x, y-4, 0.22, LIGHT),
         p(f"M {x-w/2+6} {y-88} Q {x-w/2-28} {y-74} {x-w/2-22} {y-32} L {x-w/2-4} {y-28} L {x-w/2+10} {y-70} Z", 0.4, color),
         p(f"M {x+w/2-6} {y-88} Q {x+w/2+28} {y-74} {x+w/2+22} {y-32} L {x+w/2+4} {y-28} L {x+w/2-10} {y-70} Z", 0.4, color),
         line(x-w/2-22, y-32, x-w/2-4, y-28, 0.22, LIGHT),
         line(x+w/2+22, y-32, x+w/2+4, y-28, 0.22, LIGHT)]
    if pattern:
        for i in range(3):
            s.append(line(x-w/2+6, y-4-i*4, x+w/2-6, y-4-i*4, 0.2, LIGHT))
    return s


def si(x, y, s=1.0):
    """耒耜：柄、刃、足。"""
    return [line(x, y-104*s, x, y-12*s, 0.5, INK),
            p(f"M {x-14*s} {y-12*s} L {x-8*s} {y+18*s} L {x+8*s} {y+18*s} L {x+14*s} {y-12*s} Z", 0.4, INK),
            line(x-14*s, y-16*s, x+14*s, y-16*s, 0.3, DARK),
            line(x, y-12*s, x, y+16*s, 0.25, LIGHT),
            line(x-10*s, y+8*s, x-20*s, y+10*s, 0.25, DARK)]


def star(x, y, r=4):
    return [circ(x, y, r, 0.4, INK),
            line(x-r-4, y, x-r-1, y, 0.2, INK), line(x+r+1, y, x+r+4, y, 0.2, INK),
            line(x, y-r-4, x, y-r-1, 0.2, INK), line(x, y+r+1, x, y+r+4, 0.2, INK)]


def owl(x, y, s=1.0):
    """鸱鸮剪影：身、头、耳羽、翅、爪，不画眼。"""
    return [p(f"M {x-20*s} {y-10*s} Q {x-30*s} {y-34*s} {x-6*s} {y-40*s} Q {x+14*s} {y-36*s} {x+18*s} {y-12*s} Q {x+16*s} {y+12*s} {x-8*s} {y+14*s} Q {x-20*s} {y+6*s} {x-20*s} {y-10*s} Z", 0.45, INK),
            p(f"M {x-18*s} {y-34*s} L {x-24*s} {y-48*s} L {x-10*s} {y-40*s}", 0.35, INK),
            p(f"M {x-2*s} {y-38*s} L {x+4*s} {y-52*s} L {x+10*s} {y-38*s}", 0.35, INK),
            p(f"M {x-14*s} {y-24*s} Q {x-2*s} {y-14*s} {x+8*s} {y-6*s}", 0.25, DARK),
            line(x-8*s, y+14*s, x-12*s, y+24*s, 0.28, INK), line(x-12*s, y+24*s, x-18*s, y+25*s, 0.2, INK),
            line(x-12*s, y+24*s, x-6*s, y+25*s, 0.2, INK),
            line(x+4*s, y+14*s, x+6*s, y+24*s, 0.28, INK), line(x+6*s, y+24*s, x, y+25*s, 0.2, INK),
            line(x+6*s, y+24*s, x+12*s, y+25*s, 0.2, INK)]


def nest(x, y, s=1.0):
    return [p(f"M {x-42*s} {y} Q {x-46*s} {y+30*s} {x} {y+34*s} Q {x+46*s} {y+30*s} {x+42*s} {y} Z", 0.45, DARK),
            p(f"M {x-38*s} {y} Q {x} {y+14*s} {x+38*s} {y}", 0.3, LIGHT),
            p(f"M {x-34*s} {y+10*s} Q {x} {y+24*s} {x+34*s} {y+10*s}", 0.25, LIGHT)]


def eggs(x, y, s=1.0):
    e = []
    for dx in (-16, 0, 16):
        e.append(p(f"M {x+dx*s} {y} Q {x+dx*s-10*s} {y-14*s} {x+dx*s} {y-20*s} Q {x+dx*s+10*s} {y-14*s} {x+dx*s} {y} Z", 0.3, LIGHT))
    return e


def fish(x, y, s=1.0, color=INK):
    return [p(f"M {x-26*s} {y} Q {x} {y-12*s} {x+26*s} {y} Q {x} {y+12*s} {x-26*s} {y} Z", 0.4, color),
            p(f"M {x-26*s} {y} L {x-38*s} {y-10*s} L {x-36*s} {y} L {x-38*s} {y+10*s} Z", 0.3, color),
            circ(x+12*s, y-2*s, 1.8*s, 0.25, color),
            p(f"M {x-8*s} {y-8*s} Q {x} {y} {x-8*s} {y+8*s}", 0.22, LIGHT)]


def axe(x, y, kind="fu", s=1.0, broken=False):
    """斧类：长柄，宽刃；斨方孔，銶圆刃。"""
    s0 = [line(x, y, x, y-112*s, 0.45, INK),
          line(x-6*s, y-104*s, x+6*s, y-104*s, 0.3, DARK)]
    if kind == "fu":
        s0 += [p(f"M {x} {y-112*s} L {x-44*s} {y-120*s} L {x-52*s} {y-86*s} L {x-14*s} {y-80*s} L {x} {y-92*s} Z", 0.45, INK),
               p(f"M {x-44*s} {y-120*s} Q {x-56*s} {y-104*s} {x-52*s} {y-86*s}", 0.35, INK),
               p(f"M {x-16*s} {y-82*s} Q {x-8*s} {y-86*s} {x} {y-92*s}", 0.25, LIGHT)]
    elif kind == "qiang":
        s0 += [rect(x-50*s, y-124*s, 48*s, 38*s, 0.45, INK, 2),
               rect(x-30*s, y-114*s, 12*s, 12*s, 0.25, LIGHT, 2),
               line(x-50*s, y-106*s, x-2*s, y-106*s, 0.2, LIGHT)]
    else:
        s0 += [p(f"M {x} {y-112*s} Q {x-34*s} {y-132*s} {x-50*s} {y-104*s} Q {x-46*s} {y-80*s} {x-8*s} {y-84*s} L {x} {y-96*s} Z", 0.45, INK),
               p(f"M {x-48*s} {y-104*s} Q {x-38*s} {y-94*s} {x-12*s} {y-94*s}", 0.25, LIGHT)]
    if broken:
        s0.append(p(f"M {x-30*s} {y-108*s} L {x-40*s} {y-96*s} L {x-32*s} {y-100*s} L {x-38*s} {y-88*s}", 0.3, RED))
    return s0


def shoe(x, y, s=1.0):
    return [p(f"M {x-30*s} {y} Q {x-36*s} {y-16*s} {x-18*s} {y-18*s} L {x+8*s} {y-16*s} Q {x+26*s} {y-12*s} {x+30*s} {y} Z", 0.42, INK),
            p(f"M {x-30*s} {y} L {x+30*s} {y} L {x+26*s} {y+8*s} L {x-26*s} {y+8*s} Z", 0.3, RED),
            p(f"M {x-16*s} {y-16*s} Q {x-8*s} {y-28*s} {x+4*s} {y-18*s}", 0.3, DARK),
            line(x-20*s, y-2*s, x+20*s, y-2*s, 0.2, LIGHT)]


def wolf(x, y, s=1.0):
    """狼：侧身，长吻、竖耳、蓬尾、四足，不画眼。"""
    return [p(f"M {x-26*s} {y-10*s} Q {x-10*s} {y-28*s} {x+18*s} {y-20*s} Q {x+34*s} {y-10*s} {x+26*s} {y+8*s} L {x-18*s} {y+8*s} Q {x-28*s} {y+2*s} {x-26*s} {y-10*s} Z", 0.45, INK),
            circ(x-34*s, y-18*s, 12*s, 0.42, INK),
            p(f"M {x-40*s} {y-24*s} L {x-64*s} {y-18*s} L {x-42*s} {y-12*s} Z", 0.4, INK),
            p(f"M {x-42*s} {y-28*s} L {x-46*s} {y-44*s} L {x-34*s} {y-30*s} Z", 0.32, INK),
            p(f"M {x-32*s} {y-30*s} L {x-28*s} {y-46*s} L {x-24*s} {y-30*s} Z", 0.32, INK),
            p(f"M {x+24*s} {y-12*s} Q {x+46*s} {y-26*s} {x+54*s} {y-6*s} Q {x+46*s} {y+4*s} {x+28*s} {y+2*s}", 0.38, INK),
            p(f"M {x+28*s} {y-8*s} Q {x+46*s} {y-16*s} {x+50*s} {y-4*s}", 0.25, LIGHT),
            line(x-16*s, y+6*s, x-20*s, y+30*s, 0.3, INK), line(x+2*s, y+8*s, x+2*s, y+31*s, 0.3, INK),
            line(x+18*s, y+6*s, x+20*s, y+30*s, 0.3, INK), line(x+26*s, y+2*s, x+32*s, y+28*s, 0.3, INK),
            line(x-20*s, y+30*s, x-26*s, y+31*s, 0.2, INK), line(x+2*s, y+31*s, x-4*s, y+32*s, 0.2, INK),
            line(x+20*s, y+30*s, x+14*s, y+31*s, 0.2, INK), line(x+32*s, y+28*s, x+38*s, y+29*s, 0.2, INK)]


def f154a():
    s = head("一", "七月　流火授衣", "火可流，衣不可废", "一百五十四")
    # 大火星
    s += star(130, 190, 5)
    s += star(160, 170, 3)
    s += star(165, 210, 3)
    s.append(line(130, 190, 160, 170, 0.25, DARK))
    s.append(line(130, 190, 165, 210, 0.25, DARK))
    s.append(t(150, 240, "七月流火", 8.4, DARK, "middle"))
    # 衣
    s += robe(330, 390, 96, 136, INK)
    s.append(t(330, 430, "九月授衣", 8.2, DARK, "middle"))
    # 耜
    s += si(500, 390, 1.0)
    s.append(t(500, 430, "三之日于耜", 8.2, DARK, "middle"))
    # 足迹与田
    s.append(line(80, 408, 700, 408, 0.3, LIGHT))
    for i in range(2):
        for dx in (0, 18):
            s.append(p(f"M {610+i*36+dx} 400 Q {614+i*36+dx} 386 {622+i*36+dx} 400 Q {618+i*36+dx} 394 {610+i*36+dx} 400 Z", 0.25, DARK))
    s.append(t(640, 430, "四之日举趾", 8.2, DARK, "middle"))
    s += foot("图一 · 七月　流火、授衣、于耜、举趾", "七月流火，九月授衣。")
    return "".join(s)


def f154b():
    return bfig("一", "七月　一岁之勤", "天时有常，人事有节",
                [("流火", "大火西流；七月授衣，先民之寒", "时"),
                 ("于耜", "正月修耒，二月举趾；同我妇子", "勤"),
                 ("改岁", "穹窒熏鼠，塞向墐户；入此室处", "岁")],
                "火可流，衣不可废；一岁之勤，成于授衣。", "一百五十四")


def f155a():
    s = head("二", "鸱鸮　取子与护巢", "巢可危，室不可毁", "一百五十五")
    # 枝与巢
    s.append(p("M 40 410 Q 180 360 420 330", 0.45, DARK))
    s += nest(310, 324, 1.0)
    s += eggs(310, 330, 1.0)
    s.append(t(310, 392, "既取我子，无毁我室", 8.0, DARK, "middle"))
    # 鸱鸮
    s += owl(130, 300, 1.6)
    s.append(t(130, 360, "鸱鸮", 8.2, DARK, "middle"))
    # 桑土与根
    s.append(line(500, 420, 500, 300, 0.4, DARK))
    for i in range(3):
        s.append(p(f"M 500 400 Q {470-i*8} {430-i*6} {460-i*10} 450", 0.25, DARK))
        s.append(p(f"M 500 400 Q {530+i*8} {430-i*6} {540+i*10} 450", 0.25, DARK))
    s.append(t(510, 370, "彻彼桑土", 8.0, DARK, "middle"))
    # 牖户：窗格
    s.append(rect(610, 260, 80, 72, 0.4, DARK, 2))
    s.append(line(650, 260, 650, 332, 0.25, LIGHT))
    s.append(line(610, 296, 690, 296, 0.25, LIGHT))
    s.append(t(650, 360, "绸缪牖户", 8.0, DARK, "middle"))
    s += foot("图一 · 鸱鸮　取子毁室，桑土补巢", "鸱鸮鸱鸮！既取我子，无毁我室。")
    return "".join(s)


def f155b():
    return bfig("二", "鸱鸮　未雨绸缪", "取子者在外，护巢者在内",
                [("取子", "鸱鸮取子；外患已至，室将毁", "危"),
                 ("绸缪", "彻桑土、补牖户；未阴雨而备", "防"),
                 ("哓哓", "羽敝尾翛，室翘翘；音惧而志不变", "守")],
                "巢可危，室不可毁；未雨绸缪，音哓哓而志不变。", "一百五十五")


def f156a():
    s = head("三", "东山　零雨其濛", "雨可濛，归不可迟", "一百五十六")
    # 雨
    for i in range(10):
        x = 60 + i*28
        s.append(line(x, 150, x-14, 210, 0.22, LIGHT))
    # 山
    s.append(p("M 80 400 L 170 250 L 260 400", 0.45, DARK))
    s.append(p("M 170 250 L 210 320 L 240 280", 0.3, LIGHT))
    # 归士：衣身、背囊
    s += person(330, 400, 150, 28, INK, 0.8)
    s.append(rect(302, 292, 40, 52, 0.35, DARK, 2))
    s.append(t(330, 440, "我来自东", 8.0, DARK, "middle"))
    # 车下独宿
    s.append(circ(450, 360, 22, 0.4, DARK))
    s.append(line(450, 338, 450, 382, 0.25, LIGHT))
    s.append(line(428, 360, 472, 360, 0.25, LIGHT))
    s.append(t(450, 410, "亦在车下", 7.8, DARK, "middle"))
    # 蠋在桑野
    s.append(p("M 540 300 Q 610 260 680 300", 0.4, DARK))
    for i in range(4):
        s.append(p(f"M {560+i*28} 294 Q {570+i*28} 270 {580+i*28} 294", 0.25, LIGHT))
    s.append(p("M 600 286 Q 610 276 620 286 Q 630 296 640 286", 0.3, DARK))
    s.append(t(610, 330, "蜎蜎者蠋", 7.8, DARK, "middle"))
    s += foot("图一 · 东山　零雨、归士、车下、桑蠋", "我徂东山，慆慆不归。")
    return "".join(s)


def f156b():
    return bfig("二", "东山　其旧如之何", "身归而心未归",
                [("徂东", "三年不归；归途遇雨，心西悲", "远"),
                 ("零雨", "零雨其濛；家园荒，鹿场宵行", "荒"),
                 ("其旧", "新婚孔嘉；以新问旧，不敢问", "痛")],
                "雨可濛，归不可迟；三年之戍，一朝之悲。", "一百五十六")


def f157a():
    s = head("四", "破斧　三器皆缺", "器破而国正", "一百五十七")
    s += axe(180, 400, "fu", 1.6, broken=True)
    s.append(t(180, 440, "斧 · 破", 8.2, DARK, "middle"))
    s += axe(370, 400, "qiang", 1.6, broken=True)
    s.append(t(370, 440, "斨 · 缺", 8.2, DARK, "middle"))
    s += axe(560, 400, "qiu", 1.6, broken=True)
    s.append(t(560, 440, "銶 · 缺", 8.2, DARK, "middle"))
    s.append(t(390, 250, "四国是皇", 8.2, DARK, "middle"))
    s += foot("图一 · 破斧　斧斨锜銶皆缺，四国归正", "既破我斧，又缺我斨。")
    return "".join(s)


def f157b():
    return bfig("四", "破斧　器破国正", "胜之义在安不在杀",
                [("破斧", "三器皆缺；役久兵疲", "器"),
                 ("四国", "管蔡商奄；皇、吪、遒，皆归正", "国"),
                 ("哀民", "哀我人斯；亦孔之将、嘉、休", "民")],
                "斧可破，四国不可乱；哀我人斯，亦孔之休。", "一百五十七")


def f158a():
    s = head("五", "伐柯　斧与笾豆", "柯可伐，则不可远", "一百五十八")
    s += axe(180, 400, "fu", 1.7)
    s.append(t(180, 442, "伐柯之斧", 8.2, DARK, "middle"))
    # 笾豆：二器
    for x, kind in ((410, "bian"), (560, "dou")):
        if kind == "bian":
            s.append(p(f"M {x-38} 330 L {x+38} 330 L {x+28} 372 L {x-28} 372 Z", 0.4, DARK))
            s.append(line(x-28, 348, x+28, 348, 0.25, LIGHT))
            s.append(line(x-20, 330, x-20, 300, 0.25, DARK))
            s.append(line(x+20, 330, x+20, 300, 0.25, DARK))
            s.append(t(x, 420, "笾", 8.0, DARK, "middle"))
        else:
            s.append(p(f"M {x-30} 300 Q {x} 282 {x+30} 300 L {x+24} 336 Q {x} 348 {x-24} 336 Z", 0.4, DARK))
            s.append(line(x, 348, x, 384, 0.35, DARK))
            s.append(p(f"M {x-22} 384 L {x+22} 384", 0.3, DARK))
            s.append(t(x, 420, "豆", 8.0, DARK, "middle"))
    s.append(t(485, 270, "笾豆有践", 8.4, DARK, "middle"))
    # 媒：简化为二姓牌
    s.append(rect(300, 210, 50, 36, 0.3, LIGHT, 2))
    s.append(rect(360, 210, 50, 36, 0.3, LIGHT, 2))
    s.append(t(355, 196, "匪媒不得", 7.6, DARK, "middle"))
    s += foot("图一 · 伐柯　匪斧不克，匪媒不得，笾豆有践", "伐柯如何？匪斧不克。")
    return "".join(s)


def f158b():
    return bfig("五", "伐柯　其则不远", "礼有则，则不在远",
                [("伐柯", "砍斧柄必以斧；器与事相须", "器"),
                 ("取妻", "娶妻必以媒；礼与人相须", "礼"),
                 ("笾豆", "我觏之子，笾豆有践；礼在眼前", "则")],
                "柯可伐，则不可远；笾豆有践，礼在眼前。", "一百五十八")


def f159a():
    s = head("六", "九罭　细网得鱼", "网可小，鱼不可失", "一百五十九")
    # 网：菱形网格
    s.append(p("M 80 200 L 300 170 L 340 360 L 120 390 Z", 0.45, DARK))
    for i in range(1, 5):
        s.append(line(80+i*44, 200-i*6, 120+i*44, 390-i*6, 0.25, LIGHT))
        s.append(line(80+i*42, 390-i*6, 120+i*42, 200-i*6, 0.25, LIGHT))
    s += fish(190, 290, 1.1, INK)
    s += fish(250, 330, 0.9, INK)
    s.append(t(210, 420, "九罭之鱼，鳟鲂", 8.2, DARK, "middle"))
    # 衮衣
    s += robe(540, 390, 130, 160, DARK, True)
    s.append(t(540, 440, "衮衣绣裳", 8.2, DARK, "middle"))
    s += foot("图一 · 九罭　细网得鳟鲂，衮衣绣裳", "九罭之鱼，鳟鲂。")
    return "".join(s)


def f159b():
    return bfig("六", "九罭　公不可归", "小网得大鱼，贤者将去",
                [("九罭", "细网得鳟鲂；得贤如得鱼", "得"),
                 ("鸿飞", "遵渚、遵陆；公归无所、不复", "归"),
                 ("衮衣", "留其衣，留不住其人；心悲", "留")],
                "网可小，鱼不可失；衮衣在，公不可归。", "一百五十九")


def f160a():
    s = head("七", "狼跋　跋胡疐尾", "狼可跋，德不可瑕", "一百六十")
    s += wolf(240, 320, 1.5)
    s.append(t(240, 420, "狼跋其胡，载疐其尾", 8.0, DARK, "middle"))
    # 赤舄
    s += shoe(540, 380, 1.6)
    s.append(t(540, 430, "赤舄几几", 8.2, DARK, "middle"))
    # 德音：磬一
    s.append(p("M 640 220 L 700 220 L 690 260 L 650 260 Z", 0.35, LIGHT))
    s.append(line(670, 220, 670, 190, 0.25, LIGHT))
    s.append(t(670, 290, "德音不瑕", 8.0, DARK, "middle"))
    s += foot("图一 · 狼跋　狼跋胡疐尾，公孙赤舄几几", "狼跋其胡，载疐其尾。")
    return "".join(s)


def f160b():
    return bfig("七", "狼跋　德音不瑕", "处困而安，困愈深德愈全",
                [("跋胡", "狼进则踩胡；进退皆碍", "困"),
                 ("疐尾", "狼退则绊尾；反复受阻", "困"),
                 ("不瑕", "公孙硕肤，赤舄几几；德音无疵", "德")],
                "狼可跋，德不可瑕；赤舄几几，处困而安。", "一百六十")


FIGS = {
 "sj154a-liu-huo": f154a,
 "sj154b-sui-gong": f154b,
 "sj155a-chi-xiao": f155a,
 "sj155b-wei-yu": f155b,
 "sj156a-dong-shan": f156a,
 "sj156b-ru-he": f156b,
 "sj157a-po-fu": f157a,
 "sj157b-si-guo": f157b,
 "sj158a-fa-ke": f158a,
 "sj158b-ze-bu-yuan": f158b,
 "sj159a-jiu-yu": f159a,
 "sj159b-gong-gui": f159b,
 "sj160a-lang-ba": f160a,
 "sj160b-de-yin": f160b,
}

for k, fn in FIGS.items():
    body = fn()
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 540" width="760" height="540">\n'
           + body + "\n</svg>\n")
    open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8").write(svg)
    print(k)
