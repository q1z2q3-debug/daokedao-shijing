# -*- coding: utf-8 -*-
"""SJ005《螽斯》图一（群飞版）：三只简笔螽斯、振翅声弧、土中卵块。"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(ROOT, "assets", "fig")
INK, INK2, INK3, RED, PAPER = "#1F1B17", "#5C544A", "#9A9186", "#994433", "#F7F4EE"
W, H = 760, 540

BODY = "M-34,0 C-24,-8 -2,-9 14,-7 L22,-5 C24,-1 24,2 20,4 L-2,8 C-22,9 -30,5 -34,0 Z"
HEAD = ("24", "-2")
ANT = "M28,-6 C40,-15 52,-19 61,-19"

d = []
d.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="\'Noto Serif SC\',\'Songti SC\',serif">' % (W, H, W, H))
d.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
d.append('  <text x="44" y="58" font-size="8.6" letter-spacing="2" fill="%s">周南 · 五</text>' % RED)
d.append('  <text x="380" y="60" text-anchor="middle" font-size="28" letter-spacing="14" fill="%s" font-weight="700">螽 斯</text>' % INK)
d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之五</text>' % INK3)
d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)

# 草茎
for (x0, x1, w) in [(252, 262, 2.2), (416, 424, 1.8), (472, 468, 1.5)]:
    d.append('  <path d="M%d,448 C%d,392 %d,300 %d,196" fill="none" stroke="%s" stroke-width="%.1f"/>' % (x0, (x0 + x1) // 2, x1, x1, INK, w))
d.append('  <path d="M262,448 C272,392 262,300 262,196" fill="none" stroke="%s" stroke-width="0.5"/>' % INK3)
for (x, y, dx, dy) in [(258, 258, 34, -14), (420, 300, -30, -16), (470, 340, -28, -18)]:
    d.append('  <path d="M%d,%d C%d,%d %d,%d %d,%d" fill="none" stroke="%s" stroke-width="1.2"/>'
             % (x, y, x + dx // 3, y + dy, x + 2 * dx // 3, y + int(dy * 0.7), x + dx, y + int(dy * 0.4), INK2))


def bug(tx, ty, sc, rot):
    g = []
    g.append('  <g transform="translate(%d,%d) rotate(%d) scale(%.2f)">' % (tx, ty, rot, sc))
    g.append('    <path d="%s" fill="#F1E9D5" stroke="%s" stroke-width="0.9"/>' % (BODY, INK))
    g.append('    <path d="M-28,1 C-8,-4 10,-3 20,-1" fill="none" stroke="%s" stroke-width="0.6"/>' % INK2)
    for i in range(3):
        g.append('    <path d="M%d,%d C%d,%d %d,%d %d,%d" fill="none" stroke="%s" stroke-width="0.3"/>'
                 % (-16 + i * 12, 5, -14 + i * 12, -2, -8 + i * 12, -1, -6 + i * 12, 6, INK3))
    g.append('    <ellipse cx="26" cy="-3" rx="7.0" ry="5.6" fill="#F5EEDD" stroke="%s" stroke-width="0.8"/>' % INK)
    g.append('    <circle cx="29" cy="-4" r="1.7" fill="%s"/>' % INK2)
    g.append('    <path d="M29,-8 C41,-17 53,-21 62,-21" fill="none" stroke="%s" stroke-width="1.4"/>' % INK)
    g.append('    <path d="M31,-1 C43,-10 55,-15 63,-16" fill="none" stroke="%s" stroke-width="1.1"/>' % INK2)
    # 后腿
    g.append('    <path d="M-10,7 C-16,14 -20,20 -24,26" fill="none" stroke="%s" stroke-width="2.4"/>' % INK2)
    g.append('    <path d="M-24,26 C-20,34 -13,40 -6,43" fill="none" stroke="%s" stroke-width="1.1"/>' % INK2)
    g.append('    <path d="M-6,43 L2,45" fill="none" stroke="%s" stroke-width="0.9"/>' % INK2)
    # 中前足
    g.append('    <path d="M2,8 C-1,16 -4,24 -8,31" fill="none" stroke="%s" stroke-width="1.0"/>' % INK2)
    g.append('    <path d="M16,7 C14,15 12,23 10,30" fill="none" stroke="%s" stroke-width="1.0"/>' % INK2)
    g.append('  </g>')
    return g


for item in bug(424, 254, 1.55, -12) + bug(342, 302, 1.35, -4) + bug(292, 366, 1.2, 8):
    d.append(item)

# 声弧（薨薨）
for (cx, cy, r) in [(424, 216, 32), (424, 210, 44), (342, 264, 30), (342, 258, 42), (292, 330, 26), (292, 326, 36)]:
    d.append('  <path d="M%d,%d A%d,%d 0 0 1 %d,%d" fill="none" stroke="%s" stroke-width="0.4"/>'
             % (cx - r * 0.76, cy - r * 0.6, r, r, cx + r * 0.3, cy - r * 0.9, INK3))

# 卵块（与草丛同土，左端接到草茎根部）
d.append('  <path d="M470,404 C476,424 486,440 502,444" fill="none" stroke="%s" stroke-width="0.3" stroke-dasharray="5 4"/>' % INK3)
d.append('  <path d="M470,404 C540,400 636,400 672,404" fill="none" stroke="%s" stroke-width="0.3" stroke-dasharray="7 4 1.5 4"/>' % INK3)
d.append('  <rect x="520" y="408" width="136" height="48" fill="#F3EEE0" stroke="%s" stroke-width="0.35"/>' % INK3)
for r in range(3):
    for c in range(6):
        cx, cy = 538 + c * 19 + (r % 2) * 5, 419 + r * 13
        d.append('  <ellipse cx="%d" cy="%d" rx="5.8" ry="7.0" fill="%s" stroke="%s" stroke-width="0.32"/>' % (cx, cy, "#FCF8EE", INK2))
d.append('  <path d="M520,408 C556,404 622,404 656,408" fill="none" stroke="%s" stroke-width="0.42"/>' % INK2)

d.append('  <text x="252" y="242" font-size="7.6" fill="%s">①</text>' % RED)
d.append('  <text x="386" y="206" font-size="7.6" fill="%s">②</text>' % RED)
d.append('  <text x="644" y="428" font-size="7.6" fill="%s">③</text>' % RED)

d.append('  <text x="44" y="466" font-size="7.8" fill="%s">① 螽斯　长触角，善跳；群飞则翅有声</text>' % INK2)
d.append('  <text x="316" y="466" font-size="7.8" fill="%s">② 羽　声从翅出，不在口</text>' % INK2)
d.append('  <text x="516" y="466" font-size="7.8" fill="%s">③ 卵块　土中一囊，粒可数十</text>' % INK2)
d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">螽斯羽，詵詵兮</text>' % INK)
d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">取其多子，不取其害稼</text>' % INK3)
d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj005a</text>' % INK3)
d.append('</svg>')
open(os.path.join(FIG, "sj005a-zhong-si-yu-luan.svg"), "w", encoding="utf-8").write("\n".join(d))

import cairosvg
cairosvg.svg2png(url=os.path.join(FIG, "sj005a-zhong-si-yu-luan.svg"), write_to="/tmp/sj005a.png", output_width=920)
print("ok")
