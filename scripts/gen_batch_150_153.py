# -*- coding: utf-8 -*-
"""SJ150–SJ153 曹风四篇八图：图一名物，图二义理。760×540，不填面。"""
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
            t(38, 62, "曹 风 · 之%s" % vol, 9.5, RED, ls=2),
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


def mayfly(x, y, s=1.0, color=INK):
    """蜉蝣侧视：身、头、六足、四翅、长尾。"""
    s0 = []
    # 身体
    s0.append(p("M %d %d Q %d %d %d %d Q %d %d %d %d Z" %
                (x, y, x+8*s, y-3*s, x+30*s, y-1*s, x+30*s, y+3*s, x, y+6*s), 0.45, color))
    # 头与复眼
    s0.append(circ(x-5*s, y+1*s, 4*s, 0.35, color))
    s0.append(circ(x-9*s, y, 2.2*s, 0.3, color))
    # 长尾二
    s0.append(p("M %d %d Q %d %d %d %d" % (x+30*s, y+1*s, x+50*s, y-6*s, x+68*s, y+2*s), 0.28, color))
    s0.append(p("M %d %d Q %d %d %d %d" % (x+30*s, y+3*s, x+52*s, y+4*s, x+70*s, y+10*s), 0.24, color))
    # 翅四：上二大，下二小
    s0.append(p("M %d %d Q %d %d %d %d Q %d %d %d %d Z" %
                (x+4*s, y-2*s, x+2*s, y-34*s, x+30*s, y-30*s, x+34*s, y-12*s, x+4*s, y-2*s), 0.4, color))
    s0.append(p("M %d %d Q %d %d %d %d Q %d %d %d %d Z" %
                (x+8*s, y-1*s, x+22*s, y-28*s, x+44*s, y-20*s, x+40*s, y-6*s, x+8*s, y-1*s), 0.35, color))
    s0.append(p("M %d %d Q %d %d %d %d Q %d %d %d %d Z" %
                (x+4*s, y, x+6*s, y+22*s, x+26*s, y+20*s, x+30*s, y+6*s, x+4*s, y), 0.3, color))
    s0.append(p("M %d %d Q %d %d %d %d Q %d %d %d %d Z" %
                (x+10*s, y+2*s, x+24*s, y+16*s, x+42*s, y+14*s, x+36*s, y+5*s, x+10*s, y+2*s), 0.28, color))
    # 六足
    for dx in (2, 10, 20):
        s0.append(line(x+dx*s, y+4*s, x+dx*s-6*s, y+18*s, 0.25, color))
        s0.append(line(x+dx*s+2*s, y+4*s, x+dx*s+8*s, y+18*s, 0.25, color))
    return s0


def grass(x, y, kind="lang", color=INK):
    s = []
    if kind == "lang":  # 稂：童梁，细茎穗
        for dx in (-8, 0, 8):
            s.append(line(x+dx, y, x+dx*1.2, y-40, 0.35, color))
            s.append(p("M %d %d Q %d %d %d %d" % (x+dx*1.2, y-40, x+dx*1.2-5, y-52, x+dx*1.2-2, y-58), 0.3, color))
    elif kind == "xiao":  # 萧：蒿，羽状叶
        s.append(line(x, y, x, y-44, 0.4, color))
        for i in range(3):
            yy = y-16-i*12
            s.append(p("M %d %d Q %d %d %d %d" % (x, yy, x-14, yy-8, x-20, yy+2), 0.28, color))
            s.append(p("M %d %d Q %d %d %d %d" % (x, yy, x+14, yy-8, x+20, yy+2), 0.28, color))
    else:  # 蓍：筮草，细直茎多
        for dx in (-6, -2, 2, 6):
            s.append(line(x+dx, y, x+dx*0.6, y-50, 0.28, color))
            s.append(circ(x+dx*0.6, y-52, 2, 0.25, color))
    return s


