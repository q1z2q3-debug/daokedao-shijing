# -*- coding: utf-8 -*-
"""生成 SJ096–SJ106 的图一（名物）与图二（义理），共 22 张。
齐风十一篇：鸡鸣、还、著、东方之日、东方未明、南山、甫田、卢令、敝笱、载驱、猗嗟。
白描，不填大面；全部 760x540，纸墨五色。
活物画不全只画痕迹；人不画脸；红只作结。
"""
import os
import math

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
    return [
        '<rect width="760" height="540" fill="%s"/>' % PAPER,
        '<rect x="10" y="10" width="740" height="520" fill="none" stroke="%s" stroke-width="0.6"/>' % LINE,
        '<rect x="22" y="28" width="716" height="470" fill="none" stroke="%s" stroke-width="0.8"/>' % LINE,
        t(38, 62, "齐 风 · 之%s" % vol, 9.5, RED, ls=2),
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


def person(cx, base_y, ht=126, wd=34, color=INK, opacity=1):
    s = []
    hr = ht * 0.075
    s.append(circ(cx, base_y - ht + hr, hr, 0.45, color))
    s.append(line(cx, base_y - ht + 2 * hr, cx, base_y - ht * 0.78, 0.35, color, opacity))
    s.append(p("M %.1f %.1f L %.1f %.1f L %.1f %.1f L %.1f %.1f L %.1f %.1f L %.1f %.1f Z" %
               (cx - wd * 0.55, base_y - ht * 0.78,
                cx - wd, base_y - ht * 0.40,
                cx - wd * 0.88, base_y,
                cx + wd * 0.88, base_y,
                cx + wd, base_y - ht * 0.40,
                cx + wd * 0.55, base_y - ht * 0.78), 0.5, color, opacity=opacity))
    s.append(p("M %.1f %.1f L %.1f %.1f L %.1f %.1f" %
               (cx - wd * 0.55, base_y - ht * 0.78, cx, base_y - ht * 0.62,
                cx + wd * 0.55, base_y - ht * 0.78), 0.35, color, opacity=opacity))
    s.append(line(cx - wd * 0.82, base_y - ht * 0.58, cx - wd * 1.02, base_y - ht * 0.22, 0.3, color, opacity))
    s.append(line(cx + wd * 0.82, base_y - ht * 0.58, cx + wd * 1.02, base_y - ht * 0.22, 0.3, color, opacity))
    return s


def fig2(no, vol, title, sub, rows, conclusion, code, zh_no, coda=""):
    s = head(no, vol, title, sub, code, zh_no)
    n = len(rows)
    ys = {2: (218, 300), 3: (190, 260, 330), 4: (178, 240, 302, 364)}[n]
    for i, row in enumerate(rows):
        y = ys[i]
        s.append(line(44, y + 22, 716, y + 22, 0.3, LINE))
        s.append(t(62, y, row[0], 10.4, INK, "start", "bold"))
        s.append(t(226, y, row[1], 10.8, INK, "start"))
        s.append(t(566, y, row[2], 9.4, BROWN, "start"))
    top = ys[0] - 22
    bot = ys[-1] + 22
    s.append(line(204, top, 204, bot, 0.55, RED))
    s.append(line(204, top, 212, top, 0.4, RED))
    s.append(line(204, bot, 212, bot, 0.4, RED))
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


def rooster(x, y, scale=1.0):
    """侧身雄鸡：身、头、冠、喙、尾、足；不画眼。"""
    s = []
    # 身
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
               (x-18*scale, y, x-26*scale, y-16*scale, x-18*scale, y-30*scale, x, y-32*scale,
                x+18*scale, y-34*scale, x+30*scale, y-22*scale, x+30*scale, y-10*scale,
                x+30*scale, y+12*scale, x+12*scale, y+24*scale, x-6*scale, y+24*scale), 0.6))
    # 頭
    s.append(circ(x+30*scale, y-34*scale, 10*scale, 0.5))
    # 冠
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
               (x+24*scale, y-44*scale, x+22*scale, y-54*scale, x+26*scale, y-58*scale, x+28*scale, y-50*scale,
                x+32*scale, y-56*scale, x+36*scale, y-50*scale, x+36*scale, y-44*scale), 0.4, RED))
    # 喙與肉垂
    s.append(p("M %.0f %.0f L %.0f %.0f L %.0f %.0f" %
               (x+40*scale, y-36*scale, x+50*scale, y-33*scale, x+40*scale, y-30*scale), 0.35, RED))
    s.append(p("M %.0f %.0f L %.0f %.0f L %.0f %.0f" %
               (x+39*scale, y-28*scale, x+42*scale, y-20*scale, x+36*scale, y-22*scale), 0.35, RED))
    # 尾：三根長羽
    for dy in (-8, 0, 8):
        s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
                   (x-18*scale, y+dy*scale, x-40*scale, y+(dy-10)*scale,
                    x-54*scale, y+(dy-22)*scale, x-46*scale, y+(dy-34)*scale), 0.4, BROWN))
    # 足
    for dx in (-6, 8):
        s.append(line(x+dx*scale, y+24*scale, x+dx*scale, y+42*scale, 0.4))
        s.append(p("M %.0f %.0f L %.0f %.0f M %.0f %.0f L %.0f %.0f" %
                   (x+dx*scale, y+42*scale, x+(dx-8)*scale, y+48*scale,
                    x+dx*scale, y+42*scale, x+(dx+8)*scale, y+48*scale), 0.3, BROWN))
    return s


