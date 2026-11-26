# -*- coding: utf-8 -*-
"""图式 v3：三段版心 + 全形小像 + 局部特写 + 注文带。名物图（关雎）。"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fig_geo import *
from shapely.geometry import LineString

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(ROOT, "assets", "fig")

INK, INK2, INK3, RED, PAPER = "#1F1B17", "#5C544A", "#9A9186", "#994433", "#F7F4EE"
W, H = 760, 540
d = []


def T(s):
    d.append(s)


T('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="\'Noto Serif SC\',\'Songti SC\',serif">' % (W, H, W, H))
T('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))

# ---------- 上段 ----------
T('  <text x="44" y="58" font-size="8.6" letter-spacing="2" fill="%s">周南 · 一</text>' % RED)
T('  <text x="380" y="60" text-anchor="middle" font-size="28" letter-spacing="14" fill="%s" font-weight="700">关 雎</text>' % INK)
T('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之首</text>' % INK3)
T('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)

# ---------- 中段：水 ----------
T('  <path d="M44,150 C170,142 320,138 460,144 C580,149 670,154 716,158" fill="none" stroke="%s" stroke-width="0.3" stroke-dasharray="7 4 2 5"/>' % INK3)
for i, y in enumerate([176, 196, 216, 236, 256]):
    op = 0.5 - i * 0.07
    T('  <path d="M44,%d q24,-2.6 48,0 q24,2.6 48,0 q24,-2.6 48,0 q24,2.6 48,0 q24,-2.6 48,0 q24,2.6 48,0 q24,-2.6 48,0 q24,2.6 48,0 q24,-2.6 48,0 q24,2.6 48,0 q24,-2.6 48,0 q24,2.6 48,0 q24,-2.6 48,0" fill="none" stroke="%s" stroke-width="0.28" opacity="%.2f" stroke-dasharray="16 6 3 7"/>' % (y, INK3, op))

# ---------- 沙洲 ----------
T('  <path d="M44,306 C130,292 240,284 380,288 C470,290 540,296 600,302 C660,307 696,308 716,306 C716,322 640,330 500,332 C350,334 160,332 44,306 Z" fill="#F1EBDF"/>')
T('  <path d="M44,306 C130,292 240,284 380,288 C470,290 540,296 600,302 C660,307 696,308 716,306" fill="none" stroke="%s" stroke-width="0.4"/>' % INK2)
T('  <path d="M44,306 C130,316 240,322 380,323 C470,323 540,318 600,312 C660,306 696,304 716,306" fill="none" stroke="%s" stroke-width="0.25" stroke-dasharray="4 3"/>' % INK3)

# ---------- 鸟：全形两小像 ----------
body = ell(54, 66, 40, 14.5, -6)
chest = ell(88, 62, 15, 16)
head = circle(100, 36, 9.5)
neck = ell(94, 49, 11.5, 14, 12)
beak = poly([(106, 32), (124, 35), (126, 38), (107, 43)])
tail = ell(20, 63, 17, 8, -16)
g = comb(body, chest, head, neck, beak, tail).buffer(2.2).buffer(-2.2)
bird_d, _ = to_path(g)
wing_d, _ = to_path(LineString([(62, 70), (52, 76), (36, 76), (26, 70)]).buffer(0.9).buffer(-2).buffer(2), iters=2)
leg = comb(LineString([(45, 82), (45, 94)]).buffer(1.0), LineString([(58, 82), (58, 94)]).buffer(1.0))
leg_d, _ = to_path(leg)
foot = comb(poly([(34, 93.5), (44, 101), (54, 93.5), (44, 96)]).buffer(0.4),
            poly([(40, 93.5), (44, 99), (48, 93.5), (44, 95)]))
foot_d, _ = to_path(foot)


def bird_group(tx, ty, s, flip=False):
    out = ['  <g transform="translate(%s,%s) scale(%s,%s)">' % (tx, ty, -s if flip else s, s)]
    out.append('    <path d="%s" fill="%s" stroke="%s" stroke-width="%.2f"/>' % (bird_d, PAPER, INK, 0.55 / s))
    out.append('    <path d="%s" fill="%s" stroke="%s" stroke-width="%.2f"/>' % (leg_d, PAPER, INK2, 0.4 / s))
    out.append('    <path d="M45,94 L38,100 M45,94 L45,101 M45,94 L52,100" fill="none" stroke="%s" stroke-width="%.2f"/>' % (INK2, 0.4 / s))
    out.append('    <path d="M38,100 C42,98 48,98 52,100" fill="none" stroke="%s" stroke-width="%.2f"/>' % (INK3, 0.25 / s))
    out.append('    <path d="M58,94 L51,100 M58,94 L58,101 M58,94 L65,100" fill="none" stroke="%s" stroke-width="%.2f"/>' % (INK2, 0.4 / s))
    out.append('    <path d="M51,100 C55,98 61,98 65,100" fill="none" stroke="%s" stroke-width="%.2f"/>' % (INK3, 0.25 / s))
    out.append('    <path d="M62,70 C52,76 36,76 26,70" fill="none" stroke="%s" stroke-width="%.2f"/>' % (INK2, 0.3 / s))
    out.append('    <path d="M56,74 C48,77 38,77 30,73" fill="none" stroke="%s" stroke-width="%.2f"/>' % (INK3, 0.25 / s))
    out.append('    <circle cx="100" cy="34" r="1.4" fill="%s"/>' % INK)
    out.append('    <circle cx="99.6" cy="33.6" r="0.45" fill="%s"/>' % PAPER)
    out.append('    <path d="M120,35 C116,36 112,37 108,38" fill="none" stroke="%s" stroke-width="%.2f"/>' % (INK2, 0.25 / s))
    out.append('  </g>')
    return "\n".join(out)


# 脚底 104 → 落在洲面 y≈300
T(bird_group(108, 300 - 104 * 1.12, 1.12))
T(bird_group(436, 300 - 104 * 0.96 + 5, 0.96, flip=True))

# ---------- 局部特写 ----------
T('  <defs><clipPath id="c1"><circle cx="132" cy="382" r="40"/></clipPath>'
  '<clipPath id="c2"><circle cx="244" cy="382" r="40"/></clipPath></defs>')
# ① 扁喙：独立小写生（头 + 喙）
T('  <circle cx="132" cy="382" r="40" fill="%s" stroke="%s" stroke-width="0.4"/>' % (PAPER, INK3))
T('  <path d="M116,362 C118,344 132,336 146,340 C156,343 160,350 160,358" fill="none" stroke="%s" stroke-width="0.5"/>' % INK)
T('  <path d="M160,358 C168,356 176,358 184,362 C178,366 170,368 162,367" fill="none" stroke="%s" stroke-width="0.5"/>' % INK)
T('  <path d="M160,362 C170,361 178,363 184,362" fill="none" stroke="%s" stroke-width="0.5"/>' % INK)
T('  <path d="M160,366 C170,368 176,370 184,368" fill="none" stroke="%s" stroke-width="0.45"/>' % INK2)
T('  <path d="M184,362 C188,363 190,365 190,366 C188,368 186,368 184,368" fill="%s" stroke="%s" stroke-width="0.3"/>' % ('#EFE8DB', INK2))
T('  <path d="M168,368 C174,369 180,370 186,370" fill="none" stroke="%s" stroke-width="0.18"/>' % INK3)
T('  <circle cx="146" cy="352" r="1.7" fill="%s"/>' % INK)
T('  <circle cx="145.5" cy="351.4" r="0.5" fill="%s"/>' % PAPER)
T('  <ellipse cx="168" cy="358" rx="1.4" ry="0.9" fill="none" stroke="%s" stroke-width="0.22"/>' % INK3)
T('  <path d="M124,344 C132,338 142,336 150,338" fill="none" stroke="%s" stroke-width="0.18"/>' % INK3)
# ② 蹼足：自绘局部
T('  <circle cx="244" cy="382" r="40" fill="%s" stroke="%s" stroke-width="0.4"/>' % (PAPER, INK3))
T('  <path d="M244,344 L244,392" stroke="%s" stroke-width="0.55" fill="none"/>' % INK)
T('  <path d="M244,392 C232,398 222,404 216,410" stroke="%s" stroke-width="0.45" fill="none"/>' % INK2)
T('  <path d="M244,392 L244,414" stroke="%s" stroke-width="0.45" fill="none"/>' % INK2)
T('  <path d="M244,392 C256,398 266,404 272,410" stroke="%s" stroke-width="0.45" fill="none"/>' % INK2)
T('  <path d="M216,410 C230,404 258,404 272,410" fill="none" stroke="%s" stroke-width="0.22"/>' % INK3)
T('  <path d="M244,406 C240,410 240,412 241,414 M244,406 C248,410 248,412 247,414" fill="none" stroke="%s" stroke-width="0.2"/>' % INK3)
T('  <text x="132" y="436" text-anchor="middle" font-size="7.2" fill="%s">① 扁喙</text>' % INK2)
T('  <text x="244" y="436" text-anchor="middle" font-size="7.2" fill="%s">② 蹼足</text>' % INK2)

# ---------- 荇菜 ----------
T('  <path d="M620,344 C620,326 620,306 620,292" fill="none" stroke="%s" stroke-width="0.4"/>' % INK2)
T('  <path d="M620,320 C614,314 606,310 598,308" fill="none" stroke="%s" stroke-width="0.32"/>' % INK2)
T('  <path d="M620,328 C628,322 638,318 646,316" fill="none" stroke="%s" stroke-width="0.32"/>' % INK2)
T('  <path d="M620,344 C616,352 612,358 606,362 M620,344 C620,354 620,360 620,364 M620,344 C624,352 628,358 634,362" fill="none" stroke="%s" stroke-width="0.22" stroke-dasharray="2.5 2"/>' % INK3)
for cx, cy, r in [(620, 280, 13), (596, 306, 9.5), (650, 314, 9)]:
    T('  <circle cx="%d" cy="%d" r="%.1f" fill="%s" stroke="%s" stroke-width="0.45"/>' % (cx, cy, r, PAPER, INK2))
    T('  <circle cx="%d" cy="%d" r="%.1f" fill="none" stroke="%s" stroke-width="0.18" stroke-dasharray="1.5 2.5"/>' % (cx, cy, r - 1.8, INK3))
    T('  <path d="M%d,%d L%d,%d" stroke="%s" stroke-width="0.18"/>' % (cx - r + 3, cy - 2, cx + r - 3, cy - 2, INK3))
T('  <path d="M696,318 C696,330 692,340 688,348" fill="none" stroke="%s" stroke-width="0.32"/>' % INK2)
for a in range(5):
    T('  <ellipse cx="696" cy="308" rx="3.2" ry="4.6" fill="%s" stroke="%s" stroke-width="0.28" transform="rotate(%d 696 314)"/>' % (PAPER, INK2, a * 72))
T('  <circle cx="696" cy="314" r="1.5" fill="%s"/>' % RED)
T('  <text x="700" y="360" text-anchor="middle" font-size="7.6" fill="%s">③</text>' % RED)

# ---------- 注文带 ----------
T('  <text x="44" y="466" font-size="7.8" fill="%s">① 扁喙、② 蹼足　水鸟之征：凫鹥之属，定偶而不相狎</text>' % INK2)
T('  <text x="560" y="466" font-size="7.8" fill="%s">③ 荇菜　圆叶细茎，可为菹</text>' % INK2)

# ---------- 下段 ----------
T('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
T('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">關關雎鳩，在河之洲</text>' % INK)
T('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">鸟有定偶，草无定形</text>' % INK3)
T('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj001a</text>' % INK3)
T('  <rect x="668" y="486" width="0" height="0"/>')
T('</svg>')

svg = "\n".join(d)
p = os.path.join(FIG, "sj001a-v3.svg")
open(p, "w", encoding="utf-8").write(svg)
import cairosvg
cairosvg.svg2png(url=p, write_to="/tmp/a4.png", output_width=920)
print("ok")
