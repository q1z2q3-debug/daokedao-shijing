# -*- coding: utf-8 -*-
"""SJ161–SJ170 小雅鹿鸣之什十篇二十图：图一名物，图二义理。760×540，不填面。"""
import os, sys, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from gen_batch_154_160 import (t, p, line, circ, rect, person, foot,
                               PAPER, INK, DARK, LIGHT, RED, SEAL, GOLD,
                               ZPAPER, ZINK, ZMID, LINE_L, robe, fish, nest, eggs, owl,
                               axe, shoe)
from gen_batch_123_125 import person as person_face

ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "assets", "fig")


def head(title, sub, zh_no, zhuo=False):
    paper = ZPAPER if zhuo else PAPER
    ink = ZINK if zhuo else INK
    mid = ZMID if zhuo else DARK
    border = ZMID if zhuo else LINE_L
    return ['<rect width="760" height="540" fill="%s"/>' % paper,
            '<rect x="10" y="10" width="740" height="520" fill="none" stroke="%s" stroke-width="0.6"/>' % border,
            '<rect x="22" y="28" width="716" height="470" fill="none" stroke="%s" stroke-width="0.8"/>' % border,
            t(38, 62, "小 雅 · 鹿鸣之什", 9.2, RED, ls=1.2),
            t(380, 72, title, 24.5, ink, "middle", "bold", 1.4),
            t(720, 62, "诗三百五篇 · 之%s" % zh_no, 8.6, mid, "end", ls=1),
            line(38, 100, 722, 100, 0.35, GOLD),
            t(380, 122, sub, 10.2, mid, "middle", ls=1)]


def bfig(title, sub, rows, conclusion, zh_no):
    s = head(title, sub, zh_no, True)
    ys = (190, 260, 330)
    for i, row in enumerate(rows):
        y = ys[i]
        s.append(line(44, y + 22, 716, y + 22, 0.3, ZMID))
        s.append(t(62, y, row[0], 10.4, ZINK, "start", "bold"))
        s.append(t(226, y, row[1], 10.8, ZINK, "start"))
        s.append(t(566, y, row[2], 9.4, ZMID, "start"))
    s.append(line(204, 168, 204, 352, 0.55, RED))
    s.append(line(50, 392, 710, 392, 0.35, GOLD))
    s.append(t(380, 418, conclusion, 11.2, RED, "middle", "bold", 0.6))
    s.append(t(380, 486, "图二 · 义理", 8.6, ZMID, "middle"))
    s.append('<rect x="676" y="492" width="22" height="22" fill="%s" opacity="0.13"/>' % SEAL)
    s.append(t(687, 507, "润", 8.8, SEAL, "middle"))
    return "".join(s)


def deer(x, y, s=1.0):
    """鹿侧身：长颈、楔头、枝角、细腿、短尾，不画眼。"""
    b = [p(f"M {x-50*s} {y-38*s} Q {x-26*s} {y-60*s} {x+4*s} {y-56*s} Q {x+32*s} {y-54*s} {x+42*s} {y-40*s} L {x+42*s} {y-18*s} Q {x+18*s} {y-4*s} {x-12*s} {y-6*s} Q {x-42*s} {y-8*s} {x-50*s} {y-22*s} Z", 0.45, INK),
         p(f"M {x+36*s} {y-40*s} Q {x+44*s} {y-72*s} {x+52*s} {y-96*s} L {x+64*s} {y-98*s} Q {x+54*s} {y-70*s} {x+46*s} {y-38*s} Z", 0.4, INK),
         p(f"M {x+52*s} {y-100*s} L {x+84*s} {y-94*s} Q {x+90*s} {y-90*s} {x+82*s} {y-84*s} L {x+56*s} {y-88*s} Z", 0.4, INK),
         p(f"M {x+58*s} {y-102*s} Q {x+60*s} {y-122*s} {x+78*s} {y-138*s}", 0.32, INK),
         p(f"M {x+62*s} {y-114*s} L {x+52*s} {y-132*s}", 0.28, INK),
         p(f"M {x+68*s} {y-124*s} L {x+72*s} {y-144*s}", 0.28, INK),
         p(f"M {x+74*s} {y-132*s} L {x+88*s} {y-146*s}", 0.28, INK),
         p(f"M {x+70*s} {y-100*s} L {x+76*s} {y-112*s} L {x+84*s} {y-100*s}", 0.26, INK)]
    for dx in (28, 10, -22, -38):
        b.append(p(f"M {x+dx*s} {y-6*s} L {x+dx*s-3*s} {y+18*s} L {x+dx*s+2*s} {y+30*s} L {x+dx*s-1*s} {y+50*s} L {x+dx*s-7*s} {y+52*s}", 0.28, INK))
        b.append(line(x+dx*s-3*s, y+18*s, x+dx*s+1*s, y+20*s, 0.2, LIGHT))
    b.append(p(f"M {x-50*s} {y-34*s} Q {x-62*s} {y-42*s} {x-62*s} {y-26*s}", 0.28, INK))
    return b


