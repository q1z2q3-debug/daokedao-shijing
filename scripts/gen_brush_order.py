# -*- coding: utf-8 -*-
"""生成离线单文件：三旗笔顺生长 + 笔压上墨。"""
import os, sys, math, json
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svgbrush import stroke

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INK, INK2, PAPER, RED = "#1F1B17", "#5C544A", "#F7F4EE", "#994433"

STROKES = []   # (pts, width, group)


def add(pts, w, grp):
    STROKES.append((np.asarray(pts, float), w, grp))


def Q(p0, p1, p2, n=14):
    t = np.linspace(0, 1, n)[:, None]
    a = np.array(p0, float)[None] * (1 - t) ** 2 + 2 * np.array(p1, float)[None] * (1 - t) * t + np.array(p2, float)[None] * t ** 2
    return a


# ---- 杆（三根，每根双边 + 顶饰）----
for cx, top, base in ((152, 124, 428), (380, 124, 428), (608, 124, 428)):
    add([(cx - 1.7, base), (cx - 1.7, top)], 1.6, "pole")
    add([(cx + 1.7, base), (cx + 1.7, top)], 1.6, "pole")
    add([(cx - 5.6, top), (cx - 4.4, top - 6), (cx - 2.6, top - 11), (cx, top - 15),
         (cx + 2.6, top - 11), (cx + 4.4, top - 6), (cx + 5.6, top), (cx - 5.6, top)], 1.0, "cap")

# ---- 壹 旄尾 ----
cx = 152
add([(cx - 5.4, 128), (cx - 9.4, 158), (cx - 8.4, 196)], 1.05, "tuft")
add([(cx + 5.4, 128), (cx + 9.4, 158), (cx + 8.4, 196)], 1.05, "tuft")
for i in range(10):
    x0 = cx - 7.4 + i * 1.65
    sy = 150 + (i % 5) * 8
    ey = 250 + (i % 6) * 16
    add([(x0, sy), (x0 + ((-1) ** i) * 5, ey - 32), (x0 + ((-1) ** i) * 11, ey)], 1.0, "tuft")

# ---- 贰 旗 ----
cx = 380
add([(330, 148), (430, 148)], 1.8, "flag")
add([(340, 156), (420, 156), (420, 262), (340, 262), (340, 156)], 1.4, "flag")
add([(381, 127), (430, 148)], 1.2, "flag")
for i in range(6):
    x0 = 345 + i * 12
    ln = 50 + (i % 3) * 12
    add([(x0, 262), (x0 + 2 * ((-1) ** i), 262 + ln * 0.6), (x0 + 3.4 * ((-1) ** i), 262 + ln)], 1.2, "flag")

# ---- 叁 析羽 ----
cx = 608
def feather(bx, by, L, W, ang):
    dx, dy = math.sin(ang), -math.cos(ang)
    nx, ny = -dy, dx
    left, right = [], []
    for t in np.linspace(0, 1, 12):
        wd = W * (max(0.0, math.sin(math.pi * (0.08 + t * 0.9))) ** 0.55) * 0.5
        px, py = bx + dx * L * t, by + dy * L * t
        left.append((px + nx * wd, py + ny * wd))
        right.append((px - nx * wd, py - ny * wd))
    add(left, 1.2, "fthr")
    add(right, 1.2, "fthr")
    add([(bx, by), (bx + dx * L * 0.94, by + dy * L * 0.94)], 0.7, "fthr")

for k in range(4):
    by = 186 + k * 44
    t1 = 0.17 if k % 2 == 0 else -0.17
    feather(cx + 2, by, 70, 15, t1)
    feather(cx - 2, by + 7, 60, 13, t1 * 2.0)

body = []
for i, (pts, w, grp) in enumerate(STROKES):
    d = 'M%.2f,%.2f' % (pts[0][0], pts[0][1])
    for x, y in pts[1:]:
        d += ' L%.2f,%.2f' % (x, y)
    delay = i * 130
    body.append(
        '<g class="st" data-grp="%s">'
        '<path class="grow" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1" '
        'style="animation-delay:%dms" d="%s" fill="none" stroke="%s" stroke-width="1.05"/>'
        '<path class="inkpad" style="animation-delay:%dms" d="%s" fill="%s" stroke="none"/>'
        '</g>' % (grp, delay, d, INK2, delay + 520, stroke(pts, w, col=INK, n=60), INK))

