# -*- coding: utf-8 -*-
"""图式 v2：义理图——水（动）／洲（定）／礼线（界）三层，几何承担关系，不设框、不设箭头。"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(ROOT, "assets", "fig")
INK, INK2, INK3, RED, PAPER = "#1F1B17", "#5C544A", "#9A9186", "#994433", "#F7F4EE"
W, H = 760, 540
d = []
d.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="\'Noto Serif SC\',\'Songti SC\',serif">' % (W, H, W, H))
d.append('  <rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))

# 上段
d.append('  <text x="44" y="58" font-size="8.6" letter-spacing="2" fill="%s">周南 · 一</text>' % RED)
d.append('  <text x="380" y="60" text-anchor="middle" font-size="28" letter-spacing="14" fill="%s" font-weight="700">关 雎</text>' % INK)
d.append('  <text x="716" y="58" text-anchor="end" font-size="8.2" letter-spacing="1.5" fill="%s">求 → 思 → 乐</text>' % INK3)
d.append('  <line x1="44" y1="96" x2="716" y2="96" stroke="%s" stroke-width="0.8"/>' % INK3)

# 层一：水（动）
for i, y in enumerate([116, 138, 160, 182, 204, 226, 248]):
    op = 0.62 - i * 0.06
    d.append('  <path d="M44,%d q24,-3 48,0 q24,3 48,0 q24,-3 48,0 q24,3 48,0 q24,-3 48,0 q24,3 48,0 q24,-3 48,0 q24,3 48,0 q24,-3 48,0 q24,3 48,0 q24,-3 48,0 q24,3 48,0 q24,-3 48,0" fill="none" stroke="%s" stroke-width="0.28" opacity="%.2f" stroke-dasharray="18 6 3 7"/>' % (y, INK3, op))

# 层二：洲（定）
d.append('  <path d="M44,266 C140,252 260,246 400,250 C500,253 570,258 630,262 C640,265 660,266 664,266 L664,300 C600,308 500,310 360,308 C220,306 100,300 44,294 Z" fill="#F1EBDF"/>')
d.append('  <path d="M44,266 C140,252 260,246 400,250 C500,253 570,258 630,262 C640,265 660,266 664,266" fill="none" stroke="%s" stroke-width="0.45"/>' % INK2)
d.append('  <path d="M44,294 C100,300 220,306 360,308 C500,310 640,308 716,300" fill="none" stroke="%s" stroke-width="0.25" stroke-dasharray="4 3"/>' % INK3)

# 层界：礼线
d.append('  <line x1="44" y1="368" x2="716" y2="368" stroke="%s" stroke-width="1.3"/>' % RED)
d.append('  <line x1="44" y1="372" x2="716" y2="372" stroke="%s" stroke-width="0.4" opacity="0.5"/>' % RED)

# 求：一条虚线视线，自水向洲，未达
d.append('  <path d="M660,232 C630,244 600,256 570,262" fill="none" stroke="%s" stroke-width="0.4" stroke-dasharray="5 4"/>' % INK2)
d.append('  <circle cx="566" cy="263" r="1.8" fill="none" stroke="%s" stroke-width="0.5"/>' % INK2)
d.append('  <text x="672" y="228" font-size="7.6" letter-spacing="1" fill="%s">求</text>' % INK2)

# 思：洲上一条来回折线（辗转）
d.append('  <path d="M250,300 L282,268 L312,306 L344,268 L374,304 L404,270" fill="none" stroke="%s" stroke-width="0.45"/>' % INK2)
d.append('  <path d="M250,320 L404,320" fill="none" stroke="%s" stroke-width="0.2" stroke-dasharray="3 4"/>' % INK3)
d.append('  <text x="240" y="292" font-size="7.6" letter-spacing="1" fill="%s">思</text>' % INK2)
d.append('  <text x="412" y="262" font-size="6.6" fill="%s">求之不得</text>' % INK3)

# 乐：礼线上两只钟，一声波
for cx in (516, 578):
    d.append('  <path d="M%d,340 L%d,340 L%d,368 L%d,368 Z" fill="none" stroke="%s" stroke-width="0.5"/>' % (cx - 11, cx + 11, cx + 6, cx - 6, INK))
    d.append('  <path d="M%d,334 L%d,334" fill="none" stroke="%s" stroke-width="0.5"/>' % (cx - 5, cx + 5, INK))
d.append('  <path d="M596,352 C606,346 606,358 596,353" fill="none" stroke="%s" stroke-width="0.28"/>' % INK3)
d.append('  <path d="M498,352 C488,346 488,358 498,353" fill="none" stroke="%s" stroke-width="0.28"/>' % INK3)
d.append('  <text x="640" y="352" font-size="7.6" letter-spacing="1" fill="%s">乐</text>' % INK2)

# 层名（左缘）
d.append('  <text x="44" y="112" font-size="7.4" letter-spacing="1" fill="%s">水 · 动</text>' % INK3)
d.append('  <text x="44" y="258" font-size="7.4" letter-spacing="1" fill="%s">洲 · 定</text>' % INK3)
d.append('  <text x="44" y="388" font-size="7.4" letter-spacing="1" fill="%s">礼 · 界</text>' % INK3)

# 下段
d.append('  <text x="204" y="442" text-anchor="middle" font-size="15" letter-spacing="3" fill="%s" font-weight="700">乐而不淫</text>' % RED)
d.append('  <text x="204" y="462" text-anchor="middle" font-size="7" fill="%s">得之以礼，不以纵</text>' % INK3)
d.append('  <text x="556" y="442" text-anchor="middle" font-size="15" letter-spacing="3" fill="%s" font-weight="700">哀而不伤</text>' % RED)
d.append('  <text x="556" y="462" text-anchor="middle" font-size="7" fill="%s">思之不止，不以怨</text>' % INK3)
d.append('  <text x="380" y="492" text-anchor="middle" font-size="7.2" fill="%s">情在水，礼在界；三步皆在礼内　·　《论语·八佾》3.20</text>' % INK3)
d.append('  <text x="716" y="528" text-anchor="end" font-size="7.4" letter-spacing="1" fill="%s">图二 · 义理 · sj001b</text>' % INK3)
d.append('</svg>')

p = os.path.join(FIG, "sj001b-v2.svg")
open(p, "w", encoding="utf-8").write("\n".join(d))
import cairosvg
cairosvg.svg2png(url=p, write_to="/tmp/b4.png", output_width=920)
print("ok")
