# -*- coding: utf-8 -*-
"""生成 SJ138–SJ141 陈风四篇图一/图二，共 8 张。

138 衡门、139 东门之池、140 东门之杨、141 墓门。
a 名物图墨拓，b 义理图朱拓；760x540；不填而描；人不画脸；禽兽画不全。
写盘键与正文 {{fig:...}} 严格一致。
"""
import os

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


def head(vol, title, sub, zh_no, zhuo=False):
    paper = ZPAPER if zhuo else PAPER
    ink = ZINK if zhuo else INK
    mid = ZMID if zhuo else DARK
    border = ZMID if zhuo else LINE_L
    s = [
        '<rect width="760" height="540" fill="%s"/>' % paper,
        '<rect x="10" y="10" width="740" height="520" fill="none" stroke="%s" stroke-width="0.6"/>' % border,
        '<rect x="22" y="28" width="716" height="470" fill="none" stroke="%s" stroke-width="0.8"/>' % border,
        t(38, 62, "陈 风 · 之%s" % vol, 9.5, RED, ls=2),
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


# ---------- 138 衡门 ----------

def gate_hengmen(cx, base_y, color=INK, mid=DARK):
    """衡门：两柱一横木，无堂宇；线描，不填面。"""
    s = []
    # 左柱、右柱（双线锥度）
    s.append(p("M %.0f %.0f L %.0f %.0f L %.0f %.0f L %.0f %.0f Z" %
               (cx - 86, base_y, cx - 80, base_y - 118, cx - 72, base_y - 118, cx - 76, base_y), 0.5, color))
    s.append(p("M %.0f %.0f L %.0f %.0f L %.0f %.0f L %.0f %.0f Z" %
               (cx + 76, base_y, cx + 72, base_y - 118, cx + 80, base_y - 118, cx + 86, base_y), 0.5, color))
    # 横木：一横架于两柱之上，两端略出
    s.append(p("M %.0f %.0f L %.0f %.0f L %.0f %.0f L %.0f %.0f Z" %
               (cx - 104, base_y - 128, cx + 104, base_y - 128,
                cx + 104, base_y - 114, cx - 104, base_y - 114), 0.55, color))
    # 柱础两小横
    s.append(line(cx - 96, base_y, cx - 64, base_y, 0.35, mid))
    s.append(line(cx + 64, base_y, cx + 96, base_y, 0.35, mid))
    # 门内空地影
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
               (cx - 60, base_y + 4, cx - 20, base_y + 9, cx + 20, base_y + 9, cx + 60, base_y + 4), 0.25, mid))
    return s


def spring_ripples(x0, y, color=DARK, mid=LIGHT):
    """泌水洋洋：三折疏波，不设岸。"""
    s = []
    for i, dy in enumerate((0, 14, 28)):
        w = 0.4 - i * 0.06
        c = color if i == 0 else mid
        s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
                   (x0, y + dy, x0 + 40, y + dy - 8, x0 + 90, y + dy + 8, x0 + 130, y + dy,
                    x0 + 170, y + dy - 8, x0 + 210, y + dy + 8, x0 + 250, y + dy), w, c))
    return s


def fig138a():
    s = head("三", "衡门　横木陋门", "居处虽陋，可以游息", "一百三十八")
    s.append(line(60, 392, 700, 392, 0.35, DARK))
    s += gate_hengmen(300, 392)
    s.append(t(300, 236, "衡门", 8.6, DARK, "middle"))
    s += spring_ripples(470, 356)
    s.append(t(596, 340, "泌之洋洋", 8.0, DARK, "middle"))
    # 注文
    s.append(t(44, 452, "① 衡门：横木为门，无阿塾堂宇，陋居之象", 7.8, LIGHT, "start"))
    s.append(t(44, 468, "② 栖迟：游息盘桓；门内留白，不画居人面目", 7.8, LIGHT, "start"))
    s.append(t(44, 484, "③ 泌：泉水；洋洋以疏线见水流广远，不设岸", 7.8, LIGHT, "start"))
    s += foot("图一 · 衡门 · 横木陋门、泌水洋洋", "衡门之下，可以栖迟。")
    return s


