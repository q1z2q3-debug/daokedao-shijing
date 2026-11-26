# -*- coding: utf-8 -*-
"""图式 v2：三段式版心 + 写生线描 + 三阶墨 + 单色赭。生成《关雎》名物图。"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(ROOT, "assets", "fig")
os.makedirs(FIG, exist_ok=True)

INK = "#1F1B17"   # 主形
INK2 = "#5C544A"  # 次形
INK3 = "#9A9186"  # 淡形
RED = "#994433"
PAPER = "#F7F4EE"

W, H = 760, 540


def bird(scale, flip=False):
    """侧视水鸟，局部 0-100 x, 0-110 y，脚底在 y≈110。"""
    d_body = ("M100,40 C95,37 88,36 84,38 C80,34 78,31 74,30 "
              "C70,29 66,30 62,33 C58,37 55,42 52,50 "
              "C49,56 47,60 44,62 C36,65 28,66 22,66 "
              "C16,66 10,64 8,62 C10,68 12,72 18,74 "
              "C26,80 34,84 42,85 C50,86 58,84 64,78 "
              "C69,73 72,67 74,62 C77,56 79,50 80,46 "
              "C85,44 92,43 100,40 Z")
    g = []
    g.append('    <path d="%s" fill="%s" stroke="%s" stroke-width="0.55"/>' % (d_body, PAPER, INK))
    # 翅：一笔轮廓 + 一条内部羽向
    g.append('    <path d="M44,60 C36,64 28,66 22,67" fill="none" stroke="%s" stroke-width="0.4"/>' % INK2)
    g.append('    <path d="M39,65 C33,68 27,69 23,70" fill="none" stroke="%s" stroke-width="0.3"/>' % INK3)
    # 眼
    g.append('    <circle cx="72" cy="36" r="1.2" fill="%s"/>' % INK)
    g.append('    <circle cx="71.6" cy="35.6" r="0.38" fill="%s"/>' % PAPER)
    # 喙：上下两笔
    g.append('    <path d="M96,37 C91,38 87,39 84,39" fill="none" stroke="%s" stroke-width="0.3"/>' % INK2)
    g.append('    <path d="M94,44 C90,44 87,44 84,43" fill="none" stroke="%s" stroke-width="0.3"/>' % INK2)
    # 颈线（喉到胸，一笔轻）
    g.append('    <path d="M74,54 C73,62 69,70 64,74" fill="none" stroke="%s" stroke-width="0.25"/>' % INK3)
    # 腿与蹼
    g.append('    <path d="M40,85 L40,100 M52,85 L52,100" fill="none" stroke="%s" stroke-width="0.45"/>' % INK2)
    g.append('    <path d="M40,100 C35,102 32,104 31,106" fill="none" stroke="%s" stroke-width="0.3"/>' % INK2)
    g.append('    <path d="M40,100 L40,106 M40,100 C45,102 48,104 49,106" fill="none" stroke="%s" stroke-width="0.3"/>' % INK2)
    g.append('    <path d="M31,106 C36,104 44,104 49,106" fill="none" stroke="%s" stroke-width="0.2"/>' % INK3)
    sx = -scale if flip else scale
    return '  <g transform="translate(%s,%s) scale(%s,%s)">\n%s\n  </g>\n' % ("{tx}", "{ty}", sx, scale,
                                                                          "\n".join(g))


def fw(x):
    return "{:.1f}".format(x)


out = []
out.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" '
           'font-family="\'Noto Serif SC\',\'Songti SC\',serif">' % (W, H, W, H))
out.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))

# ---------- 上段 ----------
out.append('  <text x="44" y="60" font-size="8.6" letter-spacing="2" fill="%s">周南 · 一</text>' % RED)
out.append('  <text x="380" y="62" text-anchor="middle" font-size="29" letter-spacing="14" fill="%s" font-weight="700">关 雎</text>' % INK)
out.append('  <text x="716" y="60" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之首</text>' % INK3)
out.append('  <line x1="44" y1="100" x2="716" y2="100" stroke="%s" stroke-width="0.8"/>' % INK3)

# ---------- 中段：洲、水、鸟、荇菜 ----------
# 远岸
out.append('  <path d="M44,196 C160,186 300,182 420,188 C540,193 650,200 716,206" fill="none" stroke="%s" stroke-width="0.3" stroke-dasharray="6 4 2 4"/>' % INK3)
# 水纹（渐隐）
for i, y in enumerate([228, 252, 276, 300, 324, 348]):
    op = 0.55 - i * 0.06
    out.append('  <path d="M44,%d q26,-3 52,0 q26,3 52,0 q26,-3 52,0 q26,3 52,0 q26,-3 52,0 q26,3 52,0 q26,-3 52,0 q26,3 52,0 q26,-3 52,0 q26,3 52,0" fill="none" stroke="%s" stroke-width="0.3" opacity="%.2f" stroke-dasharray="14 5 3 6"/>' % (y, INK3, op))
# 沙洲（极淡填，不规则）
out.append('  <path d="M44,382 C130,362 230,352 360,356 C450,359 520,366 590,372 C650,377 690,378 716,376 C716,392 640,398 500,400 C350,402 150,400 44,382 Z" fill="#F1EBDF" stroke="none"/>')
out.append('  <path d="M44,382 C130,362 230,352 360,356 C450,359 520,366 590,372 C650,377 690,378 716,376" fill="none" stroke="%s" stroke-width="0.4"/>' % INK2)
out.append('  <path d="M44,382 C130,390 240,396 380,396 C520,396 620,390 716,376" fill="none" stroke="%s" stroke-width="0.25" stroke-dasharray="4 3"/>' % INK3)

# 鸟一（主）
out.append(bird(1.75).replace("{tx}", "110").replace("{ty}", "200"))
# 鸟二（远、较小、镜像）
out.append(bird(1.34, flip=True).replace("{tx}", "556").replace("{ty}", "252"))

# 荇菜一株：茎、圆叶三、根须、一花
x0, y0 = 470, 430
out.append('  <path d="M%d,%d C468,400 466,378 466,356" fill="none" stroke="%s" stroke-width="0.35"/>' % (x0, y0, INK2))
out.append('  <path d="M470,430 C478,418 486,410 494,406 M470,430 C462,420 456,412 450,408 M470,430 C468,416 466,404 464,392" fill="none" stroke="%s" stroke-width="0.3"/>' % INK2)
out.append('  <path d="M470,430 C470,438 469,444 468,450 M470,430 C466,436 462,440 458,442 M470,430 C474,436 478,439 482,441" fill="none" stroke="%s" stroke-width="0.22" stroke-dasharray="2 2"/>' % INK3)
out.append('  <path d="M462,354 q4,-3 8,0 q4,3 8,0" fill="none" stroke="%s" stroke-width="0.2"/>' % INK3)
out.append('  <circle cx="466" cy="340" r="11" fill="%s" stroke="%s" stroke-width="0.45"/>' % (PAPER, INK2))
out.append('  <circle cx="466" cy="340" r="11" fill="none" stroke="%s" stroke-width="0.2" stroke-dasharray="1.5 2"/>' % INK3)
out.append('  <circle cx="494" cy="404" r="9.5" fill="%s" stroke="%s" stroke-width="0.45"/>' % (PAPER, INK2))
out.append('  <circle cx="450" cy="406" r="8.5" fill="%s" stroke="%s" stroke-width="0.45"/>' % (PAPER, INK2))
# 花
out.append('  <path d="M566,336 C566,356 560,374 552,390" fill="none" stroke="%s" stroke-width="0.35"/>' % INK2)
for a in range(5):
    out.append('  <ellipse cx="566" cy="330" rx="3.4" ry="5" fill="%s" stroke="%s" stroke-width="0.3" transform="rotate(%d 566 336)"/>' % (PAPER, INK2, a * 72))
out.append('  <circle cx="566" cy="336" r="1.6" fill="%s"/>' % RED)

# 编号
out.append('  <text x="232" y="370" font-size="7.6" fill="%s">①</text>' % RED)
out.append('  <text x="668" y="352" font-size="7.6" fill="%s">②</text>' % RED)
out.append('  <text x="400" y="374" font-size="7.6" fill="%s">③</text>' % RED)

# 注文（中段下部一行三段）
out.append('  <text x="60" y="414" font-size="7.8" fill="%s">① 雎鸠　生有定偶，并游而不相狎</text>' % INK2)
out.append('  <text x="420" y="414" font-size="7.8" fill="%s">② 荇菜　圆叶细茎，可为菹　③ 洲　水中可居</text>' % INK2)

# ---------- 下段 ----------
out.append('  <line x1="44" y1="432" x2="716" y2="432" stroke="%s" stroke-width="0.8"/>' % INK3)
out.append('  <text x="380" y="474" text-anchor="middle" font-size="17" letter-spacing="3" fill="%s">關關雎鳩，在河之洲</text>' % INK)
out.append('  <text x="380" y="494" text-anchor="middle" font-size="8.6" letter-spacing="1" fill="%s">鸟有定偶，草无定形：一章之内，一取定，一取择。</text>' % INK3)
out.append('  <text x="716" y="524" text-anchor="end" font-size="7.6" letter-spacing="1" fill="%s">图一 · 名物 · sj001a</text>' % INK3)
# 朱印
out.append('  <rect x="44" y="498" width="26" height="26" fill="%s"/>' % RED)
out.append('  <text x="57" y="511" text-anchor="middle" font-size="6.4" fill="%s">润</text>' % PAPER)
out.append('  <text x="57" y="520" text-anchor="middle" font-size="6.4" fill="%s">泽</text>' % PAPER)
out.append('</svg>')

svg = "\n".join(out)
p = os.path.join(FIG, "sj001a-v2.svg")
open(p, "w", encoding="utf-8").write(svg)

import cairosvg
cairosvg.svg2png(url=p, write_to="/tmp/a2.png", output_width=900)
print("ok")
