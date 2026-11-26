# -*- coding: utf-8 -*-
"""诗经吟诵：Piper 句级合成 → 逐句放慢、句尾拖腔、章间留白 → 叠五声琴底。
产出 docs/audio/<SJxxx>/yin-song.mp3（纯人声）与 yin-chang.mp3（人声+琴）。"""
import os, re, json, subprocess, wave, math, shutil
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs", "audio")
TMP = "/tmp/audio_work"
SR = 44100
GONG, SHANG, JUE, ZHI, YU = 196.0, 220.0, 246.9, 293.7, 329.6
MEL = [GONG, ZHI, YU, SHANG, JUE, SHANG, YU, ZHI, GONG, SHANG, JUE, ZHI, YU, JUE, SHANG, GONG]
BEAT = 0.62
SENT_GAP, CHAP_GAP, TAIL = 0.75, 2.1, 0.45


def run(cmd):
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def read_wav(p):
    with wave.open(p, "rb") as w:
        assert w.getnchannels() == 1 and w.getsampwidth() == 2
        d = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0
    return d


def write_wav(p, d):
    with wave.open(p, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((np.clip(d, -1, 1) * 32767).astype(np.int16).tobytes())


def dur(p):
    o = subprocess.check_output(["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
                                 "-of", "default=nw=1:nk=1", p])
    return float(o.strip())


def parse_srt(p):
    txt = open(p, encoding="utf-8").read().strip().split("\n\n")
    out = []
    for blk in txt:
        lines = blk.strip().splitlines()
        if len(lines) < 3:
            continue
        m = re.match(r"(\d+):(\d+):(\d+),(\d+) --> (\d+):(\d+):(\d+),(\d+)", lines[1])
        a = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + int(m.group(3)) + int(m.group(4)) / 1000
        b = int(m.group(5)) * 3600 + int(m.group(6)) * 60 + int(m.group(7)) + int(m.group(8)) / 1000
        out.append((a, b, " ".join(lines[2:]).strip()))
    return out


def tone(f, n, amp=1.0, phase=0.0):
    t = np.arange(n) / SR
    env = np.exp(-t / 0.42) * (1 - np.exp(-t / 0.02))
    v = 0.62 * np.sin(2 * np.pi * f * t + phase)
    v += 0.26 * np.sin(2 * np.pi * 2 * f * t + phase * 1.3)
    v += 0.10 * np.sin(2 * np.pi * 3 * f * t + phase * 0.7)
    return (v * env * amp).astype(np.float32)


def bed(seconds, seed):
    n = int(SR * seconds)
    buf = (0.30 * np.sin(2 * np.pi * GONG / 2 * np.arange(n) / SR)).astype(np.float32) * 0.5
    rng = np.random.default_rng(seed)
    pos, i = 0.0, 0
    while pos < seconds - 0.2:
        note = MEL[i % len(MEL)] + rng.normal(0, 0.6)
        seg = tone(note, int(SR * min(BEAT * 1.9, seconds - pos + 0.6)), 0.55, rng.uniform(0, 6.28))
        s, e = int(SR * pos), min(n, int(SR * pos) + len(seg))
        buf[s:e] += seg[: e - s]
        pos += BEAT
        i += 1
    f = int(SR * 1.0)
    buf[:f] *= np.linspace(0, 1, f)
    buf[-f:] *= np.linspace(1, 0, f)
    return (buf / (np.max(np.abs(buf)) or 1) * 0.85).astype(np.float32)


def chapter_sizes(md_path):
    txt = open(md_path, encoding="utf-8").read()
    sizes, cur = [], 0
    for line in txt.splitlines():
        if re.match(r"^##\s+第", line.strip()):
            if cur:
                sizes.append(cur)
            cur = 0
        elif line.strip() and not line.startswith("#"):
            cur += 1
    if cur:
        sizes.append(cur)
    return sizes


def main():
    srcs = sorted(f for f in os.listdir(os.path.join(ROOT, "audio_src")) if f.endswith(".md"))
    for idx, f in enumerate(srcs):
        key = f[:-3]
        sid, name = key.split("-", 1)
        work = os.path.join(TMP, sid)
        os.makedirs(work, exist_ok=True)
        subprocess.run(["python3", "/tmp/e2a-lite/tts.py", "build",
                        "--in", os.path.join(ROOT, "audio_src", f),
                        "--out", work, "--speed", "0.9", "--formats", "mp3,srt",
                        "--title", name, "--artist", "润泽说 道可道",
                        "--bitrate", "128k", "--cache", os.path.join(TMP, "cache")],
                       check=True, stdout=subprocess.DEVNULL)
        voice = os.path.join(work, name + ".mp3")
        srt = os.path.join(work, name + ".srt")
        sents = parse_srt(srt)
        sizes = chapter_sizes(os.path.join(ROOT, "audio_src", f))
        # 逐句：慢语速 + 拖腔
        parts, k = [], 0
        for ci, cnt in enumerate(sizes):
            for j in range(cnt):
                if k >= len(sents):
                    break
                a, b = sents[k][0], sents[k][1]
                seg = os.path.join(work, "seg.wav")
                run(["ffmpeg", "-y", "-ss", str(a), "-to", str(b), "-i", voice,
                     "-ar", str(SR), "-ac", "1", seg])
                body = os.path.join(work, "body.wav")
                run(["ffmpeg", "-y", "-i", seg, "-filter:a", "atempo=0.88", "-ar", str(SR), "-ac", "1", body])
                t0 = max(b - TAIL, a + 0.15)
                tail0 = os.path.join(work, "t0.wav")
                run(["ffmpeg", "-y", "-ss", str(t0), "-to", str(b), "-i", voice,
                     "-ar", str(SR), "-ac", "1", tail0])
                tail1 = os.path.join(work, "t1.wav")
                run(["ffmpeg", "-y", "-i", tail0, "-filter:a",
                     "atempo=0.5,atempo=0.5,atempo=0.8", "-ar", str(SR), "-ac", "1", tail1])
                tail = read_wav(tail1)
                tail = tail * np.linspace(0.55, 0, len(tail)) ** 1.2 * 1.6
                d = np.concatenate([read_wav(body), tail.astype(np.float32)])
                parts.append(d)
                parts.append(np.zeros(int(SR * (SENT_GAP if j < cnt - 1 else CHAP_GAP)), dtype=np.float32))
                k += 1
        voice_track = np.concatenate(parts)
        peak = np.max(np.abs(voice_track)) or 1
        voice_track = voice_track / peak * 0.92
        outdir = os.path.join(OUT, sid.lower())
        os.makedirs(outdir, exist_ok=True)
        vpath = os.path.join(work, "voice_full.wav")
        write_wav(vpath, voice_track)
        yin_song = os.path.join(outdir, "yin-song.mp3")
        run(["ffmpeg", "-y", "-i", vpath, "-af", "loudnorm=I=-15:TP=-1.5:LRA=11",
             "-c:a", "libmp3lame", "-b:a", "128k", yin_song])
        total = len(voice_track) / SR
        bpath = os.path.join(work, "bed.wav")
        write_wav(bpath, bed(total + 1.0, idx))
        yin_chang = os.path.join(outdir, "yin-chang.mp3")
        run(["ffmpeg", "-y", "-i", vpath, "-i", bpath, "-filter_complex",
             "[0:a]loudnorm=I=-15:TP=-1.5:LRA=11[v];[1:a]volume=0.26,afade=t=in:d=1[a];"
             "[v][a]amix=inputs=2:duration=first,alimiter=limit=0.95",
             "-c:a", "libmp3lame", "-b:a", "128k", yin_chang])
        print("ok", sid, round(dur(yin_song), 1), "s")


main()