# ---------- 096 鸡鸣 ----------

def fig096a():
    s = head("096", "一", "鸡鸣　三告", "鸡可误，月可误，朝不可误", "sj096a", "九六")
    # 左：鸡埘
    s.append(line(56, 402, 188, 402, 0.45, BROWN))
    s.append(line(68, 402, 68, 438, 0.35, BROWN))
    s.append(line(176, 402, 176, 438, 0.35, BROWN))
    s.append(p("M 68 438 L 58 448 M 176 438 L 186 448", 0.3, BROWN))
    s += rooster(112, 356, 0.9)
    s.append(t(122, 458, "鸡鸣", 8.6, BROWN, "middle"))
    # 中：蝇与误听
    s.append(circ(300, 270, 4.5, 0.4, INK))
    s.append(line(295, 267, 278, 252, 0.3, BROWN))
    s.append(line(305, 267, 322, 252, 0.3, BROWN))
    s.append(p("M 278 252 C 270 246 266 252 272 258", 0.35, BROWN))
    s.append(p("M 322 252 C 330 246 334 252 328 258", 0.35, BROWN))
    s.append(p("M 300 274 L 300 296 M 296 296 L 300 302 L 304 296", 0.3, BROWN))
    s.append(t(300, 232, "苍蝇之声", 9.2, RED, "middle", "bold"))
    s.append(p("M 216 290 C 246 280 260 272 274 266", 0.3, BROWN, opacity=0.7))
    s.append(t(246, 310, "误听", 8.0, BROWN, "middle"))
    # 右：月与东方
    s.append(p("M 560 250 C 540 250 526 266 526 286 C 526 306 540 322 560 322 C 548 310 542 298 542 286 C 542 272 550 260 560 250 Z", 0.5))
    s.append(line(520, 340, 700, 340, 0.4, BROWN))
    s.append(line(560, 340, 560, 320, 0.3, BROWN))
    s.append(line(620, 340, 620, 326, 0.3, BROWN))
    s.append(t(610, 232, "月出之光", 9.2, RED, "middle", "bold"))
    s.append(t(612, 362, "东方未明", 8.2, BROWN, "middle"))
    # 下：朝服
    s.append(line(370, 390, 370, 440, 0.45))
    s.append(line(430, 390, 430, 440, 0.45))
    s.append(p("M 370 390 L 386 350 L 414 350 L 430 390 Z", 0.45))
    s.append(p("M 386 350 L 388 392 L 412 392 L 414 350", 0.35, BROWN))
    s.append(p("M 370 390 L 352 412 M 430 390 L 448 412", 0.35, BROWN))
    s.append(t(74, 158, "一告", 9.4, RED))
    s.append(t(556, 158, "二告", 9.4, RED))
    s += foot("sj096a", "图一 · 鸡鸣　鸡、蝇、月、朝服", "鸡既鸣矣，朝既盈矣。匪鸡则鸣，苍蝇之声。")
    return s


def fig096b():
    return fig2("096", "一", "鸡鸣　三告", "一夜三惊，三告而朝", [
        ("一告", "鸡鸣 · 朝盈 · 蝇声", "以蝇为鸡"),
        ("二告", "东方明 · 朝昌 · 月光", "以月为明"),
        ("三告", "虫飞 · 同梦 · 会归", "以情让势"),
    ], "鸡可误，朝不可误；三告，才起身", "sj096b", "九六",
        "催得越早，越见舍不得。")


# ---------- 097 还 ----------

def fig097a():
    s = head("097", "二", "还　峱山猎", "以猎相誉，则政事自荒", "sj097a", "九七")
    # 山三峰
    s.append(p("M 44 430 L 110 330 L 150 370 L 210 270 L 260 330 L 320 250 L 390 340 L 440 300 L 500 430", 0.6))
    s.append(p("M 60 410 L 120 340 L 150 372", 0.35, BROWN))
    s.append(p("M 260 330 L 320 264 L 382 338", 0.35, BROWN))
    s.append(t(140, 308, "峱", 11.0, RED, "middle", "bold"))
    s.append(t(300, 236, "山阳", 7.6, BROWN, "middle"))
    # 蹄迹三组
    for i, (x, y) in enumerate(((90, 446), (210, 446), (330, 446))):
        for dx in (0, 14):
            s.append(p("M %d %d C %d %d %d %d %d %d" % (x+dx, y-10, x+dx-6, y-6, x+dx-6, y+4, x+dx, y+10), 0.3, BROWN))
            s.append(p("M %d %d C %d %d %d %d %d %d" % (x+dx, y+10, x+dx+6, y+6, x+dx+6, y-4, x+dx, y-10), 0.3, BROWN))
        s.append(t(x+18, 470, ("两肩", "两牡", "两狼")[i], 7.8, BROWN, "middle"))
    # 猎者相揖：两袖、两手、三指
    s.append(p("M 506 296 L 552 270 L 564 290 L 524 316 Z", 0.45))
    s.append(p("M 694 296 L 648 270 L 636 290 L 676 316 Z", 0.45))
    s.append(p("M 558 282 C 576 274 590 280 590 290 C 590 300 576 304 560 298", 0.45))
    s.append(p("M 642 282 C 624 274 610 280 610 290 C 610 300 624 304 640 298", 0.45))
    for dy in (-4, 0, 4):
        s.append(line(590, 290+dy, 604, 288+dy, 0.3, BROWN))
        s.append(line(610, 290+dy, 596, 288+dy, 0.3, BROWN))
    s.append(t(600, 232, "揖我", 9.0, RED, "middle", "bold"))
    s.append(t(600, 334, "并驱", 8.6, BROWN, "middle"))
    s.append(p("M 540 360 C 580 344 620 344 660 360", 0.4, BROWN))
    s.append(t(600, 384, "相誉", 8.0, BROWN, "middle"))
    s += foot("sj097a", "图一 · 还　峱山、并驱、两肩/牡/狼", "子之还兮，遭我乎峱之间兮。并驱从两肩兮。")
    return s


