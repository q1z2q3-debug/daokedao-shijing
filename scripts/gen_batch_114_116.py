# -*- coding: utf-8 -*-
"""生成 SJ114–SJ116 唐风三篇图一/图二，共 6 张。
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
        t(38, 62, "唐 风 · 之%s" % vol, 9.5, RED, ls=2),
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


# ---------- 画具 ----------

def cricket(x, y):
    """侧身蟋蟀：身、翅、须、六足；不画眼，不画全形。"""
    s = []
    # 身（长椭，背隆腹收）
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f Z" %
               (x - 30, y, x - 30, y - 13, x - 10, y - 17, x + 8, y - 12,
                x + 20, y - 9, x + 24, y - 2, x - 30, y), 0.55))
    # 翅覆背与翅脉
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
               (x - 20, y - 2, x - 10, y - 13, x + 6, y - 12, x + 16, y - 5), 0.35, BROWN))
    s.append(line(x - 14, y - 4, x + 10, y - 8, 0.22, BROWN))
    # 头（与身分界）
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f L %.0f %.0f Z" %
               (x + 20, y - 8, x + 28, y - 12, x + 34, y - 6, x + 32, y + 2, x + 22, y + 4), 0.45))
    # 两须
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
               (x + 32, y - 7, x + 48, y - 22, x + 60, y - 20, x + 68, y - 30), 0.3, BROWN))
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
               (x + 32, y - 5, x + 50, y - 12, x + 62, y - 8, x + 72, y - 12), 0.3, BROWN))
    # 六足：前短后长，分节折线
    legs = [(-18, -2, -24, 16, -20, 20), (-4, 2, -6, 18, -2, 22),
            (10, 2, 16, 16, 22, 20), (-18, 4, -26, 14, -30, 18),
            (-4, 4, -10, 20, -10, 24), (10, 4, 20, 14, 26, 18)]
    for x1, y1, x2, y2, x3, y3 in legs:
        s.append(p("M %.0f %.0f L %.0f %.0f L %.0f %.0f" %
                   (x + x1, y + y1, x + x2, y + y2, x + x3, y + y3), 0.28, BROWN))
    s.append(t(x, y + 38, "蟋蟀", 8.0, BROWN, "middle"))
    return s


def service_cart(x, y):
    """役车：方箱、两轮、辕；不驾车马。"""
    s = []
    # 方箱
    s.append(p("M %.0f %.0f L %.0f %.0f L %.0f %.0f L %.0f %.0f Z" %
               (x, y - 44, x + 120, y - 44, x + 120, y - 6, x, y - 6), 0.5))
    s.append(line(x, y - 26, x + 120, y - 26, 0.25, BROWN))
    # 辕
    s.append(line(x, y - 30, x - 34, y - 18, 0.4, BROWN))
    # 两轮
    s.append(circ(x + 26, y, 14, 0.45))
    s.append(circ(x + 94, y, 14, 0.45))
    s.append(line(x + 12, y, x + 40, y, 0.25, BROWN))
    s.append(line(x + 80, y, x + 108, y, 0.25, BROWN))
    s.append(t(x + 60, y + 30, "役车其休", 7.6, BROWN, "middle"))
    return s


def tree(x, y, label, h=96, lean=0):
    """单株木：干双线、两枝、叶簇；不画成林。"""
    s = []
    s.append(line(x, y, x + lean, y - h, 0.5, INK))
    s.append(line(x + 6, y, x + lean + 5, y - h, 0.35, BROWN))
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
               (x + lean, y - h + 18, x - 18, y - h + 8, x - 26, y - h - 4, x - 30, y - h - 14), 0.3, BROWN))
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
               (x + lean + 3, y - h + 24, x + 20, y - h + 14, x + 28, y - h + 2, x + 32, y - h - 8), 0.3, BROWN))
    for dx, dy in ((-28, -h - 12), (0, -h - 10), (30, -h - 6)):
        s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f Z" %
                   (x + dx, y + dy, x + dx + 12, y + dy - 8, x + dx + 20, y + dy, x + dx + 8, y + dy + 6),
                   0.25, BROWN))
    s.append(t(x + 4, y + 20, label, 7.8, BROWN, "middle"))
    return s


def robe_hang(x, y):
    """悬挂衣裳：衣架一横，衣身轮廓，袖下垂；不穿人。"""
    s = []
    s.append(line(x - 40, y - 40, x + 40, y - 40, 0.4, BROWN))
    s.append(p("M %.0f %.0f L %.0f %.0f L %.0f %.0f L %.0f %.0f L %.0f %.0f L %.0f %.0f Z" %
               (x - 14, y - 38, x - 34, y - 10, x - 26, y + 34, x + 26, y + 34,
                x + 34, y - 10, x + 14, y - 38), 0.5))
    s.append(p("M %.0f %.0f L %.0f %.0f L %.0f %.0f" %
               (x - 14, y - 38, x, y - 22, x + 14, y - 38), 0.3, BROWN))
    s.append(t(x, y + 54, "衣裳", 7.6, BROWN, "middle"))
    return s


def chariot_stop(x, y):
    """停车：舆、两轮，无马。"""
    s = []
    s.append(p("M %.0f %.0f L %.0f %.0f L %.0f %.0f L %.0f %.0f Z" %
               (x, y - 30, x + 96, y - 30, x + 96, y - 4, x, y - 4), 0.5))
    s.append(circ(x + 22, y, 12, 0.45))
    s.append(circ(x + 74, y, 12, 0.45))
    s.append(line(x, y - 18, x - 26, y - 10, 0.35, BROWN))
    s.append(t(x + 48, y + 28, "车马", 7.6, BROWN, "middle"))
    return s


def bell_drum(x, y):
    """钟鼓：悬钟一、横鼓一。"""
    s = []
    # 钟架
    s.append(line(x - 30, y - 50, x + 30, y - 50, 0.4, BROWN))
    s.append(line(x - 30, y - 50, x - 30, y - 10, 0.3, BROWN))
    s.append(line(x + 30, y - 50, x + 30, y - 10, 0.3, BROWN))
    # 钟轮廓：顶沿、两肩、钟口、钟舌
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f L %.0f %.0f Z" %
               (x - 15, y - 50, x - 19, y - 34, x - 17, y - 18, x - 10, y - 10,
                x + 10, y - 10, x + 17, y - 18, x + 19, y - 34, x + 15, y - 50), 0.5))
    s.append(line(x - 15, y - 50, x + 15, y - 50, 0.3, BROWN))
    s.append(line(x - 10, y - 10, x + 10, y - 10, 0.25, BROWN))
    s.append(line(x, y - 10, x, y - 2, 0.25, BROWN))
    s.append(circ(x, y - 1, 2.5, 0.25, BROWN))
    # 横鼓
    s.append(p("M %.0f %.0f L %.0f %.0f L %.0f %.0f L %.0f %.0f Z" %
               (x - 4, y + 6, x + 44, y + 6, x + 44, y + 26, x - 4, y + 26), 0.5))
    s.append(circ(x - 4, y + 16, 10, 0.35))
    s.append(circ(x + 44, y + 16, 10, 0.35))
    s.append(t(x + 8, y + 46, "钟鼓", 7.6, BROWN, "middle"))
    return s


def water_waves(y0):
    s = []
    for i in range(4):
        y = y0 + i * 14
        s.append(p("M 48 %.0f C 160 %.0f 300 %.0f 430 %.0f C 540 %.0f 630 %.0f 710 %.0f" %
                   (y, y - 10, y - 4, y - 12, y - 6, y - 2, y - 10), 0.28, BROWN))
    return s


def stone(cx, cy, r):
    return [circ(cx, cy, r, 0.4, BROWN),
            p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
              (cx - r * 0.6, cy - r * 0.3, cx, cy - r * 0.8, cx + r * 0.6, cy - r * 0.3,
               cx + r * 0.5, cy + r * 0.2), 0.22, BROWN)]


def robe_zhu(x, y):
    """素衣朱领：衣身无脸，朱领一处作点。"""
    s = []
    s.append(circ(x, y - 78, 10, 0.4, BROWN))
    s.append(p("M %.0f %.0f L %.0f %.0f L %.0f %.0f L %.0f %.0f L %.0f %.0f L %.0f %.0f Z" %
               (x - 16, y - 66, x - 34, y - 30, x - 28, y + 30, x + 28, y + 30,
                x + 34, y - 30, x + 16, y - 66), 0.5))
    # 朱领：领口双线朱
    s.append(p("M %.0f %.0f L %.0f %.0f L %.0f %.0f" %
               (x - 12, y - 64, x, y - 48, x + 12, y - 64), 0.35, RED))
    s.append(t(x, y + 50, "素衣朱襮", 7.6, RED, "middle", "bold"))
    return s


# ---------- 114 蟋蟀 ----------

def fig114a():
    s = head("一", "蟋蟀  岁晚", "候物先至，戒在乐时", "一百十四")
    s += cricket(130, 330)
    s += service_cart(330, 350)
    # 堂室轮廓
    s.append(rect(560, 250, 130, 150, 0.45))
    s.append(line(610, 250, 610, 400, 0.3, BROWN))
    s.append(line(560, 300, 610, 300, 0.25, BROWN))
    s.append(t(625, 236, "在堂", 8.0, BROWN, "middle"))
    # 岁晚：漏日一线
    s.append(line(80, 220, 220, 220, 0.25, BROWN))
    s.append(t(150, 208, "岁聿其莫", 7.8, BROWN, "middle"))
    s += foot("sj114a", "图一 · 蟋蟀 · 堂下蟋蟀、役车、岁晚", "蟋蟀在堂，岁聿其莫。")
    return s


def fig114b():
    return fig2("一", "蟋蟀  居外忧", "由近及远，思一层远一层",
                [("职思其居", "瞿瞿", "顾内"),
                 ("职思其外", "蹶蹶", "敏外"),
                 ("职思其忧", "休休", "安而不忘忧")],
                "乐不可荒，居不可忘；良士之顾，正在乐时",
                "一百十四", "由居而外而忧，思虑一层远一层。")


# ---------- 115 山有枢 ----------

def fig115a():
    s = head("二", "山有枢  有而不用", "物在册，用未发", "一百十五")
    # 左：山隰之木
    s.append(p("M 44 380 C 110 330 180 344 230 372", 0.35, BROWN))
    s += tree(80, 372, "枢", 92, -4)
    s += tree(170, 378, "榆", 80, 4)
    # 中：衣裳、车马
    s += robe_hang(340, 330)
    s += chariot_stop(430, 350)
    # 右：钟鼓
    s += bell_drum(610, 320)
    s += foot("sj115a", "图一 · 山有枢 · 山隰之木、衣裳车马、钟鼓", "子有衣裳，弗曳弗娄。")
    return s


def fig115b():
    return fig2("二", "山有枢  他人入室", "有而不用，归属易主",
                [("衣裳车马", "弗曳弗娄／弗驰弗驱", "他人是愉"),
                 ("廷内钟鼓", "弗洒弗埽／弗鼓弗考", "他人是保"),
                 ("酒食鼓瑟", "何不日鼓瑟", "他人入室"),
                 ("有而不用", "物在册", "归属易主")],
                "物在而不用，身没而人取；乐可以节，有不可吝",
                "一百十五", "左主位虚，右室有履迹。")


# ---------- 116 扬之水 ----------

def fig116a():
    s = head("三", "扬之水  白石朱领", "水激石明，服朱从沃", "一百十六")
    s += water_waves(300)
    for cx, cy, r in ((150, 320, 12), (250, 350, 10), (360, 316, 13),
                       (450, 352, 10), (540, 322, 12)):
        s += stone(cx, cy, r)
    s += robe_zhu(620, 330)
    s += foot("sj116a", "图一 · 扬之水 · 急流白石、素衣朱领", "扬之水，白石凿凿。")
    return s


def fig116b():
    return fig2("三", "扬之水  闻命不敢告", "前两章见色，末一章收口",
                [("白石凿凿", "素衣朱襮", "从子于沃·乐"),
                 ("白石皓皓", "素衣朱绣", "从子于鹄·忧"),
                 ("白石粼粼", "我闻有命", "不敢以告人")],
                "水不能掩石，言不能告人；叛意已成，在不敢出口处",
                "一百十六", "末格一口封缄，朱线封口。")


FIGS = [("sj114a-xishuai", fig114a), ("sj114b-liang-shi", fig114b),
        ("sj115a-shu-you-shu", fig115a), ("sj115b-ta-ren-ru-shi", fig115b),
        ("sj116a-yang-zhi-shui", fig116a), ("sj116b-you-ming", fig116b)]


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
