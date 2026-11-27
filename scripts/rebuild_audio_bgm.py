#!/usr/bin/env python3
"""Rebuild all Shijing narration: canonical text only, no chapter labels, with low guqin bed."""
import glob, os, re, subprocess, sys, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TTS = "/home/user/Doubao/chats/38454357066725378/ebook2audio-lite/tts.py"
VOICE = "/home/user/.local/share/e2a-lite/voices/zh_CN-huayan-medium.onnx"
BGM = os.path.join(ROOT, "assets/audio/bgm/guqin-calm.mp3")
WORK = os.path.join(ROOT, "audio_work/read")
CACHE = os.path.join(ROOT, "audio_work/cache")

def run(cmd):
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        print(p.stdout)
        print(p.stderr)
        raise SystemExit(p.returncode)
    return p.stdout

def duration(path):
    out = run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
               "-of", "default=noprint_wrappers=1:nokey=1", path]).strip()
    return float(out)

def main():
    files = sorted(glob.glob(os.path.join(ROOT, "audio_src", "SJ*.md")))
    os.makedirs(WORK, exist_ok=True)
    os.makedirs(CACHE, exist_ok=True)
    for idx, src in enumerate(files, 1):
        key = os.path.basename(src).split("-")[0].lower()
        first = open(src, encoding="utf-8").readline().strip()
        title = re.sub(r"^#\s*", "", first)
        title = re.sub(r"^第[一二三四五六七八九十百]+篇[　\s]*", "", title).strip() or key
        outdir = os.path.join(WORK, key)
        os.makedirs(outdir, exist_ok=True)
        print(f"[{idx}/{len(files)}] {key} {title}", flush=True)
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
        dest = os.path.join(ROOT, "docs/audio", key, "lang-du.mp3")
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        run(["cp", mixed, dest])
        srt = glob.glob(os.path.join(outdir, "*.srt"))
        if srt:
            run(["cp", srt[0], os.path.join(os.path.dirname(dest), "lang-du.srt")])
        print(f"    {d:.2f}s -> {duration(dest):.2f}s", flush=True)

if __name__ == "__main__":
    main()