def fig097b():
    return fig2("097", "二", "还　三遇三誉", "路越亮，誉越满", [
        ("一章", "山间 · 两肩 · 儇", "还：便捷"),
        ("二章", "山道 · 两牡 · 好", "茂：美"),
        ("三章", "山阳 · 两狼 · 臧", "昌：盛"),
    ], "以猎相誉，则政事自荒", "sj097b", "九七",
        "誉在猎场，荒在政事。")


# ---------- 098 著 ----------

def crown(cx, cy, color=INK):
    s = []
    # 冠體
    s.append(p("M %.0f %.0f L %.0f %.0f L %.0f %.0f L %.0f %.0f Z" %
               (cx-22, cy+24, cx-16, cy-12, cx+16, cy-12, cx+22, cy+24), 0.5, color))
    s.append(line(cx-16, cy-12, cx+16, cy-12, 0.4, color))
    s.append(line(cx-22, cy+24, cx+22, cy+24, 0.35, color))
    s.append(circ(cx, cy-18, 3.2, 0.35, RED))
    # 充耳：兩側懸繩與瑱
    for sx in (-1, 1):
        s.append(line(cx+sx*19, cy+8, cx+sx*19, cy+38, 0.35, color))
        s.append(circ(cx+sx*19, cy+42, 3.0, 0.35, RED))
    return s


def fig098a():
    s = head("098", "三", "著　三进", "礼在门内，等在三进", "sj098a", "九八")
    # 三重门框
    for i, x in enumerate((64, 270, 476)):
        w = 150 if i < 2 else 170
        s.append(line(x, 330, x, 188, 0.55))
        s.append(line(x+w, 330, x+w, 188, 0.55))
        s.append(line(x, 188, x+w, 188, 0.45))
        s.append(p("M %d 330 L %d 330 L %d 348 L %d 348 Z" % (x, x+w, x+w-10, x-10), 0.3, BROWN))
        s.append(t(x+w/2, 176, ("著", "庭", "堂")[i], 10.0, RED, "middle", "bold"))
        s.append(t(x+w/2, 350, ("门屏之间", "大门内", "堂上")[i], 7.6, BROWN, "middle"))
    # 三冠与充耳
    for i, x in enumerate((100, 306, 520)):
        s += crown(x, 230)
        s.append(t(x, 320, ("素/琼华", "青/琼莹", "黄/琼英")[i], 7.8, BROWN, "middle"))
    # 新妇在门外
    s += person(52, 420, 96, 24, BROWN, 0.8)
    s.append(line(44, 434, 60, 434, 0.35, BROWN))
    s.append(t(52, 458, "新妇", 7.6, BROWN, "middle"))
    s += foot("sj098a", "图一 · 著　门屏、庭、堂、充耳", "俟我于著乎而，充耳以素乎而，尚之以琼华乎而。")
    return s


def fig098b():
    return fig2("098", "三", "著　三进三见", "一步深一步，一饰换一色", [
        ("著", "素 · 琼华", "门屏之间"),
        ("庭", "青 · 琼莹", "大门之内"),
        ("堂", "黄 · 琼英", "升阶至堂"),
    ], "三进已尽，礼仍不见", "sj098b", "九八",
        "亲迎不亲，女自见饰。")


# ---------- 099 东方之日 ----------

def footprint(x, y, color=BROWN, op=0.7):
    s = []
    # 腳掌
    s.append(p("M %d %d C %d %d %d %d %d %d C %d %d %d %d %d %d C %d %d %d %d %d %d Z" %
               (x-5, y+2, x-7, y-2, x-3, y-5, x, y-5,
                x+3, y-5, x+7, y-2, x+5, y+2,
                x+3, y+6, x-3, y+6, x-5, y+2), 0.3, color, opacity=op))
    # 三趾
    for dx in (-4, 0, 4):
        s.append(line(x+dx, y-5, x+dx-1, y-10, 0.25, color, opacity=op))
    return s


