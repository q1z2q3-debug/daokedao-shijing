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
body{font-family:"Noto Serif SC","Songti SC","Source Han Serif SC",serif;font-size:17px;line-height:1.95;
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
"""

SHELL = """<!doctype html><html lang="zh-Hans"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<style>{css}</style></head><body>
{body}
<div class="foot">润泽说　道可道之诗经　·　{qty}<br>{foot_extra}</div>
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


def main():
    os.makedirs(CH, exist_ok=True)
    # 资源
    dst = os.path.join(DOCS, "assets", "fig")
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if os.path.isdir(dst):
        shutil.rmtree(dst)
    shutil.copytree(os.path.join(ROOT, "assets", "fig"), dst)

    files = sorted(f for f in os.listdir(BOOK) if re.match(r"SJ\d{3}-.+\.md$", f))
    entries = []
    for f in files:
        num = int(re.match(r"SJ(\d{3})", f).group(1))
        title = re.sub(r"^SJ\d{3}-", "", f)[:-3]
        raw = open(os.path.join(BOOK, f), encoding="utf-8").read()
        lines = raw.strip().split("\n")
        # 首行 h1 + 引用副行
        html = conv(raw)
        key = "sj%03d" % num
        page = SHELL.format(
            title="%s · 道可道之诗经" % title,
            desc="《诗经》第 %03d 篇 %s —— 解题、经文、韵读、字义名物、今译、章旨、诗教、分寸、存疑与跨典。" % (num, title),
            canonical="https://q1z2q3-debug.github.io/daokedao-shijing/ch/%s.html" % key,
            css=CSS, body=html, qty="第一篇　关雎" if num == 1 else "",
            foot_extra='<a href="../index.html">全书目录</a>　·　<a href="%s.html">本篇</a>' % key)
        open(os.path.join(CH, key + ".html"), "w", encoding="utf-8").write(page)
        entries.append({"no": num, "key": key, "title": title})

    # 首页
    if entries:
        idx_body = ('<h1>道可道之诗经</h1><div class="sub">润泽说　·　毛诗三百五篇</div>'
                    '<p style="text-align:center;color:#7C6D5C;font-size:14px">'
                    '卷一　周南（11 篇）　进度：%d / 305</p><hr><div class="toc">' % len(entries))
        for e in entries:
            idx_body += '<p><a href="ch/%s.html">第%03d篇　%s</a></p>' % (e["key"], e["no"], e["title"])
        idx_body += "</div>"
        open(os.path.join(DOCS, "index.html"), "w", encoding="utf-8").write(
            SHELL.format(title="道可道之诗经", desc="《诗经》三百五篇逐篇通释，周南起。",
                         canonical="https://q1z2q3-debug.github.io/daokedao-shijing/",
                         css=CSS, body=idx_body, qty="", foot_extra=""))

    json.dump({"version": open(os.path.join(ROOT, "VERSION"), encoding="utf-8").read().strip(),
               "total": 305, "count": len(entries), "chapters": entries},
              open(os.path.join(BOOK, "chapters.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("built", len(entries), "chapters")


if __name__ == "__main__":
    main()
