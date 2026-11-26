# -*- coding: utf-8 -*-
"""SJ005《螽斯》两图。图一：螽斯（羽、触角、卵块）。图二：多／聚／和 三格。"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fig_geo import *
from shapely.geometry import LineString, Point

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

# —— 草茎 ——
d.append('  <path d="M344,196 C350,250 340,330 346,404" fill="none" stroke="%s" stroke-width="2.4"/>' % INK)
d.append('  <path d="M348,196 C354,250 344,330 350,404" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
for y in (230, 268, 372):
    s = 1 if y < 300 else -1
    d.append('  <path d="M%.1f,%d C%.1f,%d %.1f,%d %.1f,%d" fill="none" stroke="%s" stroke-width="1.4"/>'
             % (347, y, 347 + s * 26, y - 16, 347 + s * 52, y - 10, 347 + s * 66, y + 4, INK2))

# —— 螽斯（侧视朝右）——
BODY = "M298,300 C314,286 366,282 398,288 C404,296 402,306 372,312 C336,316 308,312 298,300 Z"
d.append('  <path d="%s" fill="#F2EAD8" stroke="%s" stroke-width="0.75"/>' % (BODY, INK))
# 腹节
for x in (316, 334, 352, 370, 388):
    d.append('  <path d="M%d,%.1f C%d,%.1f %d,%.1f %d,%.1f" fill="none" stroke="%s" stroke-width="0.3"/>'
             % (x, 296 + (x - 298) * 0.02, x + 6, 290, x + 6, 308, x, 306 - (x - 298) * 0.01, INK3))
# 前翅（覆盖腹背）
WING = "M392,286 C356,280 316,290 302,302 C318,308 358,306 392,294 Z"
d.append('  <path d="%s" fill="#EFE6D0" stroke="%s" stroke-width="0.7"/>' % (WING, INK))
for i in range(4):
    t = i / 3.0
    d.append('  <path d="M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="none" stroke="%s" stroke-width="0.26"/>'
             % (388 - 4 * i, 288 + 2 * i, 356, 284 + 6 * t, 322, 292 + 5 * t, 306, 301 + 2 * t, INK3))
d.append('  <path d="M392,290 C398,296 400,302 394,306" fill="none" stroke="%s" stroke-width="0.5"/>' % INK2)
# 头
HEAD = "M410,284 C418,276 432,274 439,283 C444,291 439,301 428,302 C417,301 410,294 410,284 Z"
d.append('  <path d="%s" fill="#F4EDDC" stroke="%s" stroke-width="0.7"/>' % (HEAD, INK))
d.append('  <ellipse cx="435" cy="284" rx="4.4" ry="3.8" fill="%s" stroke="%s" stroke-width="0.4"/>' % (INK2, INK))
d.append('  <path d="M436,296 C440,297 442,295 442,292" fill="none" stroke="%s" stroke-width="0.4"/>' % INK3)
# 触角（长过身）
d.append('  <path d="M430,278 C452,254 490,234 526,232" fill="none" stroke="%s" stroke-width="1.3"/>' % INK)
d.append('  <path d="M434,286 C458,266 496,250 524,248" fill="none" stroke="%s" stroke-width="1.1"/>' % INK2)
# 前胸背板
d.append('  <path d="M400,286 C404,278 410,276 412,284" fill="none" stroke="%s" stroke-width="0.5"/>' % INK2)
# 足
d.append('  <path d="M414,298 C410,316 404,330 410,342" fill="none" stroke="%s" stroke-width="1.4"/>' % INK)
d.append('  <path d="M410,342 L420,346" fill="none" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <path d="M398,306 C394,324 388,338 392,352" fill="none" stroke="%s" stroke-width="1.4"/>' % INK)
d.append('  <path d="M392,352 L402,356" fill="none" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <path d="M374,308 C358,320 346,336 338,352" fill="none" stroke="%s" stroke-width="3.0"/>' % INK)
d.append('  <path d="M338,352 C346,372 354,384 364,390" fill="none" stroke="%s" stroke-width="1.5"/>' % INK)
d.append('  <path d="M364,390 L376,392" fill="none" stroke="%s" stroke-width="1.0"/>' % INK2)
for t in (0.28, 0.46, 0.64, 0.82):
    x = 338 + (364 - 338) * t
    y = 352 + (390 - 352) * t + 2 * math.sin(t * 3)
    d.append('  <path d="M%.1f,%.1f l6,-4" stroke="%s" stroke-width="0.5"/>' % (x, y, INK2))

# —— 卵块（土中剖面）——
d.append('  <path d="M462,404 C500,400 590,400 626,404" fill="none" stroke="%s" stroke-width="0.3" stroke-dasharray="7 4 1.5 4"/>' % INK3)
d.append('  <rect x="486" y="408" width="118" height="46" fill="#F3EEE0" stroke="%s" stroke-width="0.35"/>' % INK3)
for r in range(3):
    for c in range(6):
        cx, cy = 502 + c * 17 + (r % 2) * 4, 418 + r * 13
        d.append('  <ellipse cx="%d" cy="%d" rx="5.0" ry="6.4" fill="%s" stroke="%s" stroke-width="0.32"/>' % (cx, cy, "#FBF7EC", INK2))
d.append('  <path d="M486,408 C520,404 570,404 604,408" fill="none" stroke="%s" stroke-width="0.45"/>' % INK2)

# 编号
d.append('  <text x="300" y="278" font-size="7.6" fill="%s">①</text>' % RED)
d.append('  <text x="520" y="222" font-size="7.6" fill="%s">②</text>' % RED)
d.append('  <text x="600" y="424" font-size="7.6" fill="%s">③</text>' % RED)

d.append('  <text x="44" y="466" font-size="7.8" fill="%s">① 螽斯　蝗属，长触角，善跳，一产数十至百余</text>' % INK2)
d.append('  <text x="316" y="466" font-size="7.8" fill="%s">② 羽　声从翅出，不在口</text>' % INK2)
d.append('  <text x="516" y="466" font-size="7.8" fill="%s">③ 卵块　土中一囊，粒可数十</text>' % INK2)
d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">螽斯羽，詵詵兮</text>' % INK)
d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">取其多子，不取其害稼</text>' % INK3)
d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj005a</text>' % INK3)
d.append('</svg>')
open(os.path.join(FIG, "sj005a-zhong-si-yu-luan.svg"), "w", encoding="utf-8").write("\n".join(d))

# ============ 图二 ============
e = []
e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="\'Noto Serif SC\',\'Songti SC\',serif">' % (W, H, W, H))
e.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
e.append('  <rect x="10" y="10" width="740" height="500" fill="none" stroke="%s" stroke-width="1"/>' % INK3)
e.append('  <rect x="16" y="16" width="728" height="488" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
e.append('  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="%s" font-weight="700">多 · 聚 · 和</text>' % INK)
e.append('  <text x="380" y="74" text-anchor="middle" font-size="9.6" letter-spacing="2" fill="%s">《诗经》周南 · 第五篇　螽斯</text>' % INK2)
e.append('  <defs><marker id="ar5" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % RED)
cells = [(70, "詵", "诜诜，众多也", "数", INK2), (290, "揖", "揖揖，会聚也", "群", RED), (510, "蟄", "蛰蛰，和集也", "和", INK2)]
for (x, big, s1, s2, col) in cells:
    e.append('  <rect x="%d" y="150" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (x, col))
    e.append('  <text x="%d" y="214" text-anchor="middle" font-size="26" letter-spacing="2" fill="%s" font-weight="700">%s</text>' % (x + 75, col, big))
    e.append('  <text x="%d" y="254" text-anchor="middle" font-size="10" fill="#3B352F">%s</text>' % (x + 75, s1))
    e.append('  <text x="%d" y="278" text-anchor="middle" font-size="8" fill="%s">%s</text>' % (x + 75, INK3, s2))
e.append('  <line x1="220" y1="225" x2="288" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar5)"/>' % RED)
e.append('  <line x1="440" y1="225" x2="508" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar5)"/>' % RED)
e.append('  <text x="380" y="330" text-anchor="middle" font-size="8.4" fill="%s">以虫之多子，祝人之多子——比也，非兴</text>' % INK2)
e.append('  <line x1="120" y1="360" x2="640" y2="360" stroke="%s" stroke-width="0.8"/>' % INK3)
e.append('  <text x="230" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">振振</text>' % RED)
e.append('  <text x="230" y="414" text-anchor="middle" font-size="7.4" fill="%s">毛传：仁厚也——多而不厚则散</text>' % INK3)
e.append('  <text x="530" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">繩繩</text>' % RED)
e.append('  <text x="530" y="414" text-anchor="middle" font-size="7.4" fill="%s">朱子：不绝貌——盛于一时则夭</text>' % INK3)
e.append('  <text x="380" y="446" text-anchor="middle" font-size="7.4" fill="%s">《诗》三章　·　六叠字，六貌</text>' % INK3)
e.append('  <text x="120" y="512" font-size="5.6" fill="%s">诗经 · 周南</text>' % INK2)
e.append('  <text x="640" y="512" text-anchor="end" font-size="5.6" fill="%s">图二 · 多聚和 · sj005b</text>' % INK2)
e.append('</svg>')
open(os.path.join(FIG, "sj005b-duo-ju-he.svg"), "w", encoding="utf-8").write("\n".join(e))

import cairosvg
for k in ["sj005a-zhong-si-yu-luan", "sj005b-duo-ju-he"]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok")