def fig099a():
    s = head("099", "四", "东方之日　履迹", "日在前，月在后", "sj099a", "九九")
    # 左日
    s.append(circ(94, 244, 28, 0.55, RED))
    s.append(line(58, 286, 130, 286, 0.35, BROWN))
    s.append(t(94, 302, "日", 9.6, RED, "middle", "bold"))
    # 右月
    s.append(p("M 650 220 C 632 220 620 234 620 252 C 620 270 632 284 650 284 C 640 274 636 264 636 252 C 636 240 642 230 650 220 Z", 0.5))
    s.append(t(650, 302, "月", 9.6, RED, "middle", "bold"))
    # 室与闼：室有内门，闼是门内
    s.append(rect(250, 250, 150, 130, 0.55))
    s.append(line(350, 250, 350, 310, 0.35, BROWN))
    s.append(line(350, 372, 350, 380, 0.35, BROWN))
    s.append(p("M 350 310 L 330 330 L 350 372", 0.35, BROWN))
    s.append(line(258, 380, 392, 380, 0.3, BROWN))
    s.append(rect(430, 270, 100, 110, 0.45))
    s.append(p("M 430 270 L 460 300 L 460 380 L 430 380", 0.35, BROWN))
    s.append(line(430, 380, 530, 380, 0.3, BROWN))
    s.append(t(325, 238, "室", 9.0, RED, "middle", "bold"))
    s.append(t(480, 258, "闼", 9.0, RED, "middle", "bold"))
    # 脚印
    for i, x in enumerate((300, 330, 360, 390, 420, 450, 480)):
        s += footprint(x, 410 - i * 3)
    s.append(t(400, 442, "履我即", 8.0, BROWN, "middle"))
    s += foot("sj099a", "图一 · 东方之日　日、月、室、闼、履迹", "东方之日兮。彼姝者子，在我室兮。")
    return s


def fig099b():
    return fig2("099", "四", "东方之日　一进一出", "日入室，月入闼", [
        ("一章", "日 · 室 · 履我即", "来就"),
        ("二章", "月 · 闼 · 履我发", "行去"),
        ("收", "履迹 · 礼失", "门内一进"),
    ], "日在前，月在后；履迹一近，礼已不见", "sj099b", "九九",
        "跟得越紧，礼越远。")


# ---------- 100 东方未明 ----------

def robe(x, y, w=70, h=120, reverse=False):
    s = []
    # 衣身
    s.append(p("M %.0f %.0f L %.0f %.0f L %.0f %.0f L %.0f %.0f L %.0f %.0f L %.0f %.0f Z" %
               (x+18, y, x+w-18, y, x+w, y+26, x+w-4, y+h, x+4, y+h, x, y+26), 0.5))
    # 兩袖
    s.append(p("M %.0f %.0f L %.0f %.0f L %.0f %.0f L %.0f %.0f" %
               (x+10, y+22, x-18, y+42, x-10, y+64, x+14, y+46), 0.4))
    s.append(p("M %.0f %.0f L %.0f %.0f L %.0f %.0f L %.0f %.0f" %
               (x+w-10, y+22, x+w+18, y+42, x+w+10, y+64, x+w-14, y+46), 0.4))
    # 交領
    s.append(p("M %.0f %.0f L %.0f %.0f L %.0f %.0f" %
               (x+18, y, x+w/2, y+24, x+w-18, y), 0.35, BROWN))
    # 腰帶
    s.append(line(x+8, y+h*0.55, x+w-8, y+h*0.55, 0.35, BROWN))
    if reverse:
        return ['<g transform="rotate(180 %.0f %.0f)">' % (x+w/2, y+h/2)] + s + ['</g>']
    return s


def fig100a():
    s = head("100", "五", "东方未明　颠倒", "号令无节，衣冠先乱", "sj100a", "一百")
    # 左：未明天色
    s.append(line(44, 190, 220, 190, 0.4, BROWN))
    for x in (64, 96, 128, 160, 192):
        s.append(circ(x, 178, 1.6, 0.3, BROWN))
    s.append(t(132, 212, "东方未明", 8.8, RED, "middle", "bold"))
    # 中：颠倒衣裳
    s += robe(252, 258, 64, 112, False)
    s += robe(360, 270, 64, 112, True)
    s.append(line(252, 238, 424, 238, 0.3, BROWN))
    s.append(t(336, 232, "衣裳颠倒", 9.0, RED, "middle", "bold"))
    s.append(t(336, 402, "颠之倒之", 8.0, BROWN, "middle"))
    # 右：门与召
    s.append(rect(530, 260, 120, 150, 0.55))
    s.append(line(530, 260, 570, 220, 0.35))
    s.append(line(650, 260, 610, 220, 0.35))
    s.append(circ(560, 316, 5.0, 0.4, RED))
    s.append(p("M 600 320 L 600 350 L 618 350 L 618 320 Z", 0.3, BROWN))
    s.append(line(618, 320, 630, 320, 0.3, BROWN))
    s.append(t(590, 408, "自公召之", 8.0, BROWN, "middle"))
    s += foot("sj100a", "图一 · 东方未明　未明、颠倒衣裳、公召", "东方未明，颠倒衣裳。颠之倒之，自公召之。")
    return s