def horse(x, y, s=1.0):
    """马首侧视：斜颈、长面、双耳、鬃，不画眼。"""
    b = [p(f"M {x-18*s} {y+70*s} L {x-26*s} {y+12*s} L {x-18*s} {y-14*s} L {x+8*s} {y-22*s} L {x+38*s} {y-16*s} L {x+56*s} {y+0*s} Q {x+62*s} {y+6*s} {x+54*s} {y+14*s} L {x+46*s} {y+16*s} L {x+8*s} {y+10*s} L {x+0*s} {y+18*s} L {x-4*s} {y+30*s} L {x+2*s} {y+70*s} Z", 0.42, INK),
         p(f"M {x-18*s} {y-14*s} L {x-24*s} {y-36*s} L {x-8*s} {y-16*s}", 0.28, INK),
         p(f"M {x-6*s} {y-16*s} L {x-4*s} {y-38*s} L {x+6*s} {y-18*s}", 0.28, INK),
         p(f"M {x-26*s} {y+54*s} Q {x-30*s} {y+10*s} {x-18*s} {y-14*s}", 0.25, DARK),
         line(x+54*s, y+4*s, x+58*s, y+10*s, 0.2, LIGHT),
         p(f"M {x+46*s} {y+16*s} Q {x+50*s} {y+10*s} {x+48*s} {y+4*s}", 0.2, LIGHT)]
    for i in range(6):
        b.append(line(x-22*s+i*2*s, y+52*s-i*11*s, x-30*s+i*2*s, y+56*s-i*11*s, 0.2, LIGHT))
    return b


def bird(x, y, s=1.0):
    """小鸟：身、头、喙、翅、三尾、双足，不画眼。"""
    return [p(f"M {x-22*s} {y-8*s} Q {x-6*s} {y-24*s} {x+12*s} {y-14*s} Q {x+22*s} {y-6*s} {x+12*s} {y+6*s} Q {x-8*s} {y+8*s} {x-22*s} {y-8*s} Z", 0.4, INK),
            circ(x+16*s, y-20*s, 9*s, 0.35, INK),
            p(f"M {x+24*s} {y-22*s} L {x+36*s} {y-20*s} L {x+25*s} {y-15*s} Z", 0.28, INK),
            p(f"M {x-12*s} {y-8*s} Q {x-2*s} {y+2*s} {x+8*s} {y-8*s} Q {x-1*s} {y-2*s} {x-12*s} {y-8*s}", 0.22, LIGHT),
            p(f"M {x-22*s} {y-10*s} L {x-42*s} {y-22*s} L {x-38*s} {y-8*s} L {x-44*s} {y-2*s}", 0.26, INK),
            line(x+1*s, y+5*s, x+1*s, y+18*s, 0.25, INK),
            line(x+1*s, y+18*s, x-5*s, y+20*s, 0.2, INK),
            line(x+1*s, y+18*s, x+7*s, y+20*s, 0.2, INK)]


def cart(x, y, s=1.0):
    """车：轮、箱、辕、衡。"""
    b = [circ(x-34*s, y, 24*s, 0.42, DARK), circ(x+34*s, y, 24*s, 0.42, DARK)]
    for cx in (x-34*s, x+34*s):
        b += [line(cx, y, cx, y-24*s, 0.28, LIGHT), line(cx, y, cx, y+24*s, 0.28, LIGHT),
              line(cx-24*s, y, cx+24*s, y, 0.28, LIGHT), line(cx-17*s, y-17*s, cx+17*s, y+17*s, 0.22, LIGHT),
              line(cx-17*s, y+17*s, cx+17*s, y-17*s, 0.22, LIGHT)]
    b.append(rect(x-46*s, y-56*s, 92*s, 42*s, 0.42, DARK))
    b.append(line(x-46*s, y-36*s, x+46*s, y-36*s, 0.25, LIGHT))
    b.append(line(x+46*s, y-40*s, x+92*s, y-52*s, 0.32, DARK))
    b.append(line(x+92*s, y-52*s, x+92*s, y-30*s, 0.3, DARK))
    return b


def banner(x, y, s=1.0, kind="zhao"):
    """旗：杆、旗面；旐龟蛇、旄旄尾、旟鸟隼。"""
    b = [line(x, y, x, y-150*s, 0.45, DARK), line(x-10*s, y, x+10*s, y, 0.3, DARK)]
    if kind == "zhao":
        b += [p(f"M {x} {y-148*s} Q {x-34*s} {y-142*s} {x-40*s} {y-116*s} L {x-30*s} {y-122*s} L {x-20*s} {y-110*s} L {x-8*s} {y-120*s} L {x} {y-112*s} Z", 0.42, INK)]
    elif kind == "mao":
        b += [p(f"M {x} {y-146*s} Q {x-20*s} {y-140*s} {x-22*s} {y-108*s} L {x-12*s} {y-116*s} L {x-4*s} {y-104*s} L {x+2*s} {y-116*s} Z", 0.38, INK),
              p(f"M {x-18*s} {y-138*s} L {x-26*s} {y-126*s} L {x-16*s} {y-124*s}", 0.25, DARK)]
    else:
        b += [p(f"M {x} {y-148*s} L {x-38*s} {y-140*s} L {x-34*s} {y-112*s} L {x} {y-118*s} Z", 0.4, INK),
              p(f"M {x-26*s} {y-132*s} Q {x-14*s} {y-140*s} {x-6*s} {y-128*s}", 0.25, LIGHT)]
    return b


