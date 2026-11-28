# -*- coding: utf-8 -*-
"""构建《诗经》站点：book/*.md -> docs/ch/*.html + docs/index.html"""
import os, re, json, shutil, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOK = os.path.join(ROOT, "book")
DOCS = os.path.join(ROOT, "docs")
CH = os.path.join(DOCS, "ch")

CSS = """
:root{--paper:#F7F4EE;--ink:#25211D;--red:#994433;--brown:#7C6D5C;--line:#DCD5C8;}
*{box-sizing:border-box}
html,body{margin:0;background:var(--paper);color:var(--ink);overflow-x:hidden}
body{font-family:"Noto Serif CJK SC","Noto Serif SC","Songti SC","Source Han Serif SC",serif;font-size:17px;line-height:1.95;
 max-width:760px;margin:0 auto;padding:48px 28px 96px}
h1{font-size:30px;letter-spacing:3px;text-align:center;margin:6px 0 4px;font-weight:700}
.sub{text-align:center;color:var(--brown);font-size:13px;letter-spacing:1.5px;margin-bottom:6px}
h2{font-size:19px;margin:44px 0 12px;letter-spacing:2px;border-left:3px solid var(--red);padding-left:10px;font-weight:700}
h3{font-size:16px;margin:26px 0 8px;color:var(--red);letter-spacing:1px}
p{margin:0 0 14px;text-align:justify;text-justify:inter-ideograph}
p.q{background:#FCFAF6;border-left:2px solid var(--line);padding:12px 18px;margin:10px 0 18px;font-size:18px;letter-spacing:1px}
blockquote{border-left:2px solid var(--line);margin:14px 0;padding:4px 0 4px 16px;color:#3B352F;font-size:16px}
blockquote p{letter-spacing:1.2px}
table{border-collapse:collapse;width:100%;margin:14px 0;font-size:15px}
th,td{border:1px solid var(--line);padding:7px 10px;text-align:left}
th{background:#FCFAF6}
figure{margin:26px 0;text-align:center}
figure img{width:100%;max-width:760px;border:1px solid var(--line);background:#F7F4EE}
figcaption{color:var(--brown);font-size:12.5px;letter-spacing:1px;margin-top:8px}
hr{border:none;border-top:1px solid var(--line);margin:36px 0}
.foot{color:var(--brown);font-size:12px;text-align:center;margin-top:60px;letter-spacing:1px}
a{color:var(--red);text-decoration:none}
.toc{columns:2;column-gap:28px;font-size:15px}
.toc p{margin:0 0 8px;text-align:left}
.audio{margin:22px 0 30px;padding:16px 18px 14px;background:#FCFAF6;border:1px solid var(--line)}
.audio .alab{font-size:12.5px;letter-spacing:2px;color:var(--red);margin-bottom:8px}
.audio audio{width:100%;max-width:560px;height:34px;display:block;margin:0 auto}
.audio .asec{margin-top:12px;font-size:12px;letter-spacing:1px;color:var(--brown)}
.audio .asec audio{height:28px;margin-top:6px}
.audio .anote{margin-top:10px;font-size:11.5px;color:var(--brown);letter-spacing:.5px;line-height:1.7}
"""

AUDIO_BLOCK = """<div class="audio">
<div class="alab">朗读　·　普通话</div>
<audio controls preload="metadata" src="../audio/{key}/lang-du.mp3"></audio>
{alt}
<div class="anote">依经文原文朗读，章次不读出；配古琴底乐，不改速、不加拖腔。全库同一音色（豆包 TTS），非播音员录制。</div>
</div>
"""

SHELL = """<!doctype html><html lang="zh-Hans"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<style>{css}</style></head><body>
{body}
<div class="foot">{foot_head}<br>{foot_extra}</div>
</body></html>
"""


def conv(md_text):
    """md -> html；先解 {{fig:key|caption}}"""
    def fig(m):
        key, cap = m.group(1).strip(), m.group(2).strip()
        return ('<figure><img src="../assets/fig/%s.svg" alt="%s"><figcaption>%s</figcaption></figure>'
                % (key, cap, cap))
    md_text = re.sub(r"\{\{fig:([^|]+)\|([^}]+)\}\}", fig, md_text)
    r = subprocess.run(["pandoc", "-f", "markdown", "-t", "html", "--no-highlight"],
                       input=md_text, capture_output=True, text=True)
    return r.stdout


def with_audio(html, audio):
    if not audio:
        return html
    m = re.search(r"</h1>.*?</blockquote>", html, re.S)
    if m:
        p = m.end()
        return html[:p] + audio + html[p:]
    return html.replace("</h1>", "</h1>" + audio, 1)


