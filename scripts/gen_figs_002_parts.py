# -*- coding: utf-8 -*-
"""SJ002《葛覃》两图 v2：名物图逐部件绘制（不并集），义理图沿用三格语式。"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fig_geo import *
from shapely.geometry import LineString

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(ROOT, "assets", "fig")
INK, INK2, INK3, RED, PAPER = "#1F1B17", "#5C544A", "#9A9186", "#994433", "#F7F4EE"
W, H = 760, 540


def head(d, no, title, right):
    d.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    d.append('  <text x="44" y="58" font-size="8.6" letter-spacing="2" fill="%s">%s</text>' % (RED, no))
    d.append('  <text x="380" y="60" text-anchor="middle" font-size="28" letter-spacing="14" fill="%s" font-weight="700">%s</text>' % (INK, title))
    d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">%s</text>' % (INK3, right))
    d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)


def foot(d, quote, lefts, tag):
    d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
    d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">%s</text>' % (INK, quote))
    d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">%s</text>' % (INK3, lefts))
    d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">%s</text>' % (INK3, tag))


# ============ 图一：名物 ============
d = []
d.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="\'Noto Serif SC\',\'Songti SC\',serif">' % (W, H, W, H))
head(d, "周南 · 二", "葛 覃", "诗三百五篇 · 之二")

# 远谷（淡，交代「中谷」）
d.append('  <path d="M52,198 C170,178 300,168 430,176 C540,183 640,190 708,196" fill="none" stroke="%s" stroke-width="0.3" stroke-dasharray="9 5 2 5"/>' % INK3)
d.append('  <path d="M52,210 C170,192 300,182 430,190 C540,197 640,202 708,208" fill="none" stroke="%s" stroke-width="0.2" opacity="0.6"/>' % INK3)
d.append('  <path d="M52,222 C170,206 300,196 430,204" fill="none" stroke="%s" stroke-width="0.18" opacity="0.4"/>' % INK3)

# 藤
d.append('  <path d="M70,432 C104,398 132,368 160,340 C190,310 214,278 232,246 C242,226 250,212 254,200" fill="none" stroke="%s" stroke-width="2.4"/>' % INK2)
d.append('  <path d="M70,432 C104,398 132,368 160,340 C190,310 214,278 232,246" fill="none" stroke="%s" stroke-width="0.6" opacity="0.5"/>' % INK3)
d.append('  <path d="M136,364 C150,358 156,346 148,340 C141,335 136,341 139,347 C141,351 145,350 145,346" fill="none" stroke="%s" stroke-width="0.35"/>' % INK2)
d.append('  <path d="M206,288 C220,282 226,270 218,264 C211,259 206,265 209,271 C211,275 215,274 215,270" fill="none" stroke="%s" stroke-width="0.35"/>' % INK2)


def trifoliate(cx, cy, rot=0, sc=1.0):
    out = []
    out.append('  <path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="0.4"/>' % (cx, cy, cx, cy - 9 * sc, INK2))
    for side in (-1, 1):
        g = ell(cx + side * 9 * sc, cy - 13 * sc, 5.2 * sc, 11 * sc, rot + side * 42)
        out.append('  <path d="%s" fill="%s" stroke="%s" stroke-width="0.4"/>' % (to_path(g)[0], PAPER, INK2))
        out.append('  <path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="0.18"/>' %
                   (cx + side * 9 * sc, cy - 6 * sc, cx + side * 9 * sc, cy - 17 * sc, INK3))
    g = ell(cx, cy - 27 * sc, 7.4 * sc, 16 * sc, rot)
    out.append('  <path d="%s" fill="%s" stroke="%s" stroke-width="0.55"/>' % (to_path(g)[0], PAPER, INK))
    out.append('  <path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="0.22"/>' % (cx, cy - 12 * sc, cx, cy - 39 * sc, INK3))
    out.append('  <path d="M%.1f,%.1f L%.1f,%.1f M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="0.16"/>' %
               (cx, cy - 24 * sc, cx - 4 * sc, cy - 30 * sc, cx, cy - 24 * sc, cx + 4 * sc, cy - 30 * sc, INK3))
    return out


d += trifoliate(112, 396, -18, 1.0)
d += trifoliate(184, 318, 6, 0.95)
d += trifoliate(250, 244, 28, 0.86)
d.append('  <text x="258" y="208" font-size="7.6" fill="%s">①</text>' % RED)


def cloth(x, y, w, h, fine):
    out = []
    out.append('  <rect x="%d" y="%d" width="%d" height="%d" fill="%s" stroke="%s" stroke-width="0.55"/>' % (x, y, w, h, PAPER, INK))
    out.append('  <ellipse cx="%d" cy="%d" rx="%.1f" ry="8" fill="%s" stroke="%s" stroke-width="0.5"/>' % (x + w / 2, y, w / 2, PAPER, INK))
    out.append('  <ellipse cx="%d" cy="%d" rx="%.1f" ry="3.2" fill="none" stroke="%s" stroke-width="0.3"/>' % (x + w / 2, y, w / 2 - 10, INK3))
    out.append('  <path d="M%.1f,%d C%.1f,%d %.1f,%d %.1f,%d" fill="none" stroke="%s" stroke-width="0.3"/>' %
               (x + w / 2 - 3, y - 1, x + w / 2 + 3, y - 4, x + w / 2 + 5, y + 2, x + w / 2 + 2, y + 2, INK3))
    out.append('  <ellipse cx="%d" cy="%d" rx="%.1f" ry="7" fill="#EFE8DB" stroke="%s" stroke-width="0.35" opacity="0.9"/>' % (x + w / 2, y + h, w / 2, INK2))
    if fine:
        yy = y + 12
        while yy < y + h - 6:
            out.append('  <path d="M%d,%.1f C%d,%.1f %d,%.1f %d,%.1f" fill="none" stroke="%s" stroke-width="0.16" opacity="0.55"/>'
                       % (x + 4, yy, x + w * 0.4, yy + 0.8, x + w * 0.7, yy - 0.8, x + w - 4, yy, INK2))
            yy += 3.0
        for k in (0.33, 0.66):
            out.append('  <path d="M%.1f,%d L%.1f,%d" stroke="%s" stroke-width="0.2" opacity="0.45"/>' % (x + w * k, y + 8, x + w * k, y + h - 4, INK3))
    else:
        yy = y + 14
        while yy < y + h - 8:
            out.append('  <path d="M%d,%.1f C%d,%.1f %d,%.1f %d,%.1f" fill="none" stroke="%s" stroke-width="0.4" opacity="0.55"/>'
                       % (x + 4, yy, x + w * 0.35, yy + 1.6, x + w * 0.7, yy - 1.6, x + w - 4, yy, INK2))
            yy += 9.0
        for k in (0.25, 0.5, 0.75):
            out.append('  <path d="M%.1f,%d L%.1f,%d" stroke="%s" stroke-width="0.28" opacity="0.5"/>' % (x + w * k, y + 8, x + w * k, y + h - 4, INK3))
    return out


d += cloth(300, 268, 46, 118, True)
d += cloth(392, 268, 46, 118, False)
d.append('  <text x="323" y="408" text-anchor="middle" font-size="8.4" letter-spacing="2" fill="%s">絺</text>' % INK2)
d.append('  <text x="415" y="408" text-anchor="middle" font-size="8.4" letter-spacing="2" fill="%s">綌</text>' % INK2)
d.append('  <text x="268" y="252" font-size="7.6" fill="%s">②</text>' % RED)

# 灌木与黄鸟
d.append('  <path d="M540,344 C580,330 640,322 690,318 C702,317 708,317 710,317" fill="none" stroke="%s" stroke-width="1.5"/>' % INK2)
d.append('  <path d="M592,336 C596,322 600,312 606,304" fill="none" stroke="%s" stroke-width="0.75"/>' % INK2)
d.append('  <path d="%s" fill="%s" stroke="%s" stroke-width="0.35"/>' % (to_path(ell(600, 298, 5, 9, -22))[0], PAPER, INK2))
d.append('  <path d="%s" fill="%s" stroke="%s" stroke-width="0.35"/>' % (to_path(ell(672, 306, 5, 8.5, -34))[0], PAPER, INK2))

BX, BY = 636, 282
d.append('  <path d="%s" fill="%s" stroke="%s" stroke-width="0.5"/>' % (to_path(ell(BX, BY, 18, 10.5, -12))[0], "#FCF7EC", INK))
d.append('  <path d="%s" fill="%s" stroke="%s" stroke-width="0.4"/>' % (to_path(ell(BX + 26, BY + 8, 16, 4.4, 18))[0], "#FCF7EC", INK))
d.append('  <path d="%s" fill="%s" stroke="%s" stroke-width="0.5"/>' % (to_path(circle(BX - 24, BY - 10, 8))[0], "#FCF7EC", INK))
d.append('  <path d="M%d,%d L%d,%d L%d,%d Z" fill="%s" stroke="%s" stroke-width="0.4"/>' % (BX - 31, BY - 13, BX - 45, BY - 10, BX - 31, BY - 7, "#EFE8DB", INK2))
d.append('  <path d="M%d,%d C%d,%d %d,%d %d,%d" fill="none" stroke="%s" stroke-width="0.28"/>' % (BX - 4, BY + 2, BX - 10, BY + 6, BX - 20, BY + 6, BX - 26, BY + 2, INK3))
d.append('  <path d="M%d,%d C%d,%d %d,%d %d,%d" fill="none" stroke="%s" stroke-width="0.22"/>' % (BX + 2, BY - 4, BX + 10, BY - 6, BX + 18, BY - 2, BX + 24, BY + 4, INK3))
d.append('  <circle cx="%d" cy="%d" r="1.2" fill="%s"/>' % (BX - 26, BY - 12, INK))
d.append('  <circle cx="%d" cy="%d" r="0.4" fill="%s"/>' % (BX - 26.4, BY - 12.4, "#FCF7EC"))
d.append('  <path d="M%d,%d L%d,%d M%d,%d L%d,%d" stroke="%s" stroke-width="0.5"/>' % (BX - 6, BY + 9, BX - 7, BY + 28, BX + 4, BY + 9, BX + 3, BY + 28, INK2))
d.append('  <path d="M%d,%d L%d,%d M%d,%d L%d,%d M%d,%d L%d,%d M%d,%d L%d,%d M%d,%d L%d,%d M%d,%d L%d,%d" stroke="%s" stroke-width="0.3"/>'
         % (BX - 7, BY + 28, BX - 13, BY + 32, BX - 7, BY + 28, BX - 7, BY + 33, BX - 7, BY + 28, BX - 1, BY + 32,
            BX + 3, BY + 28, BX - 3, BY + 32, BX + 3, BY + 28, BX + 3, BY + 33, BX + 3, BY + 28, BX + 9, BY + 32, INK2))
d.append('  <text x="684" y="270" font-size="7.6" fill="%s">③</text>' % RED)

d.append('  <text x="44" y="466" font-size="7.8" fill="%s">① 葛　藤蔓延谷，煮而绩之，乃成布</text>' % INK2)
d.append('  <text x="308" y="466" font-size="7.8" fill="%s">② 絺綌　细曰絺，粗曰綌</text>' % INK2)
d.append('  <text x="576" y="466" font-size="7.8" fill="%s">③ 黄鸟　鹂也，鸣声喈喈</text>' % INK2)
foot(d, "葛之覃兮，施于中谷", "野有其生，室有其功", "图一 · 名物 · sj002a")
d.append('</svg>')
open(os.path.join(FIG, "sj002a-ge-yu-chi-xi.svg"), "w", encoding="utf-8").write("\n".join(d))

# ============ 图二：义理 ============
e = []
e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="\'Noto Serif SC\',\'Songti SC\',serif">' % (W, H, W, H))
e.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
e.append('  <rect x="10" y="10" width="740" height="500" fill="none" stroke="%s" stroke-width="1"/>' % INK3)
e.append('  <rect x="16" y="16" width="728" height="488" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
e.append('  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="%s" font-weight="700">野 · 室 · 家</text>' % INK)
e.append('  <text x="380" y="74" text-anchor="middle" font-size="9.6" letter-spacing="2" fill="%s">《诗经》周南 · 第二篇　葛覃</text>' % INK2)
e.append('  <defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % RED)
for (x, big, s1, s2, col) in [(70, "野", "谷中采葛", "一章", INK2), (290, "室", "为絺为綌", "二章", INK2), (510, "家", "归宁父母", "三章", RED)]:
    e.append('  <rect x="%d" y="150" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (x, col))
    e.append('  <text x="%d" y="212" text-anchor="middle" font-size="26" letter-spacing="4" fill="%s" font-weight="700">%s</text>' % (x + 75, col, big))
    e.append('  <text x="%d" y="250" text-anchor="middle" font-size="10" fill="#3B352F">%s</text>' % (x + 75, s1))
    e.append('  <text x="%d" y="276" text-anchor="middle" font-size="8" fill="%s">%s</text>' % (x + 75, INK3, s2))
e.append('  <line x1="220" y1="225" x2="288" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar)"/>' % RED)
e.append('  <line x1="440" y1="225" x2="508" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar)"/>' % RED)
e.append('  <text x="380" y="330" text-anchor="middle" font-size="8.4" fill="%s">由野入室，由室向家——三地一线，一章一地</text>' % INK2)
e.append('  <line x1="120" y1="360" x2="640" y2="360" stroke="%s" stroke-width="0.8"/>' % INK3)
e.append('  <text x="230" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">服之无斁</text>' % RED)
e.append('  <text x="230" y="414" text-anchor="middle" font-size="7.4" fill="%s">惜物力，非夸颜色</text>' % INK3)
e.append('  <text x="530" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">害澣害否</text>' % RED)
e.append('  <text x="530" y="414" text-anchor="middle" font-size="7.4" fill="%s">洗与不洗，都要问一声</text>' % INK3)
e.append('  <text x="380" y="446" text-anchor="middle" font-size="7.4" fill="%s">《诗》三章　·　各成一地</text>' % INK3)
e.append('  <text x="120" y="512" font-size="5.6" fill="%s">诗经 · 周南</text>' % INK2)
e.append('  <text x="640" y="512" text-anchor="end" font-size="5.6" fill="%s">图二 · 野室家 · sj002b</text>' % INK2)
e.append('</svg>')
open(os.path.join(FIG, "sj002b-ye-shi-jia.svg"), "w", encoding="utf-8").write("\n".join(e))

import cairosvg
for k in ["sj002a-ge-yu-chi-xi", "sj002b-ye-shi-jia"]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok")
