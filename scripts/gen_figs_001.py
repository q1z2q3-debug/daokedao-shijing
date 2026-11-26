# -*- coding: utf-8 -*-
"""生成《关雎》两图：sj001a 名物（雎鸠·荇菜），sj001b 义理（求—思—乐）。"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(ROOT, "assets", "fig")
os.makedirs(FIG, exist_ok=True)

HEAD = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 540" width="760" height="540" font-family="'Noto Serif SC','Songti SC','Source Han Serif SC',serif">
  <rect x="0" y="0" width="760" height="540" fill="#F7F4EE"/>
  <rect x="10" y="10" width="740" height="500" fill="none" stroke="#DCD5C8" stroke-width="1"/>
  <rect x="16" y="16" width="728" height="488" fill="none" stroke="#DCD5C8" stroke-width="0.6"/>
'''
FOOT = '''  <text x="120" y="512" font-size="7.6" fill="#7C6D5C">诗经 · 周南</text>
  <text x="640" y="512" text-anchor="end" font-size="7.6" fill="#7C6D5C">图{cn} · {name} · {key}</text>
</svg>
'''

# ---------- 图一：名物 ----------
a = HEAD
a += '''  <text x="380" y="54" text-anchor="middle" font-size="21" letter-spacing="8" fill="#25211D" font-weight="700">雎 鸠 与 荇 菜</text>
  <text x="380" y="76" text-anchor="middle" font-size="10.6" letter-spacing="2" fill="#7C6D5C">《诗经》周南 · 第一篇　关雎</text>
'''
# 远岸
a += '''  <path d="M 120,150 C 240,136 360,132 480,138 C 560,142 620,146 640,150" fill="none" stroke="#7C6D5C" stroke-width="0.7" opacity="0.55"/>
  <path d="M 120,156 C 240,144 360,140 470,145" fill="none" stroke="#7C6D5C" stroke-width="0.4" opacity="0.4"/>
'''
# 水波
for i, y in enumerate(range(178, 470, 30)):
    a += '  <path d="M %d,%d q 22,-4 44,0 q 22,4 44,0 q 22,-4 44,0 q 22,4 44,0 q 22,-4 44,0 q 22,4 44,0" fill="none" stroke="#8FA396" stroke-width="0.85" opacity="0.5"/>\n' % (56 + (i % 2) * 22, y)
# 沙洲
a += '''  <path d="M 156,332 C 226,306 366,300 466,320 C 528,332 548,348 526,360 C 442,384 268,382 186,362 C 148,352 138,342 156,332 Z" fill="#EAE3D6" stroke="#7C6D5C" stroke-width="0.9"/>
'''
# 雎鸠（两只，scale 1.6）
BIRD = '''    <path d="M 0,268 C 6,251 19,245 28,249 C 35,252 37,258 35,263 C 31,269 18,271 8,271 C 3,271 0,270 0,268 Z" fill="#FCFAF6" stroke="#25211D" stroke-width="1"/>
    <path d="M 8,252 C 12,246 16,244 20,246" fill="none" stroke="#25211D" stroke-width="0.7" opacity="0.8"/>
    <circle cx="30" cy="280" r="1" fill="#25211D"/>
    <path d="M 33,252 L 41,254" stroke="#25211D" stroke-width="0.9"/>
    <path d="M 27,247 C 28,242 30,240 33,240 C 31,243 31,245 30,248" fill="none" stroke="#994433" stroke-width="0.8"/>
    <path d="M 11,271 L 9,283 M 18,272 L 17,284" stroke="#25211D" stroke-width="0.9"/>
    <path d="M 9,283 L 4,285 M 9,283 L 12,286 M 17,284 L 12,287 M 17,284 L 21,287" stroke="#25211D" stroke-width="0.55"/>
'''
a += '  <g transform="translate(232,-129) scale(1.6)">\n' + BIRD + '  </g>\n'
a += '  <g transform="translate(392,-129) scale(-1.6,1.6)">\n' + BIRD + '  </g>\n'
a += '''  <text x="300" y="398" text-anchor="middle" font-size="8.6" fill="#7C6D5C">雎鸠　生有定偶，并游而不相狎</text>
'''
# 荇菜
a += '''  <g>
'''
for (cx, cy, r) in [(566, 300, 15), (610, 322, 14), (654, 298, 15), (694, 326, 14), (534, 340, 13), (636, 352, 13)]:
    a += '''    <circle cx="{cx}" cy="{cy}" r="{r}" fill="#FCFAF6" stroke="#4A5C55" stroke-width="0.9"/>
    <path d="M {cx},{cy2} L {cx2},{cy3}" stroke="#4A5C55" stroke-width="0.8"/>
    <path d="M {cx2},{cy3} L {cx3},{cy4} M {cx2},{cy3} L {cx2},{cy5} M {cx2},{cy3} L {cx4},{cy4}" stroke="#4A5C55" stroke-width="0.45" opacity="0.65"/>
'''.format(cx=cx, cy=cy, r=r, cy2=cy + r, cy3=cy + r + 20, cx2=cx - 2, cx3=cx - 9, cx4=cx + 6, cy4=cy + r + 30, cy5=cy + r + 32)
a += '''  </g>
  <text x="612" y="430" text-anchor="middle" font-size="9" fill="#4A5C55">荇菜　圆叶细茎，浮水而生，可荐为菹</text>
  <text x="612" y="444" text-anchor="middle" font-size="7.6" fill="#7C6D5C">「参差荇菜，左右流之」</text>
'''
a += '''  <line x1="120" y1="460" x2="640" y2="460" stroke="#DCD5C8" stroke-width="0.8"/>
  <text x="380" y="478" text-anchor="middle" font-size="11" fill="#25211D">鸟有定偶，草无定形：一章之内，一取定，一取择。</text>
'''
a += FOOT.format(cn="一", name="雎鸠与荇菜", key="sj001a")
open(os.path.join(FIG, "sj001a-ju-jiu-xing-cai.svg"), "w", encoding="utf-8").write(a)

# ---------- 图二：义理 ----------
b = HEAD
b += '''  <text x="380" y="52" text-anchor="middle" font-size="21" letter-spacing="8" fill="#25211D" font-weight="700">求 · 思 · 乐</text>
  <text x="380" y="74" text-anchor="middle" font-size="10" letter-spacing="2" fill="#7C6D5C">《诗经》周南 · 第一篇　关雎</text>
  <defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#994433"/></marker></defs>
'''
steps = [
    (70, "求", "寤寐求之", "有求", "#4A5C55"),
    (290, "思", "辗转反侧", "求不得", "#994433"),
    (510, "乐", "琴瑟钟鼓", "得而乐", "#4A5C55"),
]
for (x, t, s, c, col) in steps:
    b += '''  <rect x="%d" y="178" width="150" height="150" fill="#FCFAF6" stroke="%s" stroke-width="1.1"/>
  <text x="%d" y="242" text-anchor="middle" font-size="26" letter-spacing="4" fill="%s" font-weight="700">%s</text>
  <text x="%d" y="280" text-anchor="middle" font-size="11" fill="#3B352F">%s</text>
  <text x="%d" y="304" text-anchor="middle" font-size="9.4" fill="#7C6D5C">%s</text>
''' % (x, col, x + 75, col, t, x + 75, s, x + 75, c)
b += '''  <line x1="220" y1="253" x2="288" y2="253" stroke="#994433" stroke-width="1" marker-end="url(#ar)"/>
  <line x1="440" y1="253" x2="508" y2="253" stroke="#994433" stroke-width="1" marker-end="url(#ar)"/>
  <text x="380" y="356" text-anchor="middle" font-size="10" fill="#7C6D5C">情起于求，困于思，成于乐——三步都在礼内</text>
  <line x1="120" y1="360" x2="640" y2="360" stroke="#DCD5C8" stroke-width="0.8"/>
  <text x="230" y="412" text-anchor="middle" font-size="13" letter-spacing="2" fill="#994433" font-weight="700">乐而不淫</text>
  <text x="230" y="434" text-anchor="middle" font-size="9" fill="#7C6D5C">得之不以纵</text>
  <text x="530" y="412" text-anchor="middle" font-size="13" letter-spacing="2" fill="#994433" font-weight="700">哀而不伤</text>
  <text x="530" y="434" text-anchor="middle" font-size="9" fill="#7C6D5C">不得之不以怨</text>
  <text x="380" y="462" text-anchor="middle" font-size="9" fill="#7C6D5C">《论语·八佾》3.20 孔子定评</text>
'''
b += FOOT.format(cn="二", name="求思乐", key="sj001b")
open(os.path.join(FIG, "sj001b-qiu-si-le.svg"), "w", encoding="utf-8").write(b)

import cairosvg
cairosvg.svg2png(url=os.path.join(FIG, "sj001a-ju-jiu-xing-cai.svg"), write_to="/tmp/sj001a.png", output_width=760)
print("ok")
