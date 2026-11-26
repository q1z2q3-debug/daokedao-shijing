# -*- coding: utf-8 -*-
"""分片 021-027 共用图架：名物图 / 义理图两套定版坐标。
坐标与 scripts/gen_figs_012.py、gen_figs_013.py 一致；各篇只画格内母题。"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(ROOT, "assets", "fig")
INK, INK2, INK3, RED, PAPER = "#1F1B17", "#5C544A", "#9A9186", "#994433", "#F7F4EE"
W, H = 760, 540
CENTERS = [148, 378, 622]


def _name_header(d, title, juan, chnum):
    d.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="\'Noto Serif SC\',\'Songti SC\',serif">' % (W, H, W, H))
    d.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    d.append('  <text x="44" y="58" font-size="8.6" letter-spacing="2" fill="%s">%s</text>' % (RED, juan))
    d.append('  <text x="380" y="60" text-anchor="middle" font-size="26" letter-spacing="10" fill="%s" font-weight="700">%s</text>' % (INK, title))
    d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之%s</text>' % (INK3, chnum))
    d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)


def _name_footer(d, notes, quote, left, aid):
    for (x, t) in zip([44, 264, 486], notes):
        d.append('  <text x="%d" y="466" font-size="7.8" fill="%s">%s</text>' % (x, INK2, t))
    d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
    d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">%s</text>' % (INK, quote))
    d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">%s</text>' % (INK3, left))
    d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · %s</text>' % (INK3, aid))
    d.append('</svg>')


def name_fig(key, title, juan, chnum, notes, quote, left, aid, draw):
    d = []
    _name_header(d, title, juan, chnum)
    for (x, t) in zip([120, 350, 600], ["壹", "贰", "叁"]):
        d.append('  <text x="%d" y="132" font-size="7.6" fill="%s">%s</text>' % (x, RED, t))
    draw(d)
    _name_footer(d, notes, quote, left, aid)
    open(os.path.join(FIG, key + ".svg"), "w", encoding="utf-8").write("\n".join(d))
    return key


def logic_fig(key, title, sub, mark, cells, bottom, ruler1, ruler2, source, vol, bid):
    e = []
    e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="Noto Serif SC,Songti SC,serif">' % (W, H, W, H))
    e.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    e.append('  <rect x="10" y="10" width="740" height="500" fill="none" stroke="%s" stroke-width="1"/>' % INK3)
    e.append('  <rect x="16" y="16" width="728" height="488" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
    e.append('  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="%s" font-weight="700">%s</text>' % (INK, title))
    e.append('  <text x="380" y="74" text-anchor="middle" font-size="9.6" letter-spacing="2" fill="%s">%s</text>' % (INK2, sub))
    e.append('  <defs><marker id="%s" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % (mark, RED))
    xs = [70, 290, 510]
    for (x, big, s1, s2, col), cx in zip(cells, xs):
        e.append('  <rect x="%d" y="150" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (x, col))
        e.append('  <text x="%d" y="214" text-anchor="middle" font-size="28" letter-spacing="2" fill="%s" font-weight="700">%s</text>' % (x + 75, col, big))
        e.append('  <text x="%d" y="252" text-anchor="middle" font-size="10" fill="#3B352F">%s</text>' % (x + 75, s1))
        e.append('  <text x="%d" y="278" text-anchor="middle" font-size="8" fill="%s">%s</text>' % (x + 75, INK3, s2))
    e.append('  <line x1="220" y1="225" x2="288" y2="225" stroke="%s" stroke-width="1" marker-end="url(#%s)"/>' % (RED, mark))
    e.append('  <line x1="440" y1="225" x2="508" y2="225" stroke="%s" stroke-width="1" marker-end="url(#%s)"/>' % (RED, mark))
    e.append('  <text x="380" y="330" text-anchor="middle" font-size="8.4" fill="%s">%s</text>' % (INK2, bottom))
    e.append('  <line x1="120" y1="360" x2="640" y2="360" stroke="%s" stroke-width="0.8"/>' % INK3)
    e.append('  <text x="230" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">%s</text>' % (RED, ruler1[0]))
    e.append('  <text x="230" y="414" text-anchor="middle" font-size="7.4" fill="%s">%s</text>' % (INK3, ruler1[1]))
    e.append('  <text x="530" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">%s</text>' % (RED, ruler2[0]))
    e.append('  <text x="530" y="414" text-anchor="middle" font-size="7.4" fill="%s">%s</text>' % (INK3, ruler2[1]))
    e.append('  <text x="380" y="446" text-anchor="middle" font-size="7.4" fill="%s">%s</text>' % (INK3, source))
    e.append('  <text x="120" y="512" font-size="5.6" fill="%s">诗经 · %s</text>' % (INK2, vol))
    e.append('  <text x="640" y="512" text-anchor="end" font-size="5.6" fill="%s">图二 · %s · %s</text>' % (INK2, bid, key))
    e.append('</svg>')
    open(os.path.join(FIG, key + ".svg"), "w", encoding="utf-8").write("\n".join(e))
    return key


# ---- 线描基元（纯 SVG 原语，不依赖 shapely 几何并集） ----
def line(d, x1, y1, x2, y2, col=INK2, w=0.9):
    d.append('  <line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="%g"/>' % (x1, y1, x2, y2, col, w))

def path(d, dstr, col=INK2, w=0.9, fill="none"):
    d.append('  <path d="%s" fill="%s" stroke="%s" stroke-width="%g"/>' % (dstr, fill, col, w))

def circ(d, cx, cy, r, col=INK2, fill="#FCFAF6", w=0.9):
    d.append('  <circle cx="%g" cy="%g" r="%g" fill="%s" stroke="%s" stroke-width="%g"/>' % (cx, cy, r, fill, col, w))

def ell(d, cx, cy, rx, ry, col=INK2, fill="#FCFAF6", w=0.9):
    d.append('  <ellipse cx="%g" cy="%g" rx="%g" ry="%g" fill="%s" stroke="%s" stroke-width="%g"/>' % (cx, cy, rx, ry, fill, col, w))

def rect(d, x, y, w, h, col=INK2, fill="#FCFAF6", sw=0.9):
    d.append('  <rect x="%g" y="%g" width="%g" height="%g" fill="%s" stroke="%s" stroke-width="%g"/>' % (x, y, w, h, fill, col, sw))

def txt(d, x, y, s, col=RED, size=7.0, anchor="middle"):
    d.append('  <text x="%g" y="%g" text-anchor="%s" font-size="%g" fill="%s">%s</text>' % (x, y, anchor, size, col, s))

def blossom(d, cx, cy, r, col=INK2):
    """五瓣花带蕊，枝上可辨。"""
    import math
    for k in range(5):
        a = math.tau * k / 5 - math.pi / 2
        px = cx + r * math.cos(a)
        py = cy + r * math.sin(a)
        circ(d, px, py, r * 0.6, col, "#FCFAF6", 0.7)
    circ(d, cx, cy, r * 0.34, INK, "#EFEAD6", 0.7)

def reed(d, x, base, h, lean=0, col=INK2):
    """芦苇：茎、叶鞘、穗。"""
    top = (x + lean, base - h)
    path(d, "M%g,%g C%g,%g %g,%g %g,%g" % (x, base, x + lean * 0.4, base - h * 0.5, top[0], top[1] + 14, top[0], top[1]), col, 0.9)
    # 叶
    path(d, "M%g,%g Q%g,%g %g,%g" % (x, base - h * 0.55, x - 12, base - h * 0.45, x - 16, base - h * 0.3), INK3, 0.6)
    # 穗
    path(d, "M%g,%g Q%g,%g %g,%g" % (top[0], top[1] + 4, top[0] + 10, top[1] - 2, top[0] + 12, top[1] - 12), col, 0.7)

def wheel(d, cx, cy, r, col=INK2):
    """车轮：轮圈 + 辐条 + 毂。"""
    circ(d, cx, cy, r, col, "none", 1.0)
    circ(d, cx, cy, r * 0.18, col, "#FCFAF6", 0.7)
    for k in range(6):
        import math
        a = math.tau * k / 6
        line(d, cx, cy, cx + r * math.cos(a), cy + r * math.sin(a), col, 0.6)

# ---- 坐标越界自检 ----
def audit(path_keys):
    bad = []
    for k in path_keys:
        fp = os.path.join(FIG, k + ".svg")
        txt = open(fp, encoding="utf-8").read()
        for tag in ["circle", "rect", "line", "ellipse"]:
            for m in re.finditer(r"<%s\b[^>]*>" % tag, txt):
                s = m.group(0)
                for attr in ["x", "y", "x1", "y1", "x2", "y2", "cx", "cy"]:
                    mm = re.search(r"%s=\"(-?[\d.]+)\"" % attr, s)
                    if mm and not (0 <= float(mm.group(1)) <= (W if attr in ("x", "x1", "x2", "cx") else H)):
                        bad.append((k, tag, attr, mm.group(1)))
        for m in re.finditer(r"[ML](-?[\d.]+),(-?[\d.]+)", txt):
            x, y = float(m.group(1)), float(m.group(2))
            if not (0 <= x <= W and 0 <= y <= H):
                bad.append((k, "path", "M/L", (x, y)))
    return bad
