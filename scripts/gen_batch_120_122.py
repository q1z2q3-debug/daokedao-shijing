# -*- coding: utf-8 -*-
"""生成 SJ120–SJ122 唐风三篇图一/图二，共 6 张。

120 羔裘（唐风之七）、121 鸨羽（唐风之八）、122 无衣（唐风之九）。
白描线描，760×540；一图墨拓、一图朱拓；人不画脸；活物只画背、翼、足；
不填而描，先骨后皮，线三阶 0.9/0.5/0.3；闭合轮廓 stroke_closed。
写盘键与正文 {{fig:...}} 一致。
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gen_batch_096_106 as B  # noqa: E402

ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "assets", "fig")

# 七色固定（图式 13.1）
PAPER = "#F5F1E8"
INK = "#1C1917"
HEAVY = "#4A443C"
LIGHT = "#6B6259"
RED = "#A63D2F"
SEAL = "#B35142"
GOLD = "#B79A63"
LINE = "#DCD5C8"

# 朱拓备选（图式 13.1）
PAPER_Z = "#F6EFE4"
INK_Z = "#7A2F26"
SEC_Z = "#A0604F"
LIGHT_Z = "#C99A8C"

FONT = B.FONT
t, p, line, circ, rect, person = B.t, B.p, B.line, B.circ, B.rect, B.person


def paper_defs(vermilion=False):
    """纸纹：<pattern> 手写短线；禁用 feTurbulence + feColorMatrix。"""
    stroke = "#EAD9CC" if vermilion else "#E6DED1"
    return [
        '<defs><pattern id="paper" width="62" height="62" patternUnits="userSpaceOnUse">'
        '<line x1="6" y1="14" x2="20" y2="13" stroke="%s" stroke-width="0.24"/>'
        '<line x1="30" y1="38" x2="44" y2="39" stroke="%s" stroke-width="0.24"/>'
        '<line x1="18" y1="52" x2="30" y2="51" stroke="%s" stroke-width="0.24"/>'
        '</pattern></defs>' % (stroke, stroke, stroke),
    ]


def head(vol, title, sub, zh_no, vermilion=False):
    paper = PAPER_Z if vermilion else PAPER
    ink = INK_Z if vermilion else INK
    sec = SEC_Z if vermilion else HEAVY
    light = LIGHT_Z if vermilion else LIGHT
    return [
        '<rect width="760" height="540" fill="%s"/>' % paper,
        '<rect width="760" height="540" fill="url(#paper)" opacity="0.34"/>',
        '<rect x="10" y="10" width="740" height="520" fill="none" stroke="%s" stroke-width="0.6"/>' % LINE,
        '<rect x="22" y="28" width="716" height="470" fill="none" stroke="%s" stroke-width="0.8"/>' % LINE,
        t(38, 62, "唐 风 · 之%s" % vol, 9.5, RED, ls=2),
        t(380, 72, title, 25, ink, "middle", "bold", 1.6),
        t(720, 62, "诗三百五篇 · 之%s" % zh_no, 8.6, sec, "end", ls=1),
        line(38, 100, 722, 100, 0.35, GOLD),
        t(380, 122, sub, 10.2, light, "middle", ls=1),
    ]


def foot(caption, quote="", vermilion=False):
    ink = INK_Z if vermilion else INK
    s = []
    if quote:
        s.append(t(380, 468, quote, 12.4, RED, "middle", ls=0.8))
    s.append(t(380, 506, caption, 9.2, LIGHT_Z if vermilion else LIGHT, "middle", ls=1))
    s.append('<rect x="676" y="492" width="22" height="22" fill="%s" opacity="0.13"/>' % SEAL)
    s.append(t(687, 507, "润", 8.8, SEAL, "middle"))
    return s


def fig2(vol, title, sub, rows, conclusion, zh_no, coda="", vermilion=True):
    """义理图：多行并置；所变者列左，所同者收右。朱拓。"""
    s = head(vol, title, sub, zh_no, vermilion=vermilion)
    ink = INK_Z if vermilion else INK
    sec = SEC_Z if vermilion else HEAVY
    light = LIGHT_Z if vermilion else LIGHT
    n = len(rows)
    ys = {2: (218, 300), 3: (190, 260, 330)}[n]
    for i, row in enumerate(rows):
        y = ys[i]
        s.append(line(44, y + 22, 716, y + 22, 0.3, LINE))
        s.append(t(62, y, row[0], 10.4, ink, "start", "bold"))
        s.append(t(212, y, row[1], 10.8, ink, "start"))
        s.append(t(566, y, row[2], 9.4, sec, "start"))
    top = ys[0] - 22
    bot = ys[-1] + 22
    s.append(line(190, top, 190, bot, 0.55, RED))
    s.append(line(190, top, 198, top, 0.4, RED))
    s.append(line(190, bot, 198, bot, 0.4, RED))
    s.append(line(548, top + 8, 548, bot - 8, 0.35, sec))
    s.append(line(544, top + 8, 552, top + 8, 0.3, sec))
    s.append(line(544, bot - 8, 552, bot - 8, 0.3, sec))
    s.append(line(50, 392, 710, 392, 0.35, GOLD))
    s.append(t(380, 418, conclusion, 11.6, RED, "middle", "bold", 0.6))
    if coda:
        s.append(t(380, 442, coda, 8.8, light, "middle", ls=0.3))
    s.append(t(380, 486, "图二 · 义理", 8.6, light, "middle"))
    s.append('<rect x="676" y="492" width="22" height="22" fill="%s" opacity="0.13"/>' % SEAL)
    s.append(t(687, 507, "润", 8.8, SEAL, "middle"))
    return s


# ---------- 器物：羔裘（衣架，袖口豹饰） ----------

def gown(x, y, scale=1.0, col=INK, cuff_col=HEAVY, dashed=False):
    """一件挂在衣架上的裘：交领、宽袖、袖口豹饰密线；不填面。"""
    s = []
    k = scale
    dash = ' stroke-dasharray="5 4"' if dashed else ""
    # 衣架钩与横杆
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
               (x, y - 18*k, x - 4*k, y - 26*k, x + 4*k, y - 30*k, x + 8*k, y - 24*k),
               0.5, col))
    s.append(line(x - 54*k, y - 6*k, x + 54*k, y - 6*k, 0.5, col))
    # 交领：领口弧 + 两襟交结
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
               (x - 18*k, y, x - 10*k, y - 8*k, x + 10*k, y - 8*k, x + 18*k, y), 0.5, col))
    s.append(p("M %.0f %.0f L %.0f %.0f L %.0f %.0f" %
               (x - 14*k, y + 2*k, x, y + 24*k, x + 14*k, y + 2*k), 0.45, col))
    # 肩与宽袖：袖身垂落，袖口略收
    s.append(p("M %.0f %.0f L %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f L %.0f %.0f" %
               (x - 18*k, y + 2*k, x - 38*k, y + 16*k, x - 48*k, y + 46*k, x - 46*k, y + 80*k,
                x - 38*k, y + 94*k, x - 34*k, y + 94*k), 0.55, col))
    s.append(p("M %.0f %.0f L %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f L %.0f %.0f" %
               (x + 18*k, y + 2*k, x + 38*k, y + 16*k, x + 48*k, y + 46*k, x + 46*k, y + 80*k,
                x + 38*k, y + 94*k, x + 34*k, y + 94*k), 0.55, col))
    # 衣身闭合轮廓（stroke_closed），下摆微张
    body = ("M %.0f %.0f L %.0f %.0f L %.0f %.0f L %.0f %.0f Z" %
            (x - 36*k, y + 16*k, x - 30*k, y + 170*k, x + 30*k, y + 170*k, x + 36*k, y + 16*k))
    s.append('<path d="%s" fill="none" stroke="%s" stroke-width="0.55" stroke-linecap="round" stroke-linejoin="round"%s/>'
             % (body, col, dash))
    # 前中缝
    s.append(line(x, y + 24*k, x, y + 170*k, 0.3, sec_or(col)))
    # 袖口豹饰：两道束边 + 短密线（密线代色，不填面）
    for sx in (-36, 36):
        s.append(line(x + sx*k - 8*k, y + 78*k, x + sx*k + 8*k, y + 78*k, 0.4, cuff_col))
        s.append(line(x + sx*k - 8*k, y + 94*k, x + sx*k + 8*k, y + 94*k, 0.4, cuff_col))
        for j in range(3):
            s.append(line(x + sx*k - 5*k + j*5*k, y + 80*k, x + sx*k - 6*k + j*5*k, y + 92*k,
                          0.25, cuff_col))
    return s


def sec_or(col):
    if col == INK:
        return HEAVY
    if col == RED:
        return RED
    return SEC_Z


# ---------- 120a 羔裘豹袪（墨拓） ----------

def fig120a():
    s = head("七", "羔裘  豹袪", "裘可饰袖，不可饰心", "一百二十")
    s += gown(210, 190, scale=1.05)
    # 袖与民之间的隔线：不相亲比
    s.append(line(380, 210, 380, 380, 0.3, LIGHT, opacity=0.8))
    # 民者：背影，无脸
    s += person(576, 410, 112, 28, INK, 0.85)
    s.append(line(560, 356, 540, 340, 0.25, LIGHT))
    # 注文
    s.append(t(210, 392, "羔裘豹袪", 8.4, HEAVY, "middle"))
    s.append(t(380, 200, "居居", 8.0, LIGHT, "middle"))
    s.append(t(576, 336, "维子之故", 8.2, RED, "middle", "bold"))
    s += foot("图一 · 羔裘 · 羔裘豹袪、居居、故旧", "羔裘豹袪，自我人居居。")
    return s


# ---------- 120b 故与好（朱拓） ----------

def fig120b():
    return fig2("七", "羔裘  故与好", "民厚位薄，故旧不忍绝",
                [("袪", "自我人居居", "维子之故"),
                 ("褎", "自我人究究", "维子之好")],
                "裘可饰袖，不可饰心；念故不去，正是不恤之证",
                "一百二十", "民之情未绝，位之薄自见。", vermilion=True)


# ---------- 草木：栩 / 棘 / 桑 ----------

def tree_cluster(x, y, kind, col=HEAVY, light=LIGHT):
    s = []
    # 主干与两副干（丛生之貌）
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
               (x, y, x - 6, y - 30, x + 4, y - 56, x + 10, y - 80), 0.5, col))
    s.append(line(x - 10, y, x - 16, y - 44, 0.3, light))
    s.append(line(x + 10, y, x + 18, y - 40, 0.3, light))
    # 根部短丛：苞，稹也
    for i in range(5):
        bx = x - 18 + i * 9
        s.append(line(bx, y, bx - 3, y - 10, 0.22, light))
    if kind == "xu":  # 栩（柞栎）：丛生短枝
        for dx in (-18, -8, 6, 16):
            s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
                       (x + 4, y - 40, x + dx - 6, y - 52, x + dx, y - 62, x + dx + 4, y - 72),
                       0.3, light))
        for i in range(6):
            bx = x - 20 + i * 8
            by = y - 58 + (i % 2) * 12
            s.append(p("M %.0f %.0f L %.0f %.0f M %.0f %.0f L %.0f %.0f" %
                       (bx, by, bx - 5, by - 7, bx, by, bx + 5, by - 7), 0.25, light))
    elif kind == "ji":  # 棘：酸枣，枝上出刺
        for dx in (-16, 0, 16):
            s.append(p("M %.0f %.0f L %.0f %.0f" % (x + 4, y - 34, x + dx, y - 58), 0.3, col))
        for i in range(7):
            bx = x - 20 + i * 7
            by = y - 52 + (i % 3) * 10
            s.append(p("M %.0f %.0f L %.0f %.0f L %.0f %.0f" %
                       (bx, by, bx + 3, by - 8, bx + 6, by), 0.25, col))
    else:  # 桑：叶簇
        for dx, dy in ((-16, -60), (0, -74), (16, -58), (-6, -48)):
            s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f Z" %
                       (x + dx, y + dy, x + dx - 10, y + dy - 6, x + dx - 12, y + dy + 4,
                        x + dx, y + dy + 8, x + dx + 12, y + dy + 4, x + dx + 10, y + dy - 6,
                        x + dx, y + dy), 0.3, light))
    s.append(t(x, y + 18, {"xu": "栩", "ji": "棘", "sang": "桑"}[kind], 8.0, col, "middle"))
    return s


# ---------- 鸨：大鸟，只画背、翼、足；无眼无喙 ----------

def bustard(x, y, scale=1.0):
    """侧身背视：横长身背、敛翼、尾缕、长足；头缩入背廓，不画五官。"""
    s = []
    k = scale
    # 背身闭合轮廓（几何骨架：横长身，不手调贝塞尔塑形）
    body = (f"M {x-38*k:.0f} {y-2*k:.0f} "
            f"C {x-24*k:.0f} {y-16*k:.0f} {x+8*k:.0f} {y-18*k:.0f} {x+34*k:.0f} {y-10*k:.0f} "
            f"C {x+40*k:.0f} {y-2*k:.0f} {x+32*k:.0f} {y+10*k:.0f} {x+16*k:.0f} {y+12*k:.0f} "
            f"L {x-22*k:.0f} {y+12*k:.0f} Z")
    s.append(p(body, 0.6, INK))
    # 敛翼：外弧一笔，半幅羽纹四缕
    s.append(p(f"M {x-18*k:.0f} {y-10*k:.0f} C {x-6*k:.0f} {y-16*k:.0f} "
               f"{x+12*k:.0f} {y-14*k:.0f} {x+24*k:.0f} {y-4*k:.0f}", 0.4, HEAVY))
    for j in range(4):
        s.append(line(x - 12*k + j*8*k, y - 8*k, x - 10*k + j*8*k, y + 4*k, 0.25, HEAVY))
    # 尾羽三缕，收敛带出
    for dy in (-7, 0, 7):
        s.append(p(f"M {x-36*k:.0f} {y+dy*k:.0f} C {x-48*k:.0f} {y+(dy-6)*k:.0f} "
                   f"{x-54*k:.0f} {y+(dy-12)*k:.0f} {x-50*k:.0f} {y+(dy-18)*k:.0f}", 0.35, HEAVY))
    # 两长足
    for dx in (-10, 10):
        s.append(line(x + dx*k, y + 12*k, x + dx*k, y + 34*k, 0.4, INK))
        s.append(p(f"M {x+dx*k:.0f} {y+34*k:.0f} L {x+dx*k-7*k:.0f} {y+39*k:.0f} "
                   f"M {x+dx*k:.0f} {y+34*k:.0f} L {x+dx*k+7*k:.0f} {y+39*k:.0f}", 0.3, HEAVY))
    return s


# ---------- 121a 鸨羽（墨拓） ----------

def fig121a():
    s = head("八", "鸨羽  集于苞栩", "鸟不安于树，人不安于役", "一百二十一")
    s += tree_cluster(130, 392, "xu")
    # 栖枝：鸨足所据
    s.append(p("M 92 346 C 116 340 146 340 170 346", 0.4, HEAVY))
    s += bustard(130, 302, scale=1.05)
    s += tree_cluster(360, 392, "ji")
    s += tree_cluster(560, 392, "sang")
    # 征役者：背影，无脸，杖一枝
    s += person(668, 410, 108, 26, INK, 0.8)
    s.append(line(688, 356, 688, 404, 0.3, LIGHT))
    s.append(t(668, 336, "下从征役", 7.8, RED, "middle", "bold"))
    s += foot("图一 · 鸨羽 · 鸨鸟集栩、苞棘苞桑、征役者", "肃肃鸨羽，集于苞栩。")
    return s


# ---------- 121b 所极常三问（朱拓） ----------

def fig121b():
    return fig2("八", "鸨羽  所极常三问", "三问皆空，苍天悠悠",
                [("怙", "不能蓺稷黍", "曷其有所"),
                 ("食", "不能蓺黍稷", "曷其有极"),
                 ("尝", "不能蓺稻粱", "曷其有常")],
                "鸟不安于树，人不安于役；苍天悠悠，三问皆空",
                "一百二十一", "所、极、常，一层紧一层。", vermilion=True)


# ---------- 122a 命服（墨拓） ----------

def fig122a():
    s = head("九", "无衣  子之衣", "衣是虚设，命是实情", "一百二十二")
    # 左：七章之服
    s += gown(170, 210, scale=0.95, col=INK)
    s.append(t(170, 176, "七", 11, HEAVY, "middle", "bold"))
    s.append(t(170, 392, "侯伯七命", 8.0, HEAVY, "middle"))
    # 右：六章之服
    s += gown(590, 210, scale=0.95, col=INK)
    s.append(t(590, 176, "六", 11, HEAVY, "middle", "bold"))
    s.append(t(590, 392, "天子之卿", 8.0, HEAVY, "middle"))
    # 中：子之衣，虚框（所不变者，画虚）
    s += gown(380, 210, scale=1.0, col=RED, cuff_col=RED, dashed=True)
    s.append(t(380, 176, "子之衣", 10.4, RED, "middle", "bold"))
    # 命线：自天子方位下贯
    s.append(circ(380, 148, 6, 0.4, RED))
    s.append(line(380, 154, 380, 196, 0.4, RED))
    s.append(t(380, 138, "天子", 7.8, LIGHT, "middle"))
    s += foot("图一 · 无衣 · 七章六章、子之衣虚框、命线", "岂曰无衣？七兮。不如子之衣，安且吉兮。")
    return s


# ---------- 122b 安吉燠（朱拓） ----------

def fig122b():
    return fig2("九", "无衣  安·吉·燠", "命重于衣",
                [("七", "安且吉", "命服"),
                 ("六", "安且燠", "谦")],
                "衣有多件，不如命服；安与吉，都在天子一命",
                "一百二十二", "衣是虚设，命是实情。", vermilion=True)


FIGS = [
    ("sj120a-bao-qu", fig120a, False),
    ("sj120b-gu-hao", fig120b, True),
    ("sj121a-bao-yu", fig121a, False),
    ("sj121b-suo-ji-chang", fig121b, True),
    ("sj122a-ming-fu", fig122a, False),
    ("sj122b-an-ji-yu", fig122b, True),
]


def main():
    os.makedirs(OUT, exist_ok=True)
    for key, fn, verm in FIGS:
        body = paper_defs(vermilion=verm) + fn()
        svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 540" width="760" height="540">\n'
               + "\n".join(body) + "\n</svg>\n")
        path = os.path.join(OUT, key + ".svg")
        open(path, "w", encoding="utf-8").write(svg)
        print("wrote", path, len(svg))


if __name__ == "__main__":
    main()