def f150a():
    s = head("一", "蜉蝣　羽翼与麻衣", "朝生暮死，衣裳楚楚", "一百五十")
    # 水岸与草
    s.append(line(60, 396, 700, 396, 0.3, LIGHT))
    for i in range(5):
        s.append(line(90+i*130, 396, 90+i*130, 330, 0.3, LIGHT))
    # 三只蜉蝣，由小到大
    s += mayfly(140, 250, 1.6, INK)
    s += mayfly(330, 285, 1.9, INK)
    s += mayfly(490, 320, 2.1, DARK)
    # 麻衣一领：白布衣，用线不用面
    s.append(p("M 626 190 L 646 172 L 656 186 L 666 172 L 686 190 L 672 300 L 640 300 Z", 0.45, DARK))
    s.append(line(646, 186, 656, 214, 0.28, LIGHT))
    s.append(line(666, 186, 656, 214, 0.28, LIGHT))
    s.append(p("M 632 214 L 680 214", 0.25, LIGHT))
    s.append(t(656, 326, "麻衣如雪", 8.4, DARK, "middle"))
    # 注
    s.append(t(140, 214, "羽", 8.0, DARK, "middle"))
    s.append(t(330, 250, "翼", 8.0, DARK, "middle"))
    s.append(t(490, 288, "掘阅", 8.0, DARK, "middle"))
    s += foot("图一 · 蜉蝣　羽、翼、掘阅与麻衣如雪", "蜉蝣之羽，衣裳楚楚。")
    return "".join(s)


def f150b():
    return bfig("一", "蜉蝣　三归一问", "虫愈鲜明，归处愈无",
                [("归处", "羽如衣裳；鲜明在外，归处已空", "羽"),
                 ("归息", "翼如采采；衣服愈众，归息愈少", "翼"),
                 ("归说", "掘阅麻衣；洁白到极，命短到极", "雪")],
                "羽可朝生，国不可暮死；衣裳楚楚，归于何处。", "一百五十")


def f151a():
    s = head("二", "候人　戈祋与赤芾", "劳者在下，贵者在上", "一百五十一")
    # 左：候人（衣身，无脸）一手前伸
    s += person(190, 392, 150, 30, INK, 0.8)
    s.append(line(160, 300, 126, 286, 0.35, INK))
    # 戈：长柄、横刃、尖锋
    s.append(line(112, 430, 112, 236, 0.45, DARK))
    s.append(p("M 112 244 L 86 252 L 90 264 L 112 258", 0.4, DARK))
    s.append(line(86, 252, 74, 248, 0.25, DARK))
    s.append(t(102, 456, "戈", 8.2, DARK, "middle"))
    # 祋：长柄、顶端八棱
    s.append(line(258, 430, 258, 250, 0.42, DARK))
    s.append(p("M 250 250 L 258 240 L 266 250 L 258 260 Z", 0.36, DARK))
    s.append(t(258, 456, "祋", 8.2, DARK, "middle"))
    s.append(t(190, 430, "候人 · 何戈与祋", 8.0, DARK, "middle"))
    # 右：赤芾三领，挂于横架
    s.append(line(360, 270, 660, 270, 0.45, DARK))
    s.append(line(360, 270, 360, 392, 0.35, DARK))
    s.append(line(660, 270, 660, 392, 0.35, DARK))
    for i in range(3):
        x = 386 + i*92
        s.append(rect(x, 282, 64, 66, 0.4, RED, 2))
        s.append(p("M %d 282 L %d 270 L %d 270 L %d 282" % (x, x+8, x+56, x+64), 0.35, RED))
        for dx in (14, 28, 42, 56):
            s.append(line(x+dx, 292, x+dx, 338, 0.22, RED))
        s.append(line(x+6, 306, x+58, 306, 0.25, LIGHT))
    s.append(t(510, 378, "三百赤芾 · 大夫之服", 8.4, DARK, "middle"))
    s.append(t(510, 404, "服在此，德不在", 7.6, LIGHT, "middle"))
    # 朝堂一柱
    s.append(line(700, 392, 700, 230, 0.35, LIGHT))
    s += foot("图一 · 候人　荷戈祋者在下，三百赤芾者在上", "彼候人兮，何戈与祋。")
    return "".join(s)


def f151b():
    return bfig("二", "候人　服不称德", "鹈在梁，不濡翼",
                [("戈祋", "候人荷戈；劳者在下，位不在上", "劳"),
                 ("鹈梁", "鹈在鱼梁；不濡翼咮，尸位不劳", "服"),
                 ("季女", "南山朝𬯀；贤者困于下，斯饥", "饥")],
                "戈祋在肩，赤芾在朝；服不称德，季女斯饥。", "一百五十一")


