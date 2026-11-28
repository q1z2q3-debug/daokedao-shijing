# -*- coding: utf-8 -*-
"""生成 SJ079–SJ088 的图一（名物）与图二（义理），共 20 张。
只做白描，不填大面；全部 760x540，纸墨五色。
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "fig")
INK = "#1F1B17"
RED = "#A63D2F"
BROWN = "#7C6D5C"
LINE = "#DCD5C8"
PAPER = "#F5F1E8"
GOLD = "#B79A63"
FONT = "'Noto Serif CJK SC','Noto Serif SC','Songti SC','Source Han Serif SC',serif"


def t(x, y, s, size=11.5, color=INK, anchor="start", weight="normal", ls=0):
    return ('<text x="%.1f" y="%.1f" font-family="%s" font-size="%.1f" fill="%s" '
            'text-anchor="%s" font-weight="%s" letter-spacing="%.1f">%s</text>'
            % (x, y, FONT, size, color, anchor, weight, ls, s))


def p(d, w=0.55, color=INK, fill="none", opacity=1):
    return ('<path d="%s" fill="%s" stroke="%s" stroke-width="%.2f" '
            'stroke-linecap="round" stroke-linejoin="round" opacity="%.2f"/>'
            % (d, fill, color, w, opacity))


def line(x1, y1, x2, y2, w=0.55, color=INK, opacity=1):
    return ('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
            'stroke-width="%.2f" opacity="%.2f"/>' % (x1, y1, x2, y2, color, w, opacity))


def circ(cx, cy, r, w=0.55, color=INK):
    return ('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="none" stroke="%s" '
            'stroke-width="%.2f"/>' % (cx, cy, r, color, w))


def rect(x, y, wd, ht, w=0.55, color=INK, rx=0):
    return ('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" '
            'fill="none" stroke="%s" stroke-width="%.2f"/>'
            % (x, y, wd, ht, rx, color, w))


def head(no, vol, title, sub, code, zh_no):
    return (
        '<rect width="760" height="540" fill="%s"/>' % PAPER,
        '<rect x="10" y="10" width="740" height="520" fill="none" stroke="%s" stroke-width="0.6"/>' % LINE,
        '<rect x="22" y="28" width="716" height="470" fill="none" stroke="%s" stroke-width="0.8"/>' % LINE,
        t(38, 62, "郑 风 · 之%s" % vol, 9.5, RED, ls=2),
        t(380, 72, title, 26, INK, "middle", "bold", 2.0),
        t(720, 62, "诗三百五篇 · 之%s" % zh_no, 8.6, BROWN, "end", ls=1),
        line(38, 100, 722, 100, 0.35, GOLD),
        t(380, 122, sub, 10.2, BROWN, "middle", ls=1),
    )


def foot(code, caption, quote=""):
    s = []
    if quote:
        s.append(t(380, 470, quote, 13.2, RED, "middle", ls=1.2))
    s.append(t(380, 508, caption, 9.2, BROWN, "middle", ls=1))
    s.append('<rect x="676" y="492" width="22" height="22" fill="%s" opacity="0.13"/>' % RED)
    s.append(t(687, 507, "润", 8.8, RED, "middle"))
    return s


# ---------- 图一：名物 ----------

def fig079a():
    s = list(head("079", "五", "清人　河上", "三徙其营，一军皆闲", "sj079a", "七九"))
    # 河
    for y in (300, 318, 336):
        s.append(p("M 52 %d C 120 %d 210 %d 300 %d" % (y, y - 7, y + 7, y), 0.45, BROWN, opacity=0.55))
    # 三处地名
    for x, name in ((92, "彭"), (176, "消"), (260, "轴")):
        s.append(line(x, 250, x, 330, 0.5))
        s.append(line(x, 250, x + 18, 258, 0.45))
        s.append(t(x, 242, name, 12, INK, "middle", "bold"))
        s.append(t(x, 350, "河上", 8.4, BROWN, "middle"))
    s.append(t(166, 185, "三徙", 10.5, RED, "middle", ls=1))
    # 四甲
    for i, (x, y) in enumerate(((318, 238), (372, 238), (318, 300), (372, 300))):
        s.append(p("M %d %d L %d %d L %d %d L %d %d Z" % (x, y, x + 44, y - 4, x + 50, y + 52, x, y + 56), 0.65))
        s.append(line(x + 22, y + 8, x + 22, y + 48, 0.35, BROWN))
    s.append(t(368, 218, "驷介", 10.2, INK, "middle", "bold"))
    # 二矛
    for x, name in ((470, "重英"), (506, "重乔")):
        s.append(line(x, 230, x, 390, 0.55))
        s.append(p("M %d 250 L %d 244 L %d 250 L %d 262 L %d 256 L %d 250" % (x - 7, x, x + 7, x + 4, x, x - 7), 0.45, RED, opacity=0.8))
        s.append(t(x + 8, 300, name, 7.6, BROWN))
        s.append(p("M %d 390 L %d 396 L %d 390" % (x - 4, x, x + 4), 0.4, BROWN))
    s.append(t(488, 214, "二矛", 10.2, INK, "middle", "bold"))
    # 车轮
    s.append(circ(380, 402, 26, 0.6))
    s.append(circ(380, 402, 4, 0.4))
    for a in range(0, 360, 45):
        import math
        x = 380 + 24 * math.cos(math.radians(a))
        y = 402 + 24 * math.sin(math.radians(a))
        s.append(line(380, 402, x, y, 0.3, BROWN))
    s.append(t(380, 442, "一乘", 8.6, BROWN, "middle"))
    # 中军鼓旗
    s.append(circ(620, 320, 24, 0.6))
    s.append(circ(620, 320, 19, 0.35, BROWN))
    s.append(line(596, 342, 592, 386, 0.45))
    s.append(line(644, 342, 648, 386, 0.45))
    s.append(line(660, 220, 660, 390, 0.55))
    s.append(p("M 660 230 L 700 244 L 660 258 Z", 0.5, RED, opacity=0.75))
    s.append(t(620, 286, "中军", 10.2, INK, "middle", "bold"))
    s.append(t(630, 408, "作好", 9.2, RED, "middle"))
    s.append(t(70, 160, "河上三徙", 10.2, RED, ls=1))
    s.append(t(540, 160, "一军皆闲", 10.2, RED, ls=1))
    s += foot("sj079a", "图一 · 清人　河上、三徙、作好", "清人在彭，驷介旁旁。二矛重英，河上乎翱翔。")
    return s


def fig080a():
    s = list(head("080", "六", "羔裘　三英", "衣是外面，人是里子", "sj080a", "八十"))
    # 衣架
    s.append(line(300, 190, 300, 410, 0.5))
    s.append(line(460, 190, 460, 410, 0.5))
    s.append(line(290, 190, 470, 190, 0.6))
    # 羔裘
    s.append(p("M 322 196 L 438 196 L 452 230 L 468 300 L 446 306 L 446 402 L 314 402 L 314 306 L 292 300 L 308 230 Z", 0.7))
    # 领口
    s.append(p("M 344 196 L 380 236 L 416 196", 0.6))
    s.append(p("M 344 196 L 358 208 M 416 196 L 402 208", 0.4, BROWN))
    # 豹饰缘边：领、袖、下摆，用小圈
    for x, y in ((308, 230), (300, 258), (298, 286), (446, 230), (454, 258), (456, 286),
                 (320, 398), (346, 398), (372, 398), (398, 398), (424, 398), (442, 398),
                 (350, 204), (370, 220), (390, 220), (410, 204)):
        s.append(circ(x, y, 2.2, 0.4, BROWN))
    # 三英
    for x in (350, 380, 410):
        s.append(line(x, 402, x, 430, 0.45))
        s.append(p("M %d 430 L %d 438 L %d 430 L %d 438" % (x - 3, x, x + 3, x), 0.4, RED, opacity=0.8))
    s.append(t(380, 170, "羔裘", 11, INK, "middle", "bold"))
    s.append(t(70, 240, "如濡", 10.2, RED))
    s.append(t(70, 262, "润泽而柔", 8.4, BROWN))
    s.append(t(70, 330, "豹饰", 10.2, RED))
    s.append(t(70, 352, "缘边，不是整皮", 8.4, BROWN))
    s.append(t(600, 360, "三英", 10.2, RED, "middle"))
    s.append(t(600, 380, "裘饰，不是三人", 8.2, BROWN, "middle"))
    s += foot("sj080a", "图一 · 羔裘　衣、豹饰、三英", "羔裘如濡，洵直且侯。彼其之子，舍命不渝。")
    return s


def fig081a():
    s = list(head("081", "七", "遵大路　一执", "路是众人的，留是两人的", "sj081a", "八一"))
    # 大路
    s.append(line(58, 430, 310, 170, 0.55))
    s.append(line(702, 430, 450, 170, 0.55))
    s.append(line(90, 430, 330, 170, 0.3, BROWN))
    s.append(line(670, 430, 430, 170, 0.3, BROWN))
    # 路边树
    for x, y, h in ((100, 390, 58), (190, 350, 66), (610, 350, 62), (680, 390, 54)):
        s.append(line(x, y, x, y - h, 0.55))
        s.append(p("M %d %d C %d %d %d %d %d %d" % (x, y - h, x - 26, y - h - 18, x + 16, y - h - 28, x + 8, y - h - 40), 0.4, BROWN))
        s.append(p("M %d %d C %d %d %d %d %d %d" % (x, y - h + 10, x - 30, y - h - 8, x + 18, y - h - 18, x + 12, y - h - 30), 0.35, BROWN, opacity=0.7))
    # 袖与手：一只袖口，一只手抓住
    s.append(p("M 250 332 C 300 310 350 300 392 306 L 404 338 C 360 346 312 356 268 362 Z", 0.65))
    s.append(p("M 392 306 L 404 338", 0.5))
    s.append(p("M 404 310 C 426 302 442 312 440 330 C 438 348 420 354 408 344 C 398 336 398 320 404 310 Z", 0.65))
    for yy in (316, 324, 332, 340):
        s.append(p("M 424 %d C 432 %d 438 %d 436 %d" % (yy, yy - 4, yy + 1, yy + 3), 0.32, BROWN))
    s.append(t(300, 286, "袪", 11, RED, "middle", "bold"))
    s.append(t(430, 294, "手", 11, RED, "middle", "bold"))
    s.append(t(380, 398, "掺执", 9.4, BROWN, "middle"))
    s.append(t(70, 160, "大路", 10.5, RED, ls=1))
    s.append(t(640, 160, "不寁", 10.5, RED, "middle", ls=1))
    s += foot("sj081a", "图一 · 遵大路　大路、袪、手", "遵大路兮，掺执子之袪兮。")
    return s


def fig082a():
    s = list(head("082", "八", "女曰鸡鸣　晨", "鸡鸣、明星、琴瑟", "sj082a", "八二"))
    # 屋内地面
    s.append(line(60, 402, 700, 402, 0.45, BROWN))
    s.append(line(60, 176, 700, 176, 0.3, BROWN, opacity=0.5))
    # 鸡：身、颈、冠、喙、尾、足
    s.append(p("M 106 386 C 96 352 118 328 150 328 C 184 328 202 352 194 386 C 188 404 164 412 140 408 C 118 404 108 398 106 386 Z", 0.6))
    s.append(p("M 178 336 C 184 322 190 312 198 306 L 206 314 C 202 326 196 336 190 344", 0.5))
    s.append(circ(201, 306, 8, 0.45))
    s.append(p("M 209 302 L 220 308 L 209 312 Z", 0.4))
    s.append(circ(203, 303, 1.2, 0.3))
    s.append(p("M 192 294 C 194 286 200 284 204 290 C 206 284 212 284 214 290 C 216 286 222 288 220 296", 0.4, RED, opacity=0.8))
    s.append(p("M 108 352 C 84 326 76 310 82 300 C 92 314 102 330 112 342", 0.4, BROWN))
    s.append(p("M 108 360 C 82 342 72 326 78 316 C 88 330 98 344 110 352", 0.35, BROWN))
    s.append(p("M 108 370 C 84 360 70 350 72 340 C 84 350 96 360 108 366", 0.35, BROWN))
    s.append(p("M 144 348 C 134 360 136 376 146 382 C 158 388 174 378 176 364", 0.35, BROWN))
    for x in (138, 162):
        s.append(line(x, 408, x, 430, 0.35, BROWN))
        s.append(line(x, 430, x - 4, 434, 0.3, BROWN))
        s.append(line(x, 430, x + 4, 434, 0.3, BROWN))
    s.append(t(128, 446, "鸡", 8.5, BROWN, "middle"))
    # 明星
    s.append(p("M 600 172 L 606 190 L 624 196 L 606 202 L 600 220 L 594 202 L 576 196 L 594 190 Z", 0.5, RED, opacity=0.75))
    s.append(t(600, 240, "明星", 8.5, BROWN, "middle"))
    # 琴
    s.append(p("M 330 342 L 470 342 L 476 366 L 324 366 Z", 0.65))
    for x in range(344, 466, 18):
        s.append(line(x, 350, x, 358, 0.25, BROWN))
    s.append(line(324, 380, 324, 398, 0.4))
    s.append(line(476, 380, 476, 398, 0.4))
    s.append(t(398, 330, "琴瑟", 9.2, BROWN, "middle"))
    # 雁：身、颈、头、翅
    s.append(p("M 548 356 C 560 336 592 330 618 342 C 640 352 640 370 618 378 C 594 386 562 380 548 368 Z", 0.55))
    s.append(p("M 618 346 C 630 332 634 316 640 306", 0.45))
    s.append(circ(643, 304, 6, 0.4))
    s.append(p("M 648 300 L 658 304 L 648 308 Z", 0.35))
    s.append(p("M 570 348 C 584 342 600 348 604 360 C 594 368 578 364 570 356", 0.35, BROWN))
    s.append(t(590, 398, "凫雁", 8.5, BROWN, "middle"))
    # 两只碗
    for x in (500, 540):
        s.append(p("M %d 386 C %d 402 %d 402 %d 386" % (x - 14, x - 18, x + 18, x + 14), 0.45))
    s.append(t(520, 418, "共食", 8.3, BROWN, "middle"))
    s.append(t(380, 160, "天未亮，人已起", 9.8, RED, "middle", ls=1))
    s += foot("sj082a", "图一 · 女曰鸡鸣　鸡、明星、琴瑟", "女曰鸡鸣，士曰昧旦。子兴视夜，明星有烂。")
    return s


def fig083a():
    s = list(head("083", "九", "有女同车　车与花", "色在花上，声在玉上", "sj083a", "八三"))
    # 车
    s.append(rect(478, 266, 150, 86, 0.65, rx=6))
    s.append(line(478, 266, 590, 266, 0.4))
    s.append(line(540, 292, 540, 344, 0.35, BROWN))
    s.append(circ(520, 392, 28, 0.6))
    s.append(circ(520, 392, 4, 0.4))
    for a in range(0, 360, 45):
        import math
        x = 520 + 25 * math.cos(math.radians(a))
        y = 392 + 25 * math.sin(math.radians(a))
        s.append(line(520, 392, x, y, 0.28, BROWN))
    s.append(line(620, 310, 688, 330, 0.45))
    s.append(t(550, 246, "同车", 10.2, INK, "middle", "bold"))
    # 木槿枝
    s.append(p("M 116 380 C 150 300 190 230 260 206", 0.55))
    for x, y in ((160, 286), (206, 246), (254, 218)):
        for k in range(5):
            import math
            a = math.radians(k * 72 - 90)
            s.append(circ(x + 15 * math.cos(a), y + 15 * math.sin(a), 9, 0.4))
        s.append(circ(x, y, 3, 0.35, RED))
    s.append(t(180, 190, "舜华", 9.5, RED, "middle"))
    # 佩玉
    for i, x in enumerate((322, 356, 390)):
        s.append(line(x, 280, x, 360, 0.4))
        for y in (300, 320, 340, 360):
            s.append(circ(x, y, 5 if i == 1 else 4, 0.4, BROWN))
    s.append(t(356, 264, "琼琚", 9.2, BROWN, "middle"))
    s.append(t(380, 160, "一车之美", 9.8, RED, "middle", ls=1))
    s += foot("sj083a", "图一 · 有女同车　车、舜华、琼琚", "有女同车，颜如舜华。将翱将翔，佩玉琼琚。")
    return s


def fig084a():
    s = list(head("084", "十", "山有扶苏　高下", "物各得其所，人却不见", "sj084a", "八四"))
    # 山
    s.append(p("M 54 404 L 158 250 L 248 330 L 320 204 L 430 404 Z", 0.65))
    s.append(p("M 250 404 L 350 270 L 446 404 Z", 0.45, BROWN))
    # 隰
    for y in (392, 408, 424):
        s.append(line(470, y, 706, y, 0.35, BROWN, opacity=0.55))
    s.append(t(590, 446, "隰", 10.5, BROWN, "middle"))
    # 扶苏
    s.append(line(144, 330, 144, 386, 0.5))
    s.append(p("M 144 330 C 126 306 130 286 144 274 C 158 286 162 306 144 330", 0.45))
    s.append(t(144, 318, "扶苏", 7.8, BROWN, "middle"))
    # 乔松
    s.append(line(300, 300, 300, 390, 0.55))
    for y in (286, 306, 326):
        s.append(p("M 300 %d L 274 %d L 300 %d L 326 %d Z" % (y, y + 14, y + 8, y + 14), 0.4, BROWN))
    s.append(t(300, 280, "乔松", 7.8, BROWN, "middle"))
    # 荷华：荷叶、花茎、五瓣
    s.append(p("M 556 390 C 516 382 492 392 506 404 C 524 414 588 414 606 402 C 624 390 596 380 556 390 Z", 0.4, BROWN))
    s.append(line(556, 388, 556, 342, 0.4))
    for k in range(5):
        import math
        a = math.radians(k * 72 - 90)
        x = 556 + 18 * math.cos(a)
        y = 342 + 18 * math.sin(a)
        s.append(p("M 556 342 C %d %d %d %d %d %d C %d %d 556 342" % (
            x - 6, y - 4, x - 4, y + 8, x, y + 4, x + 4, y + 8), 0.4, RED, opacity=0.55))
    s.append(circ(556, 342, 3, 0.35, BROWN))
    s.append(t(556, 426, "荷华", 7.8, BROWN, "middle"))
    # 龙游
    for i in range(4):
        x = 660 + i * 9
        s.append(p("M %d 386 C %d 360 %d 340 %d 320" % (x, x - 8, x + 8, x + 2), 0.35, BROWN))
    s.append(t(678, 404, "龙游", 7.8, BROWN, "middle"))
    s.append(t(380, 162, "山高隰下", 9.8, RED, "middle", ls=1))
    s += foot("sj084a", "图一 · 山有扶苏　山、隰、四草木", "山有扶苏，隰有荷华。不见子都，乃见狂且。")
    return s


def fig085a():
    s = list(head("085", "十一", "萚兮　一叶", "风先到，叶后落", "sj085a", "八五"))
    # 枝
    s.append(p("M 700 150 C 620 176 560 214 500 282", 0.65))
    s.append(p("M 620 196 C 590 180 566 178 548 184", 0.4, BROWN))
    s.append(p("M 570 230 C 546 220 522 224 510 236", 0.35, BROWN))
    # 叶：三片尖叶，带主脉与侧脉
    for x, y, a in ((640, 190, -20), (566, 232, 10), (510, 282, -5)):
        s.append(p("M %d %d C %d %d %d %d %d %d C %d %d %d %d %d %d Z" %
                   (x, y, x - 34, y - 24, x - 52, y + 4, x - 24, y + 20,
                    x - 10, y + 24, x + 4, y + 10, x, y), 0.55))
        s.append(line(x - 28, y + 4, x + 2, y - 2, 0.3, BROWN))
        s.append(line(x - 24, y + 6, x - 30, y - 8, 0.25, BROWN))
        s.append(line(x - 18, y + 8, x - 12, y - 6, 0.25, BROWN))
    # 风
    for i, y in enumerate((330, 360, 390, 420)):
        s.append(p("M 62 %d C 150 %d 230 %d 300 %d" % (y, y - 16, y + 18, y - 4), 0.35, BROWN, opacity=0.55))
    # 落地叶
    s.append(p("M 210 430 C 230 418 252 420 262 432 C 250 442 228 444 210 430 Z", 0.45, RED, opacity=0.6))
    s.append(t(380, 162, "一叶知风", 9.8, RED, "middle", ls=1))
    s += foot("sj085a", "图一 · 萚兮　落叶、风", "萚兮萚兮，风其吹女。叔兮伯兮，倡予和女。")
    return s


def fig086a():
    s = list(head("086", "十二", "狡童　不与", "空碗比空话狠", "sj086a", "八六"))
    # 门
    s.append(rect(70, 170, 170, 240, 0.65))
    s.append(line(70, 170, 240, 410, 0.3, BROWN, opacity=0.5))
    s.append(rect(88, 192, 132, 196, 0.35, BROWN))
    # 席
    s.append(p("M 300 380 L 640 380 L 620 430 L 320 430 Z", 0.45, BROWN))
    for x in range(330, 630, 28):
        s.append(line(x, 386, x - 8, 424, 0.25, BROWN, opacity=0.55))
    # 案
    s.append(line(340, 346, 560, 346, 0.55))
    s.append(line(352, 346, 348, 382, 0.4))
    s.append(line(548, 346, 552, 382, 0.4))
    # 两碗
    s.append(p("M 378 330 C 370 352 398 352 390 330", 0.45))
    s.append(p("M 470 330 C 458 354 494 354 482 330", 0.45))
    s.append(circ(384, 338, 2, 0.3, BROWN))
    s.append(t(430, 318, "一食一空", 8.4, BROWN, "middle"))
    s.append(t(430, 362, "不与我食", 9.2, RED, "middle"))
    # 空座
    s.append(rect(580, 340, 70, 50, 0.3, BROWN, rx=4))
    s.append(t(615, 370, "空", 8.5, BROWN, "middle"))
    s.append(t(380, 162, "门半开，人不在", 9.8, RED, "middle", ls=1))
    s += foot("sj086a", "图一 · 狡童　门、食器、空座", "彼狡童兮，不与我言兮。维子之故，使我不能餐兮。")
    return s


def fig087a():
    s = list(head("087", "十三", "褰裳　二水", "水是两道门", "sj087a", "八七"))
    # 两水
    for x0, name in ((110, "溱"), (520, "洧")):
        s.append(p("M %d 190 C %d 250 %d 330 %d 420" % (x0, x0 - 20, x0 + 20, x0), 0.5, BROWN))
        s.append(p("M %d 190 C %d 250 %d 330 %d 420" % (x0 + 50, x0 + 30, x0 + 70, x0 + 50), 0.35, BROWN, opacity=0.7))
        s.append(t(x0 + 25, 176, name, 10.5, RED, "middle", "bold"))
    # 中间褰裳：一条下裳，两只手提起下摆
    s.append(line(334, 284, 426, 284, 0.6))
    s.append(p("M 334 284 L 318 412 L 442 412 L 426 284", 0.6))
    s.append(line(318, 412, 442, 412, 0.5))
    for x in (350, 380, 410):
        s.append(line(x, 292, x - 4, 408, 0.3, BROWN))
    # 手
    s.append(p("M 318 350 C 300 346 292 358 300 370 C 308 382 324 380 330 368 Z", 0.45))
    s.append(p("M 442 350 C 460 346 468 358 460 370 C 452 382 436 380 430 368 Z", 0.45))
    s.append(line(300, 370, 318, 412, 0.35, RED, opacity=0.7))
    s.append(line(460, 370, 442, 412, 0.35, RED, opacity=0.7))
    s.append(t(380, 266, "裳", 9.2, BROWN, "middle"))
    s.append(t(288, 350, "褰", 8.5, RED))
    # 对岸树
    s.append(line(680, 400, 680, 320, 0.5))
    s.append(p("M 680 320 C 654 300 654 280 680 270 C 706 280 706 300 680 320", 0.4, BROWN))
    s.append(t(680, 414, "对岸", 8.2, BROWN, "middle"))
    s.append(t(380, 162, "过水，才叫来", 9.8, RED, "middle", ls=1))
    s += foot("sj087a", "图一 · 褰裳　二水、褰裳、对岸", "子惠思我，褰裳涉溱。子不我思，岂无他人？")
    return s


def fig088a():
    s = list(head("088", "十四", "丰　巷与堂", "锦衣在里，褧衣在表", "sj088a", "八八"))
    # 巷
    s.append(line(66, 430, 66, 190, 0.5))
    s.append(line(236, 430, 236, 190, 0.5))
    s.append(line(66, 190, 236, 190, 0.4))
    s.append(t(88, 172, "巷", 10.5, RED, "middle", "bold"))
    # 堂
    s.append(rect(470, 214, 210, 190, 0.6))
    s.append(p("M 452 214 L 590 166 L 706 214", 0.55))
    s.append(t(590, 196, "堂", 10.5, RED, "middle", "bold"))
    # 锦衣 + 褧衣
    s.append(p("M 306 260 L 386 260 L 400 304 L 414 376 L 398 382 L 398 430 L 294 430 L 294 382 L 278 376 L 292 304 Z", 0.7))
    s.append(p("M 306 260 L 346 298 L 386 260", 0.45))
    # 内里锦纹
    for y in (320, 344, 368, 392):
        s.append(line(310, y, 382, y, 0.25, RED, opacity=0.55))
    # 褧衣外罩（素色，开襟）
    s.append(p("M 294 304 L 278 376 L 294 382 L 294 430 L 320 430 L 320 304", 0.5, BROWN))
    s.append(p("M 398 304 L 414 376 L 398 382 L 398 430 L 372 430 L 372 304", 0.5, BROWN))
    s.append(t(346, 246, "锦衣褧衣", 8.6, BROWN, "middle"))
    # 车
    s.append(circ(600, 400, 30, 0.6))
    for a in range(0, 360, 45):
        import math
        x = 600 + 27 * math.cos(math.radians(a))
        y = 400 + 27 * math.sin(math.radians(a))
        s.append(line(600, 400, x, y, 0.28, BROWN))
    s.append(line(600, 400, 700, 360, 0.45))
    s.append(t(650, 444, "驾予", 8.6, RED, "middle"))
    s.append(t(380, 160, "一悔一追", 9.8, RED, "middle", ls=1))
    s += foot("sj088a", "图一 · 丰　巷、堂、锦衣褧衣", "衣锦褧衣，裳锦褧裳。叔兮伯兮，驾予与行。")
    return s


# ---------- 图二：义理 ----------

def fig2(no, vol, title, sub, rows, conclusion, code, zh_no, coda=""):
    s = list(head(no, vol, title, sub, code, zh_no))
    ys = (176, 246, 316)
    for i, row in enumerate(rows[:3]):
        y = ys[i]
        s.append(line(44, y + 20, 716, y + 20, 0.3, LINE))
        s.append(t(64, y, row[0], 10.5, INK, "start", "bold"))
        s.append(t(236, y, row[1], 11.2, INK, "start"))
        s.append(t(566, y, row[2], 9.6, BROWN, "start"))
    # 左侧竖标
    s.append(line(206, 158, 206, 350, 0.55, RED))
    s.append(line(206, 158, 214, 158, 0.4, RED))
    s.append(line(206, 350, 214, 350, 0.4, RED))
    # 右侧箭头 / 虚线
    s.append(line(548, 166, 548, 340, 0.35, BROWN))
    s.append(line(544, 166, 552, 166, 0.3, BROWN))
    s.append(line(544, 340, 552, 340, 0.3, BROWN))
    # 结论
    s.append(line(50, 388, 710, 388, 0.35, GOLD))
    s.append(t(380, 414, conclusion, 12.2, RED, "middle", "bold", 1.0))
    if coda:
        s.append(t(380, 438, coda, 9.0, BROWN, "middle", ls=0.5))
    s.append(t(380, 468, "图二 · 义理", 8.6, BROWN, "middle"))
    s.append('<rect x="676" y="492" width="22" height="22" fill="%s" opacity="0.13"/>' % RED)
    s.append(t(687, 507, "润", 8.8, RED, "middle"))
    return s


def fig079b():
    return fig2("079", "五", "清人　三徙一闲", "换地不换姿态", [
        ("一章　彭", "驷介旁旁 · 二矛重英 · 翱翔", "盛"),
        ("二章　消", "驷介麃麃 · 二矛重乔 · 逍遥", "更盛"),
        ("三章　轴", "驷介陶陶 · 左旋右抽 · 作好", "盛而闲"),
    ], "三徙，一闲；众散在诗外", "sj079b", "七九", "军容越盛，军心越闲。")


def fig080b():
    return fig2("080", "六", "羔裘　身职名", "衣是外面，人是里子", [
        ("身", "舍命不渝", "衣之里"),
        ("职", "邦之司直", "位之正"),
        ("名", "邦之彦", "名之实"),
    ], "服称其人，衣不如里", "sj080b", "八十", "三章从衣写到名，越写越亮。")


def fig081b():
    return fig2("081", "七", "遵大路　一留", "从袖口到手，从旧情到旧好", [
        ("一章　袪", "执子之袪 · 无我恶 · 不寁故", "初留"),
        ("二章　手", "执子之手 · 无我魗 · 不寁好", "深留"),
        ("", "两个动作，一个请求", "慢一点"),
    ], "不寁：只请慢一点", "sj081b", "八一", "路可同，故不可挟；手可执，好不可强。")


def fig082b():
    return fig2("082", "八", "女曰鸡鸣　静好", "起、食、赠，一天的事", [
        ("一章　起", "鸡鸣 · 明星 · 弋雁", "天光"),
        ("二章　食", "加 · 宜 · 饮酒 · 琴瑟", "餐桌"),
        ("三章　赠", "来 · 顺 · 好 · 杂佩", "身上"),
    ], "静好：一天的事", "sj082b", "八二", "好不在声，在静；情不在热，在久。")


def fig083b():
    return fig2("083", "九", "有女同车　三层", "色、声、德，独缺一娶", [
        ("色", "颜如舜华 · 洵美且都", "眼"),
        ("声", "佩玉琼琚 · 佩玉将将", "耳"),
        ("德", "彼美孟姜 · 德音不忘", "心"),
    ], "三层都到，独缺一娶", "sj083b", "八三", "诗把孟姜写到十分，正为照见“不娶”。")


def fig084b():
    return fig2("084", "十", "山有扶苏　所美非美", "物各得所，人却错位", [
        ("山", "扶苏 · 乔松", "高者高"),
        ("隰", "荷华 · 龙游", "下者下"),
        ("人", "不见子都，乃见狂且", "所见非想"),
    ], "所美非美，所见非想", "sj084b", "八四", "一句“乃见”，把理想拉回眼前。")


def fig085b():
    return fig2("085", "十一", "萚兮　倡和要", "谁先发声，谁就是位", [
        ("倡", "叔兮伯兮，倡予和女", "先唱"),
        ("和", "倡予和女", "答唱"),
        ("要", "倡予要女", "成"),
    ], "位不可倒，倡不可让", "sj085b", "八五", "叶可落，风可吹；君不可等臣先唱。")


def fig086b():
    return fig2("086", "十二", "狡童　不与", "言与食，两重断", [
        ("言", "不与我言", "餐"),
        ("食", "不与我食", "息"),
        ("故", "维子之故", "怨说成念"),
    ], "不言不食，非无口，是不与", "sj086b", "八六", "一句“维子之故”，把怨说成念。")


def fig087b():
    return fig2("087", "十三", "褰裳　思与不思", "来与不来，中间一条水", [
        ("思", "褰裳涉溱", "来"),
        ("不思", "岂无他人", "退"),
        ("狂童", "狂童之狂也且", "骂而留"),
    ], "水可涉，人可换；骂不出口的留", "sj087b", "八七", "把“他人”说得越响，越见“你”在心里。")


def fig088b():
    return fig2("088", "十四", "丰　悔待嫁", "先悔，后嫁；时间在心里倒过来", [
        ("悔", "不送 · 不将", "迟"),
        ("待", "巷 · 堂", "近"),
        ("嫁", "锦衣褧衣 · 驾予", "追"),
    ], "礼在外，情在内", "sj088b", "八八", "锦衣在里，褧衣在表；美不露尽，才走得出门。")


FIGS = {
    "sj079a-he-shang": fig079a, "sj079b-san-shi": fig079b,
    "sj080a-gao-qiu": fig080a, "sj080b-san-zan": fig080b,
    "sj081a-da-lu": fig081a, "sj081b-bu-zan": fig081b,
    "sj082a-ji-ming": fig082a, "sj082b-jing-hao": fig082b,
    "sj083a-tong-che": fig083a, "sj083b-bu-qu": fig083b,
    "sj084a-shan-xi": fig084a, "sj084b-suo-mei": fig084b,
    "sj085a-tuo-ye": fig085a, "sj085b-chang-he": fig085b,
    "sj086a-jiao-tong": fig086a, "sj086b-bu-yan": fig086b,
    "sj087a-qian-shang": fig087a, "sj087b-er-shui": fig087b,
    "sj088a-feng-xiang": fig088a, "sj088b-yi-li": fig088b,
}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for name, fn in FIGS.items():
        body = "\n".join(fn())
        svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 540" width="760" height="540">\n'
               + body + "\n</svg>\n")
        open(os.path.join(OUT, name + ".svg"), "w", encoding="utf-8").write(svg)
        print("wrote", name)