def main():
    os.makedirs(CH, exist_ok=True)
    # 资源
    dst = os.path.join(DOCS, "assets", "fig")
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if os.path.isdir(dst):
        shutil.rmtree(dst)
    shutil.copytree(os.path.join(ROOT, "assets", "fig"), dst)

    MAXNO = int(os.environ.get("MAXNO", "999"))
    files = sorted(f for f in os.listdir(BOOK) if re.match(r"SJ\d{3}-.+\.md$", f) and int(f[2:5]) <= MAXNO)
    entries = []
    for f in files:
        num = int(re.match(r"SJ(\d{3})", f).group(1))
        title = re.sub(r"^SJ\d{3}-", "", f)[:-3]
        raw = open(os.path.join(BOOK, f), encoding="utf-8").read()
        lines = raw.strip().split("\n")
        # 首行 h1 + 引用副行
        html = conv(raw)
        key = "sj%03d" % num
        audio = ""
        if os.path.exists(os.path.join(DOCS, "audio", key, "lang-du.mp3")):
            alt = ""
            if os.path.exists(os.path.join(DOCS, "audio", key, "lang-du-b.mp3")):
                alt = '<div class="asec">另一音色试听：<a href="../audio/%s/lang-du-b.mp3">lang-du-b</a></div>' % key
            audio = AUDIO_BLOCK.format(key=key, alt=alt)
        page = SHELL.format(
            title="%s · 道可道之诗经" % title,
            desc="《诗经》第 %03d 篇 %s —— 解题、经文、韵读、字义名物、今译、章旨、诗教、分寸、存疑与跨典。" % (num, title),
            canonical="https://q1z2q3-debug.github.io/daokedao-shijing/ch/%s.html" % key,
            css=CSS, body=with_audio(html, audio), foot_head="润泽说　道可道之诗经" + ("　·　第一篇　关雎" if num == 1 else ""),
            foot_extra='<a href="../index.html">全书目录</a>　·　<a href="%s.html">本篇</a>' % key)
        open(os.path.join(CH, key + ".html"), "w", encoding="utf-8").write(page)
        entries.append({"no": num, "key": key, "title": title})

    # 前言
    intro = os.path.join(BOOK, "前言.md")
    if os.path.exists(intro):
        raw = open(intro, encoding="utf-8").read()
        page = SHELL.format(
            title="前言 · 道可道之诗经",
            desc="《诗经》总说：成书、六义、四家诗与朱子、本库读法与用字。",
            canonical="https://q1z2q3-debug.github.io/daokedao-shijing/intro.html",
            css=CSS, body=conv(raw), foot_head="润泽说　道可道之诗经　·　前言",
            foot_extra='<a href="index.html">全书目录</a>')
        open(os.path.join(DOCS, "intro.html"), "w", encoding="utf-8").write(page)

    # 首页（按卷分组）
    VOLS = [(1, 11, "卷一　周南"), (12, 25, "卷二　召南"), (26, 44, "卷三　邶风"),
            (45, 54, "卷四　鄘风"), (55, 64, "卷五　卫风"), (65, 74, "卷六　王风"),
            (75, 95, "卷七　郑风"), (96, 106, "卷八　齐风"),
            (107, 113, "卷九　魏风"), (114, 125, "卷十　唐风"),
            (126, 135, "卷十一　秦风")]
    if entries:
        idx_body = ('<h1>道可道之诗经</h1><div class="sub">润泽说　·　毛诗三百五篇</div>'
                    '<p style="text-align:center;font-size:14px">'
                    '<a href="intro.html">前言</a>　·　进度 %d / 305　·　各篇可听</p><hr>' % len(entries))
        left = list(entries)
        for (lo, hi, name) in VOLS:
            vol = [e for e in entries if lo <= e["no"] <= hi]
            if not vol:
                continue
            idx_body += '<h3 style="margin:22px 0 8px;border:none;color:#994433">%s（%d–%d）　已收 %d</h3><div class="toc">' % (name, lo, hi, len(vol))
            for e in vol:
                idx_body += '<p><a href="ch/%s.html">第%03d篇　%s</a></p>' % (e["key"], e["no"], e["title"])
            idx_body += "</div>"
            left = [e for e in left if not (lo <= e["no"] <= hi)]
        if left:
            idx_body += '<h3 style="margin:22px 0 8px;border:none;color:#994433">后续</h3><div class="toc">'
            for e in left:
                idx_body += '<p><a href="ch/%s.html">第%03d篇　%s</a></p>' % (e["key"], e["no"], e["title"])
            idx_body += "</div>"
        open(os.path.join(DOCS, "index.html"), "w", encoding="utf-8").write(
            SHELL.format(title="道可道之诗经", desc="《诗经》三百五篇逐篇通释，周南起。",
                         canonical="https://q1z2q3-debug.github.io/daokedao-shijing/",
                         css=CSS, body=idx_body, foot_head="润泽说　道可道之诗经", foot_extra=""))

    json.dump({"version": open(os.path.join(ROOT, "VERSION"), encoding="utf-8").read().strip(),
               "total": 305, "count": len(entries), "chapters": entries},
              open(os.path.join(BOOK, "chapters.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("built", len(entries), "chapters")


if __name__ == "__main__":
    main()