def dove(x, y, s=1.0, color=INK, chick=False):
    """鸤鸠：侧身鸽形。身椭圆，头圆，短喙，长尾，双足。"""
    b = []
    # 身体（闭合）：背线、腹线
    b.append(p("M %d %d Q %d %d %d %d Q %d %d %d %d Z" %
               (x-20*s, y-4*s, x-10*s, y-16*s, x+6*s, y-14*s,
                x+18*s, y-6*s, x+16*s, y+8*s), 0.45, color))
    # 头
    b.append(circ(x-24*s, y-18*s, 9*s, 0.4, color))
    # 喙：上下两线
    b.append(p("M %d %d L %d %d L %d %d Z" %
               (x-32*s, y-20*s, x-44*s, y-18*s, x-32*s, y-15*s), 0.32, color))
    # 眼
    b.append(circ(x-26*s, y-20*s, 1.7*s, 0.25, color))
    # 颈胸线
    b.append(p("M %d %d Q %d %d %d %d" %
               (x-18*s, y-12*s, x-14*s, y-2*s, x-8*s, y+2*s), 0.3, LIGHT))
    # 翅：内弧 + 羽线三
    b.append(p("M %d %d Q %d %d %d %d" %
               (x-8*s, y-10*s, x+2*s, y-2*s, x+14*s, y+2*s), 0.32, color))
    for i in range(3):
        b.append(p("M %d %d Q %d %d %d %d" %
                   (x-6*s+i*4*s, y-8*s+i*2*s, x+2*s+i*4*s, y-2*s+i*2*s, x+12*s+i*3*s, y+2*s), 0.22, LIGHT))
    # 尾：三根长羽
    for dy in (-2, 2, 6):
        b.append(p("M %d %d L %d %d L %d %d" %
                   (x+14*s, y-2*s+dy*s, x+34*s, y+2*s+dy*s, x+30*s, y-4*s+dy*s), 0.3, color))
    # 足
    b.append(line(x-6*s, y+9*s, x-8*s, y+20*s, 0.28, color))
    b.append(line(x+2*s, y+9*s, x+4*s, y+20*s, 0.28, color))
    b.append(line(x-8*s, y+20*s, x-15*s, y+21*s, 0.22, color))
    b.append(line(x-8*s, y+20*s, x-2*s, y+21*s, 0.22, color))
    b.append(line(x+4*s, y+20*s, x-1*s, y+21*s, 0.22, color))
    b.append(line(x+4*s, y+20*s, x+10*s, y+21*s, 0.22, color))
    if chick:
        # 雏鸟：短身、大头、短尾
        b.append(circ(x-2*s, y-4*s, 4*s, 0.3, color))
    return b


def perch(x1, x2, y):
    s = [line(x1, y, x2, y, 0.4, DARK)]
    for x in (x1+30, x1+90, x1+150, x2-18):
        if x < x2:
            s.append(line(x, y, x-8, y+10, 0.25, DARK))
            s.append(p("M %d %d Q %d %d %d %d Q %d %d %d %d Z" %
                       (x, y, x-8, y-10, x-16, y-4, x-8, y+4, x, y), 0.25, LIGHT))
    return s


def f152a():
    s = head("三", "鸤鸠　桑上七子", "仪一为平，带弁有常", "一百五十二")
    # 左：桑枝一横，母鸠在上
    s.append(p("M 60 380 Q 110 330 120 250", 0.5, DARK))
    s.append(line(100, 330, 300, 300, 0.45, DARK))
    s.append(p("M 100 300 Q 150 286 210 290", 0.35, DARK))
    for x, y in ((160, 288), (230, 294), (280, 300), (130, 320)):
        s.append(p("M %d %d Q %d %d %d %d Q %d %d %d %d Z" %
                   (x, y, x+10, y-14, x+20, y-4, x+12, y+7, x, y), 0.26, LIGHT))
    s += dove(190, 290, 1.7, INK)
    s.append(t(190, 360, "鸤鸠在桑", 8.2, DARK, "middle"))
    # 右：三枝三雏，梅、棘、榛
    for y, lab, x in ((215, "梅", 390), (275, "棘", 480), (335, "榛", 570)):
        s += perch(x-70, x+80, y)
        s += dove(x+20, y, 1.0, DARK, True)
        s.append(t(x+18, y+40, "其子在%s" % lab, 8.0, DARK, "middle"))
    # 带、弁：右上角，避三雏
    s.append(line(610, 180, 710, 180, 0.4, INK))
    s.append(rect(620, 188, 80, 12, 0.35, INK, 2))
    s.append(t(660, 218, "其带伊丝", 7.8, DARK, "middle"))
    s.append(p("M 616 252 Q 660 226 704 252 L 696 292 L 624 292 Z", 0.42, DARK))
    s.append(line(660, 226, 660, 292, 0.25, LIGHT))
    s.append(t(660, 312, "其弁伊骐", 7.8, DARK, "middle"))
    s += foot("图一 · 鸤鸠　桑上育子，带丝弁骐", "鸤鸠在桑，其子七兮。")
    return "".join(s)


