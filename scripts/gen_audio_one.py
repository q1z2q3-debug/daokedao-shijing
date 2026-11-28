# -*- coding: utf-8 -*-
"""单篇朗读合成（与 rebuild_audio_bgm.py 同一管线，只跑指定篇目，不动其余）。
用法: python3 scripts/gen_audio_one.py SJ071-葛藟
"""
import os, re, subprocess, sys, glob, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TTS = "/home/user/Doubao/chats/38454357066725378/ebook2audio-lite/tts.py"
VOICE = os.path.expanduser("~/.local/share/e2a-lite/voices/zh_CN-huayan-medium.onnx")
BGM = os.path.join(ROOT, "assets", "audio", "bgm", "guqin-calm.mp3")
CACHE = os.path.join(ROOT, "audio_work", "cache")


def run(cmd):
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        print(p.stdout); print(p.stderr)
        raise SystemExit(p.returncode)
    return p.stdout


def duration(path):
    out = run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
               "-of", "default=noprint_wrappers=1:nokey=1", path]).strip()
    return float(out)


def main():
    src_name = sys.argv[1]
    src = os.path.join(ROOT, "audio_src", src_name + ".md")
    key = src_name.split("-")[0].lower()
    title = re.sub(r"^SJ\d{3}-", "", src_name)
    outdir = os.path.join(ROOT, "audio_work", key)
    os.makedirs(outdir, exist_ok=True)
    os.makedirs(CACHE, exist_ok=True)

    run([sys.executable, TTS, "build", "--in", src, "--out", outdir,
         "--voice", VOICE, "--speed", "0.92", "--formats", "mp3,srt",
         "--title", title, "--artist", "润泽说 道可道", "--bitrate", "128k",
         "--cache", CACHE, "--jobs", "2"])

    mp3s = glob.glob(os.path.join(outdir, "*.mp3"))
    if not mp3s:
        raise SystemExit("no mp3: " + key)
    raw = max(mp3s, key=os.path.getsize)
    d = duration(raw)
    fade_out = max(1.5, d - 2.6)
    mixed = os.path.join(outdir, "lang-du.mp3")
    run(["ffmpeg", "-y", "-i", raw, "-stream_loop", "-1", "-i", BGM,
         "-filter_complex",
         f"[1:a]volume=0.085,afade=t=in:st=0:d=2,afade=t=out:st={fade_out:.3f}:d=2.6[bg];"
         "[0:a][bg]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95[out]",
         "-map", "[out]", "-ar", "44100", "-b:a", "160k", mixed])

    dest = os.path.join(ROOT, "docs", "audio", key)
    os.makedirs(dest, exist_ok=True)
    run(["cp", mixed, os.path.join(dest, "lang-du.mp3")])
    srt = glob.glob(os.path.join(outdir, "*.srt"))
    if srt:
        run(["cp", srt[0], os.path.join(dest, "lang-du.srt")])
    print(f"{key} {title} raw {d:.2f}s -> {duration(os.path.join(dest, 'lang-du.mp3')):.2f}s")


if __name__ == "__main__":
    main()