def fig138b():
    return fig2("三", "衡门　安分无求", "所求有分，所安在心",
                [("栖迟", "衡门之下，可以栖迟", "安"),
                 ("乐饥", "泌之洋洋，可以乐饥", "足"),
                 ("不必", "岂其食鱼，必河之鲂鲤；岂其取妻，必齐姜宋子", "分")],
                "衡门可栖，泌水可饥；所求有分，所安在心",
                "一百三十八", "两反问只说不必求全；不画成问句人物，朱线收在「不必」一结。")


# ---------- 139 东门之池 ----------

def herb_ma(x, base_y, color=INK, mid=DARK):
    """麻：直立茎，狭长对生叶。"""
    s = []
    s.append(line(x, base_y, x - 2, base_y - 82, 0.45, color))
    for dy in (-22, -42, -62):
        for dx in (-12, 12):
            s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f Z" %
                       (x + dx * 0.35, base_y + dy, x + dx - 7, base_y + dy - 10,
                        x + dx + 1, base_y + dy - 13, x + dx + 5, base_y + dy - 3), 0.3, mid))
    s.append(line(x - 2, base_y - 82, x - 2, base_y - 92, 0.3, mid))
    return s


def herb_zhu(x, base_y, color=INK, mid=DARK):
    """纻（苎麻）：丛生平卧多茎，阔叶卵形。"""
    s = []
    for dx in (-16, 0, 16):
        s.append(p("M %.0f %.0f L %.0f %.0f" % (x, base_y, x + dx, base_y - 62 + abs(dx) * 0.6), 0.4, mid))
    for dx, dy in ((-16, -52), (0, -62), (16, -50), (-8, -40), (8, -40)):
        s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f Z" %
                   (x + dx, base_y + dy, x + dx - 13, base_y + dy - 8,
                    x + dx + 2, base_y + dy - 13, x + dx + 11, base_y + dy - 3), 0.32, mid))
    return s


def herb_jian(x, base_y, color=INK, mid=DARK):
    """菅：似茅，柔韧长叶自基弧出、梢端下垂，茎有白粉细线。"""
    s = []
    blades = [(-30, -64), (-14, -78), (2, -82), (18, -74), (32, -58)]
    for dx, dy in blades:
        # 中叶直立，外叶弧出而梢垂
        s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
                   (x, base_y, x + dx * 0.3, base_y + dy * 0.6,
                    x + dx * 0.8, base_y + dy + 6, x + dx, base_y + dy - 4), 0.32, mid))
    s.append(line(x - 4, base_y, x - 4, base_y - 70, 0.35, color))
    return s


def fig139a():
    s = head("四", "东门之池　池中三草", "草以池柔，人以相接", "一百三十九")
    # 池岸与水
    s.append(p("M 60 356 C 220 346 420 350 700 344", 0.4, DARK))
    s.append(p("M 60 392 C 220 384 420 388 700 382", 0.25, LIGHT))
    for i, dy in enumerate((364, 376)):
        s.append(p("M 90 %.0f C 160 %.0f 240 %.0f 320 %.0f C 420 %.0f 520 %.0f 660 %.0f" %
                   (dy, dy - 6, dy + 6, dy, dy - 6, dy + 6, dy), 0.22, LIGHT))
    s += herb_ma(170, 384)
    s.append(t(170, 414, "麻 · 沤麻", 7.8, DARK, "middle"))
    s += herb_zhu(380, 386)
    s.append(t(380, 414, "纻 · 沤纻", 7.8, DARK, "middle"))
    s += herb_jian(590, 386)
    s.append(t(590, 414, "菅 · 沤菅", 7.8, DARK, "middle"))
    # 注文
    s.append(t(44, 452, "① 池：蓄水渍草之池沼；沤，渍也，治麻先以水浸", 7.8, LIGHT, "start"))
    s.append(t(44, 468, "② 麻：大麻；纻：苎麻；菅：似茅柔韧，可为索", 7.8, LIGHT, "start"))
    s.append(t(44, 484, "③ 三草各据一池位；草是兴象，不画成草圃图谱", 7.8, LIGHT, "start"))
    s += foot("图一 · 东门之池　麻纻菅三草、池中沤草", "东门之池，可以沤麻。")
    return s