def fig100b():
    s = head("100", "五", "东方未明　漏刻", "柳藩不足恃，漏箭不正", "sj100b", "一百")
    # 左：漏壶
    s.append(p("M 104 262 L 158 262 L 158 282 C 188 294 196 322 192 350 C 188 388 166 404 134 404 C 100 404 80 388 76 350 C 72 322 82 294 110 282 Z", 0.55))
    s.append(line(98, 262, 164, 262, 0.45))
    s.append(p("M 158 292 C 178 288 188 302 182 316", 0.35, BROWN))
    s.append(line(88, 340, 182, 340, 0.3, BROWN))
    for y in (300, 324, 360, 382):
        s.append(line(86, y, 96, y, 0.25, BROWN))
        s.append(line(180, y, 190, y, 0.25, BROWN))
    # 漏箭
    s.append(line(132, 246, 132, 392, 0.45, RED))
    s.append(p("M 132 246 L 126 258 L 138 258 Z", 0.3, RED))
    s.append(line(122, 286, 142, 286, 0.3, RED))
    s.append(t(136, 226, "挈壶", 9.2, RED, "middle", "bold"))
    s.append(t(136, 424, "漏箭偏斜", 7.8, BROWN, "middle"))
    # 中：柳藩（折柳为篱，横编）
    for x in (270, 300, 330, 360, 390):
        s.append(line(x, 420, x+8, 300, 0.4, BROWN))
        s.append(p("M %d %d C %d %d %d %d %d %d" % (x+8, 300, x-4, 286, x+2, 274, x+10, 284), 0.3, BROWN))
    for y in (330, 360, 390):
        s.append(p("M 262 %d C 292 %d 312 %d 342 %d C 372 %d 388 %d 404 %d" %
                   (y, y-8, y+6, y-2, y+2, y-6, y), 0.35, BROWN))
    s.append(t(330, 286, "折柳樊圃", 8.6, RED, "middle", "bold"))
    # 右：狂夫
    s += person(560, 412, 116, 30, INK, 0.8)
    s.append(p("M 548 340 L 530 320 M 572 340 L 590 320", 0.35))
    s.append(t(560, 440, "狂夫瞿瞿", 7.8, BROWN, "middle"))
    s += foot("sj100b", "图二 · 东方未明　挈壶、柳藩、狂夫", "不能辰夜，不夙则莫。")
    return s


# ---------- 101 南山 ----------

def fig101a():
    s = head("101", "六", "南山　雄狐", "礼已尽，问不休", "sj101a", "一百零一")
    # 南山
    s.append(p("M 44 430 L 120 300 L 160 350 L 230 220 L 300 330 L 380 260 L 470 430", 0.7))
    s.append(p("M 60 410 L 122 330 L 158 356", 0.35, BROWN))
    s.append(p("M 300 330 L 380 276 L 452 420", 0.35, BROWN))
    s.append(t(170, 246, "南山崔崔", 9.0, RED, "middle", "bold"))
    # 狐：背、耳、尾、四足，不畫臉
    s.append(p("M 300 330 C 312 316 334 312 352 318 C 366 322 376 334 372 346 C 364 356 346 358 332 352 C 318 346 306 338 300 330 Z", 0.5))
    s.append(p("M 350 314 L 346 300 L 355 308 M 360 312 L 363 298 L 369 308", 0.35, BROWN))
    s.append(p("M 372 326 L 386 330 L 372 334", 0.3, BROWN))
    s.append(p("M 300 330 C 280 330 270 316 276 300 C 282 286 296 286 300 298", 0.45, BROWN))
    for dy in (-4, 2, 8):
        s.append(line(300, 302+dy, 286, 294+dy, 0.25, BROWN))
    for x in (316, 332, 348, 360):
        s.append(line(x, 352, x, 378, 0.3))
        s.append(line(x, 378, x-4, 382, 0.25, BROWN))
    s.append(t(340, 290, "雄狐", 8.4, BROWN, "middle"))
    # 鲁道
    s.append(line(500, 430, 710, 360, 0.55))
    s.append(line(520, 430, 710, 372, 0.3, BROWN))
    s.append(t(620, 410, "鲁道有荡", 9.0, RED, "middle", "bold"))
    # 归者背影
    s += person(690, 372, 86, 20, BROWN, 0.7)
    s.append(t(690, 392, "齐子由归", 7.4, BROWN, "middle"))
    s += foot("sj101a", "图一 · 南山　南山、雄狐、鲁道", "南山崔崔，雄狐绥绥。鲁道有荡，齐子由归。")
    return s


def fig101b():
    return fig2("101", "六", "南山　四问", "四问不答，礼已尽", [
        ("一问", "既曰归止 · 曷又怀止", "归/怀"),
        ("二问", "既曰庸止 · 曷又从止", "庸/从"),
        ("三问", "既曰告止 · 曷又鞠止", "告/鞠"),
        ("四问", "既曰得止 · 曷又极止", "得/极"),
    ], "礼一步，问一步；问的是礼，刺的是淫", "sj101b", "一百零一",
        "四问不答，答案在“曷又”。")


# ---------- 102 甫田 ----------

