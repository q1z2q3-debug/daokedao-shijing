# -*- coding: utf-8 -*-
"""干旄 15 秒短片：SVG 逐帧渲染 → ffmpeg 合成（含朗读音轨）。"""
import os, sys, math, subprocess, shutil
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svgbrush import stroke, INK, INK2, PAPER, RED, GREY

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TMP = "/tmp/short053"
W, H, FPS = 960, 540, 12
import subprocess as _sp
_d = _sp.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
              "-of", "default=nw=1:nk=1", os.path.join(ROOT, "docs", "audio", "sj053", "lang-du.mp3")],
             capture_output=True, text=True)
DUR = (float(_d.stdout.strip()) if _d.stdout.strip() else 22.0) + 0.6
N = int(FPS * DUR)


def Q(p0, p1, p2, n=16):
    t = np.linspace(0, 1, n)[:, None]
    return (np.array(p0, float)[None] * (1 - t) ** 2
            + 2 * np.array(p1, float)[None] * (1 - t) * t
            + np.array(p2, float)[None] * t ** 2)


# 线集：按笔序，前 6 秒画完
S = []
for cx, top, base in ((192, 196, 486), (480, 196, 486), (768, 196, 486)):
    S.append(([(cx - 1.7, base), (cx - 1.7, top)], 1.5, "pole"))
    S.append(([(cx + 1.7, base), (cx + 1.7, top)], 1.5, "pole"))
    S.append(([(cx - 5.6, top), (cx - 3.4, top - 7), (cx, top - 16), (cx + 3.4, top - 7), (cx + 5.6, top)], 1.0, "cap"))
cx = 192
S.append(([(cx - 5.4, 200), (cx - 9.4, 232), (cx - 8.4, 268)], 1.0, "tuft"))
S.append(([(cx + 5.4, 200), (cx + 9.4, 232), (cx + 8.4, 268)], 1.0, "tuft"))
for i in range(7):
    x0 = cx - 7 + i * 2.2
    ey = 330 + (i % 5) * 16
    S.append(([(x0, 222), (x0 + ((-1) ** i) * 6, ey - 34), (x0 + ((-1) ** i) * 12, ey)], 0.9, "tuft"))
cx = 480
S.append(([(cx - 50, 220), (cx + 50, 220)], 1.6, "flag"))
S.append(([(cx - 40, 228), (cx + 40, 228), (cx + 40, 340), (cx - 40, 340), (cx - 40, 228)], 1.2, "flag"))
S.append(([(cx + 1, 199), (cx + 50, 220)], 1.0, "flag"))
for i in range(6):
    x0 = cx - 36 + i * 14
    ln = 56 + (i % 3) * 12
    S.append(([(x0, 340), (x0 + 2 * ((-1) ** i), 340 + ln * 0.6), (x0 + 3.4 * ((-1) ** i), 340 + ln)], 1.0, "flag"))
cx = 768
for k in range(3):
    by = 244 + k * 54
    for dx in (-5, 5):
        L, Wd = 66, 17
        ang = dx * 0.028
        dxx, dyy = math.sin(ang), -math.cos(ang)
        nx, ny = -dyy, dxx
        pts_l, pts_r = [], []
        for t in np.linspace(0, 1, 10):
            wd = Wd * (max(0.0, math.sin(math.pi * (0.08 + t * 0.9))) ** 0.55) * 0.5
            px, py = cx + dx + dxx * L * t, by + dyy * L * t
            pts_l.append((px + nx * wd, py + ny * wd))
            pts_r.append((px - nx * wd, py - ny * wd))
        S.append((pts_l, 0.9, "fthr"))
        S.append((pts_r, 0.9, "fthr"))

T_DRAW0, T_END_DRAW = 2.2, min(10.0, DUR * 0.45)
GAP = (T_END_DRAW - T_DRAW0) / len(S)


def cut(pts, ratio):
    """按长度取前 ratio 段。"""
    if ratio >= 1:
        return pts
    p = np.asarray(pts, float)
    seg = np.linalg.norm(np.diff(p, axis=0), axis=1)
    s = np.concatenate([[0], np.cumsum(seg)])
    tot = s[-1] * ratio
    out = [p[0]]
    for i in range(1, len(p)):
        if s[i] <= tot:
            out.append(p[i])
        else:
            r = (tot - s[i - 1]) / max(1e-6, seg[i - 1])
            out.append(p[i - 1] + (p[i] - p[i - 1]) * r)
            break
    return np.array(out)