HTML = """<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="content=width=device-width,initial-scale=1">
<title>笔顺生长 · 干旄三旗</title>
<style>
  :root { --paper:#F7F4EE; --ink:#1F1B17; --mid:#5C544A; --red:#994433; --grey:#9A9186; }
  *{box-sizing:border-box} body{margin:0;background:#E8E4DA;font-family:"Noto Serif SC","Songti SC",serif}
  .wrap{max-width:1000px;margin:24px auto;background:var(--paper);padding:18px 22px 26px;
        box-shadow:0 2px 18px rgba(0,0,0,.12)}
  .hd{display:flex;align-items:baseline;justify-content:space-between;border-bottom:1px solid var(--grey);padding-bottom:8px}
  .hd h1{margin:0;font-size:20px;letter-spacing:8px;color:var(--ink)}
  .hd .meta{font-size:11px;color:var(--grey);letter-spacing:1px}
  .stage{display:block;width:100%;height:auto}
  .bar{display:flex;gap:10px;margin-top:12px;align-items:center;flex-wrap:wrap}
  button{font-family:inherit;font-size:12px;letter-spacing:1px;padding:7px 14px;cursor:pointer;
         background:transparent;border:1px solid var(--mid);color:var(--ink)}
  button:hover{background:#EFEBE1}
  .hint{font-size:11px;color:var(--grey);margin-left:auto}
  body.ink-only .inkpad{opacity:1!important;animation:none!important}
  body.paused .grow,body.paused .inkpad{animation-play-state:paused!important}
</style></head>
<body>
<div class="wrap">
  <div class="hd"><h1>笔顺生长</h1><div class="meta">干旄三旗 · 鄘风五十三 · 以中心线示笔序，后上墨</div></div>
  <svg class="stage" viewBox="0 0 760 528" xmlns="http://www.w3.org/2000/svg">
    <rect width="760" height="528" fill="#F7F4EE"/>
    <text x="44" y="40" font-size="9" fill="#994433" letter-spacing="2">鄘风 · 四</text>
    <text x="380" y="40" text-anchor="middle" font-size="20" letter-spacing="8" fill="#1F1B17">干 旄</text>
    <text x="716" y="40" text-anchor="end" font-size="9" fill="#9A9186">之五十三</text>
    <line x1="44" y1="54" x2="716" y2="54" stroke="#9A9186" stroke-width=".8"/>
    __BODY__
    <line x1="44" y1="462" x2="716" y2="462" stroke="#9A9186" stroke-width=".8"/>
    <text x="380" y="496" text-anchor="middle" font-size="14" letter-spacing="3" fill="#1F1B17">孑孑干旄，在浚之郊</text>
  </svg>
  <div class="bar">
    <button id="replay">重 画</button>
    <button id="pause">暂停</button>
    <button id="toggle">只看笔压</button>
    <span class="hint">共 __N__ 笔 · 每笔先出骨线，500ms 后压墨</span>
  </div>
</div>
<style>
  .grow{animation:grow .72s ease-in-out forwards}
  @keyframes grow{from{stroke-dashoffset:1}to{stroke-dashoffset:0}}
  .inkpad{opacity:0;animation:ink .26s ease forwards}
  @keyframes ink{to{opacity:1}}
</style>
<script>
const stage=document.querySelector('.stage');
function restart(){const html=stage.innerHTML;stage.innerHTML='';stage.innerHTML=html;}
document.getElementById('replay').onclick=()=>{document.body.classList.remove('ink-only','paused');restart();};
document.getElementById('pause').onclick=(e)=>{const p=document.body.classList.toggle('paused');e.target.textContent=p?'继 续':'暂 停';};
document.getElementById('toggle').onclick=(e)=>{const t=document.body.classList.toggle('ink-only');e.target.textContent=t?'看生长':'只看笔压';};
</script>
</body></html>"""

out = HTML.replace("__BODY__", "\n    ".join(body)).replace("__N__", str(len(STROKES)))
path = os.path.join(ROOT, "docs", "lab", "brush-order.html")
os.makedirs(os.path.dirname(path), exist_ok=True)
open(path, "w", encoding="utf-8").write(out)
print("strokes", len(STROKES), "bytes", os.path.getsize(path))