def mountain(x, y, s=1.0):
    return [p(f"M {x-80*s} {y} L {x-30*s} {y-92*s} L {x+6*s} {y-32*s} L {x+36*s} {y-112*s} L {x+82*s} {y} Z", 0.45, DARK),
            p(f"M {x+36*s} {y-112*s} L {x+52*s} {y-64*s} L {x+66*s} {y-92*s}", 0.28, LIGHT),
            p(f"M {x-30*s} {y-92*s} L {x-18*s} {y-52*s} L {x-6*s} {y-82*s}", 0.25, LIGHT)]


def pine(x, y, s=1.0):
    b = [line(x, y, x, y-150*s, 0.42, DARK)]
    for i in range(3):
        yy = y - 56*s - i*38*s
        b.append(p(f"M {x-52*s+i*8*s} {yy} L {x} {yy-34*s} L {x+52*s-i*8*s} {yy}", 0.35, INK))
        for j in range(5):
            b.append(line(x-40*s+j*18*s, yy-2*s, x-36*s+j*18*s, yy-12*s, 0.2, LIGHT))
    b.append(line(x-12*s, y, x-26*s, y+8*s, 0.25, DARK))
    b.append(line(x+12*s, y, x+26*s, y+8*s, 0.25, DARK))
    return b


def frond(x, y, s=1.0, kind="di"):
    """常棣花枝：枝、三花、五瓣、萼、蕊。"""
    b = [p(f"M {x-60*s} {y} Q {x-10*s} {y-24*s} {x+54*s} {y-8*s}", 0.38, DARK)]
    for i, (fx, fy) in enumerate(((x-42*s, y-22*s), (x-4*s, y-40*s), (x+38*s, y-22*s))):
        for k in range(5):
            a = -math.pi/2 + k*2*math.pi/5
            b.append(p(f"M {fx} {fy} Q {fx+20*s*math.cos(a-0.32)} {fy+20*s*math.sin(a-0.32)} {fx+18*s*math.cos(a)} {fy+18*s*math.sin(a)} Q {fx+14*s*math.cos(a+0.32)} {fy+14*s*math.sin(a+0.32)} {fx} {fy} Z", 0.26, LIGHT))
        for k in range(5):
            a = -math.pi/2 + k*2*math.pi/5
            b.append(line(fx, fy, fx+6*s*math.cos(a), fy+6*s*math.sin(a), 0.2, DARK))
        b.append(circ(fx, fy, 2.4*s, 0.25, RED))
        b.append(p(f"M {fx-8*s} {fy+9*s} L {fx} {fy+2*s} L {fx+8*s} {fy+9*s}", 0.22, DARK))
    return b


def dou(x, y, s=1.0):
    """豆：圈足、柄、盘、盖。"""
    return [p(f"M {x-32*s} {y-28*s} Q {x-36*s} {y-14*s} {x} {y-10*s} Q {x+36*s} {y-14*s} {x+32*s} {y-28*s} Z", 0.38, DARK),
            line(x-10*s, y-10*s, x-8*s, y+12*s, 0.35, DARK),
            line(x+10*s, y-10*s, x+8*s, y+12*s, 0.35, DARK),
            p(f"M {x-26*s} {y+12*s} Q {x} {y+4*s} {x+26*s} {y+12*s} L {x+22*s} {y+20*s} L {x-22*s} {y+20*s} Z", 0.35, DARK),
            p(f"M {x-26*s} {y-28*s} Q {x} {y-40*s} {x+26*s} {y-28*s}", 0.3, LIGHT)]


def bian(x, y, s=1.0):
    """笾：浅竹盘、圈足、编织线。"""
    return [p(f"M {x-38*s} {y-18*s} L {x+38*s} {y-18*s} L {x+28*s} {y+8*s} L {x-28*s} {y+8*s} Z", 0.38, DARK),
            p(f"M {x-30*s} {y+8*s} L {x+30*s} {y+8*s} L {x+22*s} {y+18*s} L {x-22*s} {y+18*s} Z", 0.3, DARK),
            line(x-34*s, y-12*s, x+34*s, y-12*s, 0.2, LIGHT),
            line(x-30*s, y-4*s, x+30*s, y-4*s, 0.2, LIGHT),
            line(x-26*s, y+3*s, x+26*s, y+3*s, 0.2, LIGHT)]


