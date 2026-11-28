# -*- coding: utf-8 -*-
"""从 book/SJNNN-*.md 的「二　经文」重出语音稿：只留原文，章标降为小标题。

旧稿有三处毛病：把「第一章」写成正文行、少数篇把今译当经文、个别篇串入校记。
本脚本以 book 的经文引文为唯一来源，繁转简后重写 audio_src/，不作任何增补。
用法：python3 scripts/build_audio_src.py [--check]
"""
import os
import re
import glob
import sys
import zhconv

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOK = os.path.join(ROOT, "book")
OUT = os.path.join(ROOT, "audio_src")
CHECK = "--check" in sys.argv


def parse_经文(md_path):
    t = open(md_path, encoding="utf-8").read()
    m = re.search(r"^##\s*二[\s　]*(.*?)经文\s*$(.*?)^##\s*三", t, re.M | re.S)
    if not m:
        return None
    chapters = []
    cur = []
    started = False
    for line in m.group(2).splitlines():
        s = line.strip()
        if s.startswith("**分章**"):
            break
        mm = re.match(r"^第([一二三四五六七八九十百]+)章$", s)
        if mm:
            if started and cur:
                chapters.append(cur)
            cur = []
            started = True
            continue
        if not s.startswith(">"):
            continue
        x = s.lstrip("> ").strip()
        if not x:
            continue
        x = zhconv.convert(x, "zh-cn")
        for a, b in (("𫮃", "墠"), ("𬮱", "闉"), ("𫈉", "蕳"), ("𬣙", "訏"),
                     ("镅", "鋂"), ("𫚈", "鱮"), ("艺麻", "蓺麻")):
            x = x.replace(a, b)
        x = re.sub(r"^第[一二三四五六七八九十百]+章[　\s]*", "", x)
        if x:
            cur.append(x)
    if cur:
        chapters.append(cur)
    return chapters


def title_of(md_path):
    t = open(md_path, encoding="utf-8").read()
    m = re.search(r"^#\s+(.+)$", t, re.M)
    name = m.group(1).strip() if m else ""
    name = re.sub(r"[（(].*?[）)]", "", name).strip()
    return zhconv.convert(name, "zh-cn").replace("𫮃", "墠")


def main():
    os.makedirs(OUT, exist_ok=True)
    n_changed = 0
    for f in sorted(glob.glob(os.path.join(BOOK, "SJ*.md"))):
        chapters = parse_经文(f)
        if not chapters:
            print("skip(no经文) " + os.path.basename(f))
            continue
        lines = ["# " + title_of(f), ""]
        marks = ["第一章", "第二章", "第三章", "第四章", "第五章", "第六章",
                 "第七章", "第八章", "第九章", "第十章", "第十一章", "第十二章"]
        for i, verses in enumerate(chapters):
            label = marks[i] if i < len(marks) else "第" + str(i + 1) + "章"
            lines.append("## " + label)
            lines.append("")
            for v in verses:
                lines.append(v)
                lines.append("")
        text = "\n".join(lines).rstrip() + "\n"
        key = os.path.basename(f)[:-3]
        out = os.path.join(OUT, key + ".md")
        old = open(out, encoding="utf-8").read() if os.path.exists(out) else ""
        if old != text:
            n_changed += 1
            if not CHECK:
                open(out, "w", encoding="utf-8").write(text)
    print(("将改 " if CHECK else "已改 ") + str(n_changed) + " 篇；章数 " + str(len(chapters)))


if __name__ == "__main__":
    main()