def fig139b():
    return fig2("四", "东门之池　晤对三事", "愿在歌语言笑",
                [("晤歌", "东门之池，可以沤麻", "对歌"),
                 ("晤语", "东门之池，可以沤纻", "相对"),
                 ("晤言", "东门之池，可以沤菅", "相言")],
                "沤草以池，接人以礼；愿在晤对，情不踰闲",
                "一百三十九", "两人相对之位留空，不画面目；相接之愿，画实则坐实私情。")


# ---------- 140 东门之杨 ----------

def poplar(x, base_y, h=168, color=INK, mid=DARK):
    """杨：柳之扬起者。主干双线锥度，枝上扬，叶簇以疏椭圆轮廓。"""
    s = []
    s.append(p("M %.0f %.0f L %.0f %.0f L %.0f %.0f L %.0f %.0f Z" %
               (x - 7, base_y, x - 3, base_y - h, x + 3, base_y - h, x + 7, base_y), 0.5, color))
    branches = [(-4, -h + 40, -34, -h + 12), (4, -h + 56, 32, -h + 22),
                (-2, -h + 74, -26, -h + 44), (2, -h + 88, 24, -h + 58),
                (0, -h + 100, 0, -h - 12)]
    for bx, by, ex, ey in branches:
        s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
                   (x + bx, base_y + by, x + bx * 1.6, base_y + by - 10,
                    x + ex * 0.7, base_y + ey + 10, x + ex, base_y + ey), 0.35, mid))
    # 叶簇：小椭圆轮廓，不填
    for lx, ly in ((-34, -h + 12), (32, -h + 22), (-26, -h + 44), (24, -h + 58), (0, -h - 12)):
        s.append(circ(x + lx, base_y + ly, 9, 0.28, mid))
        s.append(circ(x + lx - 8, base_y + ly + 8, 6, 0.25, mid))
        s.append(circ(x + lx + 8, base_y + ly + 7, 6, 0.25, mid))
    return s


def star(cx, cy, r=16, color=INK):
    """明星：四芒辉星，不作靶心。"""
    s = []
    pts = [(cx, cy - r), (cx + r * 0.22, cy - r * 0.22), (cx + r, cy),
           (cx + r * 0.22, cy + r * 0.22), (cx, cy + r), (cx - r * 0.22, cy + r * 0.22),
           (cx - r, cy), (cx - r * 0.22, cy - r * 0.22)]
    d = "M " + " L ".join("%.0f %.0f" % (x, y) for x, y in pts) + " Z"
    s.append(p(d, 0.4, color))
    for a in (45, 135, 225, 315):
        import math
        rx = math.cos(math.radians(a)) * (r + 8)
        ry = math.sin(math.radians(a)) * (r + 8)
        s.append(line(cx + rx * 0.5, cy + ry * 0.5, cx + rx, cy + ry, 0.25, color))
    return s


def fig140a():
    s = head("五", "东门之杨　杨叶明星", "叶盛于下，星明于上", "一百四十")
    # 东门两短柱（淡线，隐于树后）
    s.append(line(350, 392, 350, 300, 0.3, LIGHT))
    s.append(line(410, 392, 410, 300, 0.3, LIGHT))
    s.append(line(344, 300, 416, 300, 0.3, LIGHT))
    s += poplar(250, 392)
    s += poplar(520, 392)
    s.append(t(250, 414, "杨 · 其叶牂牂", 7.8, DARK, "middle"))
    s.append(t(520, 414, "杨 · 其叶肺肺", 7.8, DARK, "middle"))
    s += star(380, 176, 16, INK)
    s.append(t(380, 148, "明星煌煌", 8.4, RED, "middle", "bold"))
    # 注文
    s.append(t(44, 452, "① 杨：柳之扬起者；牂牂、肺肺，皆叶盛之貌", 7.8, LIGHT, "start"))
    s.append(t(44, 468, "② 明星：启明星；四芒作辉，不作十字靶心", 7.8, LIGHT, "start"))
    s.append(t(44, 484, "③ 门下留空位；候者与不至者皆不画，不画面目", 7.8, LIGHT, "start"))
    s += foot("图一 · 东门之杨　杨叶牂牂、明星煌煌", "东门之杨，其叶牂牂。")
    return s