def sheng(x, y, s=1.0):
    """笙：葫芦座、竹管、簧。"""
    b = [p(f"M {x-20*s} {y} Q {x-30*s} {y+24*s} {x} {y+28*s} Q {x+30*s} {y+24*s} {x+20*s} {y} Z", 0.4, DARK)]
    for i in range(5):
        xx = x - 16*s + i*8*s
        b.append(line(xx, y, xx-2*s, y-70*s, 0.3, INK))
        b.append(line(xx-2*s, y-70*s, xx+2*s, y-72*s, 0.2, LIGHT))
    b.append(line(x-18*s, y-18*s, x+18*s, y-18*s, 0.3, LIGHT))
    return b


def basket(x, y, s=1.0):
    """筐：梯形、双提、编织线。"""
    return [p(f"M {x-34*s} {y-46*s} L {x+34*s} {y-46*s} L {x+26*s} {y+26*s} L {x-26*s} {y+26*s} Z", 0.4, DARK),
            p(f"M {x-30*s} {y-46*s} Q {x} {y-78*s} {x+30*s} {y-46*s}", 0.35, DARK),
            line(x-32*s, y-26*s, x+32*s, y-26*s, 0.22, LIGHT),
            line(x-30*s, y-6*s, x+30*s, y-6*s, 0.22, LIGHT),
            line(x-28*s, y+12*s, x+28*s, y+12*s, 0.22, LIGHT)]


def wine(x, y, s=1.0):
    """酒器：壶身、口、双耳、圈足。"""
    return [p(f"M {x-28*s} {y-96*s} Q {x-38*s} {y-44*s} {x-20*s} {y-10*s} L {x+20*s} {y-10*s} Q {x+38*s} {y-44*s} {x+28*s} {y-96*s} Z", 0.42, DARK),
            p(f"M {x-28*s} {y-96*s} Q {x} {y-108*s} {x+28*s} {y-96*s}", 0.32, LIGHT),
            p(f"M {x-28*s} {y-76*s} Q {x-44*s} {y-70*s} {x-40*s} {y-52*s}", 0.28, INK),
            p(f"M {x+28*s} {y-76*s} Q {x+44*s} {y-70*s} {x+40*s} {y-52*s}", 0.28, INK),
            line(x-16*s, y-10*s, x-18*s, y+2*s, 0.3, DARK),
            line(x+16*s, y-10*s, x+18*s, y+2*s, 0.3, DARK),
            line(x-24*s, y-4*s, x+24*s, y-4*s, 0.25, LIGHT)]


def sheep(x, y, s=1.0):
    """羊：身、头、耳、四足、尾，不画眼。"""
    return [p(f"M {x-38*s} {y-28*s} Q {x-34*s} {y-56*s} {x} {y-58*s} Q {x+34*s} {y-56*s} {x+38*s} {y-28*s} Q {x+34*s} {y-2*s} {x} {y} Q {x-34*s} {y-2*s} {x-38*s} {y-28*s} Z", 0.42, INK),
            circ(x+45*s, y-38*s, 12*s, 0.35, INK),
            p(f"M {x+52*s} {y-48*s} L {x+62*s} {y-58*s} L {x+62*s} {y-40*s}", 0.28, INK),
            p(f"M {x+40*s} {y-46*s} Q {x+34*s} {y-58*s} {x+44*s} {y-50*s}", 0.22, LIGHT),
            line(x-24*s, y, x-26*s, y+30*s, 0.3, INK), line(x+24*s, y, x+26*s, y+30*s, 0.3, INK),
            line(x-26*s, y+30*s, x-32*s, y+31*s, 0.2, INK), line(x+26*s, y+30*s, x+32*s, y+31*s, 0.2, INK),
            p(f"M {x-38*s} {y-36*s} Q {x-52*s} {y-40*s} {x-50*s} {y-24*s}", 0.25, INK)]


def stump(x, y, s=1.0):
    """伐木：树桩、年轮、斧。"""
    return [p(f"M {x-40*s} {y} L {x-34*s} {y-78*s} L {x+34*s} {y-78*s} L {x+40*s} {y} Z", 0.42, DARK),
            p(f"M {x-34*s} {y-78*s} Q {x} {y-88*s} {x+34*s} {y-78*s}", 0.3, LIGHT),
            circ(x, y-78*s, 12*s, 0.25, LIGHT),
            circ(x, y-78*s, 6*s, 0.2, LIGHT),
            line(x+40*s, y, x+48*s, y+2*s, 0.25, DARK)]


