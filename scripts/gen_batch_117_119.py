# -*- coding: utf-8 -*-
"""生成 SJ117–SJ119 唐风三篇图一/图二，共 6 张。
760x540；a 图墨拓，b 图朱拓；不填大面；先骨后皮；线三阶。
人不画脸；活物画不全只画痕迹；红只作结。写盘键与正文 {{fig:...}} 一致。
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "assets", "fig")

# 图式 13.1 定色（全书统一，不逐图另调）
PAPER = "#F5F1E8"      # 宣纸米
INK = "#1C1917"        # 焦墨
HEAVY = "#4A443C"      # 重墨
LIGHT = "#6B6259"      # 淡墨
RED = "#A63D2F"        # 朱砂
SEAL = "#B35142"       # 印泥
GOLD = "#B79A63"       # 泥金
LINE = "#DCD5C8"       # 边框辅助线

# 朱拓备选：纸 #F6EFE4，墨 #7A2F26，次层 #A0604F
ZHUO_PAPER = "#F6EFE4"
ZHUO_MAIN = "#7A2F26"
ZHUO_SUB = "#A0604F"

FONT = "'Noto Serif CJK SC','Noto Serif SC','Songti SC','Source Han Serif SC',serif"


def t(x, y, s, size=11.5, color=INK, anchor="start", weight="normal", ls=0):
    return ('<text x="%.1f" y="%.1f" font-family="%s" font-size="%.1f" fill="%s" '
            'text-anchor="%s" font-weight="%s" letter-spacing="%.1f">%s</text>'
            % (x, y, FONT, size, color, anchor, weight, ls, s))


def p(d, w=0.55, color=INK, fill="none"):
    return ('<path d="%s" fill="%s" stroke="%s" stroke-width="%.2f" '
            'stroke-linecap="round" stroke-linejoin="round"/>'
            % (d, fill, color, w))


def line(x1, y1, x2, y2, w=0.55, color=INK):
    return ('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
            'stroke-width="%.2f"/>' % (x1, y1, x2, y2, color, w))


def circ(cx, cy, r, w=0.55, color=INK):
    return ('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="none" stroke="%s" '
            'stroke-width="%.2f"/>' % (cx, cy, r, color, w))


def rect(x, y, wd, ht, w=0.55, color=INK):
    return ('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="0" '
            'fill="none" stroke="%s" stroke-width="%.2f"/>'
            % (x, y, wd, ht, color, w))


def person(cx, base_y, ht=118, wd=30, color=INK):
    """背影人形：头圆、身廓、袖；无脸。"""
    s = []
    hr = ht * 0.075
    s.append(circ(cx, base_y - ht + hr, hr, 0.45, color))
    s.append(line(cx, base_y - ht + 2 * hr, cx, base_y - ht * 0.78, 0.35, color))
    s.append(p("M %.1f %.1f L %.1f %.1f L %.1f %.1f L %.1f %.1f L %.1f %.1f L %.1f %.1f Z" %
               (cx - wd * 0.55, base_y - ht * 0.78,
                cx - wd, base_y - ht * 0.40,
                cx - wd * 0.88, base_y,
                cx + wd * 0.88, base_y,
                cx + wd, base_y - ht * 0.40,
                cx + wd * 0.55, base_y - ht * 0.78), 0.5, color))
    s.append(p("M %.1f %.1f L %.1f %.1f L %.1f %.1f" %
               (cx - wd * 0.55, base_y - ht * 0.78, cx, base_y - ht * 0.62,
                cx + wd * 0.55, base_y - ht * 0.78), 0.35, color))
    s.append(line(cx - wd * 0.82, base_y - ht * 0.58, cx - wd * 1.02, base_y - ht * 0.22, 0.3, color))
    s.append(line(cx + wd * 0.82, base_y - ht * 0.58, cx + wd * 1.02, base_y - ht * 0.22, 0.3, color))
    return s


def palette(tuo):
    if tuo == "zhuo":
        return dict(paper=ZHUO_PAPER, main=ZHUO_MAIN, sub=ZHUO_SUB, note=ZHUO_SUB, red=RED)
    return dict(paper=PAPER, main=INK, sub=HEAVY, note=LIGHT, red=RED)


def head(vol, title, sub, zh_no, tuo="mo"):
    c = palette(tuo)
    return [
        '<rect width="760" height="540" fill="%s"/>' % c["paper"],
        '<rect x="10" y="10" width="740" height="520" fill="none" stroke="%s" stroke-width="0.6"/>' % LINE,
        '<rect x="22" y="28" width="716" height="470" fill="none" stroke="%s" stroke-width="0.8"/>' % LINE,
        t(38, 62, "唐 风 · 之%s" % vol, 9.5, c["red"], ls=2),
        t(380, 72, title, 25, c["main"], "middle", "bold", 1.6),
        t(720, 62, "诗三百五篇 · 之%s" % zh_no, 8.6, c["note"], "end", ls=1),
        line(38, 100, 722, 100, 0.35, GOLD),
        t(380, 122, sub, 10.2, c["note"], "middle", ls=1),
    ]


def foot(caption, quote="", tuo="mo"):
    c = palette(tuo)
    s = []
    if quote:
        s.append(t(380, 468, quote, 12.4, c["red"], "middle", ls=0.8))
    s.append(t(380, 506, caption, 9.2, c["note"], "middle", ls=1))
    s.append('<rect x="676" y="492" width="22" height="22" fill="%s" opacity="0.13"/>' % c["red"])
    s.append(t(687, 507, "润", 8.8, c["red"], "middle"))
    return s


def fig2(vol, title, sub, rows, conclusion, zh_no, coda="", tuo="zhuo"):
    c = palette(tuo)
    s = head(vol, title, sub, zh_no, tuo)
    n = len(rows)
    ys = {2: (218, 300), 3: (190, 260, 330)}[n]
    for i, row in enumerate(rows):
        y = ys[i]
        s.append(line(44, y + 22, 716, y + 22, 0.3, LINE))
        s.append(t(62, y, row[0], 10.4, c["main"], "start", "bold"))
        s.append(t(226, y, row[1], 10.8, c["main"], "start"))
        s.append(t(566, y, row[2], 9.4, c["note"], "start"))
    top = ys[0] - 22
    bot = ys[-1] + 22
    s.append(line(204, top, 204, bot, 0.55, c["red"]))
    s.append(line(204, top, 212, top, 0.4, c["red"]))
    s.append(line(204, bot, 212, bot, 0.4, c["red"]))
    s.append(line(548, top + 8, 548, bot - 8, 0.35, c["sub"]))
    s.append(line(544, top + 8, 552, top + 8, 0.3, c["sub"]))
    s.append(line(544, bot - 8, 552, bot - 8, 0.3, c["sub"]))
    s.append(line(50, 392, 710, 392, 0.35, GOLD))
    s.append(t(380, 418, conclusion, 11.6, c["red"], "middle", "bold", 0.6))
    if coda:
        s.append(t(380, 442, coda, 8.8, c["note"], "middle", ls=0.3))
    s.append(t(380, 486, "图二 · 义理", 8.6, c["note"], "middle"))
    s.append('<rect x="676" y="492" width="22" height="22" fill="%s" opacity="0.13"/>' % c["red"])
    s.append(t(687, 507, "润", 8.8, c["red"], "middle"))
    return s


# ---------- 117 椒聊 ----------

def pod_cluster(cx, cy, color, sub):
    """椒房成簇：六枚小实围一束，枝针刺笔点出。"""
    s = []
    spots = [(-11, -6), (7, -11), (15, 3), (-3, 9), (-15, 3), (0, -2)]
    for dx, dy in spots:
        s.append(circ(cx + dx, cy + dy, 4.4, 0.32, color))
    for dx, dy in ((-11, -6), (15, 3), (-3, 9), (-15, 3)):
        s.append(line(cx + dx, cy + dy - 5, cx + dx - 3, cy + dy - 9, 0.22, sub))
        s.append(line(cx + dx, cy + dy + 5, cx + dx + 3, cy + dy + 9, 0.22, sub))
    return s


def fig117a():
    c = palette("mo")
    s = head("四", "椒聊  盈升盈匊", "椒实蕃衍，枝远条长", "一百十七", "mo")
    # 椒树主干与枝
    s.append(p("M 286 400 C 282 344 290 292 300 236", 0.6, c["main"]))
    s.append(p("M 300 264 C 274 238 252 228 228 214", 0.42, c["sub"]))
    s.append(p("M 300 252 C 328 230 352 218 378 206", 0.42, c["sub"]))
    s.append(p("M 300 240 C 296 214 300 194 308 174", 0.42, c["sub"]))
    s.append(p("M 292 300 C 272 288 256 284 240 278", 0.35, c["sub"]))
    s.append(p("M 304 296 C 326 286 344 282 360 276", 0.35, c["sub"]))
    for cx, cy in ((228, 210), (378, 202), (308, 170), (262, 228),
                   (342, 220), (240, 274), (360, 272)):
        s += pod_cluster(cx, cy, c["main"], c["sub"])
    # 左：升（量器）
    s.append(p("M 92 314 C 118 304 152 304 178 314", 0.55, c["main"]))
    s.append(p("M 92 314 C 100 336 102 358 108 374 C 124 382 148 382 164 374 C 170 358 172 336 178 314", 0.55, c["main"]))
    s.append(line(104, 334, 90, 326, 0.35, c["sub"]))
    s.append(line(166, 334, 180, 326, 0.35, c["sub"]))
    for dx, dy in ((116, 334), (134, 342), (150, 332), (130, 354)):
        s.append(circ(dx, dy, 3.8, 0.3, c["red"]))
    s.append(t(135, 398, "升", 8.2, c["note"], "middle"))
    # 右：匊（两手捧）
    s.append(p("M 516 352 C 528 332 550 330 560 346", 0.5, c["main"]))
    s.append(p("M 596 352 C 584 332 562 330 552 346", 0.5, c["main"]))
    s.append(p("M 524 352 C 516 366 524 380 540 382", 0.35, c["sub"]))
    s.append(p("M 588 352 C 596 366 588 380 572 382", 0.35, c["sub"]))
    s.append(p("M 524 352 C 540 360 572 360 588 352", 0.3, c["sub"]))
    for dx, dy in ((538, 344), (554, 348), (568, 342), (552, 356)):
        s.append(circ(dx, dy, 3.8, 0.3, c["red"]))
    s.append(t(556, 398, "匊", 8.2, c["note"], "middle"))
    s.append(t(300, 424, "椒聊", 8.6, c["red"], "middle", "bold"))
    s += foot("图一 · 椒聊 · 椒树、盈升、盈匊", "椒聊之实，蕃衍盈升。", "mo")
    return s


def fig117b():
    return fig2("四", "椒聊  蕃衍与硕大", "实蕃于器，德厚于身",
                [("盈升", "蕃衍满器", "一章之实"),
                 ("盈匊", "蕃衍满手", "二章之实"),
                 ("无朋 · 且笃", "硕大而厚", "形德并盛")],
                "枝远而实蕃；盛在沃，忧在昭",
                "一百十七", "长枝伸向界外，叹词不点破。", "zhuo")


# ---------- 118 绸缪 ----------

def bundle(x, base_y, kind, c):
    """束薪／束刍／束楚：束腰两道，缕根接在束身内。"""
    s = []
    if kind == "xin":  # 薪：柴枝
        tops = [(-24, -68), (-14, -82), (-4, -74), (6, -84), (16, -74), (26, -66)]
        for dx, dy in tops:
            s.append(line(x, base_y - 18, x + dx, base_y + dy, 0.42, c["main"]))
    elif kind == "chu":  # 刍：草束，弯缕
        for dx in (-22, -12, -2, 8, 18, 24):
            s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
                       (x, base_y - 18, x + dx * 0.4, base_y - 44,
                        x + dx, base_y - 62, x + dx * 1.05, base_y - 74), 0.36, c["sub"]))
    else:  # 楚：荆条，带刺（kind == "ci"）
        tops = [(-20, -70), (-8, -82), (4, -78), (16, -72), (24, -64)]
        for dx, dy in tops:
            s.append(line(x, base_y - 18, x + dx, base_y + dy, 0.42, c["main"]))
            s.append(line(x + dx * 0.6, base_y + dy + 16, x + dx * 0.6 - 5, base_y + dy + 11, 0.24, c["sub"]))
            s.append(line(x + dx * 0.6, base_y + dy + 28, x + dx * 0.6 + 5, base_y + dy + 23, 0.24, c["sub"]))
    # 束腰两道
    s.append(line(x - 20, base_y - 26, x + 20, base_y - 26, 0.5, c["red"]))
    s.append(line(x - 18, base_y - 14, x + 18, base_y - 14, 0.38, c["sub"]))
    # 缕根下垂
    for dx in (-12, -5, 2, 9, 15):
        s.append(line(x + dx, base_y - 12, x + dx + 2, base_y + 4, 0.26, c["sub"]))
    return s


def star3(cx, cy, c):
    return [circ(cx, cy, 3.8, 0.4, c["main"]),
            circ(cx + 13, cy - 7, 3.2, 0.35, c["main"]),
            circ(cx + 26, cy + 2, 3.8, 0.4, c["main"])]


def fig118a():
    c = palette("mo")
    s = head("五", "绸缪  束薪三星", "三束待礼，三星移夜", "一百十八", "mo")
    # 三束
    s += bundle(150, 380, "xin", c)
    s += bundle(380, 380, "chu", c)
    s += bundle(610, 380, "ci", c)
    s.append(t(150, 410, "束薪", 8.0, c["note"], "middle"))
    s.append(t(380, 410, "束刍", 8.0, c["note"], "middle"))
    s.append(t(610, 410, "束楚", 8.0, c["note"], "middle"))
    # 三星三移：在天（高左）、在隅（中）、在户（低右，近户）
    s += star3(110, 168, c)
    s.append(t(134, 190, "在天", 7.6, c["note"], "middle"))
    s += star3(340, 208, c)
    s.append(t(364, 230, "在隅", 7.6, c["note"], "middle"))
    s += star3(570, 248, c)
    s.append(t(594, 270, "在户", 7.6, c["note"], "middle"))
    # 户：右门户轮廓
    s.append(line(660, 190, 660, 360, 0.4, c["sub"]))
    s.append(line(700, 190, 700, 360, 0.4, c["sub"]))
    s.append(line(660, 190, 700, 190, 0.4, c["sub"]))
    s.append(t(680, 378, "户", 7.8, c["note"], "middle"))
    s += foot("图一 · 绸缪 · 束薪、束刍、束楚与三星", "绸缪束薪，三星在天。", "mo")
    return s


def fig118b():
    return fig2("五", "绸缪  三束三星三叹", "星位渐低，婚夜渐深",
                [("束薪", "在天", "良人"),
                 ("束刍", "在隅", "邂逅"),
                 ("束楚", "在户", "粲者")],
                "星移三舍，婚失其时；喜是真的，晚也是真的",
                "一百十八", "三章星位渐低渐近，叹句留空。", "zhuo")


# ---------- 119 杕杜 ----------

def du_tree(x, base_y, c):
    s = []
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
               (x, base_y, x - 2, base_y - 56, x + 4, base_y - 100, x + 8, base_y - 150), 0.6, c["main"]))
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
               (x + 6, base_y - 110, x - 16, base_y - 128, x - 32, base_y - 134, x - 50, base_y - 142), 0.42, c["sub"]))
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
               (x + 6, base_y - 100, x + 26, base_y - 118, x + 42, base_y - 124, x + 56, base_y - 130), 0.42, c["sub"]))
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
               (x + 2, base_y - 80, x - 14, base_y - 92, x - 26, base_y - 96, x - 38, base_y - 100), 0.35, c["sub"]))
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
               (x + 4, base_y - 70, x + 22, base_y - 80, x + 36, base_y - 84, x + 48, base_y - 88), 0.35, c["sub"]))

    def leaf(cx, cy, rot):
        s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f Z" %
                   (cx, cy, cx + 5, cy - 3.4, cx + 10, cy - 1, cx + 6, cy + 3.4), 0.26, c["sub"]))

    # 叶簇：两侧分簇，不相连接
    for cx, cy in ((-50, -142), (-28, -128), (56, -130), (32, -118),
                    (8, -150), (-38, -100), (48, -88), (-16, -116)):
        for dx, dy in ((-6, -3), (5, -5), (8, 4), (-4, 6)):
            leaf(x + cx + dx, base_y + cy + dy, 0)
    return s


def fig119a():
    c = palette("mo")
    s = head("六", "杕杜  孤特独行", "叶盛相比，人独无亲", "一百十九", "mo")
    s += du_tree(250, 400, c)
    s.append(t(250, 424, "杜（赤棠）", 8.0, c["note"], "middle"))
    # 地面与远路
    s.append(line(44, 400, 716, 400, 0.35, c["sub"]))
    s.append(p("M 430 400 C 520 396 620 392 710 390", 0.3, c["sub"]))
    # 独行之人，背影无脸
    s += person(540, 424, 116, 28, c["main"])
    s.append(t(540, 448, "独行", 7.8, c["note"], "middle"))
    s += foot("图一 · 杕杜 · 孤杜、其叶、独行之人", "有杕之杜，其叶湑湑。", "mo")
    return s


def fig119b():
    c = palette("zhuo")
    s = head("六", "杕杜  同父同姓", "他人非无人，宗族先已疏", "一百十九", "zhuo")
    rows = [("湑湑", "踽踽", "同父 · 兄弟"),
            ("菁菁", "睘睘", "同姓 · 同祖")]
    ys = (208, 288)
    for i, row in enumerate(rows):
        y = ys[i]
        s.append(line(44, y + 22, 716, y + 22, 0.3, LINE))
        s.append(t(62, y, row[0], 10.4, c["main"], "start", "bold"))
        s.append(t(226, y, row[1], 10.8, c["main"], "start"))
        s.append(t(566, y, row[2], 9.4, c["note"], "start"))
    top, bot = ys[0] - 22, ys[-1] + 22
    s.append(line(204, top, 204, bot, 0.55, c["red"]))
    s.append(line(204, top, 212, top, 0.4, c["red"]))
    s.append(line(204, bot, 212, bot, 0.4, c["red"]))
    # 两问同叹
    s.append(t(380, 352, "嗟行之人，胡不比焉？", 10.0, c["main"], "middle"))
    s.append(t(380, 378, "人无兄弟，胡不佽焉？", 10.0, c["main"], "middle"))
    s.append(line(50, 392, 710, 392, 0.35, GOLD))
    s.append(t(380, 418, "叶盛犹相比，人独无兄弟；同姓疏远，异姓谁辅", 11.2, c["red"], "middle", "bold", 0.6))
    s.append(t(380, 442, "左树右人，中留断线；他人虚写，宗亲属落。", 8.8, c["note"], "middle", ls=0.3))
    s.append(t(380, 486, "图二 · 义理", 8.6, c["note"], "middle"))
    s.append('<rect x="676" y="492" width="22" height="22" fill="%s" opacity="0.13"/>' % c["red"])
    s.append(t(687, 507, "润", 8.8, c["red"], "middle"))
    return s


FIGS = [("sj117a-jiao-liao", fig117a), ("sj117b-yuan-tiao", fig117b),
        ("sj118a-shu-xin", fig118a), ("sj118b-san-xing", fig118b),
        ("sj119a-di-du", fig119a), ("sj119b-tong-xing", fig119b)]


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
