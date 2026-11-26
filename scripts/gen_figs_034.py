# -*- coding: utf-8 -*-
"""SJ034《匏有苦叶》两图。图一：匏瓜·济水深浅·雉鸣舟子。图二：待渡—有度—须友。"""
import os, sys, re, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fig_geo import *
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(ROOT, "assets", "fig")
INK, INK2, INK3, RED, PAPER = "#1F1B17", "#5C544A", "#9A9186", "#994433", "#F7F4EE"
W, H = 760, 540

def bounds_ok(svg, tag):
    s = re.sub(r'xmlns="[^"]*"', "", svg)
    s = re.sub(r"#[0-9A-Fa-f]{6}", "", svg)
    s = re.sub(r'font-size="[^"]*"', "", s)
    s = re.sub(r'letter-spacing="[^"]*"', "", s)
    nums = [float(x) for x in re.findall(r"-?\d+\.?\d*", s)]
    xs = nums[0::2]; ys = nums[1::2]
    bad = [n for n in xs if n < 0 or n > W] + [n for n in ys if n < 0 or n > H]
    print(tag, "x[%.1f,%.1f] y[%.1f,%.1f] %s" % (min(xs), max(xs), min(ys), max(ys), "OK" if not bad else "OUT: %s" % bad))

d = []
d.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="\'Noto Serif SC\',\'Songti SC\',serif">' % (W, H, W, H))
d.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
d.append('  <text x="44" y="58" font-size="8.6" letter-spacing="2" fill="%s">邶风 · 三</text>' % RED)
d.append('  <text x="380" y="60" text-anchor="middle" font-size="26" letter-spacing="10" fill="%s" font-weight="700">匏有苦葉</text>' % INK)
d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">诗三百五篇 · 之三十四</text>' % INK3)
d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)