def wei(x, y, s=1.0, stage=0):
    """薇：野豌豆，三阶段：初生、柔、刚。"""
    h = 34 + stage*22
    b = [line(x, y, x, y-h*s, 0.3, DARK)]
    for i in range(3 if stage < 2 else 4):
        yy = y - (12 + i*12)*s
        b.append(p(f"M {x} {yy} Q {x-16*s} {yy-10*s} {x-24*s} {yy-2*s} Q {x-12*s} {yy+4*s} {x} {yy} Z", 0.25, LIGHT))
        b.append(p(f"M {x} {yy-4*s} Q {x+16*s} {yy-12*s} {x+24*s} {yy-4*s} Q {x+12*s} {yy+2*s} {x} {yy-4*s} Z", 0.25, LIGHT))
    if stage == 2:
        for i in range(2):
            b.append(p(f"M {x-8*s} {y-(h-8)*s} Q {x-14*s} {y-(h+4)*s} {x-4*s} {y-(h+2)*s} Z", 0.25, INK))
    return b


def willow(x, y, s=1.0):
    b = [line(x, y, x, y-130*s, 0.42, DARK)]
    for i in range(3):
        b.append(p(f"M {x} {y-100*s+i*10*s} Q {x-40*s-i*10*s} {y-116*s} {x-52*s-i*12*s} {y-60*s}", 0.3, DARK))
        b.append(p(f"M {x} {y-100*s+i*10*s} Q {x+40*s+i*10*s} {y-116*s} {x+52*s+i*12*s} {y-60*s}", 0.3, DARK))
    for i in range(8):
        xx = x - 46*s + i*13*s
        b.append(line(xx, y-108*s, xx-4*s, y-58*s, 0.2, LIGHT))
    return b


