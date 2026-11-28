# -*- coding: utf-8 -*-
"""生成 SJ135–SJ137 图一/图二，共 6 张。

135 权舆（秦风之终）、136 宛丘（陈风之首）、137 东门之枌（陈风之二）。
a 名物图墨拓，b 义理图朱拓；760x540；不填而描；人不画脸；活物画不全。
写盘键与正文 {{fig:...}} 严格一致。
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gen_batch_123_125 as B
from gen_batch_123_125 import (t, p, line, circ, rect, person, foot,
                               PAPER, INK, DARK, LIGHT, RED, SEAL, GOLD,
                               ZPAPER, ZINK, ZMID, LINE_L)

ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "assets", "fig")


def headw(wind, vol, title, sub, zh_no, zhuo=False):
    paper = ZPAPER if zhuo else PAPER
    ink = ZINK if zhuo else INK
    mid = ZMID if zhuo else DARK
    border = ZMID if zhuo else LINE_L
    return [
        '<rect width="760" height="540" fill="%s"/>' % paper,
        '<rect x="10" y="10" width="740" height="520" fill="none" stroke="%s" stroke-width="0.6"/>' % border,
        '<rect x="22" y="28" width="716" height="470" fill="none" stroke="%s" stroke-width="0.8"/>' % border,
        t(38, 62, "%s 风 · %s" % (wind, vol), 9.5, RED, ls=2),
        t(380, 72, title, 25, ink, "middle", "bold", 1.6),
        t(720, 62, "诗三百五篇 · 之%s" % zh_no, 8.6, mid, "end", ls=1),
        line(38, 100, 722, 100, 0.35, GOLD),
        t(380, 122, sub, 10.2, mid, "middle", ls=1),
    ]


def fig2(wind, vol, title, sub, rows, conclusion, zh_no, coda=""):
    ink, mid = ZINK, ZMID
    s = headw(wind, vol, title, sub, zh_no, zhuo=True)
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


# ---------- 器物 ----------

def gui(x, top_y, color=INK, mid=DARK, scale=1.0):
    """簋：圆口食器，碗身 + 圈足 + 两耳；线描不填。"""
    w = 13 * scale
    h = 17 * scale
    s = []
    # 碗身
    s.append(p("M %.0f %.0f L %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f L %.0f %.0f Z" %
               (x - w, top_y, x - w * 0.8, top_y + h,
                x - w * 0.4, top_y + h * 1.2, x + w * 0.4, top_y + h * 1.2,
                x + w * 0.8, top_y + h, x + w, top_y), 0.5, color))
    # 口沿
    s.append(line(x - w, top_y, x + w, top_y, 0.35, mid))
    # 圈足
    s.append(line(x - w * 0.32, top_y + h * 1.2, x - w * 0.32, top_y + h * 1.7, 0.35, mid))
    s.append(line(x + w * 0.32, top_y + h * 1.2, x + w * 0.32, top_y + h * 1.7, 0.35, mid))
    s.append(line(x - w * 0.5, top_y + h * 1.7, x + w * 0.5, top_y + h * 1.7, 0.35, mid))
    # 两耳
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
               (x - w, top_y + 3, x - w - 7, top_y + 2, x - w - 7, top_y + 9, x - w * 0.8, top_y + 10), 0.3, mid))
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
               (x + w, top_y + 3, x + w + 7, top_y + 2, x + w + 7, top_y + 9, x + w * 0.8, top_y + 10), 0.3, mid))
    return s


def feather(x, y, color=DARK, scale=1.0):
    """鹭羽翳：一杆 + 一束长羽，舞者所持；不画成活鹭。"""
    s = []
    s.append(line(x, y, x, y - 46 * scale, 0.35, color))
    for i, dx in enumerate((-10, -5, 0, 5, 10)):
        s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
                   (x, y - 40 * scale,
                    x + dx - 3, y - 52 * scale, x + dx, y - 60 * scale,
                    x + dx + 2, y - 46 * scale), 0.25, color))
    return s


# ---------- 135 权舆 ----------

def fig135a():
    s = headw("秦", "之十", "权舆　昔厚今薄", "礼由厚转薄，所叹在继始", "一百三十五")
    # 左：昔 · 食案四簋
    s.append(t(150, 176, "昔 · 每食四簋", 10.4, INK, "middle", "bold"))
    s.append(rect(80, 316, 150, 12, 0.45, DARK))
    s.append(line(92, 328, 92, 366, 0.35, DARK))
    s.append(line(218, 328, 218, 366, 0.35, DARK))
    for x in (104, 138, 172, 206):
        s += gui(x, 300)
    # 右：今 · 一薄食
    s.append(t(570, 176, "今 · 每食无余／不饱", 10.4, INK, "middle", "bold"))
    s += gui(560, 330, scale=0.85)
    s.append(p("M 544 356 C 556 350 570 350 582 356", 0.25, LIGHT))
    # 中界一线
    s.append(line(380, 200, 380, 380, 0.3, GOLD))
    # 注文
    s.append(t(44, 452, "① 簋：圆口食器，圈足；四簋为礼食之盛", 7.8, LIGHT, "start"))
    s.append(t(44, 468, "② 左器多而具，右器一而薄；厚薄以器之多少见", 7.8, LIGHT, "start"))
    s.append(t(44, 484, "③ 不画人；所叹在礼意，不在面色", 7.8, LIGHT, "start"))
    s += foot("图一 · 权舆 · 昔之大具、今之无余", "於我乎！夏屋渠渠，今也每食无余。")
    return s


def fig135b():
    return fig2("秦", "之十", "权舆　有始无终", "所叹在继始，不在啬敛",
                [("始", "夏屋渠渠 · 每食四簋", "厚"),
                 ("今", "每食无余 · 每食不饱", "薄"),
                 ("不承权舆", "有始而无终", "叹")],
                "礼由厚转薄，所叹在继始；是无终，不是素啬",
                "一百三十五", "与魏风唐风之俭并置：彼病在取民，此病在无终。")


# ---------- 136 宛丘 ----------

def basin(x0, y0, color=DARK):
    """宛丘地形：四方高、中央下；以两坡弧线出之。"""
    s = []
    s.append(p("M 60 300 C 140 250 210 330 300 352 C 390 330 460 250 540 300 C 610 326 660 318 700 306", 0.45, color))
    s.append(p("M 60 316 C 140 268 214 344 300 366 C 386 344 456 268 540 316 C 610 340 660 332 700 320", 0.25, LIGHT))
    return s


def fig136a():
    s = headw("陈", "之首", "宛丘　丘上丘下", "四方高，中央下", "一百三十六")
    s += basin(60, 300)
    # 三位置标
    s.append(t(150, 244, "丘之上", 7.8, DARK, "middle"))
    s.append(t(300, 386, "丘之下", 7.8, DARK, "middle"))
    s.append(t(560, 296, "丘之道", 7.8, DARK, "middle"))
    # 鼓（左坡）
    s.append(circ(150, 300, 16, 0.5, INK))
    s.append(line(150, 316, 150, 340, 0.35, DARK))
    s.append(line(138, 340, 162, 340, 0.3, DARK))
    s.append(t(150, 372, "坎其击鼓", 7.4, LIGHT, "middle"))
    # 缶（右道）
    s.append(p("M 548 316 C 548 300 572 300 572 316 L 568 332 C 562 336 554 336 552 332 Z", 0.5, INK))
    s.append(line(548, 316, 572, 316, 0.3, DARK))
    s.append(t(560, 352, "坎其击缶", 7.4, LIGHT, "middle"))
    # 舞者剪影（丘下），执鹭羽，不画脸
    s += person(300, 360, 104, 26, INK, 0.9)
    s.append(line(316, 316, 336, 296, 0.3, DARK))
    s += feather(336, 296)
    s.append(t(300, 402, "值其鹭羽", 7.4, LIGHT, "middle"))
    # 注文
    s.append(t(44, 452, "① 宛丘：四方高、中央下；丘形以两坡弧线出，不作尖山", 7.8, LIGHT, "start"))
    s.append(t(44, 468, "② 鹭羽／鹭翿：舞者所持羽翳，一杆一束羽，不是活鹭", 7.8, LIGHT, "start"))
    s.append(t(44, 484, "③ 舞者只作剪影，不画五官；鼓缶为节乐之器", 7.8, LIGHT, "start"))
    s += foot("图一 · 宛丘 · 丘形、鼓缶、羽翿剪影", "子之汤兮，宛丘之上兮。")
    return s


def fig136b():
    return fig2("陈", "之首", "宛丘　有情无望", "舞无冬夏，即无节度",
                [("丘上", "子之汤兮，洵有情兮", "有情"),
                 ("丘下·丘道", "无冬无夏，值其羽翿", "无望"),
                 ("鼓缶", "坎其击鼓 · 坎其击缶", "无度")],
                "洵有情兮，而无望兮；舞无冬夏，即无节度",
                "一百三十六", "陈风之艳在其地，其失在其政；不可读成单纯风情画。")


# ---------- 137 东门之枌 ----------

def elm(x, base_y, color=INK, mid=DARK):
    """枌（白榆）：白皮干，圆冠，荚叶小点。"""
    s = []
    s.append(p("M %.0f %.0f L %.0f %.0f L %.0f %.0f L %.0f %.0f Z" %
               (x - 6, base_y, x - 3, base_y - 96, x + 3, base_y - 96, x + 6, base_y), 0.5, color))
    s.append(circ(x, base_y - 116, 30, 0.35, mid))
    s.append(circ(x - 18, base_y - 104, 18, 0.3, mid))
    s.append(circ(x + 18, base_y - 104, 18, 0.3, mid))
    for dx, dy in ((-12, -116), (8, -126), (16, -108), (-4, -104)):
        s.append(circ(x + dx, base_y + dy, 2.4, 0.25, mid))
    return s


def oak(x, base_y, color=INK, mid=DARK):
    """栩（柞栎）：裂叶冠，橡子小圈。"""
    s = []
    s.append(p("M %.0f %.0f L %.0f %.0f L %.0f %.0f L %.0f %.0f Z" %
               (x - 6, base_y, x - 3, base_y - 92, x + 3, base_y - 92, x + 6, base_y), 0.5, color))
    # 裂叶冠：三朵轮廓
    s.append(circ(x - 20, base_y - 108, 17, 0.35, mid))
    s.append(circ(x + 20, base_y - 108, 17, 0.35, mid))
    s.append(circ(x, base_y - 122, 20, 0.35, mid))
    # 橡子
    for dx, dy in ((-14, -104), (10, -116), (18, -100)):
        s.append(circ(x + dx, base_y + dy, 3, 0.25, mid))
        s.append(line(x + dx, base_y + dy - 3, x + dx, base_y + dy - 7, 0.2, mid))
    return s


def fig137a():
    s = headw("陈", "之二", "东门之枌　树下婆娑", "二树成荫，舞于其下", "一百三十七")
    s += elm(176, 384)
    s.append(t(176, 414, "枌 · 白榆", 8.0, DARK, "middle"))
    s += oak(560, 384)
    s.append(t(560, 414, "栩 · 柞栎", 8.0, DARK, "middle"))
    # 婆娑者剪影，立于二树之间
    s += person(368, 384, 100, 26, INK, 0.9)
    s.append(line(352, 336, 336, 318, 0.3, DARK))
    s.append(line(384, 336, 400, 318, 0.3, DARK))
    s.append(t(368, 414, "婆娑其下", 7.8, LIGHT, "middle"))
    # 注文
    s.append(t(44, 452, "① 枌：白榆，皮色白，荚叶；栩：柞栎，裂叶而有橡子", 7.8, LIGHT, "start"))
    s.append(t(44, 468, "② 婆娑：盘旋起舞；舞者只作剪影，不画五官", 7.8, LIGHT, "start"))
    s.append(t(44, 484, "③ 二树各有形，不画成两团同影", 7.8, LIGHT, "start"))
    s += foot("图一 · 东门之枌 · 白榆、柞栎、树下婆娑", "东门之枌，宛丘之栩。")
    return s


def pepper_hand(x, y, color=RED, mid=DARK):
    """握椒：一掌（袖口）托一握椒粒；椒粒可数，不作整枝。"""
    s = []
    # 袖口
    s.append(p("M %.0f %.0f L %.0f %.0f L %.0f %.0f L %.0f %.0f Z" %
               (x - 22, y + 16, x - 14, y, x + 14, y, x + 22, y + 16), 0.4, mid))
    # 椒粒一握
    for dx, dy in ((-8, -4), (0, -8), (8, -4), (-4, -10), (4, -12)):
        s.append(circ(x + dx, y + dy, 3.2, 0.3, color))
    return s


def fig137b():
    s = fig2("陈", "之二", "东门之枌　弃业赠椒", "业弃于麻，情定于椒",
             [("树下", "婆娑其下", "会舞"),
              ("市井", "不绩其麻 · 市也婆娑", "弃业"),
              ("赠椒", "视尔如荍 · 贻我握椒", "定情")],
             "业弃于麻，情定于椒；市井之舞，是风也是失",
             "一百三十七", "辞面相乐，诗旨疾乱；不把此篇读成单纯恋情诗。")
    # 右下补握椒一握（义理图之实指）
    s += pepper_hand(674, 350)
    s.append(t(674, 386, "握椒", 7.4, LIGHT, "middle"))
    return s


# 注：sj135a-quan-yu / sj135b-bu-cheng 归 gen_batch_129_135.py 批量产出，
# 本脚本只维护陈风两篇（136、137），避免重复写覆盖。
FIGS = [
    ("sj136a-wan-qiu", fig136a),
    ("sj136b-you-dang", fig136b),
    ("sj137a-dong-men-fen", fig137a),
    ("sj137b-wo-jiao", fig137b),
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
