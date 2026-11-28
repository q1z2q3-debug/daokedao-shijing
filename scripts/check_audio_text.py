# -*- coding: utf-8 -*-
"""语音稿对经文：逐篇比对纯汉字序列，判是否为原文。"""
import os
import re
import glob
import zhconv

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)


def jingwen(md):
    t = open(md, encoding="utf-8").read()
    m = re.search(r"^##\s*二[\s　]*(.*?)经文\s*$(.*?)^##\s*三", t, re.M | re.S)
    if not m:
        return None
    out = []
    for line in m.group(2).splitlines():
        s = line.strip()
        if s.startswith("**分章**"):
            break
        if s.startswith(">"):
            x = s.lstrip("> ").strip()
            if x:
                x = zhconv.convert(x, "zh-cn")
                x = re.sub(r"第[一二三四五六七八九十]+章", "", x)
                out.append(x)
    return out


def han(x):
    return re.sub(r"[^\u4e00-\u9fff]", "", x)


ok = 0
bad = []
for f in sorted(glob.glob("book/SJ0*.md")):
    key = os.path.basename(f)[:5]
    a = "audio_src/" + os.path.basename(f)[:-3] + ".md"
    if not os.path.exists(a):
        bad.append(key + " 缺稿")
        continue
    j = han("".join(jingwen(f) or []))
    t = open(a, encoding="utf-8").read()
    body = han("".join(l.strip() for l in t.splitlines() if l.strip() and not l.startswith("#")))
    if body == j:
        ok += 1
    else:
        bad.append(key + " " + str(len(body)) + "/" + str(len(j)))
print("ok " + str(ok) + " bad " + str(len(bad)))
print("\n".join(bad))
