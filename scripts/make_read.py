# -*- coding: utf-8 -*-
"""干净普通话朗读：Piper 原样合成，不做拉伸、不加伴奏。"""
import os, subprocess, shutil, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs", "audio")
TMP = "/tmp/audio_work"
for f in sorted(x for x in os.listdir(os.path.join(ROOT, "audio_src")) if x.endswith(".md")):
    key, name = f[:-3].split("-", 1)
    sid = key.lower()
    work = os.path.join(TMP, sid, "read")
    os.makedirs(work, exist_ok=True)
    subprocess.run(["python3", "/tmp/e2a-lite/tts.py", "build",
                    "--in", os.path.join(ROOT, "audio_src", f), "--out", work,
                    "--speed", "1.0", "--formats", "mp3,srt", "--title", name,
                    "--artist", "润泽说 道可道", "--bitrate", "128k",
                    "--cache", os.path.join(TMP, "cache")],
                   check=True, stdout=subprocess.DEVNULL)
    d = os.path.join(OUT, sid)
    os.makedirs(os.path.join(d, "lab"), exist_ok=True)
    for old, new in [("%s.mp3" % name, "lang-du.mp3"), ("%s.srt" % name, "lang-du.srt")]:
        src = os.path.join(work, old)
        if os.path.exists(src):
            shutil.copy(src, os.path.join(d, new))
    for old in ["yin-chang.mp3", "yin-song.mp3"]:
        p = os.path.join(d, old)
        if os.path.exists(p):
            shutil.move(p, os.path.join(d, "lab", old))
    dur = subprocess.check_output(["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
                                   "-of", "default=nw=1:nk=1", os.path.join(d, "lang-du.mp3")])
    print("ok", sid, round(float(dur), 1), "s")