def fig140b():
    return fig2("五", "东门之杨　期会失候", "人不至而星自明",
                [("牂牂·煌煌", "昏以为期，明星煌煌", "候"),
                 ("肺肺·晢晢", "昏以为期，明星晢晢", "久")],
                "昏以为期，星为之明；人既不至，叶自牂牂",
                "一百四十", "负约之人不补画；候者只留空位，星独守时。")


# ---------- 141 墓门 ----------

def thorn_bush(x, base_y, color=INK, mid=DARK):
    """棘：酸枣丛，枝曲折出刺，刺短而硬。"""
    s = []
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f" %
               (x - 28, base_y, x - 32, base_y - 46, x - 14, base_y - 86, x + 4, base_y - 88,
                x + 22, base_y - 82, x + 30, base_y - 44, x + 28, base_y), 0.35, mid))
    branches = [(-18, -52), (-6, -70), (6, -74), (16, -58), (22, -40)]
    for bx, by in branches:
        s.append(p("M %.0f %.0f L %.0f %.0f" % (x, base_y, x + bx, base_y + by), 0.4, mid))
    # 刺：短硬小叉
    for bx, by in ((-16, -40), (-4, -54), (8, -52), (18, -38), (-10, -62), (12, -64)):
        s.append(p("M %.0f %.0f L %.0f %.0f" % (x + bx, base_y + by, x + bx - 7, base_y + by - 10), 0.25, color))
        s.append(p("M %.0f %.0f L %.0f %.0f" % (x + bx, base_y + by, x + bx + 7, base_y + by - 8), 0.25, color))
    return s


def axe(x, base_y, color=INK, mid=DARK):
    """斧：一柄斜置，斧首开楔轮廓；不画挥斧之人。"""
    s = []
    # 柄
    s.append(line(x, base_y, x + 22, base_y - 88, 0.45, color))
    # 斧首：开口四边形，外刃斜出（参 112 伐檀斧形）
    s.append(p("M %.0f %.0f L %.0f %.0f L %.0f %.0f L %.0f %.0f" %
               (x + 16, base_y - 92, x + 38, base_y - 102,
                x + 46, base_y - 86, x + 24, base_y - 78), 0.4, mid))
    s.append(line(x + 20, base_y - 86, x + 30, base_y - 84, 0.25, mid))
    return s


def owl_sil(x, base_y, color=INK, mid=DARK):
    """鸮剪影：身、首、喙、尾、两足；只画背与足，不画全形面目。"""
    s = []
    # 身廓（闭合轮廓 stroke_closed）
    s.append(p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f Z" %
               (x - 18, base_y - 64, x - 22, base_y - 96, x - 10, base_y - 112, x - 6, base_y - 112,
                x + 10, base_y - 112, x + 20, base_y - 94, x + 18, base_y - 62), 0.5, color))
    # 耳羽两笔
    s.append(p("M %.0f %.0f L %.0f %.0f L %.0f %.0f" % (x - 6, base_y - 108, x - 10, base_y - 122, x - 2, base_y - 110), 0.35, mid))
    s.append(p("M %.0f %.0f L %.0f %.0f L %.0f %.0f" % (x + 6, base_y - 108, x + 10, base_y - 122, x + 2, base_y - 110), 0.35, mid))
    # 尾两缕
    s.append(line(x - 6, base_y - 64, x - 8, base_y - 46, 0.3, mid))
    s.append(line(x + 6, base_y - 64, x + 8, base_y - 46, 0.3, mid))
    # 两足
    s.append(line(x - 5, base_y - 46, x - 5, base_y - 34, 0.3, mid))
    s.append(line(x + 5, base_y - 46, x + 5, base_y - 34, 0.3, mid))
    return s