def fig102a():
    s = head("102", "七", "甫田　大与小", "田过大则莠，思过远则劳", "sj102a", "一百零二")
    # 大田
    for y in (260, 300, 340, 380):
        s.append(line(54, y, 360, y, 0.35, BROWN))
    for x in (54, 160, 266, 360):
        s.append(line(x, 250, x, 392, 0.3, BROWN))
    # 莠草：三葉一穗，高過禾
    for x in (86, 126, 166, 206, 246, 286, 326):
        s.append(p("M %d 332 C %d 310 %d 292 %d 276" % (x, x-6, x-12, x-16), 0.3, BROWN))
        s.append(p("M %d 332 C %d 314 %d 306 %d 288" % (x, x+2, x+4, x+2), 0.3, BROWN))
        s.append(p("M %d 332 C %d 312 %d 308 %d 282" % (x, x+9, x+14, x+16), 0.3, BROWN))
        s.append(p("M %d 278 C %d 268 %d 270 %d 282 C %d 292 %d 288 %d 278 Z" %
                   (x-16, x-18, x-14, x-12, x-10, x-14, x-16), 0.3, BROWN))
    s.append(t(208, 238, "维莠骄骄", 9.0, RED, "middle", "bold"))
    s.append(t(208, 414, "甫田", 8.0, BROWN, "middle"))
    # 童子与弁
    s += person(520, 420, 104, 26, INK, 0.8)
    s.append(circ(504, 322, 6.0, 0.35, BROWN))
    s.append(circ(536, 322, 6.0, 0.35, BROWN))
    s.append(t(520, 300, "总角丱兮", 7.6, BROWN, "middle"))
    # 弁冠在頭上
    s.append(p("M 500 300 L 510 278 L 530 278 L 540 300 Z", 0.45))
    s.append(line(500, 300, 540, 300, 0.35))
    s.append(line(520, 278, 520, 286, 0.3, BROWN))
    s.append(t(520, 268, "突而弁兮", 8.4, RED, "middle", "bold"))
    s += foot("sj102a", "图一 · 甫田　大田、莠、总角童子", "无田甫田，维莠骄骄。无思远人，劳心忉忉。")
    return s


def fig102b():
    return fig2("102", "七", "甫田　大中小", "田/思/序，一层收一层", [
        ("一章", "田甫田 · 莠骄骄", "力不给"),
        ("二章", "思远人 · 心忉忉", "人不至"),
        ("三章", "总角丱 · 突而弁", "循序至"),
    ], "田过大则莠，思过远则劳；从小至大，循序则成", "sj102b", "一百零二",
        "不是一跳就到，是循序而到。")


# ---------- 103 卢令 ----------

def fig103a():
    s = head("103", "八", "卢令　犬与人", "犬有环，人有德", "sj103a", "一百零三")
    # 犬背：身、頭、耳、尾、四足，不畫臉
    s.append(p("M 112 344 C 112 326 134 316 158 316 C 184 316 204 328 208 346 C 212 366 198 380 178 384 C 156 388 136 384 122 378 C 104 370 100 358 112 344 Z", 0.6))
    s.append(p("M 204 334 C 214 322 230 322 236 334 C 242 344 236 354 226 354", 0.5))
    s.append(p("M 214 324 L 214 308 L 222 318 M 228 318 L 230 304 L 236 316", 0.35, BROWN))
    s.append(p("M 236 340 L 248 340 L 236 346", 0.3, BROWN))
    s.append(p("M 112 344 C 92 344 82 330 86 314 C 90 300 102 300 106 312", 0.45, BROWN))
    for x in (126, 150, 176, 198):
        s.append(line(x, 380, x, 410, 0.35))
        s.append(line(x, 410, x-5, 416, 0.25, BROWN))
    # 頸環
    for dy in (0, 14, 28):
        s.append(p("M 196 %d C 204 %d 214 %d 220 %d" % (336+dy, 328+dy, 328+dy, 336+dy), 0.4, RED))
    s.append(t(170, 288, "卢令令", 8.8, RED, "middle", "bold"))
    # 人（只画冠须衣）
    s += person(560, 412, 120, 32, INK, 0.8)
    s.append(p("M 520 344 C 512 354 516 372 526 378 M 600 344 C 608 354 604 372 594 378", 0.35, BROWN))
    s.append(t(560, 300, "其人美且仁", 8.6, RED, "middle", "bold"))
    s.append(t(560, 440, "须鬓/才能", 7.6, BROWN, "middle"))
    s += foot("sj103a", "图一 · 卢令　田犬、环铃、人", "卢令令，其人美且仁。")
    return s


def fig103b():
    return fig2("103", "八", "卢令　三环三德", "环越重，铃越密", [
        ("一章", "卢令令 · 美且仁", "单环"),
        ("二章", "卢重环 · 美且鬈", "子母环"),
        ("三章", "卢重鋂 · 美且偲", "一环贯二"),
    ], "犬有环，人有德；田猎之誉，不在犬", "sj103b", "一百零三",
        "美到无可美，荒到无可荒。")


# ---------- 104 敝笱 ----------

def fish(x, y, w=34, h=18, color=INK):
    return [
        p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f Z" %
          (x, y, x+w*0.3, y-h, x+w*0.7, y-h, x+w, y,
           x+w*0.7, y+h, x+w*0.3, y+h, x, y), 0.4, color),
        p("M %.0f %.0f L %.0f %.0f L %.0f %.0f" % (x, y, x-8, y-7, x-8, y+7), 0.3, color),
    ]