def f152b():
    return bfig("三", "鸤鸠　仪一不忒", "所移者子，所不异者仪",
                [("仪一", "桑枝不移；威仪始终如一", "一"),
                 ("心结", "其心固结；带丝弁骐，服有常", "固"),
                 ("正国", "仪不忒；正四国、正国人", "正")],
                "鸠养七子，仪一为平；带丝弁骐，正国在常。", "一百五十二")


def f153a():
    s = head("四", "下泉　寒泉浸苞", "泉冽而苗困，寤叹念京", "一百五十三")
    # 泉源：左上石隙，双弧
    s.append(p("M 60 150 Q 100 132 140 150", 0.45, DARK))
    s.append(p("M 70 164 Q 100 150 130 164", 0.32, DARK))
    s.append(circ(100, 170, 5, 0.3, DARK))
    s.append(t(100, 200, "冽彼下泉", 8.4, DARK, "middle"))
    # 三股下流，折而入池
    for dx in (-16, 0, 16):
        s.append(p("M %d 176 Q %d 240 %d 280 Q %d 320 %d 348" %
                   (100+dx, 112+dx, 100+dx*1.4, 92+dx*2, 100+dx*2.2), 0.3, DARK))
    # 池：椭圆水线
    s.append(p("M 50 356 Q 130 338 210 356 Q 130 374 50 356", 0.38, LIGHT))
    s.append(p("M 70 366 Q 130 352 190 366", 0.25, LIGHT))
    # 三草沿池：稂、萧、蓍
    s += grass(250, 360, "lang", INK)
    s += grass(330, 368, "xiao", INK)
    s += grass(410, 372, "shi", DARK)
    s.append(t(250, 430, "苞稂", 7.8, DARK, "middle"))
    s.append(t(330, 430, "苞萧", 7.8, DARK, "middle"))
    s.append(t(410, 430, "苞蓍", 7.8, DARK, "middle"))
    # 寤叹者：坐于人形低座，一手按胸
    s.append(line(500, 392, 590, 392, 0.4, DARK))
    s += person(545, 392, 118, 20, INK, 0.8)
    s.append(p("M 520 300 Q 545 284 566 300", 0.3, DARK))
    s.append(t(545, 430, "忾我寤叹", 8.2, DARK, "middle"))
    # 周京：城墙、二阙、三门
    s.append(line(640, 330, 720, 330, 0.35, LIGHT))
    s.append(line(640, 330, 640, 286, 0.35, LIGHT))
    s.append(line(720, 330, 720, 286, 0.35, LIGHT))
    for x in (656, 676, 696):
        s.append(rect(x, 300, 8, 30, 0.3, LIGHT, 0))
    s.append(line(640, 286, 720, 286, 0.3, LIGHT))
    s.append(t(680, 354, "念彼周京", 8.0, DARK, "middle"))
    s += foot("图一 · 下泉　寒泉浸稂萧蓍，寤叹念周京", "冽彼下泉，浸彼苞稂。")
    return "".join(s)


def f153b():
    return bfig("四", "下泉　黍苗得雨", "泉寒是政，雨膏是望",
                [("寒泉", "泉冽浸苞；稂萧蓍皆病，民困", "困"),
                 ("念京", "寤叹念周京；思明王贤伯", "望"),
                 ("黍苗", "芃芃黍苗，阴雨膏之；四国有王", "兴")],
                "泉冽而苗困，雨膏而黍兴；念彼京师，思郇伯之劳。", "一百五十三")


FIGS = {
 "sj150a-fu-you": f150a,
 "sj150b-gui-chu": f150b,
 "sj151a-hou-ren": f151a,
 "sj151b-bu-cheng": f151b,
 "sj152a-shi-jiu": f152a,
 "sj152b-yi-yi": f152b,
 "sj153a-xia-quan": f153a,
 "sj153b-xi-bo": f153b,
}

for k, fn in FIGS.items():
    body = fn()
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 540" width="760" height="540">\n'
           + body + "\n</svg>\n")
    open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8").write(svg)
    print(k)
