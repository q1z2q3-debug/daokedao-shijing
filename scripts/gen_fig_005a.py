# -*- coding: utf-8 -*-
"""SJ005《螽斯》图一：抱茎之螽，长触角，翅发声，土中卵块。"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(ROOT, "assets", "fig")
INK, INK2, INK3, RED, PAPER = "#1F1B17", "#5C544A", "#9A9186", "#994433", "#F7F4EE"
W, H = 760, 540

d = []
d.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="\'Noto Serif SC\',\'Songti SC\',serif">' % (W, H, W, H))
d.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
d.append('  <text x="44" y="58" font-size="8.6" letter-spacing="2" fill="%s">周南 · 五</text>' % RED)
d.append('  <text x="380" y="60" text-anchor="middle" font-size="28" letter-spacing="14" fill="%s" font-weight="700">螽 斯</text>' % INK)
d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之五</text>' % INK3)
d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)

# —— 草茎（斜，抱于虫足之下）——
d.append('  <path d="M262,452 C296,392 320,336 336,272 C346,232 344,206 340,192" fill="none" stroke="%s" stroke-width="2.6"/>' % INK)
d.append('  <path d="M267,450 C300,390 324,334 340,270 C350,230 348,204 344,190" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
# 叶片
for (x, y, sx, sy, ex, ey) in [(338, 214, 306, 196, 286, 206), (330, 250, 366, 230, 392, 238), (312, 330, 276, 316, 258, 328)]:
    d.append('  <path d="M%.1f,%d C%.1f,%d %.1f,%d %.1f,%d" fill="none" stroke="%s" stroke-width="1.3"/>'
             % (x, y, (x + sx) / 2, (y + sy) / 2, (sx + ex) / 2, (sy + ey) / 2, ex, ey, INK2))

# —— 虫体（朝右）——
d.append('  <path d="M302,292 C332,272 402,272 442,282 C448,292 444,306 402,310 C352,314 314,306 302,292 Z" fill="#F2EAD8" stroke="%s" stroke-width="0.8"/>' % INK)
for x in (324, 348, 372, 396, 420):
    d.append('  <path d="M%d,%.1f C%d,%.1f %d,%.1f %d,%.1f" fill="none" stroke="%s" stroke-width="0.3"/>'
             % (x, 290, x + 8, 284, x + 8, 304, x, 308, INK3))
# 前翅
d.append('  <path d="M434,280 C396,272 342,282 320,298 C342,308 398,310 436,294 Z" fill="#EFE6D0" stroke="%s" stroke-width="0.75"/>' % INK)
for i in range(4):
    d.append('  <path d="M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="none" stroke="%s" stroke-width="0.26"/>'
             % (430 - 6 * i, 284 + 2 * i, 392, 278 + 8 * (i / 3.0), 348, 288 + 8 * (i / 3.0), 324, 297, INK3))
d.append('  <path d="M434,288 C440,294 442,300 436,305" fill="none" stroke="%s" stroke-width="0.5"/>' % INK2)
# 头
d.append('  <path d="M446,280 C456,270 472,269 480,279 C486,288 480,300 466,301 C452,300 446,291 446,280 Z" fill="#F4EDDC" stroke="%s" stroke-width="0.75"/>' % INK)
d.append('  <ellipse cx="476" cy="277" rx="5.2" ry="4.4" fill="%s" stroke="%s" stroke-width="0.4"/>' % (INK2, INK))
d.append('  <path d="M478,293 C483,295 486,292 486,288" fill="none" stroke="%s" stroke-width="0.45"/>' % INK3)
# 触角（长过身）
d.append('  <path d="M460,272 C486,240 540,214 588,212" fill="none" stroke="%s" stroke-width="1.5"/>' % INK)
d.append('  <path d="M468,281 C494,252 548,232 586,231" fill="none" stroke="%s" stroke-width="1.2"/>' % INK2)
# 足（三对，抓茎）
d.append('  <path d="M450,300 C446,320 440,334 430,344" fill="none" stroke="%s" stroke-width="1.5"/>' % INK)
d.append('  <path d="M430,344 L420,350" fill="none" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <path d="M422,306 C416,326 408,338 398,348" fill="none" stroke="%s" stroke-width="1.5"/>' % INK)
d.append('  <path d="M398,348 L390,354" fill="none" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <path d="M378,308 C360,320 342,332 328,344" fill="none" stroke="%s" stroke-width="3.2"/>' % INK)
d.append('  <path d="M328,344 C338,366 350,382 364,390" fill="none" stroke="%s" stroke-width="1.6"/>' % INK)
d.append('  <path d="M364,390 L378,392" fill="none" stroke="%s" stroke-width="1.0"/>' % INK2)
for t in (0.25, 0.45, 0.65, 0.85):
    x = 328 + (364 - 328) * t
    y = 344 + (390 - 344) * t + 3 * math.sin(t * 3)
    d.append('  <path d="M%.1f,%.1f l7,-4" stroke="%s" stroke-width="0.5"/>' % (x, y, INK2))

# —— 卵块 ——
d.append('  <path d="M488,406 C530,402 630,402 664,406" fill="none" stroke="%s" stroke-width="0.3" stroke-dasharray="7 4 1.5 4"/>' % INK3)
d.append('  <rect x="512" y="410" width="140" height="50" fill="#F3EEE0" stroke="%s" stroke-width="0.35"/>' % INK3)
for r in range(3):
    for c in range(6):
        cx, cy = 530 + c * 20 + (r % 2) * 5, 421 + r * 14
        d.append('  <ellipse cx="%d" cy="%d" rx="6.0" ry="7.4" fill="%s" stroke="%s" stroke-width="0.34"/>' % (cx, cy, "#FCF8EE", INK2))
d.append('  <path d="M512,410 C550,405 616,405 652,410" fill="none" stroke="%s" stroke-width="0.45"/>' % INK2)

# 编号
d.append('  <text x="316" y="266" font-size="7.6" fill="%s">①</text>' % RED)
d.append('  <text x="580" y="202" font-size="7.6" fill="%s">②</text>' % RED)
d.append('  <text x="646" y="432" font-size="7.6" fill="%s">③</text>' % RED)

d.append('  <text x="44" y="466" font-size="7.8" fill="%s">① 螽斯　蝗属，长触角，善跳，一产数十至百余</text>' % INK2)
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