def fig104a():
    s = head("104", "九", "敝笱　鱼过", "笱破不能制鱼", "sj104a", "一百零四")
    # 鱼梁
    s.append(line(44, 388, 710, 388, 0.55, BROWN))
    for x in (70, 120, 170, 220, 270, 320):
        s.append(line(x, 388, x, 420, 0.3, BROWN))
    # 破笱：右壁缺口
    s.append(p("M 160 300 L 300 300 L 300 326", 0.55))
    s.append(p("M 300 354 L 292 380 L 170 380 L 160 300", 0.55))
    for x in (180, 205, 230, 255, 280):
        s.append(line(x, 300, x, 380, 0.3, BROWN))
    for y in (320, 348):
        s.append(line(166, y, 294, y, 0.3, BROWN))
    s.append(p("M 300 326 L 310 336 L 300 346", 0.4, RED))
    s.append(t(228, 286, "敝笱在梁", 8.8, RED, "middle", "bold"))
    # 鱼出缺口
    for i, (x, y) in enumerate(((312, 340), (372, 356), (432, 340))):
        s += fish(x, y, 52, 22)
        s.append(t(x+20, y+34, ("鲂鳏", "鲂鱮", "唯唯")[i], 7.4, BROWN, "middle"))
    # 从者
    for i in range(5):
        s += person(560 + i*30, 420, 60, 12, BROWN, 0.6)
    s.append(t(620, 444, "其从如云", 7.4, BROWN, "middle"))
    s += foot("sj104a", "图一 · 敝笱　破笱、鱼、从者", "敝笱在梁，其鱼鲂鳏。齐子归止，其从如云。")
    return s


def fig104b():
    return fig2("104", "九", "敝笱　不能制", "鱼越大，笱越显破", [
        ("一章", "鲂鳏 · 如云", "大鱼出"),
        ("二章", "鲂鱮 · 如雨", "从更密"),
        ("三章", "唯唯 · 如水", "流更远"),
    ], "笱破不能制鱼，夫弱不能制妻；从者越多，恶越大", "sj104b", "一百零四",
        "诗不写淫，只写从。")


# ---------- 105 载驱 ----------

def fig105a():
    s = head("105", "十", "载驱　车与路", "车越盛，路越荡", "sj105a", "一百零五")
    # 车后户
    s.append(circ(180, 372, 34, 0.55))
    s.append(circ(180, 372, 5, 0.4, BROWN))
    s.append(rect(200, 300, 180, 100, 0.55))
    s.append(line(200, 330, 380, 330, 0.3, BROWN))
    s.append(line(200, 360, 380, 360, 0.3, BROWN))
    for x in (220, 250, 280, 310, 340, 370):
        s.append(line(x, 300, x, 400, 0.3, BROWN))
    s.append(p("M 380 300 L 410 320 L 410 380 L 380 400", 0.45, RED))
    s.append(t(290, 286, "簟茀朱鞟", 8.8, RED, "middle", "bold"))
    # 四骊：只畫四轡與八蹄，不畫馬身
    s.append(line(440, 286, 600, 286, 0.35, BROWN))
    for x in (456, 496, 536, 576):
        s.append(circ(x, 286, 4.0, 0.3, RED))
        s.append(p("M %d 286 C %d 320 %d 354 %d 386" % (x, x-4, x+4, x), 0.35, BROWN))
        for dx in (-5, 5):
            s.append(p("M %d 396 C %d 390 %d 394 %d 402" % (x+dx, x+dx-4, x+dx-4, x+dx), 0.3, BROWN))
    s.append(t(516, 262, "四骊济济", 8.4, BROWN, "middle"))
    # 水
    for y in (400, 414):
        s.append(p("M 440 %d C 480 %d 520 %d 560 %d 600 %d 640 %d 680 %d" %
                   (y, y-6, y+2, y-4, y-8, y+2, y), 0.3, BROWN, opacity=0.6))
    s.append(t(560, 438, "汶水汤汤", 7.6, BROWN, "middle"))
    s += foot("sj105a", "图一 · 载驱　车、簟茀、四骊、汶水", "载驱薄薄，簟茀朱鞟。鲁道有荡，齐子发夕。")
    return s


def fig105b():
    return fig2("105", "十", "载驱　四程", "夜行、乐易、闲游、纵放", [
        ("一章", "发夕 · 夜行", "离宿至旦"),
        ("二章", "岂弟 · 乐易", "无所愧"),
        ("三章", "翱翔 · 闲游", "示众"),
        ("四章", "游遨 · 纵放", "恶远播"),
    ], "车越盛，路越荡；不是赶路，是示众", "sj105b", "一百零五",
        "恶越远，车越轻。")


# ---------- 106 猗嗟 ----------

def arrow(x, y, dx=0, dy=-16, color=RED):
    return [
        line(x, y, x+dx, y+dy, 0.35, color),
        p("M %.0f %.0f L %.0f %.0f L %.0f %.0f" % (x+dx, y+dy, x+dx-4, y+dy+8, x+dx+4, y+dy+8), 0.3, color),
    ]


