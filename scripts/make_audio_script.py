# -*- coding: utf-8 -*-
"""从 book/SJNNN-*.md 抽经文（繁体引文），转简体，生成吟诵稿 md。"""
import os, re, sys, glob
import zhconv

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOK = os.path.join(ROOT, "book")
OUT = os.path.join(ROOT, "audio_src")
os.makedirs(OUT, exist_ok=True)


def parse(md_path):
    text = open(md_path, encoding="utf-8").read()
    title = re.search(r"^#\s+(.+)$", text, re.M).group(1).strip()
    m = re.search(r"^##\s*二[\s　]*(.*?)经文\s*$(.*?)^##\s*三", text, re.M | re.S)
    if not m:
        return None
    body = m.group(2)
    chapters, cur, label = [], [], None
    for line in body.splitlines():
        s = line.strip()
        mm = re.match(r"^第([一二三四五六七八九十]+)章$", s)
        if mm:
            if cur:
                chapters.append((label, cur))
            cur, label = [], "第%s章" % mm.group(1)
            continue
        if s.startswith(">"):
            t = s.lstrip("> ").strip()
            if t:
                cur.append(t)
        elif s.startswith("**分章**"):
            break
    if cur:
        chapters.append((label, cur))
    return title, chapters


def main():
    files = sorted(glob.glob(os.path.join(BOOK, "SJ0*.md")))
    for f in files:
        r = parse(f)
        if not r:
            print("skip", f)
            continue
        title, chapters = r
        name = re.sub(r"[（(].*?[）)]", "", title).strip()
        simp_title = zhconv.convert(name, "zh-cn")
        lines = ["# %s" % simp_title, ""]
        for label, verses in chapters:
            lines.append("## %s" % zhconv.convert(label, "zh-cn"))
            lines.append("")
            for v in verses:
                lines.append(zhconv.convert(v, "zh-cn"))
                lines.append("")
        key = os.path.basename(f).split(".")[0]
        out = os.path.join(OUT, key + ".md")
        open(out, "w", encoding="utf-8").write("\n".join(lines))
        print("ok", key, len(chapters), "chapters")


main()