# 壹 · 匏瓜悬蔓（圆腹、长蒂、垂蔓、叶簇）
# 垂蔓
d.append('  <path d="M148,128 C140,150 156,168 146,196" fill="none" stroke="%s" stroke-width="1.0"/>' % INK2)
# 叶柄：左叶
d.append('  <line x1="142" y1="172" x2="124" y2="178" stroke="%s" stroke-width="0.7"/>' % INK2)
# 叶簇：两瓣叶＋叶脉
d.append('  <path d="M124,178 C106,166 96,176 102,190 C112,198 126,192 130,182 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <line x1="106" y1="182" x2="126" y2="180" stroke="%s" stroke-width="0.45"/>' % INK3)
# 叶柄：右叶
d.append('  <line x1="152" y1="164" x2="172" y2="170" stroke="%s" stroke-width="0.7"/>' % INK2)
d.append('  <path d="M172,170 C188,158 200,168 196,182 C186,190 174,184 170,176 Z" fill="#FCFAF6" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <line x1="176" y1="174" x2="192" y2="176" stroke="%s" stroke-width="0.45"/>' % INK3)
# 大匏瓜：圆腹＋收颈＋蒂
d.append('  <path d="M128,214 C112,232 110,268 126,292 C138,310 160,310 172,292 C188,268 186,232 170,214 C162,204 136,204 128,214 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.2"/>' % INK2)
d.append('  <path d="M146,204 L150,192 L156,204" fill="#EFEAD6" stroke="%s" stroke-width="0.9"/>' % INK2)
# 腹棱
d.append('  <path d="M148,214 C144,244 144,272 150,298" fill="none" stroke="%s" stroke-width="0.5"/>' % INK3)
# 小匏瓜
d.append('  <path d="M176,286 C168,296 168,314 178,324 C186,332 198,330 202,320 C206,308 200,292 190,286 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
# 卷须
d.append('  <path d="M134,150 C122,146 118,156 126,160" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
d.append('  <text x="148" y="372" text-anchor="middle" font-size="7.0" fill="%s">匏瓜悬蔓，叶枯可用</text>' % RED)

# 贰 · 济水深浅（近岸撩衣涉者，远水连衣涉者，两道水纹）
# 岸坡
d.append('  <path d="M300,300 L330,276 L356,276" fill="none" stroke="%s" stroke-width="0.9"/>' % INK2)
# 浅水涉者（侧身：发冠、肩线、宽袖、撩起衣裾）
d.append('  <circle cx="330" cy="234" r="9" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <path d="M325,227 C327,221 333,221 335,227" fill="none" stroke="%s" stroke-width="0.8"/>' % INK2)
d.append('  <line x1="326" y1="243" x2="326" y2="248" stroke="%s" stroke-width="0.8"/>' % INK2)
# 肩线＋宽袖＋袍身
d.append('  <path d="M318,250 L342,250" fill="none" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <path d="M318,250 C312,258 314,272 320,280 L318,288 L330,292 L342,288 L340,276 C346,266 344,256 342,250 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
# 撩起的衣角（外掀一襟）
d.append('  <path d="M340,270 L352,264 L348,278 Z" fill="#EFEAD6" stroke="%s" stroke-width="0.8"/>' % INK2)
d.append('  <line x1="322" y1="258" x2="338" y2="258" stroke="%s" stroke-width="0.45"/>' % INK3)
# 深水涉者（背影：发髻、宽肩、袍裾及水）
d.append('  <circle cx="420" cy="234" r="9" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <circle cx="420" cy="224" r="3.5" fill="#FCFAF6" stroke="%s" stroke-width="0.8"/>' % INK2)
d.append('  <line x1="416" y1="243" x2="416" y2="248" stroke="%s" stroke-width="0.8"/>' % INK2)
d.append('  <path d="M406,250 L434,250" fill="none" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <path d="M406,250 C402,264 404,284 410,300 L420,304 L430,300 C436,284 438,264 434,250 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <line x1="412" y1="260" x2="428" y2="260" stroke="%s" stroke-width="0.45"/>' % INK3)
# 水纹两道：浅疏深密
for k in range(3):
    y = 312 + k * 14
    d.append('  <path d="M300,%d C312,%d 324,%d 336,%d C348,%d 360,%d 372,%d" fill="none" stroke="%s" stroke-width="0.5"/>' % (y, y-3, y+3, y-3, y+3, y-3, y, INK3))
for k in range(4):
    y = 316 + k * 12
    d.append('  <path d="M384,%d C396,%d 408,%d 420,%d C432,%d 444,%d 456,%d" fill="none" stroke="%s" stroke-width="0.55"/>' % (y, y-3, y+3, y-3, y+3, y-3, y, INK2))
d.append('  <text x="378" y="386" text-anchor="middle" font-size="7.0" fill="%s">深则厉，浅则揭</text>' % RED)

# 叁 · 雉鸣与舟子（雉身冠尾；小舟与招手船夫）
# 雉身
d.append('  <path d="M578,238 C572,248 574,262 584,268 C594,272 604,266 604,254 C604,244 596,238 588,238 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % INK2)
d.append('  <circle cx="586" cy="228" r="10" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % INK2)
# 冠羽
d.append('  <line x1="580" y1="220" x2="576" y2="208" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <line x1="586" y1="218" x2="586" y2="204" stroke="%s" stroke-width="0.9"/>' % INK2)
d.append('  <line x1="592" y1="220" x2="596" y2="208" stroke="%s" stroke-width="0.9"/>' % INK2)
# 喙
d.append('  <path d="M595,226 L608,230 L595,234 Z" fill="#EFEAD6" stroke="%s" stroke-width="0.8"/>' % INK2)
d.append('  <circle cx="589" cy="226" r="1.4" fill="%s"/>' % INK)
# 长尾两羽
d.append('  <path d="M578,258 C566,276 558,296 554,318" fill="none" stroke="%s" stroke-width="1.3"/>' % INK2)
d.append('  <path d="M582,260 C576,278 572,296 570,316" fill="none" stroke="%s" stroke-width="0.5"/>' % INK3)
# 腿
d.append('  <line x1="584" y1="268" x2="582" y2="282" stroke="%s" stroke-width="0.7"/>' % INK2)
d.append('  <line x1="590" y1="268" x2="592" y2="282" stroke="%s" stroke-width="0.7"/>' % INK2)
# 舟
d.append('  <path d="M612,318 L672,318 L660,340 L624,340 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % INK2)
d.append('  <line x1="616" y1="318" x2="668" y2="318" stroke="%s" stroke-width="0.7"/>' % INK3)
# 船夫（侧身：发冠、肩线、宽袖、抬臂招手）
d.append('  <circle cx="638" cy="280" r="8" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <path d="M634,274 C636,269 641,269 643,274" fill="none" stroke="%s" stroke-width="0.8"/>' % INK2)
d.append('  <line x1="634" y1="288" x2="634" y2="292" stroke="%s" stroke-width="0.8"/>' % INK2)
d.append('  <path d="M628,292 L648,292" fill="none" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <path d="M628,292 C624,300 626,312 630,318 L638,320 L646,318 C650,312 652,300 648,292 Z" fill="#FCFAF6" stroke="%s" stroke-width="1.0"/>' % INK2)
# 招手抬臂＋袖
d.append('  <path d="M646,296 L658,284" fill="none" stroke="%s" stroke-width="1.0"/>' % INK2)
d.append('  <path d="M652,290 C658,288 662,292 660,296 C656,298 652,296 650,294 Z" fill="#EFEAD6" stroke="%s" stroke-width="0.7"/>' % INK2)
# 水波
d.append('  <path d="M604,348 C616,345 628,351 640,348 C652,345 664,351 676,348" fill="none" stroke="%s" stroke-width="0.5"/>' % INK3)
d.append('  <text x="622" y="372" text-anchor="middle" font-size="7.0" fill="%s">雉鸣求牡，招招舟子</text>' % RED)

for (x, t) in [(120, "壹"), (350, "贰"), (600, "叁")]:
    d.append('  <text x="%d" y="132" font-size="7.6" fill="%s">%s</text>' % (x, RED, t))
d.append('  <text x="44" y="466" font-size="7.8" fill="%s">壹 匏瓜　悬蔓圆腹，叶枯可用</text>' % INK2)
d.append('  <text x="264" y="466" font-size="7.8" fill="%s">贰 济水　深浅有度，厉揭随水</text>' % INK2)
d.append('  <text x="486" y="466" font-size="7.8" fill="%s">叁 雉舟　物求其类，舟子相呼</text>' % INK2)
d.append('  <line x1="44" y1="478" x2="716" y2="478" stroke="%s" stroke-width="0.8"/>' % INK3)
d.append('  <text x="380" y="512" text-anchor="middle" font-size="16" letter-spacing="3" fill="%s">人涉卬否，卬須我友</text>' % INK)
d.append('  <text x="44" y="524" font-size="7.4" letter-spacing="1" fill="%s">待而不轻渡，结伴而后行</text>' % INK3)
d.append('  <text x="716" y="524" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图一 · 名物 · sj034a</text>' % INK3)
d.append('</svg>')
svg_a = "\n".join(d)
open(os.path.join(FIG, "sj034a-pao-you-ku-ye.svg"), "w", encoding="utf-8").write(svg_a)
bounds_ok(svg_a, "034a")

# 图二
e = []
e.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="Noto Serif SC,Songti SC,serif">' % (W, H, W, H))
e.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
e.append('  <rect x="10" y="10" width="740" height="500" fill="none" stroke="%s" stroke-width="1"/>' % INK3)
e.append('  <rect x="16" y="16" width="728" height="488" fill="none" stroke="%s" stroke-width="0.6"/>' % INK3)
e.append('  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="%s" font-weight="700">待渡 · 有度 · 須友</text>' % INK)
e.append('  <text x="380" y="74" text-anchor="middle" font-size="9.6" letter-spacing="2" fill="%s">《诗经》邶风 · 第九篇　匏有苦叶</text>' % INK2)
e.append('  <defs><marker id="ar14" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % RED)
cells = [(70, "待渡", "人涉卬否", "众渡我留", INK2), (290, "有度", "深厉浅揭", "深浅有节", RED), (510, "須友", "卬須我友", "结伴而后行", INK2)]
for (x, big, s1, s2, col) in cells:
    e.append('  <rect x="%d" y="150" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>' % (x, col))
    e.append('  <text x="%d" y="214" text-anchor="middle" font-size="28" letter-spacing="2" fill="%s" font-weight="700">%s</text>' % (x + 75, col, big))
    e.append('  <text x="%d" y="252" text-anchor="middle" font-size="10" fill="#3B352F">%s</text>' % (x + 75, s1))
    e.append('  <text x="%d" y="278" text-anchor="middle" font-size="8" fill="%s">%s</text>' % (x + 75, INK3, s2))
e.append('  <line x1="220" y1="225" x2="288" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar14)"/>' % RED)
e.append('  <line x1="440" y1="225" x2="508" y2="225" stroke="%s" stroke-width="1" marker-end="url(#ar14)"/>' % RED)
e.append('  <text x="380" y="330" text-anchor="middle" font-size="8.4" fill="%s">于物见度，于人见守；不轻渡，不躁进，待侣同行</text>' % INK2)
e.append('  <line x1="120" y1="360" x2="640" y2="360" stroke="%s" stroke-width="0.8"/>' % INK3)
e.append('  <text x="230" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">卬</text>' % RED)
e.append('  <text x="230" y="414" text-anchor="middle" font-size="7.4" fill="%s">我也，人涉卬否</text>' % INK3)
e.append('  <text x="530" y="392" text-anchor="middle" font-size="13" letter-spacing="2" fill="%s" font-weight="700">須</text>' % RED)
e.append('  <text x="530" y="414" text-anchor="middle" font-size="7.4" fill="%s">待也，卬须我友</text>' % INK3)
e.append('  <text x="380" y="446" text-anchor="middle" font-size="7.4" fill="%s">《邶风·匏有苦叶》「深则厉，浅则揭」「卬须我友」</text>' % INK3)
e.append('  <text x="120" y="512" font-size="5.6" fill="%s">诗经 · 邶风</text>' % INK2)
e.append('  <text x="640" y="512" text-anchor="end" font-size="5.6" fill="%s">图二 · 待渡有度须友 · sj034b</text>' % INK2)
e.append('</svg>')
svg_b = "\n".join(e)
open(os.path.join(FIG, "sj034b-qi-qing-bu-du.svg"), "w", encoding="utf-8").write(svg_b)
bounds_ok(svg_b, "034b")

import cairosvg
for k in ["sj034a-pao-you-ku-ye", "sj034b-qi-qing-bu-du"]:
    cairosvg.svg2png(url=os.path.join(FIG, k + ".svg"), write_to="/tmp/%s.png" % k, output_width=920)
print("ok")
