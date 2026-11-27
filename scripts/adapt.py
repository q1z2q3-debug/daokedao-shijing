# -*- coding: utf-8 -*-
"""适配层：粗细、颜色、硬软

三条量纲，各自有公式，不靠眼调。

1 粗细适配 —— 线宽随物体的画面尺寸走，不随页面走。
   视觉宽度恒定律：w / h ≈ 常数。h 是该物在画布上的高度。
        w = clamp(k * h, 0.38, 1.05),  k = 0.0034
   h=208 的舟 → 0.71；h=110 的河 → 0.37；h=60 的小兽 → 0.38（下限兜住）
   同页两物若 h 差 3 倍而线宽相同，读者会读到「不在一个世界」。

2 颜色适配 —— 墨色按「退远度」分配，不按「部位」分配。
        L(d) = 25 + 88 * d      d ∈ [0,1]，d=0 焦墨、d=1 最远
   前景 d 0.00–0.15｜结构 d 0.30–0.45｜环境（水、云、远树）d 0.55–0.75
   同一层内所有笔必须同色；颜色是层次的函数，不是心情的函数。

3 硬软适配 —— 由「物性」定笔性。
   硬（器物、建筑、骨骼、直线结构）：等压、转角保留、方收。
        w1 = w*0.92, taper_start 0.00, taper_end 0.06
   半硬（衣、须、发、草）：起轻、中实、收尖。
        w1 = w*0.55, taper_start 0.20, taper_end 0.55
   软（水、云、烟、雾）：双端俱弱、断开分节、波峰加粗。
        w1 = w*0.40, taper_start 0.45, taper_end 0.60
"""
import math

INK_TOP = (0x1C, 0x19, 0x17)


def clamp(v, lo, hi):
    return max(lo, min(hi, v))


def w_of(size, k=0.0034, lo=0.38, hi=1.05):
    """粗细适配：size 为物体在画布上的高度（px）。"""
    return clamp(k * size, lo, hi)


def tone(d=0.0):
    """颜色适配：d 为退远度，返回 hex。"""
    d = clamp(d, 0.0, 1.0)
    L = 25 + 88 * d
    # 墨并非中性灰：R>G>B 各差 2–4，冷灰会发脏
    return '#%02X%02X%02X' % (int(L + 3), int(L), int(L - 3))


PENS = {
    'hard': dict(wmul=0.95, ts=0.00, te=0.00),
    'half': dict(wmul=0.55, ts=0.18, te=0.50),
    'soft': dict(wmul=0.42, ts=0.32, te=0.50),
}


def compensate(kind):
    """视觉重量补偿：软笔两端收成细，平均宽低于标称，须按比例放大。
    三条适配各自算对、并置却不齐，缺的就是这一层——适配的目标不是参数正确，
    而是同一页上三格视觉重量相等。"""
    p = PENS[kind]
    return 1.0 / max(0.55, 1.0 - 0.30 * (p['ts'] + p['te']))


def pen(kind='hard'):
    return PENS[kind]


def stroke(fn, pts, size, kind='hard', depth=0.0, col=None, n=None):
    """一次出笔：粗细由 size、浓淡由 depth、软硬由 kind。

    fn 为 svgbrush.stroke，使本模块不直接依赖其内部。
    """
    p = pen(kind)
    w = w_of(size) * compensate(kind)
    w1 = w * p['wmul']
    return fn(pts, w, w1, n=n or max(12, int(len(pts) * 2.2)),
              col=col or tone(depth), taper_start=p['ts'], taper_end=p['te'])
