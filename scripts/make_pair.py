# -*- coding: utf-8 -*-
"""两图上下并置：svg -> png(920) -> PIL 竖排，输出 dist/pair-NNN.png。

规格（沿用既有成图）：
  - cairosvg 渲染，输出宽 920；
  - a 图在上、b 图在下，竖排，两图间距 GAP=20px；
  - 纸色 RGB(247,244,238)，半透明边缘先摊到纸色上再合成，避免黑边；
  - 输出文件名 pair-%03d.png（三位篇号）。

篇号解析：兼容两位 / 三位文件名（sj073a-…、sj100b-…），按整数篇号配对。

用法：
  python3 scripts/make_pair.py            # 全量：assets/fig 下所有可配对的篇
  python3 scripts/make_pair.py 73         # 仅第 73 篇
  python3 scripts/make_pair.py 73 113      # 闭区间 73–113
缺 b 图（或缺 a 图）的篇跳过并打印告警，不生成文件。
"""
import os, sys, glob, re, tempfile
import cairosvg
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(ROOT, "assets", "fig")
DIST = os.path.join(ROOT, "dist")
os.makedirs(DIST, exist_ok=True)

PAPER = (247, 244, 238)
GAP = 20
WIDTH = 920
# 篇号文件名：sj + 两位或三位数字 + a/b + 后缀
NAME_RE = re.compile(r"sj(\d{2,3})([ab])-")


def collect():
    """返回 {篇号int: {'a': path, 'b': path}}。"""
    figs = {}
    for f in glob.glob(os.path.join(FIG, "sj*[ab]-*.svg")):
        m = NAME_RE.search(os.path.basename(f))
        if not m:
            continue
        num, side = int(m.group(1)), m.group(2)
        figs.setdefault(num, {})[side] = f
    return figs


def render_on_paper(svg_path):
    """渲染 svg 到 920 宽，摊到纸色上，返回 RGB Image。"""
    tmp = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
    tmp.close()
    try:
        cairosvg.svg2png(url=svg_path, write_to=tmp.name, output_width=WIDTH)
        rgba = Image.open(tmp.name).convert("RGBA")
        paper = Image.new("RGB", rgba.size, PAPER)
        paper.paste(rgba, mask=rgba.split()[3])  # 用 alpha 摊到纸色，杜绝黑边
        return paper
    finally:
        os.unlink(tmp.name)


def make(num, figs):
    entry = figs.get(num, {})
    a, b = entry.get("a"), entry.get("b")
    if not a or not b:
        print("[skip] 篇 %03d：缺图 a=%s b=%s" % (num, bool(a), bool(b)))
        return False
    imgs = [render_on_paper(a), render_on_paper(b)]
    h = sum(i.height for i in imgs) + GAP
    canvas = Image.new("RGB", (WIDTH, h), PAPER)
    y = 0
    for im in imgs:
        canvas.paste(im, (0, y))
        y += im.height + GAP
    out = os.path.join(DIST, "pair-%03d.png" % num)
    canvas.save(out)
    print("[ok]   pair-%03d.png  %s" % (num, canvas.size))
    return True


def parse_range(argv, nums):
    if len(argv) == 0:
        return sorted(nums)
    if len(argv) == 1:
        return [int(argv[0])]
    lo, hi = int(argv[0]), int(argv[1])
    if lo > hi:
        lo, hi = hi, lo
    return list(range(lo, hi + 1))


if __name__ == "__main__":
    figs = collect()
    targets = parse_range(sys.argv[1:], figs.keys())
    made, skipped = 0, []
    for num in targets:
        if make(num, figs):
            made += 1
        else:
            skipped.append(num)
    print("--- 汇总：出图 %d 张；跳过 %d 篇 %s ---"
          % (made, len(skipped), ["%03d" % n for n in skipped]))
