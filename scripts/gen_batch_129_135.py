# -*- coding: utf-8 -*-
"""SJ129–SJ135 秦风十四图：图一名物，图二义理。760×540，不填面。"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
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


def bfig(vol, title, sub, rows, conclusion, zh_no):
    s = headq(vol, title, sub, zh_no, True)
    n = len(rows)
    ys = {2: (210, 300), 3: (190, 260, 330), 4: (178, 240, 302, 364)}[n]
    for i, row in enumerate(rows):
        y = ys[i]
        s.append(line(44, y + 22, 716, y + 22, 0.3, ZMID))
        s.append(t(62, y, row[0], 10.4, ZINK, "start", "bold"))
        s.append(t(226, y, row[1], 10.8, ZINK, "start"))
        s.append(t(566, y, row[2], 9.4, ZMID, "start"))
    s.append(line(204, ys[0]-22, 204, ys[-1]+22, 0.55, RED))
    s.append(line(50, 392, 710, 392, 0.35, GOLD))
    s.append(t(380, 418, conclusion, 11.6, RED, "middle", "bold", 0.6))
    s.append(t(380, 486, "图二 · 义理", 8.6, ZMID, "middle"))
    s.append('<rect x="676" y="492" width="22" height="22" fill="%s" opacity="0.13"/>' % SEAL)
    s.append(t(687, 507, "润", 8.8, SEAL, "middle"))
    return "".join(s)


def reed(x, y, h=110, color=INK):
    s = [line(x, y, x, y-h, 0.5, color)]
    for i in range(4):
        yy = y - 14 - i*20
        s.append(p("M %d %d Q %d %d %d %d" % (x, yy, x-18, yy-18, x-34, yy-8), 0.35, color))
        s.append(p("M %d %d Q %d %d %d %d" % (x, yy, x+18, yy-18, x+34, yy-8), 0.35, color))
    s.append(p("M %d %d L %d %d" % (x, y-h, x+2, y-h-14), 0.45, RED))
    return s


def wave(x, y, w=180, color=LIGHT):
    return [p(f"M {x} {y} Q {x+w//4} {y-10} {x+w//2} {y} Q {x+3*w//4} {y+10} {x+w} {y}", 0.35, color)]


def tree(x, y, h=80, color=INK, fruit=False):
    s = [line(x, y, x, y-h*0.5, 0.55, color),
         p("M %d %d Q %d %d %d %d Q %d %d %d %d Q %d %d %d %d Z" %
           (x-22, y-h*0.5, x-30, y-h*0.8, x-14, y-h, x, y-h-10,
            x+16, y-h, x+30, y-h*0.8, x+22, y-h*0.5), 0.4, color)]
    if fruit:
        for dx, dy in [(-10,-h+10),(4,-h+2),(14,-h+12)]:
            s.append(circ(x+dx, y+dy, 2, 0.5, RED))
    return s


def f129a():
    s = headq("四", "蒹葭　秋水白露", "可望不可即", "一百二十九")
    for x in (70, 102, 134, 166, 198, 230):
        s += reed(x, 392, 112 if x % 3 else 96, INK if x < 180 else DARK)
    for y in (330, 362, 392):
        s += wave(250, y, 440, LIGHT)
    s.append(line(620, 300, 620, 392, 0.45, DARK))
    s += person(640, 330, 86, 24, LIGHT, 0.7)
    for x, y in [(300, 210), (350, 190), (410, 220)]:
        s.append(circ(x, y, 2.4, 0.5, LIGHT))
    s += foot("图一 · 蒹葭　芦苇、白露、水岸", "所谓伊人，在水一方")
    return "".join(s)


def f130a():
    s = headq("五", "终南　山产与礼服", "山有常产，服有常制", "一百三十")
    s.append(p("M 60 392 L 180 210 L 300 392", 0.6, INK))
    s.append(p("M 220 392 L 360 180 L 500 392", 0.55, DARK))
    s.append(p("M 410 392 L 540 240 L 680 392", 0.5, LIGHT))
    s += tree(180, 360, 82, DARK, True)
    s += tree(540, 360, 76, LIGHT, True)
    s.append(rect(250, 330, 90, 62, 0.55, INK, 2))
    s.append(line(250, 350, 340, 350, 0.35, LIGHT))
    s += person(470, 392, 96, 28)
    s.append(p("M 452 330 L 488 330 L 496 382 L 444 382 Z", 0.45, DARK))
    s += foot("图一 · 终南　山、条梅、锦衣狐裘", "颜如渥丹，其君也哉")
    return "".join(s)


def f131a():
    s = headq("六", "黄鸟　三良临穴", "鸟可栖，人不可殉", "一百三十一")
    for x, col in [(120, INK), (220, DARK), (320, LIGHT)]:
        s += tree(x, 392, 86, col)
    s.append(p("M 110 210 Q 128 192 146 210 Q 128 224 110 210 Z", 0.45, INK))
    s.append(line(128, 210, 120, 196, 0.35, INK)); s.append(line(128, 210, 136, 196, 0.35, INK))
    s.append(rect(430, 300, 220, 92, 0.6, INK, 2))
    for x in (470, 540, 610):
        s += person(x, 300, 70, 20, DARK)
    s.append(line(430, 340, 650, 340, 0.3, LIGHT))
    s += foot("图一 · 黄鸟　黄鸟止棘、三良、墓穴", "临其穴，惴惴其栗")
    return "".join(s)


def f132a():
    s = headq("七", "晨风　鹯飞北林", "鸟有林，人无归", "一百三十二")
    s.append(p("M 120 210 L 160 196 L 196 206 L 178 224 L 140 226 Z", 0.5, INK))
    s.append(line(178, 210, 204, 198, 0.35, INK))
    for x in (90, 130, 170, 210, 250):
        s.append(line(x, 392, x, 240, 0.35, LIGHT))
    s.append(p("M 60 392 L 250 392 L 210 250 L 100 250 Z", 0.3, LIGHT))
    s += tree(400, 392, 80, DARK, True)
    s.append(p("M 560 392 L 590 356 L 640 360 L 660 392 Z", 0.45, DARK))
    s.append(line(584, 372, 584, 392, 0.4, DARK)); s.append(line(636, 372, 636, 392, 0.4, DARK))
    s += foot("图一 · 晨风　鹯飞北林、苞栎、六驳", "未见君子，忧心钦钦")
    return "".join(s)


def f133a():
    s = headq("八", "无衣　袍泽裳与三兵", "衣可共，同不可假", "一百三十三")
    for i, x in enumerate((90, 190, 290)):
        s.append(p("M %d 260 L %d 250 L %d 380 L %d 380 Z" % (x, x+54, x+64, x-10), 0.5, INK if i < 2 else DARK))
        s.append(line(x+6, 270, x+46, 270, 0.3, LIGHT))
    s.append(line(470, 392, 470, 210, 0.55, DARK))
    s.append(p("M 470 210 L 482 188 L 494 210 Z", 0.5, DARK))
    s.append(line(510, 392, 510, 220, 0.55, DARK))
    s.append(p("M 510 220 L 522 198 L 534 220 Z", 0.5, DARK))
    s.append(rect(570, 270, 70, 80, 0.5, INK, 2))
    s.append(line(570, 300, 640, 300, 0.35, LIGHT))
    s += foot("图一 · 无衣　袍泽裳、戈矛甲兵", "岂曰无衣，与子同袍")
    return "".join(s)


def f134a():
    s = headq("九", "渭阳　渭水车马", "渭可渡，思不可渡", "一百三十四")
    for y in (330, 362, 392):
        s += wave(60, y, 420, LIGHT)
    s.append(rect(250, 330, 100, 34, 0.55, INK, 2))
    s.append(circ(274, 380, 12, 0.45, INK)); s.append(circ(326, 380, 12, 0.45, INK))
    for x in (152, 172, 192, 212):
        s.append(p("M %d 310 L %d 300 L %d 310 L %d 340 L %d 340 Z" % (x, x+12, x+24, x+22, x), 0.45, DARK))
    s.append(circ(600, 290, 34, 0.55, RED)); s.append(circ(600, 290, 22, 0.35, RED))
    s += foot("图一 · 渭阳　渭水、路车、乘黄", "何以赠之，琼瑰玉佩")
    return "".join(s)


def f135a():
    s = headq("十", "权舆　夏屋四簋", "屋可大，食不可薄", "一百三十五")
    s.append(line(120, 392, 120, 250, 0.55, INK)); s.append(line(340, 392, 340, 250, 0.55, INK))
    s.append(line(100, 250, 360, 250, 0.6, INK))
    s.append(line(120, 250, 230, 180, 0.45, DARK)); s.append(line(340, 250, 230, 180, 0.45, DARK))
    for x in (470, 520, 570, 620):
        s.append(p("M %d 360 Q %d 392 %d 360 Q %d 330 %d 360 Z" % (x, x+16, x+32, x+16, x), 0.45, INK))
    s.append(p("M 470 410 Q 486 438 502 410 Q 486 384 470 410 Z", 0.35, LIGHT))
    s += foot("图一 · 权舆　夏屋、四簋、今食无余", "于嗟乎，不承权舆")
    return "".join(s)


FIGS = {
 "sj129a-jian-jia": f129a,
 "sj129b-san-jing": lambda: bfig("四", "蒹葭　三候·三涯·三求", "白露三变，伊人常在中央",
   [("苍苍","白露为霜，在水一方；逆流路长","始求"),("凄凄","白露未晞，在水之湄；逆流路跻","再求"),("采采","白露未已，在水之涘；逆流路右","三求")],
   "水可溯，人不可即；白露三变，伊人常在中央。", "一百二十九"),
 "sj130a-zhong-nan": f130a,
 "sj130b-fu-de": lambda: bfig("五", "终南　山产·服制·寿考", "山有常产，服有常制",
   [("山产","有条有梅，有纪有堂；地有所出","地"),("服制","锦衣狐裘，黻衣绣裳；位有所服","服"),("寿考","佩玉将将，寿考不忘；德有所终","德")],
   "山可常有，服不可虚；颜丹玉将，寿考在不忘。", "一百三十"),
 "sj131a-huang-niao": f131a,
 "sj131b-san-liang": lambda: bfig("六", "黄鸟　特·防·御与百身", "三良越贤，殉越不义",
   [("奄息","百夫之特；临穴惴栗","特"),("仲行","百夫之防；临穴惴栗","防"),("针虎","百夫之御；临穴惴栗","御")],
   "鸟可栖，人不可殉；百身可赎，三良不返。", "一百三十一"),
 "sj132a-chen-feng": f132a,
 "sj132b-san-wen": lambda: bfig("七", "晨风　钦钦·靡乐·如醉", "三问不改，忘才成定",
   [("钦钦","未见君子，忧心钦钦；鸟有林","初忧"),("靡乐","未见君子，忧心靡乐；木有匹","深忧"),("如醉","未见君子，忧心如醉；人无归","极忧")],
   "林可郁，忘不可返；三如何，都是忘。", "一百三十二"),
 "sj133a-tong-pao": f133a,
 "sj133b-san-tong": lambda: bfig("八", "无衣　同袍·同泽·同裳", "衣可无，同不可无",
   [("同袍","岂曰无衣，与子同袍；修我戈矛","外"),("同泽","岂曰无衣，与子同泽；修我矛戟","内"),("同裳","岂曰无衣，与子同裳；修我甲兵","下")],
   "衣可无，同不可无；三修三同，师出有名。", "一百三十三"),
 "sj134a-wei-yang": f134a,
 "sj134b-si-mu": lambda: bfig("九", "渭阳　送舅·赠物·思母", "物愈重，思愈无以为赠",
   [("送舅","曰至渭阳；送有尽处","送"),("赠物","路车乘黄，琼瑰玉佩；物有价","赠"),("思母","悠悠我思；思无尽处","思")],
   "渭可渡，思不可渡；路车琼瑰，都是母面。", "一百三十四"),
 "sj135a-quan-yu": f135a,
 "sj135b-bu-cheng": lambda: bfig("十", "权舆　昔厚·今薄·不承", "盛在始不在终",
   [("昔厚","夏屋渠渠，每食四簋；有始","昔"),("今薄","每食无余，每食不饱；无终","今"),("不承","于嗟乎，不承权舆；始终断","叹")],
   "屋可大，食不可薄；不承权舆，盛在始不在终。", "一百三十五"),
}

for k, fn in FIGS.items():
    body = fn()
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 540" width="760" height="540">\n'
           + body + "\n</svg>\n")
    open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8").write(svg)
    print(k)
