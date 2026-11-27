# -*- coding: utf-8 -*-
"""fourier_shape · 用谐波定义器形

1) 闭合轮廓 → 复数序列 → FFT → 取前 k 阶 → 重建（k 即「概括度」）
2) 两个器形系数线性插值 → 同族形空间的连续变形
3) 开放曲线 → 镜像延拓 → FFT 低通 → 平滑
4) 笔触抖动 → 1/f 相位噪声叠加（低频定势、高频细纹）
"""
import numpy as np


def resample_closed(pts, n=256):
    pts = np.asarray(pts, float)
    if np.allclose(pts[0], pts[-1]):
        pts = pts[:-1]
    pts = np.vstack([pts, pts[:1]])
    seg = np.linalg.norm(np.diff(pts, axis=0), axis=1)
    s = np.concatenate([[0], np.cumsum(seg)])
    tt = np.linspace(0, s[-1], n, endpoint=False)
    x = np.interp(tt, s, pts[:, 0])
    y = np.interp(tt, s, pts[:, 1])
    return np.stack([x, y], 1)


def fd_coeff(pts, k=16):
    z = resample_closed(pts, 256)
    c = np.fft.fft(z[:, 0] + 1j * z[:, 1])
    keep = np.zeros_like(c)
    keep[0] = c[0]
    for i in range(1, k + 1):
        keep[i] = c[i]
        keep[-i] = c[-i]
    return keep


def fd_rebuild(coeff, n=256):
    z = np.fft.ifft(coeff.real + 1j * coeff.imag, n=n)
    return np.stack([z.real, z.imag], 1)


def fd_smooth(pts, k=16):
    return fd_rebuild(fd_coeff(pts, k))


def fd_between(a, b, t, k=16):
    """同族两形插值：系数域线性过渡。"""
    ca, cb = fd_coeff(a, k), fd_coeff(b, k)
    return fd_rebuild(ca * (1 - t) + cb * t)


def smooth_open(pts, k=8):
    """开放折线低通：首尾镜像延拓后截断高频。"""
    pts = np.asarray(pts, float)
    mir = np.vstack([pts, pts[::-1][1:]])
    z = mir[:, 0] + 1j * mir[:, 1]
    c = np.fft.fft(z)
    keep = np.zeros_like(c)
    keep[:k + 1] = c[:k + 1]
    keep[-k:] = c[-k:]
    zz = np.fft.ifft(keep)
    return np.stack([zz.real, zz.imag], 1)[:len(pts)]


def power_law_noise(n, beta=1.6, seed=0):
    """1/f^beta 噪声（粉红/布朗之间），用于笔触与纸纹。"""
    rng = np.random.default_rng(seed)
    f = np.fft.rfftfreq(n)
    f[0] = 1e-9
    amps = 1.0 / (f ** (beta / 2.0))
    ph = rng.uniform(0, 2 * np.pi, len(f))
    spec = amps * np.exp(1j * ph)
    sig = np.fft.irfft(spec, n)
    sig = (sig - sig.min()) / (np.ptp(sig) + 1e-9)
    return sig - 0.5


def wobble(pts, amp=0.8, beta=1.6, seed=0, scale=1.0):
    """沿法向叠加 1/f 噪声，得「手的气」。"""
    pts = np.asarray(pts, float)
    n = len(pts)
    d = np.gradient(pts, axis=0)
    ln = np.linalg.norm(d, axis=1)
    ln[ln < 1e-9] = 1.0
    nrm = np.stack([-d[:, 1] / ln, d[:, 0] / ln], 1)
    sig = power_law_noise(n, beta, seed) * amp * scale
    return pts + nrm * sig[:, None]