def fig141a():
    s = head("六", "墓门　棘与斧斯", "凶僻之门，恶木生焉", "一百四十一")
    s.append(line(60, 392, 700, 392, 0.35, DARK))
    # 墓门双扉
    s.append(p("M 250 392 L 250 262 L 430 262 L 430 392", 0.5, INK))
    s.append(line(250, 262, 430, 262, 0.5, INK))
    s.append(line(340, 262, 340, 392, 0.35, DARK))
    s.append(line(250, 320, 340, 320, 0.25, LIGHT))
    s.append(line(340, 320, 430, 320, 0.25, LIGHT))
    s.append(t(340, 244, "墓门", 8.6, DARK, "middle"))
    s += thorn_bush(560, 392)
    s.append(t(560, 414, "棘 · 斧以斯之", 7.8, DARK, "middle"))
    s += axe(150, 392)
    s.append(t(168, 414, "斧", 7.8, DARK, "middle"))
    # 注文
    s.append(t(44, 452, "① 墓门：墓道之门，凶僻之地；棘：有刺之酸枣", 7.8, LIGHT, "start"))
    s.append(t(44, 468, "② 斯：析也；斧斜置，不画挥斧之人", 7.8, LIGHT, "start"))
    s.append(t(44, 484, "③ 门内留白；不良之人不画面目，恶木只以线立形", 7.8, LIGHT, "start"))
    s += foot("图一 · 墓门　墓门有棘、斧以斯之", "墓门有棘，斧以斯之。")
    return s


def fig141b():
    s = fig2("六", "墓门　刺不良", "讯不顾，思已晚",
             [("国人知之", "夫也不良，国人知之", "公著"),
              ("歌以讯之", "夫也不良，歌以讯之", "告谏"),
              ("颠倒思予", "讯予不顾，颠倒思予", "已晚")],
             "知而不改，讯而不顾；颠倒思予，已晚无及",
             "一百四十一", "梅枝与鸮剪影置右侧；不良之人不画，朱线断在「思予」一结。")
    # 右侧梅枝与鸮剪影（朱拓内），插入「图二 · 义理」款识之前
    ox, oy = 656, 300
    owl = [
        # 横枝短栖，足握其上；枝不穿过鸟身
        line(630, 278, 684, 274, 0.4, ZINK),
        p("M 672 276 L 682 264", 0.3, ZMID),
        # 鸮剪影：身、首、耳羽、短尾、两足；只画背与足，不画面目
        p("M %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f C %.0f %.0f %.0f %.0f %.0f %.0f Z" %
          (ox - 15, oy - 38, ox - 18, oy - 60, ox - 10, oy - 72, ox - 4, oy - 72,
           ox + 10, oy - 72, ox + 17, oy - 58, ox + 15, oy - 38), 0.45, ZINK),
        p("M %.0f %.0f L %.0f %.0f L %.0f %.0f" % (ox - 5, oy - 69, ox - 9, oy - 81, ox - 1, oy - 71), 0.3, ZMID),
        p("M %.0f %.0f L %.0f %.0f L %.0f %.0f" % (ox + 5, oy - 69, ox + 9, oy - 81, ox + 1, oy - 71), 0.3, ZMID),
        p("M %.0f %.0f L %.0f %.0f L %.0f %.0f" % (ox - 5, oy - 38, ox - 7, oy - 28, ox - 2, oy - 38), 0.3, ZMID),
        p("M %.0f %.0f L %.0f %.0f L %.0f %.0f" % (ox + 5, oy - 38, ox + 7, oy - 28, ox + 2, oy - 38), 0.3, ZMID),
    ]
    cut = next(i for i, e in enumerate(s) if "图二 · 义理" in e)
    return s[:cut] + owl + s[cut:]


FIGS = [
    ("sj138a-heng-men", fig138a),
    ("sj138b-an-fen", fig138b),
    ("sj139a-zhi-chi", fig139a),
    ("sj139b-wu-yan", fig139b),
    ("sj140a-zhi-yang", fig140a),
    ("sj140b-ming-xing", fig140b),
    ("sj141a-mu-men", fig141a),
    ("sj141b-ci-e", fig141b),
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
