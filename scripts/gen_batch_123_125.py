# -*- coding: utf-8 -*-
"""生成 SJ123–SJ125 唐风收卷三篇图一/图二，共 6 张。

123 有杕之杜、124 葛生、125 采苓。
a 名物图墨拓，b 义理图朱拓；760x540；不填而描；人不画脸；活物画不全。
写盘键与正文 {{fig:...}} 严格一致。
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "assets", "fig")

# 定色七色（图式 13.1）
PAPER = "#F5F1E8"
INK = "#1C1917"      # 焦墨 主体
DARK = "#4A443C"     # 重墨 次层
LIGHT = "#6B6259"    # 淡墨 注文
RED = "#A63D2F"      # 朱砂
SEAL = "#B35142"     # 印泥 只用于小印
GOLD = "#B79A63"     # 泥金 分隔线
# 朱拓备选（图式 13.1）
ZPAPER = "#F6EFE4"
ZINK = "#7A2F26"
ZMID = "#A0604F"
LINE_L = "#DCD5C8"

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


def person(cx, base_y, ht=126, wd=34, color=INK, opacity=1):
    """无脸人形：头一圈、身一廓、两袖；不画五官。"""
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
                cx + wd * 0.55, base_y - ht * 0.78), 0.5, color, "none", opacity))
    s.append(p("M %.1f %.1f L %.1f %.1f L %.1f %.1f" %
               (cx - wd * 0.55, base_y - ht * 0.78, cx, base_y - ht * 0.62,
                cx + wd * 0.55, base_y - ht * 0.78), 0.35, color, "none", opacity))
    s.append(line(cx - wd * 0.82, base_y - ht * 0.58, cx - wd * 1.02, base_y - ht * 0.22, 0.3, color, opacity))
    s.append(line(cx + wd * 0.82, base_y - ht * 0.58, cx + wd * 1.02, base_y - ht * 0.22, 0.3, color, opacity))
    return s


def head(vol, title, sub, zh_no, zhuo=False):
    paper = ZPAPER if zhuo else PAPER
    ink = ZINK if zhuo else INK
    mid = ZMID if zhuo else DARK
    border = ZMID if zhuo else LINE_L
    s = [
        '<rect width="760" height="540" fill="%s"/>' % paper,
        '<rect x="10" y="10" width="740" height="520" fill="none" stroke="%s" stroke-width="0.6"/>' % border,
        '<rect x="22" y="28" width="716" height="470" fill="none" stroke="%s" stroke-width="0.8"/>' % border,
        t(38, 62, "唐 风 · 之%s" % vol, 9.5, RED, ls=2),
        t(380, 72, title, 25, ink, "middle", "bold", 1.6),
        t(720, 62, "诗三百五篇 · 之%s" % zh_no, 8.6, mid, "end", ls=1),
        line(38, 100, 722, 100, 0.35, GOLD),
        t(380, 122, sub, 10.2, mid, "middle", ls=1),
    ]
    return s


def foot(caption, quote="", zhuo=False):
    ink = ZINK if zhuo else INK
    mid = ZMID if zhuo else LIGHT
    s = []
    if quote:
        s.append(t(380, 468, quote, 12.4, RED, "middle", ls=0.8))
    s.append(t(380, 506, caption, 9.2, mid, "middle", ls=1))
    s.append('<rect x="676" y="492" width="22" height="22" fill="%s" opacity="0.13"/>' % SEAL)
    s.append(t(687, 507, "润", 8.8, SEAL, "middle"))
    return s


def fig2(vol, title, sub, rows, conclusion, zh_no, coda=""):
    zhuo = True
    ink = ZINK
    mid = ZMID
    s = head(vol, title, sub, zh_no, zhuo=True)
    n = len(rows)
    ys = {2: (218, 300), 3: (190, 260, 330), 4: (178, 240, 302, 364)}[n]
    for i, row in enumerate(rows):
        y = ys[i]
        s.append(line(44, y + 22, 716, y + 22, 0.3, mid))
        s.append(t(62, y, row[0], 10.4, ink, "start", "bold"))
        s.append(t(226, y, row[1], 10.8, ink, "start"))
        s.append(t(566, y, row[2], 9.4, mid, "start"))
    top = ys[0] - 22
    bot = ys[-1] + 22
    s.append(line(204, top, 204, bot, 0.55, RED))
    s.append(line(204, top, 212, top, 0.4, RED))
    s.append(line(204, bot, 212, bot, 0.4, RED))
    s.append(line(548, top + 8, 548, bot - 8, 0.35, mid))
    s.append(line(544, top + 8, 552, top + 8, 0.3, mid))
    s.append(line(544, bot - 8, 552, bot - 8, 0.3, mid))
    s.append(line(50, 392, 710, 392, 0.35, GOLD))
    s.append(t(380, 418, conclusion, 11.6, RED, "middle", "bold", 0.6))
    if coda:
        s.append(t(380, 442, coda, 8.8, mid, "middle", ls=0.3))
    s.append(t(380, 486, "图二 · 义理", 8.6, mid, "middle"))
    s.append('<rect x="676" y="492" width="22" height="22" fill="%s" opacity="0.13"/>' % SEAL)
    s.append(t(687, 507, "润", 8.8, SEAL, "middle"))
    return s


# ---------- 123 有杕之杜 ----------

def lone_tree(x, base_y, color=INK, mid=DARK):
    """孤生赤棠：主干孤直，旁枝稀疏，荫只一小圈；不画繁叶。"""
    s = []
    # 主干（双线锥度）
    s.append(p("M %.0f %.0f L %.0f %.0f L %.0f %.0f L %.0f %.0f Z" %
               (x - 7, base_y, x - 3, base_y - 108, x + 3, base_y - 108, x + 7, base_y), 0.55, color))
    # 三枝疏出
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
               (x - 2, base_y - 70, x - 24, base_y - 84, x - 38, base_y - 96, x - 46, base_y - 116), 0.35, mid))
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
               (x + 2, base_y - 82, x + 22, base_y - 92, x + 34, base_y - 104, x + 40, base_y - 122), 0.35, mid))
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
               (x, base_y - 100, x - 6, base_y - 116, x - 4, base_y - 128, x, base_y - 136), 0.3, mid))
    # 荫：三圈疏轮廓，不填
    s.append(circ(x - 24, base_y - 122, 18, 0.3, mid))
    s.append(circ(x + 18, base_y - 128, 20, 0.3, mid))
    s.append(circ(x, base_y - 140, 16, 0.3, mid))
    # 地影一小弧
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
               (x - 26, base_y + 4, x - 10, base_y + 9, x + 12, base_y + 9, x + 28, base_y + 4), 0.3, mid))
    return s


def fig123a():
    s = head("十", "有杕之杜　道左孤杜", "荫薄之杜，留不住人", "一百二十三")
    # 道：一曲一直
    s.append(p("M 60 402 C 200 384 340 392 500 372 C 580 362 650 366 700 356", 0.4, DARK))
    s.append(p("M 60 414 C 200 396 340 404 500 384 C 580 374 650 378 700 368", 0.25, LIGHT))
    s += lone_tree(210, 392)
    s.append(t(210, 430, "杜（赤棠·孤生）", 7.8, DARK, "middle"))
    # 君子虚位：空圈 + 地面迹，不画人
    s.append(circ(560, 372, 14, 0.3, LIGHT))
    s.append(p("M 536 396 C 552 390 572 390 588 396", 0.25, LIGHT))
    s.append(t(560, 350, "君子 · 未至", 7.8, RED, "middle", "bold"))
    # 注文
    s.append(t(44, 452, "① 道左：道东；二章道周，道之曲处", 7.8, LIGHT, "start"))
    s.append(t(44, 468, "② 杕：特生孤特之貌，非树名", 7.8, LIGHT, "start"))
    s.append(t(44, 484, "③ 好之在心，款待无由；人未来，画实则坐实", 7.8, LIGHT, "start"))
    s += foot("图一 · 有杕之杜 · 孤杜、道左、君子未来", "有杕之杜，生于道左。")
    return s


def fig123b():
    return fig2("十", "有杕之杜　好与无由", "好贤不已，食之无由",
                [("中心好之", "好贤之心不已", "诚"),
                 ("噬肯适我", "一问来不来", "惧"),
                 ("曷饮食之", "款待之由无着", "短")],
                "好之不已，食之无由；荫薄之杜，留不住人",
                "一百二十三", "君子在虚位；画实，便把「噬肯」一问坐实。")


# ---------- 124 葛生 ----------

def vine_on_shrub(x, y, color=INK, mid=DARK):
    """楚（酸枣丛）上覆葛藤：松廓包住枝簇 + 藤条翻卷，只描不填。"""
    s = []
    # 灌丛松廓（不闭合描一圈，示丛之轮廓）
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
               (x - 30, y, x - 34, y - 40, x - 18, y - 82, x + 2, y - 84,
                x + 24, y - 80, x + 32, y - 40, x + 30, y), 0.35, mid))
    # 枝簇：自基部分出五枝
    branches = [(-20, -56), (-8, -70), (4, -74), (14, -60), (22, -46)]
    for bx, by in branches:
        s.append(p("M %.0f %.0f L %.0f %.0f" % (x, y, x + bx, y + by), 0.4, mid))
    # 小刺
    for bx, by in ((-16, -44), (-4, -56), (10, -52), (18, -38)):
        s.append(p("M %.0f %.0f L %.0f %.0f" % (x + bx, y + by, x + bx - 6, y + by - 9), 0.25, mid))
    # 葛藤覆上
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
               (x - 30, y - 62, x - 8, y - 92, x + 18, y - 88, x + 34, y - 60), 0.45, color))
    # 藤叶三笔
    for lx, ly in ((-18, -82), (6, -86), (24, -72)):
        s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f Z" %
                   (x + lx, y + ly, x + lx - 12, y + ly - 7, x + lx - 14, y + ly + 3, x + lx, y + ly + 5), 0.28, mid))
    return s


def creeping_vine(x, y, color=INK, mid=DARK):
    """蔹蔓于野：横走茎 + 成对小叶，伏地蔓延。"""
    s = []
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
               (x, y, x + 36, y - 12, x + 76, y + 8, x + 118, y - 2), 0.45, color))
    for i, dx in enumerate((16, 44, 72, 100)):
        yy = y - 4 + (i % 2) * 7
        s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f Z" %
                   (x + dx, yy, x + dx - 14, yy - 12, x + dx - 7, yy - 18, x + dx + 4, yy - 6), 0.3, mid))
        s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f Z" %
                   (x + dx, yy, x + dx + 14, yy - 10, x + dx + 17, yy, x + dx + 5, yy + 5), 0.3, mid))
    return s


def horn_pillow(x, y, color=INK, mid=DARK):
    """角枕：横枕圆角框，两端角上翘；线描，不填。"""
    s = []
    # 枕身：圆角横框
    s.append(p("M %.0f %.0f L %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f L %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f Z" %
               (x + 12, y - 12, x + 68, y - 12,
                x + 80, y - 12, x + 80, y + 12, x + 68, y + 12,
                x + 12, y + 12,
                x, y + 12, x, y - 12, x + 12, y - 12), 0.5, color))
    # 两端角
    s.append(p("M %.0f %.0f L %.0f %.0f L %.0f %.0f" % (x + 10, y - 10, x + 2, y - 24, x + 16, y - 14), 0.4, mid))
    s.append(p("M %.0f %.0f L %.0f %.0f L %.0f %.0f" % (x + 70, y - 10, x + 78, y - 24, x + 64, y - 14), 0.4, mid))
    # 枕面两道束纹
    s.append(line(x + 30, y - 10, x + 30, y + 10, 0.25, mid))
    s.append(line(x + 52, y - 10, x + 52, y + 10, 0.25, mid))
    return s


def brocade_quilt(x, y, color=INK, mid=DARK):
    """锦衾：被框轮廓 + 内部密线代纹，绝不施面。"""
    s = []
    s.append(rect(x, y, 104, 76, 0.5, color))
    # 折边
    s.append(line(x, y + 18, x + 104, y + 18, 0.3, mid))
    # 密线代纹（短而不齐）
    for i in range(7):
        yy = y + 28 + i * 7
        s.append(line(x + 10 + (i % 2) * 4, yy, x + 94, yy, 0.2, mid))
    for i in range(5):
        xx = x + 18 + i * 16
        s.append(line(xx, y + 24, xx, y + 70, 0.18, mid))
    return s


def fig124a():
    s = head("十一", "葛生　蒙楚蔓野", "草木有托，所美无归", "一百二十四")
    s.append(line(44, 392, 716, 392, 0.35, DARK))
    s += vine_on_shrub(130, 384)
    s.append(t(130, 424, "葛蒙楚", 7.8, DARK, "middle"))
    s += creeping_vine(280, 380)
    s.append(t(330, 424, "蔹蔓于野／域", 7.8, DARK, "middle"))
    s += horn_pillow(470, 300)
    s.append(t(510, 278, "角枕粲", 7.8, DARK, "middle"))
    s += brocade_quilt(596, 286)
    s.append(t(648, 384, "锦衾烂", 7.8, DARK, "middle"))
    # 注文
    s.append(t(44, 452, "① 楚：荆条；棘：酸枣丛。葛藤覆之，蔹草蔓延", 7.8, LIGHT, "start"))
    s.append(t(44, 468, "② 角枕、锦衾以线立形；纹用密线，不以面代线", 7.8, LIGHT, "start"))
    s.append(t(44, 484, "③ 诗中无死者面目；此图不画人，只留枕衾与草蔓", 7.8, LIGHT, "start"))
    s += foot("图一 · 葛生 · 葛蔹蒙蔓、角枕锦衾", "葛生蒙楚，蔹蔓于野。")
    return s


def fig124b():
    return fig2("十一", "葛生　三独与同穴", "生前三独，死后一誓",
                [("独处", "葛生蒙楚，蔹蔓于野", "野"),
                 ("独息", "葛生蒙棘，蔹蔓于域", "墓"),
                 ("独旦", "角枕粲兮，锦衾烂兮", "夜"),
                 ("同穴", "百岁之后，归于其居·室", "誓")],
                "草木有托，所美无归；生不能同处，死乃誓同穴",
                "一百二十四", "圹只画轮廓，不画墓中人；倒章往复，不作错简读。")


# ---------- 125 采苓 ----------

def herb_ligc(x, base_y, color=INK, mid=DARK):
    """苓（甘草）：直立茎，羽状小叶。"""
    s = []
    s.append(line(x, base_y, x - 2, base_y - 78, 0.45, color))
    for dy in (-20, -38, -56):
        for dx in (-13, 13):
            s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f Z" %
                       (x + dx * 0.4, base_y + dy, x + dx - 6, base_y + dy - 9,
                        x + dx + 2, base_y + dy - 12, x + dx + 6, base_y + dy - 3), 0.3, mid))
    s.append(circ(x - 2, base_y - 82, 5, 0.3, mid))
    return s


def herb_bitter(x, base_y, color=INK, mid=DARK):
    """苦（苦菜）：基生莲座叶。"""
    import math
    s = []
    for a in (-80, -40, 0, 40, 80):
        rx = math.cos(math.radians(a)) * 42
        ry = math.sin(math.radians(a)) * 20
        s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f Z" %
                   (x, base_y, x + rx * 0.5, base_y + ry - 10,
                    x + rx, base_y + ry - 4, x + rx * 0.6, base_y + ry + 5), 0.34, mid))
    s.append(circ(x, base_y - 6, 5, 0.3, color))
    return s


def herb_turnip(x, base_y, color=INK, mid=DARK):
    """葑（蔓菁）：阔叶 + 根块轮廓。"""
    s = []
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f Z" %
               (x - 12, base_y, x - 18, base_y - 16, x + 18, base_y - 16, x + 12, base_y), 0.45, mid))
    for dx in (-18, 0, 18):
        s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
                   (x + dx * 0.5, base_y - 14, x + dx - 8, base_y - 36,
                    x + dx + 6, base_y - 46, x + dx + 10, base_y - 28), 0.32, mid))
    return s


def fig125a():
    s = head("十二", "采苓　首阳三菜", "菜是兴象，戒在听言", "一百二十五")
    # 首阳山脊
    s.append(p("M 56 372 C 180 300 320 276 470 296 C 580 310 650 330 704 348", 0.45, DARK))
    s.append(p("M 56 384 C 190 316 330 294 470 312 C 580 326 650 344 704 360", 0.25, LIGHT))
    s.append(t(360, 262, "首阳", 8.4, DARK, "middle"))
    s += herb_ligc(170, 350)
    s.append(t(170, 380, "苓 · 之巅", 7.6, DARK, "middle"))
    s += herb_bitter(372, 372)
    s.append(t(372, 396, "苦 · 之下", 7.6, DARK, "middle"))
    s += herb_turnip(566, 356)
    s.append(t(566, 386, "葑 · 之东", 7.6, DARK, "middle"))
    # 篮与袖手，不画全身
    s.append(p("M 650 372 C 664 362 684 366 686 386 C 688 400 674 408 660 402", 0.4, DARK))
    s.append(line(640, 372, 662, 382, 0.3, LIGHT))
    # 注文
    s.append(t(44, 452, "① 苓：甘草；苦：苦菜；葑：蔓菁。三菜各据一山位", 7.8, LIGHT, "start"))
    s.append(t(44, 468, "② 首阳：首山之南；巅、下、东，以位置分三章", 7.8, LIGHT, "start"))
    s.append(t(44, 484, "③ 采者只留篮与袖手；不画全身，不画五官", 7.8, LIGHT, "start"))
    s += foot("图一 · 采苓 · 首阳山、苓苦葑三菜", "采苓采苓，首阳之巅。")
    return s


def fig125b():
    return fig2("十二", "采苓　三层防线", "言可舍，不可然",
                [("无信", "人之为言，苟亦无信", "不信"),
                 ("无与", "舍旃舍旃，苟亦无然", "不许"),
                 ("无从", "人之为言，苟亦无从", "不听")],
                "言可舍，不可然；审听徐察，谗乃无得",
                "一百二十五", "谗言一格虚而不画人；朱线只收在「胡得」一诘。")


FIGS = [
    ("sj123a-you-di-du", fig123a),
    ("sj123b-han-xian", fig123b),
    ("sj124a-ge-sheng", fig124a),
    ("sj124b-tong-xue", fig124b),
    ("sj125a-cai-ling", fig125a),
    ("sj125b-yuan-chan", fig125b),
]


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
