# -*- coding: utf-8 -*-
"""生成 SJ089–SJ095 的图一（名物）与图二（义理），共 14 张。
郑风收尾七篇：东门之墠、风雨、子衿、扬之水、出其东门、野有蔓草、溱洧。
白描，不填大面；全部 760x540，纸墨五色。
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
    return (
        '<rect width="760" height="540" fill="%s"/>' % PAPER,
        '<rect x="10" y="10" width="740" height="520" fill="none" stroke="%s" stroke-width="0.6"/>' % LINE,
        '<rect x="22" y="28" width="716" height="470" fill="none" stroke="%s" stroke-width="0.8"/>' % LINE,
        t(38, 62, "郑 风 · 之%s" % vol, 9.5, RED, ls=2),
        t(380, 72, title, 25, INK, "middle", "bold", 1.6),
        t(720, 62, "诗三百五篇 · 之%s" % zh_no, 8.6, BROWN, "end", ls=1),
        line(38, 100, 722, 100, 0.35, GOLD),
        t(380, 122, sub, 10.2, BROWN, "middle", ls=1),
    )


def foot(code, caption, quote=""):
    s = []
    if quote:
        s.append(t(380, 468, quote, 12.8, RED, "middle", ls=1.0))
    s.append(t(380, 506, caption, 9.2, BROWN, "middle", ls=1))
    s.append('<rect x="676" y="492" width="22" height="22" fill="%s" opacity="0.13"/>' % RED)
    s.append(t(687, 507, "润", 8.8, RED, "middle"))
    return s


def person(cx, base_y, ht=126, wd=34, color=INK, opacity=1):
    """有头无脸的人形：头、肩、交领、长衣、双袖。"""
    s = []
    hr = ht * 0.075
    s.append(circ(cx, base_y - ht + hr, hr, 0.45, color))
    s.append(line(cx, base_y - ht + 2 * hr, cx, base_y - ht * 0.78, 0.35, color, opacity))
    s.append(p("M %d %d L %d %d L %d %d L %d %d L %d %d L %d %d Z" %
               (cx - wd * 0.55, base_y - ht * 0.78,
                cx - wd, base_y - ht * 0.40,
                cx - wd * 0.88, base_y,
                cx + wd * 0.88, base_y,
                cx + wd, base_y - ht * 0.40,
                cx + wd * 0.55, base_y - ht * 0.78), 0.5, color, opacity=opacity))
    s.append(p("M %d %d L %d %d L %d %d" %
               (cx - wd * 0.55, base_y - ht * 0.78, cx, base_y - ht * 0.62,
                cx + wd * 0.55, base_y - ht * 0.78), 0.35, color, opacity=opacity))
    s.append(line(cx - wd * 0.82, base_y - ht * 0.58, cx - wd * 1.02, base_y - ht * 0.22, 0.3, color, opacity))
    s.append(line(cx + wd * 0.82, base_y - ht * 0.58, cx + wd * 1.02, base_y - ht * 0.22, 0.3, color, opacity))
    return s


def fig2(no, vol, title, sub, rows, conclusion, code, zh_no, coda=""):
    s = list(head(no, vol, title, sub, code, zh_no))
    ys = (180, 250, 320)
    for i, row in enumerate(rows[:3]):
        y = ys[i]
        s.append(line(44, y + 22, 716, y + 22, 0.3, LINE))
        s.append(t(62, y, row[0], 10.4, INK, "start", "bold"))
        s.append(t(226, y, row[1], 10.8, INK, "start"))
        s.append(t(566, y, row[2], 9.4, BROWN, "start"))
    s.append(line(204, 160, 204, 356, 0.55, RED))
    s.append(line(204, 160, 212, 160, 0.4, RED))
    s.append(line(204, 356, 212, 356, 0.4, RED))
    s.append(line(548, 168, 548, 350, 0.35, BROWN))
    s.append(line(544, 168, 552, 168, 0.3, BROWN))
    s.append(line(544, 350, 552, 350, 0.3, BROWN))
    s.append(line(50, 388, 710, 388, 0.35, GOLD))
    s.append(t(380, 414, conclusion, 12.0, RED, "middle", "bold", 0.8))
    if coda:
        s.append(t(380, 438, coda, 8.8, BROWN, "middle", ls=0.4))
    s.append(t(380, 486, "图二 · 义理", 8.6, BROWN, "middle"))
    s.append('<rect x="676" y="492" width="22" height="22" fill="%s" opacity="0.13"/>' % RED)
    s.append(t(687, 507, "润", 8.8, RED, "middle"))
    return s


# ---------- 089 东门之墠 ----------

def fig089a():
    s = list(head("089", "十五", "东门之墠　近", "平地看得见，门走不进", "sj089a", "八九"))
    # 左：东门与墠
    s.append(line(64, 190, 64, 420, 0.5))
    s.append(line(210, 190, 210, 420, 0.5))
    s.append(line(64, 190, 210, 190, 0.45))
    s.append(p("M 64 420 L 210 420 L 230 442 L 84 442 Z", 0.4, BROWN))
    s.append(t(137, 176, "东门", 9.5, RED, "middle", "bold"))
    s.append(rect(82, 360, 108, 46, 0.35, BROWN))
    s.append(t(137, 390, "墠", 9.4, INK, "middle", "bold"))
    # 中：阪与茹藘
    s.append(line(230, 430, 430, 292, 0.65))
    s.append(line(250, 430, 440, 300, 0.3, BROWN))
    s.append(t(335, 278, "阪", 9.4, RED, "middle", "bold"))
    for x, y in ((260, 404), (292, 382), (326, 358), (360, 334), (394, 312)):
        s.append(line(x, y, x - 2, y + 28, 0.35, BROWN))
        s.append(p("M %d %d C %d %d %d %d %d %d C %d %d %d %d %d %d Z" %
                   (x, y, x - 14, y - 12, x - 20, y - 2, x - 10, y + 4,
                    x - 4, y + 7, x + 3, y + 2, x, y), 0.45, BROWN))
        s.append(p("M %d %d C %d %d %d %d %d %d" %
                   (x - 2, y + 28, x - 8, y + 38, x + 2, y + 44, x - 4, y + 52), 0.35, RED, opacity=0.7))
    s.append(t(290, 330, "茹藘", 9.2, RED, "middle", "bold"))
    s.append(t(318, 350, "茜草，可染绛", 7.8, BROWN, "middle"))
    # 右：栗树与成行家室
    s.append(line(600, 420, 600, 250, 0.55))
    s.append(p("M 600 300 C 570 280 548 286 530 300", 0.4, BROWN))
    s.append(p("M 600 330 C 632 310 654 316 672 330", 0.4, BROWN))
    for cx, cy in ((542, 310), (578, 290), (628, 314), (662, 338)):
        s.append(p("M %d %d C %d %d %d %d %d %d C %d %d %d %d %d %d Z" %
                   (cx, cy, cx - 9, cy - 10, cx + 4, cy - 14, cx + 7, cy - 3,
                    cx + 5, cy + 6, cx - 4, cy + 5, cx, cy), 0.4, BROWN))
    s.append(t(600, 234, "栗", 9.5, RED, "middle", "bold"))
    for x in (548, 604, 660):
        s.append(p("M %d 420 L %d 390 L %d 390 L %d 420 Z" % (x, x, x + 46, x + 46), 0.45))
        s.append(p("M %d 390 L %d 374 L %d 374 L %d 390 Z" % (x, x + 6, x + 40, x + 46), 0.4))
    s.append(t(604, 452, "有践家室", 8.6, BROWN, "middle"))
    s.append(t(72, 150, "室迩", 9.5, RED))
    s.append(t(664, 150, "人远", 9.5, RED, "end"))
    s += foot("sj089a", "图一 · 东门之墠　墠、阪、茹藘、栗", "东门之墠，茹藘在阪。其室则迩，其人甚远。")
    return s


def fig089b():
    return fig2("089", "十五", "东门之墠　近远", "门可看见，人不可即", [
        ("一章", "墠平 · 阪高 · 茹藘在阪", "地有难易"),
        ("二章", "栗树 · 有践家室", "家可指认"),
        ("收", "岂不尔思 · 子不我即", "远在对方"),
    ], "室可迩，人不可即；路可平，礼不可越", "sj089b", "八九",
        "不是我不去，是你不来就。")


# ---------- 090 风雨 ----------

def fig090a():
    s = list(head("090", "十六", "风雨　鸡鸣", "天越暗，鸡越不停", "sj090a", "九十"))
    # 三层风雨
    for i, x0 in enumerate((56, 300, 546)):
        op = 0.38 + i * 0.12
        for k in range(5):
            x = x0 + 10 + k * 18
            s.append(line(x, 150, x - 24, 260, 0.35, BROWN, opacity=op))
        for k in range(4):
            y = 180 + k * 36
            s.append(p("M %d %d C %d %d %d %d %d %d" % (x0, y, x0 + 46, y - 4, x0 + 82, y + 5, x0 + 118, y), 0.3, BROWN, opacity=0.45))
    s.append(t(112, 290, "凄凄", 9.0, BROWN, "middle"))
    s.append(t(358, 290, "潇潇", 9.0, BROWN, "middle"))
    s.append(t(606, 290, "如晦", 9.0, RED, "middle", "bold"))
    # 鸡埘
    s.append(rect(390, 344, 96, 78, 0.55))
    s.append(line(390, 374, 486, 374, 0.35, BROWN))
    s.append(p("M 408 344 L 408 322 L 470 322 L 470 344", 0.5))
    # 鸡：头、冠、喙、身、尾、足
    s.append(p("M 424 350 C 418 332 424 318 436 318 C 446 318 448 330 442 340", 0.55))
    s.append(p("M 436 318 L 432 308 L 438 306 L 440 314", 0.4, RED))
    s.append(p("M 448 330 L 456 332 L 448 336", 0.35, RED))
    s.append(p("M 424 350 C 402 368 404 402 430 408 C 456 412 472 392 466 366 C 464 352 452 344 442 344", 0.55))
    s.append(p("M 424 380 C 412 392 416 404 430 406", 0.35, BROWN))
    s.append(p("M 466 366 C 486 352 498 356 506 370", 0.4, BROWN))
    for dy in (-6, 0, 6):
        s.append(line(466, 366 + dy, 496, 372 + dy, 0.28, BROWN, opacity=0.7))
    s.append(line(434, 408, 430, 430, 0.4))
    s.append(line(456, 408, 460, 430, 0.4))
    s.append(t(438, 452, "鸡栖于埘", 8.6, BROWN, "middle"))
    # 门与灯
    s.append(rect(620, 300, 96, 140, 0.55))
    s.append(line(620, 300, 680, 250, 0.4))
    s.append(line(716, 300, 656, 250, 0.4))
    s.append(p("M 654 440 L 654 352 L 684 352 L 684 440", 0.4))
    s.append(circ(660, 380, 5, 0.45, RED))
    s.append(t(668, 470, "既见", 8.6, RED, "middle"))
    s.append(t(112, 160, "风雨不改", 8.8, BROWN, "middle"))
    s.append(t(596, 160, "鸡鸣不已", 8.8, BROWN, "middle"))
    s += foot("sj090a", "图一 · 风雨　风雨、鸡埘、门灯", "风雨如晦，鸡鸣不已。既见君子，云胡不喜。")
    return s


def fig090b():
    return fig2("090", "十六", "风雨　三见三定", "外面越乱，里面越定", [
        ("一章", "凄凄 · 喈喈", "夷：平"),
        ("二章", "潇潇 · 胶胶", "瘳：病愈"),
        ("三章", "如晦 · 不已", "喜：心亮"),
    ], "三见，三定；风雨未停，心已停", "sj090b", "九十",
        "鸡不改时，君子不改度。")


# ---------- 091 子衿 ----------

def fig091a():
    s = list(head("091", "十七", "子衿　城阙", "青在领上，不在脸上", "sj091a", "九一"))
    # 衣领
    s.append(p("M 90 190 L 150 190 L 172 220 L 160 410 L 80 410 L 68 220 Z", 0.65))
    s.append(p("M 90 190 L 120 250 L 150 190", 0.55))
    s.append(p("M 104 190 L 120 250 L 136 190", 0.35, BROWN))
    s.append(p("M 68 220 L 56 300 L 70 410", 0.4, BROWN))
    s.append(p("M 172 220 L 184 300 L 170 410", 0.4, BROWN))
    s.append(t(120, 176, "衿", 10.0, RED, "middle", "bold"))
    s.append(t(120, 438, "青领", 8.3, BROWN, "middle"))
    # 佩玉
    s.append(line(300, 210, 300, 250, 0.35, BROWN))
    s.append(line(380, 210, 380, 250, 0.35, BROWN))
    s.append(p("M 300 250 C 318 262 362 262 380 250", 0.45, BROWN))
    s.append(circ(340, 276, 16, 0.55))
    s.append(circ(340, 276, 7, 0.35, BROWN))
    s.append(line(324, 276, 308, 300, 0.35, BROWN))
    s.append(line(356, 276, 372, 300, 0.35, BROWN))
    s.append(p("M 308 300 L 314 330 L 302 330 L 308 300", 0.4))
    s.append(p("M 372 300 L 378 330 L 366 330 L 372 300", 0.4))
    s.append(t(340, 196, "佩", 9.8, RED, "middle", "bold"))
    s.append(t(340, 356, "青组绶", 8.2, BROWN, "middle"))
    # 城阙：城墙、城垛、双阙、门洞
    s.append(rect(530, 300, 170, 130, 0.55))
    s.append(rect(548, 246, 134, 54, 0.5))
    s.append(p("M 520 246 L 615 206 L 710 246", 0.55))
    s.append(p("M 590 430 L 590 340 L 636 340 L 636 430", 0.4))
    for x in range(540, 700, 22):
        s.append(rect(x, 286, 12, 14, 0.3, BROWN))
    for x in range(558, 682, 20):
        s.append(rect(x, 234, 10, 12, 0.3, BROWN))
    s.append(rect(508, 340, 22, 90, 0.4, BROWN))
    s.append(rect(700, 340, 22, 90, 0.4, BROWN))
    s.append(line(548, 300, 710, 300, 0.3, BROWN))
    s.append(line(548, 330, 710, 330, 0.3, BROWN))
    s.append(t(615, 190, "城阙", 9.8, RED, "middle", "bold"))
    s.append(t(615, 452, "登高而望", 8.2, BROWN, "middle"))
    s.append(t(62, 150, "青青子衿", 8.8, RED))
    s += foot("sj091a", "图一 · 子衿　衿、佩、城阙", "青青子衿，悠悠我心。纵我不往，子宁不嗣音？")
    return s


def fig091b():
    return fig2("091", "十七", "子衿　一日三月", "等得站不住，一天成三个月", [
        ("往", "纵我不往", "退一步"),
        ("来", "子宁不嗣音 / 不来", "进一句"),
        ("等", "挑兮达兮 · 在城阙", "站不住"),
    ], "衿可青，音不可断；一日可度，三月难挨", "sj091b", "九一",
        "反问是最后一条路。")


# ---------- 092 扬之水 ----------

def fig092a():
    s = list(head("092", "十八", "扬之水　不流", "水急，不等于有力", "sj092a", "九二"))
    # 水
    for i, y in enumerate((232, 270, 308, 346)):
        s.append(p("M 56 %d C 130 %d 200 %d 270 %d C 330 %d 380 %d 446 %d" %
                   (y, y - 14, y + 12, y - 2, y + 8, y - 10, y + 4), 0.45, BROWN, opacity=0.7))
    s.append(t(160, 392, "扬之水", 9.0, RED, "middle", "bold"))
    # 岸与两捆柴
    s.append(line(446, 210, 446, 430, 0.4, BROWN))
    for x, y, name in ((492, 330, "束楚"), (628, 330, "束薪")):
        for k in range(4):
            s.append(line(x + k * 9, y, x - 12 + k * 9, y + 88, 0.45, BROWN))
        s.append(line(x - 12, y + 22, x + 44, y + 16, 0.55, RED, opacity=0.7))
        s.append(line(x - 16, y + 60, x + 48, y + 54, 0.55, RED, opacity=0.7))
        s.append(t(x + 16, y - 14, name, 9.2, RED, "middle", "bold"))
    s.append(t(560, 438, "水过柴不移", 8.4, BROWN, "middle"))
    s.append(t(62, 160, "急而无力", 9.2, RED))
    s += foot("sj092a", "图一 · 扬之水　急流、束楚、束薪", "扬之水，不流束楚。终鲜兄弟，维予与女。")
    return s


def fig092b():
    return fig2("092", "十八", "扬之水　只二人", "水不流，言不信", [
        ("水", "扬之水 · 不流束楚", "势急"),
        ("言", "人实迋女 · 人实不信", "言多"),
        ("人", "终鲜兄弟 · 维予二人", "只剩二"),
    ], "水急不能流，言多不能信；所恃只二人", "sj092b", "九二",
        "二人之外，皆是外人。")


# ---------- 093 出其东门 ----------

def fig093a():
    s = list(head("093", "十九", "出其东门　如云", "众到没有脸，才见一个", "sj093a", "九三"))
    # 东门
    s.append(line(58, 190, 58, 420, 0.5))
    s.append(line(186, 190, 186, 420, 0.5))
    s.append(line(58, 190, 186, 190, 0.45))
    s.append(p("M 44 190 L 122 154 L 200 190", 0.5))
    s.append(p("M 94 420 L 94 330 L 150 330 L 150 420", 0.4))
    s.append(t(122, 176, "东门", 9.2, RED, "middle", "bold"))
    # 如云 / 如荼：人形与白花
    for x, h in ((238, 120), (286, 132), (334, 124), (382, 138)):
        s += person(x, 404, ht=h, wd=28, color=BROWN, opacity=0.72)
    s.append(t(310, 212, "如云", 8.8, BROWN, "middle"))
    for x, y in ((430, 352), (460, 362), (490, 348), (520, 360)):
        for k in range(5):
            ang = math.radians(k * 72)
            s.append(line(x, y, x + 15 * math.cos(ang), y + 15 * math.sin(ang), 0.28, BROWN))
        s.append(circ(x, y, 3, 0.4, RED))
    s.append(t(475, 392, "如荼", 8.8, BROWN, "middle"))
    # 缟衣綦巾：一人独立于众外
    s += person(588, 416, ht=150, wd=40, color=INK)
    s.append(p("M 574 282 C 574 258 602 258 602 282", 0.45, BROWN))
    s.append(t(588, 246, "缟衣綦巾", 8.6, RED, "middle", "bold"))
    s.append(t(588, 440, "一人", 8.6, BROWN, "middle"))
    s.append(t(62, 150, "有女如云", 8.8, RED))
    s.append(t(680, 150, "匪我思存", 8.8, RED, "end"))
    s += foot("sj093a", "图一 · 出其东门　东门、如云、如荼、素衣", "出其东门，有女如云。虽则如云，匪我思存。")
    return s


def fig093b():
    return fig2("093", "十九", "出其东门　众与一", "如云不如一人，如荼不如素衣", [
        ("一章", "如云 · 匪我思存", "众"),
        ("二章", "如荼 · 匪我思且", "更多"),
        ("一人", "缟衣綦巾 / 缟衣茹藘", "素"),
    ], "众美不如一人，素衣才安", "sj093b", "九三",
        "不是不见众，是见了众仍选一。")


# ---------- 094 野有蔓草 ----------

def fig094a():
    s = list(head("094", "二十", "野有蔓草　春露", "露未干，人未老", "sj094a", "九四"))
    # 草地：蔓草有横走茎，不是一根一根
    for x in (86, 210, 330, 452, 574, 690):
        s.append(p("M %d 420 C %d 412 %d 414 %d 420" % (x - 22, x - 8, x + 18, x + 34), 0.35, BROWN, opacity=0.55))
        for k in range(4):
            bx = x - 14 + k * 10
            s.append(p("M %d 420 C %d 388 %d 366 %d 354" % (bx, bx - 16, bx + 16, bx + 4), 0.4, BROWN, opacity=0.65))
        s.append(p("M %d 420 C %d 394 %d 398 %d 378" % (x, x + 14, x + 28, x + 24), 0.3, BROWN, opacity=0.5))
    # 露珠：落在叶尖与草叶上
    for x, y in ((92, 358), (156, 372), (226, 346), (300, 368), (438, 360), (512, 370), (646, 352)):
        s.append(p("M %d %d C %d %d %d %d %d %d C %d %d %d %d %d %d Z" %
                   (x, y, x - 4, y - 8, x + 4, y - 10, x + 5, y - 2,
                    x + 4, y + 4, x - 2, y + 4, x, y), 0.35, BROWN))
    s.append(t(366, 338, "零露", 8.8, RED, "middle", "bold"))
    s.append(t(366, 386, "蔓草", 8.8, BROWN, "middle"))
    # 两个人：有头无脸，一左一右
    s += person(282, 420, ht=130, wd=32, color=BROWN, opacity=0.9)
    s += person(496, 420, ht=130, wd=32, color=RED, opacity=0.8)
    s.append(t(282, 276, "一人", 8.0, BROWN, "middle"))
    s.append(t(496, 276, "一人", 8.0, RED, "middle"))
    s.append(t(372, 288, "邂逅", 9.0, RED, "middle", "bold"))
    s.append(line(322, 320, 450, 320, 0.35, BROWN, opacity=0.55))
    s += foot("sj094a", "图一 · 野有蔓草　蔓草、零露、两人", "野有蔓草，零露漙兮。有美一人，清扬婉兮。")
    return s


def fig094b():
    return fig2("094", "二十", "野有蔓草　时与遇", "不期而会，各得其所", [
        ("时", "蔓草 · 零露漙 / 瀼瀼", "春"),
        ("遇", "邂逅相遇", "不期"),
        ("愿", "适我愿 · 与子偕臧", "各得"),
    ], "露未干，人未老；邂逅不是约", "sj094b", "九四",
        "时不可约，愿可定。")


# ---------- 095 溱洧 ----------

def fig095a():
    s = list(head("095", "二十一", "溱洧　兰与勺药", "礼不在，花为凭", "sj095a", "九五"))
    # 两水：岸线、波纹、流向
    for x0, name in ((86, "溱"), (566, "洧")):
        s.append(p("M %d 188 C %d 258 %d 342 %d 432" % (x0 - 2, x0 - 22, x0 + 24, x0 - 2), 0.5, BROWN))
        s.append(p("M %d 188 C %d 258 %d 342 %d 432" % (x0 + 54, x0 + 28, x0 + 74, x0 + 52), 0.5, BROWN))
        for k in range(5):
            y = 220 + k * 40
            s.append(p("M %d %d C %d %d %d %d %d %d" % (x0 + 6, y, x0 + 20, y - 6, x0 + 38, y + 6, x0 + 48, y), 0.3, BROWN, opacity=0.55))
        s.append(t(x0 + 26, 176, name, 9.8, RED, "middle", "bold"))
    # 兰草：三茎，对叶，顶生小花（不是兰花）
    for sx in (330, 346, 362):
        s.append(line(sx, 386, sx - 2, 286, 0.45, BROWN))
        for k in range(3):
            y = 356 - k * 26
            s.append(p("M %d %d C %d %d %d %d %d %d C %d %d %d %d %d %d Z" %
                       (sx, y, sx - 12, y - 10, sx - 24, y - 6, sx - 26, y + 2,
                        sx - 24, y + 8, sx - 12, y + 6, sx, y), 0.35, BROWN))
            s.append(p("M %d %d C %d %d %d %d %d %d C %d %d %d %d %d %d Z" %
                       (sx, y - 12, sx + 12, y - 22, sx + 24, y - 18, sx + 26, y - 10,
                        sx + 24, y - 4, sx + 12, y - 6, sx, y - 12), 0.35, BROWN))
        for dx, dy in ((-5, -2), (4, -5), (0, 5)):
            s.append(circ(sx + dx, 284 + dy, 3.2, 0.35, RED))
    s.append(t(346, 238, "蕳（兰）", 8.8, RED, "middle", "bold"))
    # 勺药：三朵五瓣，带叶
    for x, y in ((474, 358), (514, 334), (554, 362)):
        for k in range(5):
            ang = math.radians(k * 72 - 90)
            s.append(p("M %d %d C %d %d %d %d %d %d C %d %d %d %d %d %d Z" %
                       (x, y, x + 8 * math.cos(ang) - 5, y + 8 * math.sin(ang) - 5,
                        x + 18 * math.cos(ang) + 2, y + 18 * math.sin(ang) + 2,
                        x + 22 * math.cos(ang), y + 22 * math.sin(ang),
                        x + 18 * math.cos(ang) - 2, y + 18 * math.sin(ang) - 2,
                        x + 8 * math.cos(ang) + 5, y + 8 * math.sin(ang) + 5, x, y), 0.38, RED, opacity=0.75))
        s.append(circ(x, y, 3, 0.4, BROWN))
        s.append(line(x, y + 22, x, y + 52, 0.3, BROWN))
        s.append(p("M %d %d C %d %d %d %d %d %d" % (x, y + 36, x + 16, y + 40, x + 24, y + 30, x + 28, y + 22), 0.3, BROWN))
    s.append(t(514, 406, "勺药", 8.8, RED, "middle", "bold"))
    # 士女：有头无脸
    s += person(226, 416, ht=132, wd=32, color=BROWN)
    s += person(414, 416, ht=126, wd=30, color=RED, opacity=0.85)
    s.append(p("M 396 292 C 396 270 432 270 432 292", 0.35, RED, opacity=0.7))
    s.append(t(226, 270, "士", 8.2, BROWN, "middle"))
    s.append(t(414, 270, "女", 8.2, RED, "middle"))
    s.append(t(372, 160, "涣涣", 9.0, RED, "middle"))
    s += foot("sj095a", "图一 · 溱洧　两水、蕳、勺药", "溱与洧，方涣涣兮。士与女，方秉蕳兮。")
    return s


def fig095b():
    s = list(head("095", "二十一", "溱洧　再问", "一问一答，再问才到水外", "sj095b", "九五"))
    xs = (64, 196, 328, 460, 592)
    labels = ("女曰\n观乎", "士曰\n既且", "且往\n观乎", "洧外\n洵訏", "赠之\n勺药")
    for i, (x, lab) in enumerate(zip(xs, labels)):
        s.append(rect(x, 190, 100, 96, 0.55, INK if i < 3 else RED))
        parts = lab.split("\n")
        s.append(t(x + 50, 228, parts[0], 10.0, INK if i < 3 else RED, "middle", "bold"))
        s.append(t(x + 50, 254, parts[1], 9.2, BROWN, "middle"))
        if i < 4:
            s.append(line(x + 102, 238, x + 128, 238, 0.45, BROWN))
            s.append(p("M %d 238 L %d 234 M %d 238 L %d 242" % (x + 128, x + 128, x + 128, x + 128), 0.35, BROWN))
    # 下排：水线
    for k in range(3):
        s.append(p("M 56 %d C 180 %d 260 %d 360 %d C 470 %d 580 %d 704 %d" %
                   (330 + k * 14, 318 + k * 14, 350 + k * 14, 324 + k * 14, 360 + k * 14, 338 + k * 14, 344 + k * 14), 0.35, BROWN, opacity=0.6))
    s.append(t(380, 402, "再问一次，才过水；礼不在，花为凭", 11.2, RED, "middle", "bold"))
    s.append(t(380, 430, "一章问，二章再问；问不变，水渐清。", 8.8, BROWN, "middle"))
    s.append(t(380, 486, "图二 · 义理", 8.6, BROWN, "middle"))
    s.append('<rect x="676" y="492" width="22" height="22" fill="%s" opacity="0.13"/>' % RED)
    s.append(t(687, 507, "润", 8.8, RED, "middle"))
    return s


FIGS = {
    "sj089a-dong-men": fig089a, "sj089b-shi-er-ren-yuan": fig089b,
    "sj090a-feng-yu-ji-ming": fig090a, "sj090b-san-jian-san-ding": fig090b,
    "sj091a-zi-jin-cheng-que": fig091a, "sj091b-yi-ri-san-yue": fig091b,
    "sj092a-yang-zhi-shui": fig092a, "sj092b-er-ren-yi-zhu": fig092b,
    "sj093a-dong-men-ru-yun": fig093a, "sj093b-yi-ren-su-yi": fig093b,
    "sj094a-man-cao-ling-lu": fig094a, "sj094b-xie-hou-zhi-shi": fig094b,
    "sj095a-zhen-wei-lan-shao": fig095a, "sj095b-zai-wen-zhi-yue": fig095b,
}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for name, fn in FIGS.items():
        body = "\n".join(fn())
        svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 540" width="760" height="540">\n'
               + body + "\n</svg>\n")
        open(os.path.join(OUT, name + ".svg"), "w", encoding="utf-8").write(svg)
        print("wrote", name)