def snow(x, y, n=8):
    b = []
    for i in range(n):
        xx = x + (i % 4)*22 - 2
        yy = y - (i // 4)*18
        b.append(line(xx, yy, xx+4, yy+4, 0.2, LIGHT))
        b.append(line(xx+4, yy, xx, yy+4, 0.2, LIGHT))
    return b


def du(x, y, s=1.0):
    """孤杜：独干、三枝、叶、果。"""
    b = [p(f"M {x-8*s} {y} L {x-4*s} {y-120*s} L {x+4*s} {y-120*s} L {x+8*s} {y} Z", 0.4, DARK)]
    for i in range(3):
        b.append(p(f"M {x} {y-80*s-i*14*s} Q {x-38*s} {y-98*s-i*10*s} {x-54*s} {y-76*s-i*6*s}", 0.3, DARK))
        b.append(p(f"M {x} {y-80*s-i*14*s} Q {x+38*s} {y-98*s-i*10*s} {x+54*s} {y-76*s-i*6*s}", 0.3, DARK))
    for i in range(6):
        b.append(circ(x-38*s+ (i%3)*38*s, y-92*s-(i//3)*24*s, 3.2*s, 0.25, RED))
    return b


def turtle(x, y, s=1.0):
    """龟甲：背甲、腹甲、头、四足、甲纹。"""
    b = [p(f"M {x-34*s} {y-12*s} Q {x-40*s} {y-42*s} {x} {y-48*s} Q {x+40*s} {y-42*s} {x+34*s} {y-12*s} Q {x} {y+4*s} {x-34*s} {y-12*s} Z", 0.4, DARK),
         circ(x+42*s, y-24*s, 9*s, 0.3, DARK),
         line(x-34*s, y-24*s, x+34*s, y-24*s, 0.22, LIGHT),
         line(x, y-48*s, x, y+2*s, 0.22, LIGHT),
         line(x-20*s, y-44*s, x-24*s, y-2*s, 0.2, LIGHT),
         line(x+20*s, y-44*s, x+24*s, y-2*s, 0.2, LIGHT)]
    for dx in (-28, 24):
        b.append(line(x+dx*s, y-6*s, x+dx*s-6*s, y+10*s, 0.25, DARK))
    return b


def yarrow(x, y, s=1.0):
    b = []
    for i in range(3):
        xx = x - 18 + i*18
        b.append(line(xx, y, xx-2, y-96*s, 0.28, DARK))
        b.append(p(f"M {xx-2} {y-96*s} Q {xx-14} {y-106*s} {xx-20} {y-96*s}", 0.22, LIGHT))
        b.append(p(f"M {xx-2} {y-96*s} Q {xx+10} {y-108*s} {xx+16} {y-96*s}", 0.22, LIGHT))
    return b


def trap(x, y, s=1.0):
    """罶：曲梁鱼笱，竹编，开口。"""
    b = [p(f"M {x-46*s} {y-26*s} L {x+44*s} {y-26*s} L {x+30*s} {y+46*s} L {x-30*s} {y+46*s} Z", 0.42, DARK),
         p(f"M {x-46*s} {y-26*s} Q {x-54*s} {y-52*s} {x-36*s} {y-56*s} L {x-18*s} {y-30*s}", 0.3, DARK),
         p(f"M {x+44*s} {y-26*s} Q {x+54*s} {y-52*s} {x+36*s} {y-56*s} L {x+18*s} {y-30*s}", 0.3, DARK)]
    for i in range(4):
        b.append(line(x-40*s+i*14*s, y-22*s, x-26*s+i*12*s, y+42*s, 0.22, LIGHT))
    for i in range(3):
        b.append(line(x-42*s, y-6*s+i*14*s, x+42*s, y-6*s+i*14*s, 0.2, LIGHT))
    return b


def city(x, y, s=1.0):
    b = [p(f"M {x-60*s} {y} L {x-60*s} {y-56*s} L {x+60*s} {y-56*s} L {x+60*s} {y} Z", 0.42, DARK)]
    for i in range(5):
        b.append(rect(x-56*s+i*24*s, y-70*s, 12*s, 16*s, 0.28, DARK))
    b.append(p(f"M {x-18*s} {y} L {x-18*s} {y-34*s} Q {x} {y-50*s} {x+18*s} {y-34*s} L {x+18*s} {y} Z", 0.32, LIGHT))
    b.append(line(x-60*s, y-10*s, x+60*s, y-10*s, 0.22, LIGHT))
    return b


def f161a():
    s = head("鹿鸣　鹿鸣食苹", "鹿鸣而友至，酒行而道明", "一百六十一")
    s += deer(170, 400, 1.2)
    for i in range(4):
        s.append(p(f"M {270+i*18} 408 Q {278+i*18} 380 {286+i*18} 408", 0.28, DARK))
        s.append(p(f"M {278+i*18} 408 Q {284+i*18} 390 {292+i*18} 404", 0.22, LIGHT))
    s.append(t(300, 438, "食野之苹", 8.2, DARK, "middle"))
    s += sheng(470, 392, 1.1)
    s.append(t(470, 438, "鼓瑟吹笙", 8.2, DARK, "middle"))
    s += basket(620, 392, 1.1)
    s.append(t(620, 438, "承筐是将", 8.2, DARK, "middle"))
    s += foot("图一 · 鹿鸣　鹿鸣食苹，瑟笙承筐", "呦呦鹿鸣，食野之苹。")
    return "".join(s)


def f161b():
    return bfig("鹿鸣　示我周行", "宴饮是形，周行是神",
                [("鹿鸣", "鹿得苹而鸣，呼其同类；人得酒而乐，敬其嘉宾", "兴"),
                 ("德音", "德音孔昭；视民不恌，君子是则是效", "德"),
                 ("周行", "承筐是将；人之好我，示我周行", "道")],
                "鹿鸣而友至，酒行而道明；示我周行，宴不徒宴。", "一百六十一")


def f162a():
    s = head("四牡　周道倭迟", "路可倭迟，心不可不归", "一百六十二")
    for i, x in enumerate((110, 230, 350, 470)):
        s += horse(x, 400, 0.86)
    s.append(p("M 50 462 Q 170 452 290 458", 0.3, LIGHT)); s.append(p("M 310 458 Q 430 450 550 458", 0.3, LIGHT)); s.append(p("M 570 458 Q 650 452 720 456", 0.3, LIGHT))
    s.append(t(300, 440, "四牡騑騑", 8.2, DARK, "middle"))
    s += bird(650, 330, 1.3)
    s.append(p("M 610 410 L 610 340", 0.35, DARK))
    s.append(p("M 610 370 Q 650 350 700 360", 0.3, DARK))
    s.append(t(660, 438, "鵻集苞栩", 8.2, DARK, "middle"))
    s += foot("图一 · 四牡　四牡騑騑，鵻集苞栩", "四牡騑騑，周道倭迟。")
    return "".join(s)


def f162b():
    return bfig("四牡　作歌将母", "忠孝同在一身",
                [("騑騑", "四牡行不止，周道回远；岂不怀归", "行"),
                 ("靡盬", "王事无止息；不遑启处，不遑将父", "劳"),
                 ("将母", "驾彼四骆，作歌以告；将母来谂", "告")],
                "路可倭迟，心不可不归；王事靡盬，作歌以告母。", "一百六十二")


def f163a():
    s = head("皇皇者华　原隰光华", "华可皇皇，心不可满", "一百六十三")
    s += frond(150, 390, 1.25)
    s.append(t(150, 438, "皇皇者华", 8.2, DARK, "middle"))
    s += horse(430, 400, 1.0)
    for i in range(6):
        s.append(line(472, 396+i*2, 610, 316+i*8, 0.25, DARK))
    s.append(t(500, 438, "六辔如濡", 8.2, DARK, "middle"))
    s.append(p("M 80 470 Q 340 450 700 466", 0.28, LIGHT))
    s += foot("图一 · 皇皇者华　原隰光华，六辔在途", "皇皇者华，于彼原隰。")
    return "".join(s)


def f163b():
    return bfig("皇皇者华　四问有序", "光华在外，靡及在内",
                [("原隰", "花照原隰；征夫众多，常恐不及", "往"),
                 ("六辔", "驹、骐、骆、骃；辔愈熟，行愈远", "行"),
                 ("四问", "诹其端、谋其体、度其宜、询其疑", "问")],
                "华可皇皇，心不可满；六辔在手，四问在途。", "一百六十三")


def f164a():
    s = head("常棣　花萼相依", "花有萼，人有兄", "一百六十四")
    s += frond(160, 400, 1.35)
    s.append(t(160, 442, "常棣之华", 8.2, DARK, "middle"))
    s += bird(390, 390, 1.5)
    s.append(p("M 320 436 Q 390 414 460 436", 0.35, DARK))
    s.append(t(390, 456, "脊令在原", 7.8, DARK, "middle"))
    s += bian(590, 360, 1.0)
    s += dou(670, 400, 1.0)
    s.append(t(630, 442, "傧尔笾豆", 7.8, DARK, "middle"))
    s += foot("图一 · 常棣　花萼相依，脊令急难", "常棣之华，鄂不韡韡。")
    return "".join(s)


def f164b():
    return bfig("常棣　难则同，安则思", "兄弟之亲在难中见",
                [("死丧", "死丧之威，兄弟孔怀；原隰裒矣，兄弟求矣", "难"),
                 ("急难", "脊令在原，兄弟急难；良朋永叹，不能代", "救"),
                 ("既翕", "丧乱既平，反不如友生；是究是图", "警")],
                "花有萼，人有兄；难则同，安则思。", "一百六十四")


def f165a():
    s = head("伐木　鸟鸣求友", "木可伐，友不可失", "一百六十五")
    s += stump(150, 420, 1.2)
    s += axe(215, 410, "fu", 1.0)
    s.append(t(180, 456, "伐木丁丁", 8.0, DARK, "middle"))
    s += bird(390, 320, 1.4)
    s.append(t(390, 438, "鸟鸣嘤嘤", 8.0, DARK, "middle"))
    s += wine(550, 410, 1.1)
    s += sheep(660, 400, 1.0)
    s.append(t(610, 456, "酾酒有藇", 8.0, DARK, "middle"))
    s += foot("图一 · 伐木　伐木丁丁，鸟鸣求友", "伐木丁丁，鸟鸣嘤嘤。")
    return "".join(s)


def f165b():
    return bfig("伐木　友不可失", "失德不在大，常在一饭",
                [("嘤鸣", "鸟出幽谷，迁于乔木；犹求友声", "求"),
                 ("酾酒", "酾酒有藇，肥羜八簋；宁适不来，微我弗顾", "厚"),
                 ("乾餱", "民之失德，乾餱以愆；薄食可以绝友", "戒")],
                "木可伐，友不可失；乾餱虽薄，愆在其中。", "一百六十五")


def f166a():
    s = head("天保　山阜川至", "天可保，福不可骄", "一百六十六")
    s += mountain(150, 410, 1.2)
    s.append(t(150, 446, "如山如阜", 8.0, DARK, "middle"))
    # 川
    for i in range(3):
        s.append(p(f"M 300 {360+i*20} Q 360 {346+i*20} 420 {360+i*20} Q 480 {374+i*20} 540 {360+i*20}", 0.28, LIGHT))
    s.append(t(420, 446, "如川之方至", 8.0, DARK, "middle"))
    s += pine(650, 410, 1.1)
    s.append(t(650, 446, "如松柏之茂", 8.0, DARK, "middle"))
    # 月日
    s.append(circ(590, 200, 14, 0.3, DARK))
    s.append(circ(650, 180, 12, 0.3, RED))
    s.append(t(620, 240, "如月之恒，如日之升", 7.6, DARK, "middle"))
    s += foot("图一 · 天保　山阜川至，松柏南山", "天保定尔，以莫不兴。")
    return "".join(s)


def f166b():
    return bfig("天保　民质日用", "福不在奇，在日用",
                [("天保", "亦孔之固；单厚多益，何福不除", "基"),
                 ("孝享", "吉蠲为饎，禴祠烝尝；万寿无疆", "祭"),
                 ("日用", "民之质矣，日用饮食；群黎百姓", "实")],
                "天可保，福不可骄；松柏之茂，在日用饮食。", "一百六十六")


def f167a():
    s = head("采薇　薇三态", "薇可采，归不可期", "一百六十七")
    for i, x in enumerate((100, 170, 240)):
        s += wei(x, 420, 1.0, i)
    s.append(t(170, 456, "薇亦作、柔、刚", 7.8, DARK, "middle"))
    s += cart(370, 390, 1.0)
    s.append(t(370, 456, "戎车既驾", 7.8, DARK, "middle"))
    s += willow(620, 410, 1.0)
    s += snow(560, 260, 8)
    s.append(t(610, 456, "杨柳雨雪", 7.8, DARK, "middle"))
    s += foot("图一 · 采薇　薇三态，戎车四牡", "采薇采薇，薇亦作止。")
    return "".join(s)


def f167b():
    return bfig("采薇　莫知我哀", "以壮写悲，以缓收壮",
                [("靡家", "靡室靡家，玁狁之故；不遑启居", "戍"),
                 ("三捷", "戎车四牡，象弭鱼服；一月三捷", "战"),
                 ("来思", "杨柳依依，雨雪霏霏；莫知我哀", "归")],
                "薇可采，归不可期；杨柳雨雪，一身之哀。", "一百六十七")


def f168a():
    s = head("出车　建旗城方", "车可出，心不可骄", "一百六十八")
    s += cart(140, 400, 1.0)
    s.append(t(140, 446, "我出我车", 7.8, DARK, "middle"))
    s += banner(340, 430, 1.0, "zhao")
    s += banner(430, 430, 1.0, "mao")
    s += banner(520, 430, 1.0, "yu")
    s.append(t(430, 456, "旐 · 旄 · 旟", 7.8, DARK, "middle"))
    s += city(660, 420, 1.0)
    s.append(t(660, 456, "城彼朔方", 7.8, DARK, "middle"))
    s += foot("图一 · 出车　出车建旗，城彼朔方", "我出我车，于彼牧矣。")
    return "".join(s)


def f168b():
    return bfig("出车　玁狁于夷", "旗正而心悄悄",
                [("出车", "于牧于郊；设旐建旄，旗旐央央", "行"),
                 ("简书", "王事多难，不遑启居；畏此简书", "戒"),
                 ("于夷", "春日还归，执讯获丑；玁狁于夷", "平")],
                "车可出，心不可骄；旗可扬，简书不可违。", "一百六十八")


def f169a():
    s = head("杕杜　孤棠其实", "树可独，人不可独", "一百六十九")
    s += du(160, 430, 1.2)
    s.append(t(160, 466, "有杕之杜", 7.8, DARK, "middle"))
    s += cart(390, 400, 1.0)
    s.append(t(390, 466, "檀车幝幝", 7.8, DARK, "middle"))
    s += turtle(600, 390, 1.0)
    s += yarrow(690, 420, 1.0)
    s.append(t(640, 466, "卜筮偕止", 7.8, DARK, "middle"))
    s += foot("图一 · 杕杜　孤棠其实，檀车四牡", "有杕之杜，有睆其实。")
    return "".join(s)


def f169b():
    return bfig("杕杜　征夫迩止", "卜可言近，归不可必",
                [("继日", "王事靡盬，继嗣我日；日月阳止", "久"),
                 ("忧亲", "陟彼北山，言采其杞；忧我父母", "望"),
                 ("卜筮", "期逝不至；卜筮偕止，会言近止", "近")],
                "树可独，人不可独；卜可言近，归不可必。", "一百六十九")


def f170a():
    s = head("鱼丽　鱼丽于罶", "鱼可丽，酒可旨", "一百七十")
    s += trap(170, 380, 1.3)
    s.append(t(170, 446, "鱼丽于罶", 8.0, DARK, "middle"))
    for i in range(3):
        s += fish(300+i*55, 330+i*26, 0.9)
    for i in range(3):
        s += fish(470+i*50, 390-i*18, 0.8)
    s.append(t(430, 456, "鲿 · 鲨 · 鲂 · 鳢 · 鰋 · 鲤", 7.8, DARK, "middle"))
    s += wine(670, 420, 1.0)
    s.append(t(670, 456, "君子有酒", 8.0, DARK, "middle"))
    s += foot("图一 · 鱼丽　鱼丽于罶，六鱼旨酒", "鱼丽于罶，鲿鲨。")
    return "".join(s)


def f170b():
    return bfig("鱼丽　维其时矣", "物盛而时，礼乃备",
                [("多矣", "鱼入罶，酒旨多；盛而不嘉，则暴物", "盛"),
                 ("旨矣", "鲂鳢鰋鲤；美而不偕，则偏", "美"),
                 ("有矣", "物有而时；足而不时，则竭", "时")],
                "鱼可丽，酒可旨；物盛而时，礼乃备。", "一百七十")


FIGS = {
    "sj161a-lu-ming": f161a, "sj161b-zhou-xing": f161b,
    "sj162a-si-mu": f162a, "sj162b-jiang-mu": f162b,
    "sj163a-huang-hua": f163a, "sj163b-zi-zou": f163b,
    "sj164a-chang-di": f164a, "sj164b-mo-ru-xiong-di": f164b,
    "sj165a-fa-mu": f165a, "sj165b-you-sheng": f165b,
    "sj166a-tian-bao": f166a, "sj166b-song-bai": f166b,
    "sj167a-cai-wei": f167a, "sj167b-mo-zhi-wo-ai": f167b,
    "sj168a-chu-che": f168a, "sj168b-nan-zhong": f168b,
    "sj169a-di-du": f169a, "sj169b-bu-shi": f169b,
    "sj170a-yu-li": f170a, "sj170b-wei-qi-shi": f170b,
}


def main():
    os.makedirs(OUT, exist_ok=True)
    for k, fn in FIGS.items():
        svg = fn()
        svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 540" width="760" height="540">' + svg + '</svg>'
        open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8").write(svg)
        print(k)


if __name__ == "__main__":
    main()