def fig106a():
    s = head("106", "十一", "猗嗟　威仪技艺", "美越全，缺越显", "sj106a", "一百零六")
    # 鲁君：不画脸，眼线浮在头侧
    s += person(210, 420, 160, 42, INK, 0.9)
    s.append(p("M 180 286 C 190 280 200 282 206 288 M 214 288 C 220 282 230 280 240 286", 0.3, RED))
    s.append(t(210, 258, "美目扬兮", 7.6, BROWN, "middle"))
    s.append(p("M 178 360 L 170 400 M 242 360 L 250 400", 0.3, BROWN))
    s.append(t(210, 446, "巧趋跄兮", 7.6, BROWN, "middle"))
    # 射侯
    s.append(rect(430, 230, 180, 180, 0.55))
    s.append(rect(470, 270, 100, 100, 0.4, BROWN))
    s.append(rect(495, 295, 50, 50, 0.4, RED))
    s.append(t(520, 222, "侯", 8.8, RED, "middle", "bold"))
    s.append(t(520, 324, "正", 9.2, RED, "middle", "bold"))
    for i, (x, y) in enumerate(((508, 300), (526, 306), (514, 318), (534, 320))):
        s += arrow(x, y+20, dx=0, dy=-18)
    s.append(t(520, 442, "四矢反兮", 7.8, BROWN, "middle"))
    # 弓与弦
    s.append(p("M 668 230 C 636 268 636 342 668 380", 0.45, BROWN))
    s.append(line(668, 230, 668, 380, 0.25, BROWN))
    s.append(line(610, 305, 668, 305, 0.3, RED))
    s.append(p("M 610 305 L 618 300 L 618 310", 0.25, RED))
    s.append(t(690, 306, "射则臧", 7.4, BROWN, "middle"))
    s += foot("sj106a", "图一 · 猗嗟　美目、趋跄、射侯、四矢", "猗嗟昌兮，颀而长兮。巧趋跄兮，射则臧兮。")
    return s


def fig106b():
    s = head("106", "十一", "猗嗟　一缺", "威仪、技艺、射艺皆备，独缺防闲", "sj106b", "一百零六")
    # 三满格
    boxes = [(60, "威仪", "貌·仪"), (230, "技艺", "舞·射"), (400, "射艺", "正·贯")]
    for x, name, sub in boxes:
        s.append(rect(x, 220, 140, 120, 0.55))
        s.append(t(x+70, 258, name, 13.0, INK, "middle", "bold"))
        s.append(t(x+70, 292, sub, 9.0, BROWN, "middle"))
        s.append(line(x+20, 316, x+120, 316, 0.35, RED))
    # 空一格
    s.append(rect(576, 220, 130, 120, 0.6, RED))
    s.append(t(641, 258, "防闲其母", 10.4, RED, "middle", "bold"))
    s.append(t(641, 292, "独缺", 9.2, BROWN, "middle"))
    s.append(line(550, 280, 570, 280, 0.4, RED))
    s.append(t(560, 264, "缺", 8.0, RED, "middle"))
    # 底：甥
    s.append(line(50, 380, 710, 380, 0.35, GOLD))
    s.append(t(380, 410, "展我甥兮：明说是齐甥，正为驳“齐侯之子”", 10.2, INK, "middle", "bold", 0.4))
    s.append(t(380, 438, "美越全，缺越显；惜乎其独少此耳", 9.4, BROWN, "middle"))
    s.append(t(380, 486, "图二 · 义理", 8.6, BROWN, "middle"))
    s.append('<rect x="676" y="492" width="22" height="22" fill="%s" opacity="0.13"/>' % RED)
    s.append(t(687, 507, "润", 8.8, RED, "middle"))
    return s


FIGS = [fig096a, fig096b, fig097a, fig097b, fig098a, fig098b, fig099a, fig099b,
        fig100a, fig100b, fig101a, fig101b, fig102a, fig102b, fig103a, fig103b,
        fig104a, fig104b, fig105a, fig105b, fig106a, fig106b]

KEYS = {
    "sj096a": "sj096a-ji-ming-cang-ying", "sj096b": "sj096b-san-gao",
    "sj097a": "sj097a-qiu-shan-lie", "sj097b": "sj097b-san-yu",
    "sj098a": "sj098a-zhu-ting-tang", "sj098b": "sj098b-san-jin",
    "sj099a": "sj099a-dong-fang-ri-yue", "sj099b": "sj099b-lu-ji",
    "sj100a": "sj100a-dian-dao-yi-shang", "sj100b": "sj100b-lou-ke",
    "sj101a": "sj101a-nan-shan-xiong-hu", "sj101b": "sj101b-si-wen",
    "sj102a": "sj102a-fu-tian-you-zi", "sj102b": "sj102b-xu",
    "sj103a": "sj103a-lu-ling", "sj103b": "sj103b-san-huan",
    "sj104a": "sj104a-bi-gou", "sj104b": "sj104b-yu-gou",
    "sj105a": "sj105a-zai-qu", "sj105b": "sj105b-si-cheng",
    "sj106a": "sj106a-yi-jie", "sj106b": "sj106b-mei-que",
}


def main():
    os.makedirs(OUT, exist_ok=True)
    for fn in FIGS:
        body = fn()
        code = KEYS[fn.__name__.replace("fig", "sj")]
        svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 540" width="760" height="540">\n'
               + "\n".join(body) + "\n</svg>\n")
        path = os.path.join(OUT, code + ".svg")
        open(path, "w", encoding="utf-8").write(svg)
        print("wrote", path, len(svg))


if __name__ == "__main__":
    main()
