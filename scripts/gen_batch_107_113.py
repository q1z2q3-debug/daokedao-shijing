# -*- coding: utf-8 -*-
"""生成 SJ107–SJ113 魏风七篇图一/图二，共 14 张。
白描，760x540，纸墨五色；人不画脸；活物画不全只画痕迹；红只作结。
写盘键与正文 {{fig:...}} 一致。
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gen_batch_096_106 as B

ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "assets", "fig")
INK = B.INK
RED = B.RED
BROWN = B.BROWN
LINE = B.LINE
PAPER = B.PAPER
GOLD = B.GOLD
t, p, line, circ, rect, person = B.t, B.p, B.line, B.circ, B.rect, B.person


def head(vol, title, sub, zh_no):
    return [
        '<rect width="760" height="540" fill="%s"/>' % PAPER,
        '<rect x="10" y="10" width="740" height="520" fill="none" stroke="%s" stroke-width="0.6"/>' % LINE,
        '<rect x="22" y="28" width="716" height="470" fill="none" stroke="%s" stroke-width="0.8"/>' % LINE,
        t(38, 62, "魏 风 · 之%s" % vol, 9.5, RED, ls=2),
        t(380, 72, title, 25, INK, "middle", "bold", 1.6),
        t(720, 62, "诗三百五篇 · 之%s" % zh_no, 8.6, BROWN, "end", ls=1),
        line(38, 100, 722, 100, 0.35, GOLD),
        t(380, 122, sub, 10.2, BROWN, "middle", ls=1),
    ]


def foot(code, caption, quote=""):
    s = []
    if quote:
        s.append(t(380, 468, quote, 12.4, RED, "middle", ls=0.8))
    s.append(t(380, 506, caption, 9.2, BROWN, "middle", ls=1))
    s.append('<rect x="676" y="492" width="22" height="22" fill="%s" opacity="0.13"/>' % RED)
    s.append(t(687, 507, "润", 8.8, RED, "middle"))
    return s


def fig2(vol, title, sub, rows, conclusion, zh_no, coda=""):
    s = head(vol, title, sub, zh_no)
    n = len(rows)
    ys = {3: (190, 260, 330), 4: (178, 240, 302, 364)}[n]
    for i, row in enumerate(rows):
        y = ys[i]
        s.append(line(44, y + 22, 716, y + 22, 0.3, LINE))
        s.append(t(62, y, row[0], 10.4, INK, "start", "bold"))
        s.append(t(212, y, row[1], 10.8, INK, "start"))
        s.append(t(566, y, row[2], 9.4, BROWN, "start"))
    top = ys[0] - 22
    bot = ys[-1] + 22
    s.append(line(190, top, 190, bot, 0.55, RED))
    s.append(line(190, top, 198, top, 0.4, RED))
    s.append(line(190, bot, 198, bot, 0.4, RED))
    s.append(line(548, top + 8, 548, bot - 8, 0.35, BROWN))
    s.append(line(544, top + 8, 552, top + 8, 0.3, BROWN))
    s.append(line(544, bot - 8, 552, bot - 8, 0.3, BROWN))
    s.append(line(50, 392, 710, 392, 0.35, GOLD))
    s.append(t(380, 418, conclusion, 11.6, RED, "middle", "bold", 0.6))
    if coda:
        s.append(t(380, 442, coda, 8.8, BROWN, "middle", ls=0.3))
    s.append(t(380, 486, "图二 · 义理", 8.6, BROWN, "middle"))
    s.append('<rect x="676" y="492" width="22" height="22" fill="%s" opacity="0.13"/>' % RED)
    s.append(t(687, 507, "润", 8.8, RED, "middle"))
    return s


def shoe(x, y):
    s = []
    # 侧视：鞋底、鞋面、鞋口、编绳
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f L %.0f %.0f L %.0f %.0f Z" %
               (x+2, y+92, x-2, y+84, x+2, y+74, x+14, y+72,
                x+160, y+72, x+160, y+92), 0.55))
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
               (x+16, y+74, x+24, y+30, x+58, y+16, x+94, y+26,
                x+126, y+34, x+146, y+54, x+152, y+74), 0.55))
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
               (x+34, y+46, x+62, y+30, x+104, y+30, x+132, y+48), 0.4, BROWN))
    for i in range(4):
        s.append(line(x+34+i*26, y+46, x+28+i*26, y+76, 0.28, BROWN))
    for i in range(2):
        s.append(line(x+24, y+54+i*12, x+144, y+52+i*12, 0.26, BROWN))
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
               (x+38, y+40, x+44, y+28, x+56, y+28, x+60, y+40), 0.3, RED))
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
               (x+112, y+40, x+118, y+28, x+130, y+28, x+134, y+40), 0.3, RED))
    s.append(t(x+78, y-12, "葛屦", 8.4, BROWN, "middle"))
    return s


def fig107a():
    s = head("一", "葛屦  履霜", "俭在物，褊在心", "一百七")
    s += shoe(78, 250)
    # 女手缝裳
    s.append(rect(400, 250, 130, 130, 0.45))
    s.append(p("M 412 274 L 518 274 L 518 318 L 412 318 Z", 0.3, BROWN))
    s.append(p("M 412 318 L 470 318 L 470 366 L 412 366", 0.3, BROWN))
    s.append(p("M 538 290 C 548 278 560 282 558 296 C 556 310 544 316 536 308", 0.4))
    s.append(p("M 400 300 C 386 316 386 342 398 358", 0.35))
    s.append(line(516, 300, 548, 344, 0.3, BROWN))
    s.append(t(466, 236, "掺掺女手", 8.4, RED, "middle", "bold"))
    s.append(t(466, 404, "缝裳", 7.6, BROWN, "middle"))
    # 象揥
    s.append(p("M 566 206 C 602 198 630 208 636 226", 0.4, BROWN))
    s.append(p("M 566 206 L 548 198 M 636 226 L 644 246", 0.3, BROWN))
    s.append(circ(572, 208, 5, 0.3, RED))
    s.append(t(604, 258, "象揥", 7.8, BROWN, "middle"))
    s += foot("sj107a", "图一 · 葛屦 · 葛屦、女手、象揥", "纠纠葛屦，可以履霜；掺掺女手，可以缝裳。")
    return s


def fig107b():
    return fig2("一", "葛屦  俭与褊", "四者可，一心不可",
                [("葛屦", "可履霜", "物尽其用"),
                 ("女手", "可缝裳", "手尽其能"),
                 ("象揥", "可佩", "礼数不缺"),
                 ("褊心", "不可", "窄处成刺")],
                "履霜可，褊心不可；俭不是德，啬才是刺",
                "一百七", "宽处写物，窄处写心。")


def leafplant(x, y, h, label, color=BROWN, broad=False):
    s = []
    s.append(line(x, y, x-2, y-h, 0.4, color))
    leaves = [(-28, -h*0.35, 24, 9), (24, -h*0.45, 26, 10),
              (-34, -h*0.62, 30, 12), (34, -h*0.70, 30, 12),
              (-18, -h*0.82, 26, 11), (18, -h*0.88, 24, 10)]
    for dx, dy, w, hh in leaves:
        s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f Z" %
                   (x, y+dy, x+dx*0.3, y+dy-hh, x+dx-w*0.3, y+dy-hh, x+dx, y+dy,
                    x+dx+w*0.3, y+dy+hh*0.7, x+dx*0.3, y+dy+hh*0.7, x, y+dy), 0.3, color))
    if broad:
        s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
                   (x-2, y-h, x-12, y-h-10, x-2, y-h-14, x+4, y-h-8), 0.25, color))
    s.append(t(x, y+20, label, 7.8, RED if label == "桑" else color, "middle"))
    return s


def fig108a():
    s = head("二", "汾沮洳  采菜", "美在野，位在朝", "一百八")
    s.append(p("M 48 380 C 160 358 250 372 330 356 C 420 338 540 356 710 332", 0.4, BROWN))
    for i in range(3):
        y0 = 392 + i*10
        s.append(p("M 54 %d C 180 %d 330 %d 520 %d C 590 %d 660 %d 710 %d" %
                   (y0, 372+i*10, 386+i*10, 368+i*10, 360+i*10, 364+i*10, 356+i*10), 0.25, BROWN))
    for x, h, label, broad in ((110, 92, "莫", False), (270, 118, "桑", True), (450, 88, "藚", False)):
        s += leafplant(x, 374, h, label, BROWN, broad)
    s.append(p("M 660 368 C 680 356 704 360 706 384 C 708 402 692 412 674 404", 0.4, BROWN))
    # 采者背影与篮
    s += person(600, 430, 110, 28, INK, 0.85)
    s.append(p("M 612 360 C 632 356 650 370 654 392 C 656 408 642 420 624 418", 0.4, BROWN))
    s.append(t(620, 338, "彼其之子", 7.4, BROWN, "middle"))
    s += foot("sj108a", "图一 · 汾沮洳 · 汾水、采莫、采桑、采藚", "彼其之子，美无度；殊异乎公路。")
    return s


def fig108b():
    return fig2("二", "汾沮洳  美与位", "美者不在位",
                [("美无度", "采莫者", "公路"),
                 ("美如英", "采桑者", "公行"),
                 ("美如玊", "采藚者", "公族"),
                 ("殊异", "远不同", "错位")],
                "美在野，位在朝；美无度，位有度",
                "一百八", "三官三格，与左三美错位；错位一画，刺就出来。")


def peach(x, y, thorn=False):
    s = []
    # 主干
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
               (x, y+116, x-8, y+76, x+4, y+40, x+16, y+4), 0.55))
    branches = [((-30, 44), (24, 18)), ((28, 52), (56, 24)), ((6, 84), (-18, 72)), ((-2, 66), (34, 58))]
    for (dx1, dy1), (dx2, dy2) in branches:
        s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
                   (x+16, y+dy1, x+dx1, y+dy1-8, x+dx2*0.7, y+dy2+6, x+dx2, y+dy2), 0.35, BROWN))
    if thorn:
        for i in range(8):
            bx = x - 34 + i*11
            by = y + 46 + (i%3)*18
            s.append(p("M %.0f %.0f L %.0f %.0f L %.0f %.0f" % (bx, by, bx+4, by-8, bx+8, by), 0.25, BROWN))
        for i in range(5):
            s.append(circ(x-22+i*14, y+34+(i%2)*20, 3.0, 0.3, RED))
    else:
        for i in range(5):
            fx = x - 26 + i*15
            fy = y + 30 + (i%3)*16
            s.append(circ(fx, fy, 4.0, 0.35, RED))
            s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
                       (fx+3, fy-4, fx+12, fy-14, fx+20, fy-10, fx+18, fy-2), 0.25, BROWN))
        for i in range(4):
            lx = x + 20 + (i%2)*20
            ly = y + 56 + i*10
            s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f Z" %
                       (lx, ly, lx+16, ly-8, lx+22, ly+2, lx+8, ly+8), 0.25, BROWN))
    s.append(t(x+8, y+138, "棘" if thorn else "桃", 8.2, BROWN, "middle"))
    return s


def fig109a():
    s = head("三", "园有桃  歌且谣", "物可食，忧不可食", "一百九")
    s.append(rect(44, 250, 210, 180, 0.45))
    s += peach(80, 280, False)
    s.append(rect(496, 250, 210, 180, 0.45))
    s += peach(530, 282, True)
    s += person(390, 438, 118, 28, INK, 0.85)
    s.append(line(390, 330, 390, 380, 0.3, RED))
    s.append(t(390, 246, "歌且谣", 8.2, RED, "middle", "bold"))
    s.append(t(390, 448, "心之忧矣", 7.2, BROWN, "middle"))
    s += foot("sj109a", "图一 · 园有桃 · 桃、棘、歌者、行国", "心之忧矣，我歌且谣。")
    return s


def fig109b():
    return fig2("三", "园有桃  忧与无人知", "桃可食，忧不可食",
                [("园有桃", "实可殽", "物"),
                 ("园有棘", "实可食", "物"),
                 ("心之忧", "歌且谣", "人"),
                 ("其谁知之", "无人知", "空")],
                "桃可食，忧不可食；无人知，才说勿思",
                "一百九", "末格空，反语才落得下。")


def mountain(x, y, h, kind):
    s = []
    s.append(p("M %.0f %.0f L %.0f %.0f L %.0f %.0f L %.0f %.0f" %
               (x, y, x+50, y-h, x+80, y-h+22, x+150, y), 0.55))
    if kind == "hu":
        for i in range(3):
            tx = x+40+i*28
            s.append(line(tx, y-18, tx, y-52, 0.3, BROWN))
            s.append(p("M %.0f %.0f L %.0f %.0f M %.0f %.0f L %.0f %.0f" %
                       (tx, y-44, tx-12, y-54, tx, y-44, tx+10, y-56), 0.25, BROWN))
    elif kind == "gang":
        s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
                   (x+20, y-30, x+44, y-64, x+74, y-52, x+100, y-18), 0.3, BROWN))
    s.append(t(x+75, y+16, {"hu": "岵", "qi": "屺", "gang": "冈"}[kind], 8.0, BROWN, "middle"))
    return s


def fig110a():
    s = head("四", "陟岵  三望", "山可登，亲不可见", "一百十")
    s += mountain(50, 410, 120, "hu")
    s += mountain(280, 410, 140, "qi")
    s += mountain(520, 410, 120, "gang")
    s += person(424, 402, 92, 22, INK, 0.85)
    s.append(line(424, 320, 396, 300, 0.25, BROWN))
    s.append(t(424, 432, "瞻望", 7.4, BROWN, "middle"))
    s += foot("sj110a", "图一 · 陟岵 · 岵、屺、冈、登者", "陟彼岵兮，瞻望父兮。")
    return s


def fig110b():
    return fig2("四", "陟岵  三叮咛", "三叮咛，都是盼归",
                [("父曰", "夙夜无已", "犹来无止"),
                 ("母曰", "夙夜无寐", "犹来无弃"),
                 ("兄曰", "夙夜必偕", "犹来无死")],
                "山可登，亲不可见；三叮咛，都是盼归",
                "一百十", "由止到弃到死，一层重一层。")


def mulberry(x, y):
    s = []
    s.append(line(x, y, x, y-46, 0.4))
    for dx, dy in ((-18, -52), (0, -62), (18, -52)):
        s.append(circ(x+dx, y+dy, 16, 0.3, BROWN))
    s.append(line(x, y-46, x-20, y-60, 0.3, BROWN))
    s.append(line(x, y-46, x+20, y-60, 0.3, BROWN))
    return s


def fig111a():
    s = head("五", "十亩之间  桑者", "桑可采，地不可居", "一百十一")
    s.append(rect(60, 250, 240, 160, 0.45))
    for x in (90, 150, 210, 270):
        s += mulberry(x, 400)
    s += person(380, 420, 104, 26, INK, 0.85)
    s += person(450, 420, 104, 26, BROWN, 0.7)
    s.append(p("M 368 360 L 352 352 M 446 360 L 430 352", 0.3, BROWN))
    s.append(t(410, 236, "行与子还 / 逝", 8.6, RED, "middle", "bold"))
    s += foot("sj111a", "图一 · 十亩之间 · 桑田、桑者、还逝", "十亩之间兮，桑者闲闲兮。")
    return s


def fig111b():
    return fig2("五", "十亩之间  还与逝", "田越小，人越远",
                [("十亩之间", "桑者闲闲", "还"),
                 ("十亩之外", "桑者泄泄", "逝"),
                 ("还", "向内", "归"),
                 ("逝", "向外", "去")],
                "桑可采，地不可居；还与逝，都是退",
                "一百十一", "箭头一出，退意就明。")


def log_and_axe(x, y):
    s = []
    s.append(p("M %.0f %.0f L %.0f %.0f L %.0f %.0f L %.0f %.0f Z" %
               (x, y, x+180, y-8, x+180, y+18, x, y+26), 0.45))
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f Z" %
               (x, y, x-10, y+4, x-10, y+22, x, y+26,
                x+8, y+22, x+8, y+4, x, y), 0.35, BROWN))
    for i in range(5):
        s.append(line(x+22+i*34, y+2, x+22+i*34, y+24, 0.2, BROWN))
    s.append(line(x+150, y-4, x+176, y-44, 0.35, BROWN))
    s.append(p("M %.0f %.0f L %.0f %.0f L %.0f %.0f L %.0f %.0f" %
               (x+170, y-44, x+188, y-56, x+196, y-40, x+178, y-30), 0.4, INK))
    return s


def fig112a():
    s = head("六", "伐檀  河干", "檀可伐，禾不可白取", "一百十二")
    s.append(line(44, 360, 710, 360, 0.35, BROWN))
    for i in range(3):
        y0 = 374 + i*10
        s.append(p("M 48 %d C 160 %d 300 %d 430 %d C 530 %d 620 %d 706 %d" %
                   (y0, 356+i*10, 370+i*10, 352+i*10, 340+i*10, 352+i*10, 344+i*10), 0.25, BROWN))
    s += log_and_axe(80, 280)
    s += person(360, 420, 112, 28, INK, 0.85)
    s.append(line(360, 350, 330, 306, 0.3, BROWN))
    # 庭中
    s.append(rect(530, 230, 170, 150, 0.45))
    s.append(line(540, 270, 690, 270, 0.35, BROWN))
    for x in (560, 610, 660):
        s.append(line(x, 270, x, 290, 0.3, BROWN))
        s.append(p("M %d 290 C %d 282 %d 282 %d 292 C %d 304 %d 310 %d 304 C %d 300 %d 296 %d 290 Z" %
                   (x, x-14, x-10, x, x+10, x+14, x, x-6, x-8, x), 0.3, BROWN))
        for dx in (-5, 5):
            s.append(line(x+dx, 304, x+dx, 318, 0.2, BROWN))
    for x in (550, 600, 650):
        s.append(p("M %d 340 C %d 320 %d 320 %d 340 L %d 380 L %d 380 Z" %
                   (x, x, x+28, x+28, x+28, x), 0.35, BROWN))
    s.append(t(615, 218, "尔庭", 7.4, BROWN, "middle"))
    s += foot("sj112a", "图一 · 伐檀 · 河干、伐木、庭中悬兽", "不稼不穑，胡取禾三百廛兮？")
    return s


def fig112b():
    return fig2("六", "伐檀  劳与素餐", "出力者在河干，取禾者在庭中",
                [("伐檀", "坎坎", "劳"),
                 ("取禾", "三百廛", "不稼"),
                 ("悬兽", "县貆", "不狩"),
                 ("素餐", "无功而食", "反语")],
                "檀可伐，禾不可白取；河水清，庭中赃",
                "一百十二", "末格空而红，反语才站得住。")


def rat(x, y):
    s = []
    # 侧身：身、尖头、双耳、长尾、四足，不画脸
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f Z" %
               (x+18, y+44, x+26, y+22, x+58, y+16, x+86, y+26,
                x+104, y+32, x+118, y+42, x+126, y+52,
                x+112, y+66, x+70, y+70, x+18, y+44), 0.55))
    # 尖头
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f L %.0f %.0f Z" %
               (x+112, y+34, x+124, y+28, x+136, y+32, x+144, y+42, x+124, y+46), 0.45))
    # 耳
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
               (x+108, y+28, x+104, y+16, x+112, y+10, x+118, y+22), 0.3, BROWN))
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
               (x+122, y+24, x+124, y+12, x+132, y+10, x+134, y+22), 0.3, BROWN))
    # 尾
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
               (x+20, y+48, x-4, y+50, x-16, y+32, x-8, y+14,
                x-2, y+2, x+8, y+4, x+6, y+14), 0.35, BROWN))
    for dx in (38, 62, 86):
        s.append(line(x+dx, y+64, x+dx, y+82, 0.3))
    s.append(line(x+144, y+42, x+154, y+48, 0.25, BROWN))
    s.append(t(x+62, y-6, "硕鼠", 8.2, RED, "middle", "bold"))
    return s


def grain(x, y):
    s = []
    for i in range(4):
        s.append(line(x+i*4, y, x+i*4-2, y-46, 0.25, BROWN))
        s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
                   (x+i*4, y-40, x+i*4-8, y-50, x+i*4-6, y-56, x+i*4, y-52), 0.2, BROWN))
    s.append(line(x-4, y-18, x+4, y-22, 0.25, RED))
    s.append(line(x+6, y-28, x+14, y-32, 0.25, RED))
    return s


def fig113a():
    s = head("七", "硕鼠  无食我黍", "鼠可去，土不可寻", "一百十三")
    s += rat(80, 300)
    for x, label in ((280, "黍"), (360, "麦"), (440, "苗")):
        s += grain(x, 390)
        s.append(t(x, 410, label, 7.4, BROWN, "middle"))
    s += person(600, 424, 110, 26, BROWN, 0.8)
    s.append(line(618, 360, 650, 350, 0.25, BROWN))
    s.append(t(620, 340, "去女", 7.6, RED, "middle", "bold"))
    s += foot("sj113a", "图一 · 硕鼠 · 大鼠、黍麦苗、去者", "硕鼠硕鼠，无食我黍。")
    return s


def fig113b():
    return fig2("七", "硕鼠  三岁与乐土", "乐土越唱，号声越真",
                [("三岁贯女", "久侍", "莫我肯顾"),
                 ("逝将去女", "誓去", "适彼乐土"),
                 ("乐土", "想象", "爰得我所"),
                 ("永号", "谁之", "乐土成空")],
                "鼠可去，土不可寻；乐土越唱，号声越真",
                "一百十三", "右格虚，朱线穿出；虚一格，乐土才不成广告。")


FIGS = [("sj107a-ge-ju", fig107a), ("sj107b-jian-bian", fig107b),
        ("sj108a-fen-ju-ru", fig108a), ("sj108b-mei-wei", fig108b),
        ("sj109a-yuan-tao", fig109a), ("sj109b-wu-ren-zhi", fig109b),
        ("sj110a-zhi-hu", fig110a), ("sj110b-san-ding-ning", fig110b),
        ("sj111a-shi-mu", fig111a), ("sj111b-huan-shi", fig111b),
        ("sj112a-fa-tan", fig112a), ("sj112b-su-can", fig112b),
        ("sj113a-shuo-shu", fig113a), ("sj113b-le-tu", fig113b)]


def main():
    os.makedirs(OUT, exist_ok=True)
    for key, fn in FIGS:
        body = fn()
        svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 540" width="760" height="540">\n'
               + "\n".join(body) + "\n</svg>\n")
        path = os.path.join(OUT, key + ".svg")
        open(path, "w", encoding="utf-8").write(svg)
        print("wrote", path, len(svg))


if __name__ == "__main__":
    main()