def frame(t):
    p = []
    # 镜头：后 4 秒缓慢推近
    T_CAM = T_END_DRAW + 3.6
    if t < T_CAM:
        sc, tx, ty = 1.0, 0.0, 0.0
    else:
        u = min(1.0, (t - T_CAM) / max(2.0, DUR - T_CAM - 1.0))
        e = u * u * (3 - 2 * u)
        sc, tx, ty = 1.0 + 0.09 * e, 0.0, 5.0 * e
    p.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" '
             'font-family="Noto Serif SC,Songti SC,serif" stroke-linejoin="round" stroke-linecap="round">' % (W, H, W, H))
    p.append('<rect width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    # 页眉（2 秒后淡入）
    a_head = np.clip((t - 1.2) / 1.2, 0, 1)
    p.append('<g transform="translate(%d,%d) scale(%.4f) translate(%d,%d)">' % (W / 2, H / 2, sc, -W / 2, -H / 2 + ty))
    p.append('<text x="56" y="76" font-size="10" fill="%s" letter-spacing="2" opacity="%.2f">鄘风 · 四</text>' % (RED, a_head))
    p.append('<text x="%d" y="80" text-anchor="middle" font-size="30" letter-spacing="12" fill="%s" opacity="%.2f">干 旄</text>'
             % (W / 2, INK, a_head))
    p.append('<line x1="56" y1="100" x2="%d" y2="100" stroke="%s" stroke-width="0.8" opacity="%.2f"/>' % (W - 56, GREY, a_head))

    # 笔顺生长
    for i, (pts, w, grp) in enumerate(S):
        t0 = T_DRAW0 + i * GAP
        r = np.clip((t - t0) / GAP, 0, 1)
        if r <= 0:
            continue
        d = cut(pts, r)
        if len(d) < 2:
            continue
        p.append(stroke(d, w, col=INK, n=50, taper_start=0.15, taper_end=0.3))

    # 鸟隼（6.2–8.2 淡入）
    a_b = np.clip((t - (T_END_DRAW + 0.6)) / 1.6, 0, 1)
    if a_b > 0:
        p.append('<g opacity="%.2f">' % (a_b * 0.9))
        for (bx, by, s2) in ((470, 268, 0.9), (492, 300, 0.7)):
            p.append(stroke(Q((bx - 12 * s2, by + 3 * s2), (bx, by - 5 * s2), (bx + 12 * s2, by + 1 * s2)), 0.7, n=18))
            p.append(stroke(Q((bx - 1 * s2, by - 1 * s2), (bx - 11 * s2, by - 16 * s2), (bx - 22 * s2, by - 7 * s2)), 0.6, n=18))
            p.append(stroke(Q((bx + 3 * s2, by - 1 * s2), (bx + 9 * s2, by - 14 * s2), (bx + 20 * s2, by - 3 * s2)), 0.6, n=18))
        p.append('</g>')

    p.append('</g>')
    # 引句（脱离镜头，固定在屏幕下方）
    a_q = np.clip((t - (T_END_DRAW + 1.8)) / 1.6, 0, 1)
    p.append('<text x="%d" y="%d" text-anchor="middle" font-size="21" letter-spacing="3" fill="%s" opacity="%.2f">孑孑干旄，在浚之郊</text>'
             % (W / 2, H - 58, INK, a_q))
    # 落款
    a_s = np.clip((t - (DUR - 4.0)) / 1.6, 0, 1)
    p.append('<text x="%d" y="%d" text-anchor="middle" font-size="11" letter-spacing="2" fill="%s" opacity="%.2f">润泽说 道可道之诗经 · 鄘风五十三</text>'
             % (W / 2, H - 24, GREY, a_s))
    p.append('</svg>')
    return '\n'.join(p)


if __name__ == "__main__":
    shutil.rmtree(TMP, ignore_errors=True)
    os.makedirs(TMP, exist_ok=True)
    import cairosvg
    for f in range(N):
        t = f / FPS
        cairosvg.svg2png(bytestring=frame(t).encode('utf-8'),
                         write_to=os.path.join(TMP, "f%03d.png" % f), output_width=W)
        if f % 24 == 0:
            print("frame", f, "/", N)
    out = os.path.join(ROOT, "dist", "short-053-ganmao.mp4")
    cmd = ["ffmpeg", "-y", "-framerate", str(FPS), "-i", os.path.join(TMP, "f%03d.png"),
           "-i", os.path.join(ROOT, "docs", "audio", "sj053", "lang-du.mp3"),
           "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20",
           "-c:a", "aac", "-b:a", "128k", "-shortest", out]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("mp4", os.path.getsize(out))
