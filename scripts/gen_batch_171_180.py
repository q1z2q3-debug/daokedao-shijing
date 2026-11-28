# -*- coding: utf-8 -*-
"""SJ171–SJ180 小雅南有嘉鱼之什十篇二十图：图一名物，图二义理。760×540，白描不填面。"""
import os, sys, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from gen_batch_123_125 import (t, p, line, circ, rect, person, foot,
                               PAPER, INK, DARK, LIGHT, RED, SEAL, GOLD,
                               ZPAPER, ZINK, ZMID, LINE_L)

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
            t(38, 62, "小 雅 · 南有嘉鱼之什", 9.0, RED, ls=1.0),
            t(380, 72, title, 24.5, ink, "middle", "bold", 1.4),
            t(722, 62, "诗三百五篇 · 之%s" % zh_no, 8.6, mid, "end", ls=1),
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


def panel(x, y, w, h):
    return [rect(x, y, w, h, 0.35, LINE_L),
            line(x+10, y+10, x+18, y+10, 0.22, GOLD),
            line(x+10, y+10, x+10, y+18, 0.22, GOLD)]


def fish(x, y, s=1.0, color=INK):
    return [p(f"M {x-24*s} {y} Q {x} {y-11*s} {x+24*s} {y} Q {x} {y+11*s} {x-24*s} {y} Z", 0.34, color),
            p(f"M {x-24*s} {y} L {x-35*s} {y-9*s} L {x-33*s} {y} L {x-35*s} {y+9*s} Z", 0.26, color),
            circ(x+11*s, y-2*s, 1.6*s, 0.18, color),
            p(f"M {x-8*s} {y-7*s} Q {x} {y} {x-8*s} {y+7*s}", 0.18, LIGHT)]


def nettrap(x, y, s=1.0):
    """罩/汕：竹编鱼器，开口、束腰、编织线。"""
    b = [p(f"M {x-42*s} {y-38*s} L {x-28*s} {y+38*s} L {x+28*s} {y+38*s} L {x+42*s} {y-38*s} Z", 0.36, DARK),
         p(f"M {x-42*s} {y-38*s} Q {x} {y-52*s} {x+42*s} {y-38*s}", 0.28, DARK),
         p(f"M {x-20*s} {y-22*s} Q {x} {y-32*s} {x+20*s} {y-22*s}", 0.22, LIGHT)]
    for i in range(4):
        b.append(line(x-36*s+i*20*s, y-32*s, x-22*s+i*14*s, y+34*s, 0.18, LIGHT))
    for i in range(3):
        b.append(line(x-38*s, y-12*s+i*16*s, x+38*s, y-12*s+i*16*s, 0.18, LIGHT))
    b.append(p(f"M {x} {y-44*s} L {x} {y-60*s}", 0.24, DARK))
    return b


def gourd(x, y, s=1.0):
    return [circ(x, y+18*s, 13*s, 0.28, DARK),
            circ(x, y-2*s, 9*s, 0.26, DARK),
            p(f"M {x} {y+5*s} Q {x+4*s} {y+10*s} {x} {y+14*s}", 0.18, LIGHT),
            p(f"M {x} {y-11*s} L {x-2*s} {y-24*s}", 0.22, DARK)]


def bent_tree(x, y, s=1.0):
    b = [p(f"M {x-8*s} {y} L {x-5*s} {y-90*s} Q {x-2*s} {y-110*s} {x+18*s} {y-116*s} Q {x+38*s} {y-118*s} {x+42*s} {y-104*s}", 0.4, DARK),
         p(f"M {x-4*s} {y-86*s} Q {x-28*s} {y-104*s} {x-38*s} {y-98*s}", 0.26, DARK),
         p(f"M {x+6*s} {y-104*s} Q {x+8*s} {y-124*s} {x+20*s} {y-132*s}", 0.24, DARK)]
    for i in range(5):
        b.append(p(f"M {x+18*s+i*4*s} {y-112*s} Q {x+22*s+i*4*s} {y-120*s} {x+28*s+i*4*s} {y-116*s}", 0.18, LIGHT))
    return b


def bird(x, y, s=1.0):
    return [p(f"M {x-18*s} {y-6*s} Q {x-4*s} {y-21*s} {x+12*s} {y-12*s} Q {x+20*s} {y-5*s} {x+11*s} {y+5*s} Q {x-6*s} {y+7*s} {x-18*s} {y-6*s} Z", 0.32, INK),
            circ(x+15*s, y-17*s, 8*s, 0.28, INK),
            p(f"M {x+22*s} {y-18*s} L {x+33*s} {y-16*s} L {x+23*s} {y-12*s}", 0.22, INK),
            p(f"M {x-18*s} {y-8*s} L {x-34*s} {y-18*s} L {x-30*s} {y-6*s} L {x-36*s} {y-1*s}", 0.22, INK),
            line(x, y+4*s, x, y+16*s, 0.2, INK),
            line(x, y+16*s, x-5*s, y+17*s, 0.16, INK),
            line(x, y+16*s, x+5*s, y+17*s, 0.16, INK)]


def mountain(x, y, s=1.0):
    return [p(f"M {x-85*s} {y} L {x-30*s} {y-80*s} L {x+2*s} {y-34*s} L {x+34*s} {y-96*s} L {x+84*s} {y} Z", 0.38, DARK),
            p(f"M {x-30*s} {y-80*s} L {x-18*s} {y-42*s} L {x-6*s} {y-70*s}", 0.2, LIGHT),
            p(f"M {x+34*s} {y-96*s} L {x+48*s} {y-56*s} L {x+62*s} {y-80*s}", 0.2, LIGHT)]


def grass(x, y, s=1.0, blades=5):
    b = []
    for i in range(blades):
        dx = -18*s + i*9*s
        h = (34 + (i % 3)*8)*s
        b.append(p(f"M {x+dx} {y} Q {x+dx-5*s} {y-h*0.6} {x+dx-9*s} {y-h}", 0.26, DARK))
        b.append(p(f"M {x+dx} {y} Q {x+dx+4*s} {y-h*0.5} {x+dx+7*s} {y-h*0.9}", 0.2, LIGHT))
    return b


def plant(x, y, s=1.0, leaves=3, fruit=False, color=INK):
    b = [line(x, y, x, y-72*s, 0.32, DARK)]
    for i in range(leaves):
        yy = y - (12 + i*14)*s
        b.append(p(f"M {x} {yy} Q {x-20*s} {yy-14*s} {x-30*s} {yy-4*s} Q {x-16*s} {yy+4*s} {x} {yy} Z", 0.24, color))
        b.append(p(f"M {x} {yy-3*s} Q {x+18*s} {yy-16*s} {x+28*s} {yy-6*s} Q {x+16*s} {yy+1*s} {x} {yy-3*s} Z", 0.24, color))
    if fruit:
        for i in range(3):
            b.append(circ(x-12*s+i*12*s, y-78*s, 3*s, 0.2, RED))
    return b


def herb(x, y, s=1.0, blades=7, flower=False):
    """草：弧形叶、叶鞘、穗或小花。"""
    b = []
    for i in range(blades):
        dx = (-24 + i*8)*s
        h = (54 + (i % 3)*10)*s
        b.append(p(f"M {x+dx} {y} Q {x+dx-6*s} {y-h*0.55} {x+dx-12*s} {y-h}", 0.28, DARK))
        b.append(p(f"M {x+dx-2*s} {y-h*0.45} Q {x+dx-12*s} {y-h*0.55} {x+dx-16*s} {y-h*0.35}", 0.2, LIGHT))
        b.append(p(f"M {x+dx+2*s} {y-h*0.55} Q {x+dx+10*s} {y-h*0.62} {x+dx+13*s} {y-h*0.42}", 0.2, LIGHT))
    if flower:
        for i in range(3):
            fx = x - 14*s + i*14*s
            fy = y - 62*s - (i % 2)*8*s
            b.append(line(x, y-20*s, fx, fy, 0.18, DARK))
            b.append(circ(fx, fy, 3.2*s, 0.2, DARK))
            for k in range(3):
                b.append(line(fx, fy, fx-4*s+k*4*s, fy-5*s, 0.15, LIGHT))
    return b


def tree(x, y, s=1.0, fruit=False):
    """树：主干、三枝、团冠、果点。"""
    b = [p(f"M {x-6*s} {y} L {x-3*s} {y-54*s} L {x+3*s} {y-54*s} L {x+6*s} {y} Z", 0.4, DARK)]
    for i in range(3):
        b.append(p(f"M {x} {y-44*s-i*10*s} Q {x-24*s} {y-56*s-i*8*s} {x-34*s} {y-38*s-i*8*s}", 0.26, DARK))
        b.append(p(f"M {x} {y-44*s-i*10*s} Q {x+24*s} {y-56*s-i*8*s} {x+34*s} {y-38*s-i*8*s}", 0.26, DARK))
    for i in range(5):
        b.append(p(f"M {x-30*s+i*15*s} {y-48*s} Q {x-20*s+i*10*s} {y-78*s} {x-4*s+i*8*s} {y-50*s}", 0.22, LIGHT))
    if fruit:
        for i in range(4):
            b.append(circ(x-24*s+i*16*s, y-56*s-(i%2)*14*s, 3.0*s, 0.2, RED))
    return b


def eplant(x, y, s=1.0):
    """莪：萝蒿，羽状叶丛，顶生小白花。"""
    b = []
    for i in range(5):
        dx = (-18 + i*9)*s
        b.append(p(f"M {x+dx} {y} Q {x+dx-10*s} {y-26*s} {x+dx-18*s} {y-54*s}", 0.26, DARK))
        for k in range(2):
            yy = y - (12+k*12)*s
            b.append(p(f"M {x+dx-2*s} {yy} Q {x+dx-14*s} {yy-4*s} {x+dx-20*s} {yy+2*s}", 0.18, LIGHT))
    for i in range(3):
        fx = x - 12*s + i*12*s
        b.append(line(x, y-18*s, fx, y-64*s, 0.18, DARK))
        b.append(circ(fx, y-64*s, 2.8*s, 0.2, DARK))
    return b


def dew(x, y, n=3, color=INK):
    b = []
    for i in range(n):
        b.append(circ(x + (i % 2)*12, y - (i//2)*10, 2.8, 0.22, color))
        b.append(p(f"M {x+(i%2)*12} {y-(i//2)*10+3} Q {x+(i%2)*12} {y-(i//2)*10+7} {x+(i%2)*12-2} {y-(i//2)*10+8}", 0.16, LIGHT))
    return b


def wine(x, y, s=1.0):
    return [p(f"M {x-20*s} {y-54*s} Q {x-26*s} {y-26*s} {x-15*s} {y-6*s} L {x+15*s} {y-6*s} Q {x+26*s} {y-26*s} {x+20*s} {y-54*s} Z", 0.34, DARK),
            p(f"M {x-20*s} {y-54*s} Q {x} {y-62*s} {x+20*s} {y-54*s}", 0.26, LIGHT),
            p(f"M {x-20*s} {y-44*s} Q {x-32*s} {y-38*s} {x-28*s} {y-26*s}", 0.22, DARK),
            p(f"M {x+20*s} {y-44*s} Q {x+32*s} {y-38*s} {x+28*s} {y-26*s}", 0.22, DARK),
            line(x-10*s, y-6*s, x-12*s, y+4*s, 0.24, DARK),
            line(x+10*s, y-6*s, x+12*s, y+4*s, 0.24, DARK),
            line(x-16*s, y-2*s, x+16*s, y-2*s, 0.2, LIGHT)]


def bow(x, y, s=1.0, color=RED):
    return [p(f"M {x-48*s} {y-46*s} Q {x-12*s} {y} {x-48*s} {y+46*s}", 0.38, color),
            line(x-48*s, y-46*s, x-48*s, y+46*s, 0.22, DARK),
            line(x-46*s, y, x+30*s, y, 0.3, DARK),
            p(f"M {x+30*s} {y} L {x+22*s} {y-5*s} L {x+22*s} {y+5*s} Z", 0.22, DARK)]


def drum(x, y, s=1.0):
    return [p(f"M {x-34*s} {y-28*s} Q {x} {y-44*s} {x+34*s} {y-28*s} L {x+34*s} {y+26*s} Q {x} {y+42*s} {x-34*s} {y+26*s} Z", 0.36, DARK),
            line(x-34*s, y-10*s, x+34*s, y-10*s, 0.18, LIGHT),
            line(x-34*s, y+10*s, x+34*s, y+10*s, 0.18, LIGHT),
            line(x-34*s, y+26*s, x-48*s, y+38*s, 0.26, DARK),
            line(x+34*s, y+26*s, x+48*s, y+38*s, 0.26, DARK)]


def bell(x, y, s=1.0):
    return [p(f"M {x-18*s} {y-36*s} Q {x-26*s} {y-6*s} {x-24*s} {y+18*s} L {x+24*s} {y+18*s} Q {x+26*s} {y-6*s} {x+18*s} {y-36*s} Z", 0.32, DARK),
            p(f"M {x-18*s} {y-36*s} Q {x} {y-46*s} {x+18*s} {y-36*s}", 0.24, LIGHT),
            p(f"M {x-8*s} {y+18*s} L {x-10*s} {y+26*s} L {x+10*s} {y+26*s} L {x+8*s} {y+18*s}", 0.24, DARK),
            line(x, y+26*s, x, y+34*s, 0.22, DARK)]


def ride(x, y, s=1.0, kind="zhao"):
    b = [circ(x-28*s, y, 20*s, 0.34, DARK), circ(x+28*s, y, 20*s, 0.34, DARK)]
    for cx in (x-28*s, x+28*s):
        b += [line(cx, y, cx, y-20*s, 0.2, LIGHT), line(cx, y, cx, y+20*s, 0.2, LIGHT),
              line(cx-20*s, y, cx+20*s, y, 0.2, LIGHT), line(cx-14*s, y-14*s, cx+14*s, y+14*s, 0.16, LIGHT)]
    b.append(rect(x-38*s, y-50*s, 76*s, 36*s, 0.34, DARK))
    b.append(line(x-38*s, y-32*s, x+38*s, y-32*s, 0.2, LIGHT))
    b.append(line(x+38*s, y-36*s, x+76*s, y-48*s, 0.26, DARK))
    return b


def horse_head(x, y, s=1.0):
    b = [p(f"M {x-14*s} {y+54*s} L {x-20*s} {y+8*s} L {x-14*s} {y-10*s} L {x+4*s} {y-16*s} L {x+30*s} {y-12*s} L {x+46*s} {y+2*s} Q {x+50*s} {y+7*s} {x+44*s} {y+13*s} L {x+36*s} {y+14*s} L {x+4*s} {y+8*s} L {x-2*s} {y+16*s} L {x+2*s} {y+54*s} Z", 0.34, INK),
         p(f"M {x-14*s} {y-10*s} L {x-18*s} {y-28*s} L {x-6*s} {y-12*s}", 0.22, INK),
         p(f"M {x-4*s} {y-12*s} L {x-2*s} {y-30*s} L {x+5*s} {y-14*s}", 0.22, INK),
         line(x+44*s, y+5*s, x+47*s, y+10*s, 0.18, LIGHT)]
    for i in range(4):
        b.append(line(x-16*s+i*2*s, y+40*s-i*8*s, x-22*s+i*2*s, y+44*s-i*8*s, 0.16, LIGHT))
    return b


def flag(x, y, s=1.0, kind="zhao"):
    b = [line(x, y, x, y-126*s, 0.36, DARK), line(x-8*s, y, x+8*s, y, 0.24, DARK)]
    if kind == "zhao":
        b += [p(f"M {x} {y-124*s} Q {x-30*s} {y-116*s} {x-34*s} {y-94*s} L {x-24*s} {y-100*s} L {x-14*s} {y-90*s} L {x-4*s} {y-100*s} L {x} {y-92*s} Z", 0.34, INK)]
    elif kind == "mao":
        b += [p(f"M {x} {y-124*s} Q {x-18*s} {y-118*s} {x-20*s} {y-90*s} L {x-10*s} {y-98*s} L {x-2*s} {y-88*s} L {x+4*s} {y-98*s} Z", 0.32, INK)]
        for i in range(3):
            b.append(line(x-16*s+i*2*s, y-118*s, x-22*s+i*4*s, y+(-104+i*3)*s, 0.18, DARK))
    else:
        b += [p(f"M {x} {y-124*s} L {x-34*s} {y-116*s} L {x-30*s} {y-92*s} L {x} {y-98*s} Z", 0.34, INK),
              p(f"M {x-22*s} {y-110*s} Q {x-12*s} {y-118*s} {x-5*s} {y-108*s}", 0.2, LIGHT)]
    return b


def falcon(x, y, s=1.0):
    return [p(f"M {x-26*s} {y} Q {x-8*s} {y-18*s} {x+18*s} {y-10*s} Q {x+34*s} {y-2*s} {x+20*s} {y+8*s} L {x-12*s} {y+10*s} Z", 0.32, INK),
            p(f"M {x-6*s} {y-4*s} Q {x+2*s} {y-24*s} {x+20*s} {y-34*s} Q {x+16*s} {y-12*s} {x+12*s} {y-6*s}", 0.26, DARK),
            p(f"M {x-4*s} {y+2*s} Q {x+8*s} {y+18*s} {x+28*s} {y+30*s} Q {x+12*s} {y+30*s} {x-6*s} {y+18*s}", 0.26, DARK),
            p(f"M {x-24*s} {y+2*s} L {x-44*s} {y-6*s} L {x-38*s} {y+8*s} L {x-46*s} {y+12*s}", 0.22, INK),
            p(f"M {x+18*s} {y-8*s} L {x+34*s} {y-12*s} L {x+26*s} {y-4*s}", 0.18, INK)]


def deer(x, y, s=1.0):
    b = [p(f"M {x-38*s} {y-18*s} Q {x-22*s} {y-38*s} {x+6*s} {y-34*s} Q {x+28*s} {y-32*s} {x+34*s} {y-18*s} L {x+30*s} {y+2*s} Q {x+2*s} {y+10*s} {x-24*s} {y+4*s} Z", 0.32, INK),
         p(f"M {x+30*s} {y-22*s} Q {x+38*s} {y-48*s} {x+46*s} {y-62*s} L {x+56*s} {y-64*s} Q {x+48*s} {y-42*s} {x+38*s} {y-18*s} Z", 0.3, INK),
         p(f"M {x+52*s} {y-66*s} L {x+68*s} {y-62*s} Q {x+72*s} {y-58*s} {x+66*s} {y-54*s} L {x+54*s} {y-58*s} Z", 0.24, INK),
         p(f"M {x+56*s} {y-68*s} L {x+58*s} {y-88*s} L {x+50*s} {y-80*s}", 0.2, INK),
         p(f"M {x+62*s} {y-68*s} L {x+70*s} {y-92*s} L {x+76*s} {y-86*s}", 0.2, INK)]
    for dx in (18, 2, -18, -30):
        b.append(line(x+dx*s, y+2*s, x+dx*s-2*s, y+38*s, 0.22, INK))
        b.append(line(x+dx*s-2*s, y+38*s, x+dx*s-6*s, y+39*s, 0.16, INK))
    b.append(p(f"M {x-38*s} {y-14*s} Q {x-48*s} {y-20*s} {x-46*s} {y-8*s}", 0.18, INK))
    return b


def sun(x, y, r=18):
    b = [circ(x, y, r, 0.3, RED)]
    for i in range(8):
        a = i*math.pi/4
        b.append(line(x+ (r+4)*math.cos(a), y+(r+4)*math.sin(a),
                      x+(r+13)*math.cos(a), y+(r+13)*math.sin(a), 0.22, RED))
    return b


def f171a():
    s = head("南有嘉鱼　嘉鱼罩汕", "鱼可取，贤不可失", "一百七十一")
    s += panel(54, 150, 210, 270)
    s += nettrap(150, 320, 1.0)
    s += fish(120, 230, 0.7); s += fish(180, 250, 0.7)
    s.append(t(150, 408, "罩 · 汕", 8.2, DARK, "middle"))
    s += panel(274, 150, 212, 270)
    s += fish(350, 270, 1.2); s += fish(410, 300, 1.0); s += fish(370, 340, 0.9)
    s.append(t(380, 408, "嘉鱼", 8.2, DARK, "middle"))
    s += panel(496, 150, 210, 270)
    s += bent_tree(610, 404, 1.2); s += gourd(588, 334, 1.25); s += gourd(646, 318, 1.15)
    s.append(t(600, 408, "樛木 · 甘瓠", 7.8, DARK, "middle"))
    s += foot("图一 · 南有嘉鱼　罩汕取鱼，樛木累瓠", "南有嘉鱼，烝然罩罩。")
    return "".join(s)


def f171b():
    return bfig("南有嘉鱼　乐与贤", "取鱼有器，取贤有礼",
                [("罩汕", "鱼有罩汕，贤有燕礼；器不对则鱼不得", "取"),
                 ("樛木", "木下曲而甘瓠累；主愈谦，贤愈附", "下"),
                 ("又思", "由乐而衎，由衎而绥；乐贤不已", "久")],
                "鱼可罩，贤不可失；樛木下垂，甘瓠自累。", "一百七十一")


def f172a():
    s = head("南山有台　二山草木", "山不弃贱草，邦不弃小材", "一百七十二")
    s += mountain(170, 328, 1.15)
    s += herb(108, 400, 1.05, 7, False); s += herb(172, 402, 1.1, 8, False)
    s += tree(236, 400, 1.0, True)
    s.append(t(170, 424, "台 · 莱 · 杞", 7.6, DARK, "middle"))
    s += mountain(580, 328, 1.15)
    s += tree(518, 400, 1.0, False); s += tree(580, 402, 1.05, False)
    s += tree(642, 400, 0.95, True)
    s.append(t(580, 424, "桑 · 杨 · 李", 7.6, DARK, "middle"))
    s += panel(300, 166, 160, 226)
    for i, w in enumerate((118, 96, 74)):
        s.append(rect(380-w/2, 330-i*18, w, 18, 0.3, DARK))
    s.append(line(330, 330, 430, 330, 0.2, LIGHT))
    s.append(t(380, 422, "邦家之基", 7.6, DARK, "middle"))
    s += foot("图一 · 南山有台　二山草木，邦家之基", "南山有台，北山有莱。")
    return "".join(s)


def f172b():
    return bfig("南山有台　乐得贤", "得贤则邦基立",
                [("基", "台莱贱草亦生；山不弃小材，邦不弃小贤", "始"),
                 ("光", "桑杨常用；贤在朝，则邦有荣光", "显"),
                 ("保艾", "眉寿黄耇，终以安其后；得贤不止用之", "传")],
                "山有台莱，邦有贤基；寿不在己，在保艾后。", "一百七十二")


def f173a():
    s = head("蓼萧　萧上零露", "露不择贵贱", "一百七十三")
    s += panel(54, 150, 210, 270)
    s += grass(150, 396, 1.7, 7); s += dew(142, 286, 3); s += dew(168, 318, 3)
    s.append(t(150, 418, "蓼彼萧斯", 7.8, DARK, "middle"))
    s += panel(274, 150, 212, 270)
    s += person(380, 404, 148, 34)
    s.append(t(380, 418, "既见君子", 7.8, DARK, "middle"))
    s += panel(496, 150, 210, 270)
    s += bell(598, 338, 1.5); s += bell(658, 366, 1.15)
    s.append(t(620, 418, "和鸾雝雝", 7.8, DARK, "middle"))
    s += foot("图一 · 蓼萧　萧上零露，既见君子", "蓼彼萧斯，零露湑兮。")
    return "".join(s)


def f173b():
    return bfig("蓼萧　泽及四海", "泽不先近，不能远",
                [("心写", "见君子而心舒；燕笑语而有誉处", "近"),
                 ("龙光", "为龙为光；其德不爽，寿考不忘", "德"),
                 ("万福", "宜兄宜弟；和鸾雝雝，万福攸同", "远")],
                "露可零，泽不可私；萧虽微，露及之。", "一百七十三")


def f174a():
    s = head("湛露　露待阳晞", "夜饮有宗，则不野", "一百七十四")
    s += panel(54, 150, 210, 270)
    s += grass(150, 396, 1.55, 7); s += dew(142, 296, 3); s += dew(170, 330, 3)
    s.append(t(150, 418, "湛湛露斯", 7.8, DARK, "middle"))
    s += panel(274, 150, 212, 270)
    s += wine(380, 398, 1.5)
    s.append(t(380, 418, "厌厌夜饮", 7.8, DARK, "middle"))
    s += panel(496, 150, 210, 270)
    s += plant(588, 398, 1.3, 5, True); s += plant(652, 398, 1.2, 4, True)
    s.append(t(620, 418, "桐 · 椅", 7.8, DARK, "middle"))
    s += foot("图一 · 湛露　露待阳晞，夜饮在宗", "湛湛露斯，匪阳不晞。")
    return "".join(s)


def f174b():
    return bfig("湛露　恩以礼成", "厚而不礼，则溺",
                [("匪阳", "露非阳不晞；饮非礼不成", "则"),
                 ("在宗", "夜饮在宗庙；燕而有宗，则不野", "礼"),
                 ("令仪", "显允君子，莫不令德；岂弟君子，莫不令仪", "节")],
                "露可湛，夜不可荒；不醉无归，归在有仪。", "一百七十四")


def f175a():
    s = head("彤弓　彤弓弛藏", "弓在袋，不在手", "一百七十五")
    s += panel(54, 150, 210, 270)
    s += bow(150, 320, 1.55, RED)
    s.append(t(150, 418, "彤弓弨兮", 7.8, DARK, "middle"))
    s += panel(274, 150, 212, 270)
    s += drum(374, 330, 1.45); s += bell(450, 374, 1.0)
    s.append(t(380, 418, "钟鼓既设", 7.8, DARK, "middle"))
    s += panel(496, 150, 210, 270)
    s += rect(556, 276, 100, 56, 0.32, DARK)
    s += p("M 556 276 Q 606 244 656 276", 0.3, DARK)
    s += bow(606, 304, 0.95, DARK)
    s.append(t(600, 418, "受言櫜之", 7.8, DARK, "middle"))
    s += foot("图一 · 彤弓　彤弓弛藏，钟鼓既设", "彤弓弨兮，受言藏之。")
    return "".join(s)


def f175b():
    return bfig("彤弓　赏以功", "赏在朝，不在私",
                [("藏", "受言藏之；弓是杀器，赐而藏，不耀武", "敬"),
                 ("贶", "中心贶之；赏以功，不以私昵", "诚"),
                 ("酬", "钟鼓既设，一朝酬之；酬以礼，不以货", "报")],
                "弓可弨，功不可虚；钟鼓既设，赏在朝。", "一百七十五")


def f176a():
    s = head("菁菁者莪　莪生三地", "地有高下，教不择地", "一百七十六")
    s += mountain(148, 312, 0.95)
    s += eplant(112, 398, 1.05); s += eplant(152, 402, 1.15); s += eplant(192, 398, 1.0)
    s.append(t(150, 424, "中阿", 7.6, DARK, "middle"))
    s += panel(266, 184, 214, 208)
    for i in range(3):
        s.append(p(f"M 280 {330+i*22} Q 373 {318+i*22} 466 {330+i*22}", 0.22, LIGHT))
    s += eplant(340, 356, 0.95); s += eplant(382, 360, 1.05); s += eplant(424, 356, 0.95)
    s.append(t(376, 424, "中沚", 7.6, DARK, "middle"))
    s += mountain(610, 312, 0.95)
    s += eplant(570, 398, 1.0); s += eplant(610, 402, 1.15); s += eplant(650, 398, 1.0)
    s.append(t(610, 424, "中陵", 7.6, DARK, "middle"))
    s += p("M 480 424 Q 528 442 576 424 Q 556 456 510 456 Q 480 442 480 424 Z", 0.3, DARK)
    s += line(488, 434, 450, 416, 0.24, DARK)
    s.append(t(528, 474, "杨舟", 7.0, DARK, "middle"))
    s += foot("图一 · 菁菁者莪　莪生三地，杨舟浮沉", "菁菁者莪，在彼中阿。")
    return "".join(s)


def f176b():
    return bfig("菁菁者莪　乐育材", "育材之终，不在赐，在心休",
                [("有仪", "莪生阿；既见君子，乐且有仪", "礼"),
                 ("百朋", "莪生陵；锡我百朋，赐以成材", "赐"),
                 ("心休", "杨舟载沉载浮；材成而心休", "安")],
                "莪可生，材不可弃；杨舟浮沉，心休在育。", "一百七十六")


def f177a():
    s = head("六月　戎车四牡", "六月可出征，民不可久劳", "一百七十七")
    s += panel(54, 150, 270, 270)
    s += ride(190, 360, 1.1)
    s.append(t(190, 418, "戎车既饬", 7.6, DARK, "middle"))
    s += panel(340, 150, 180, 270)
    for i, (x, yy) in enumerate(((390, 272), (478, 272), (390, 372), (478, 372))):
        s += horse_head(x, yy, 0.92)
    s.append(t(440, 418, "四牡骙骙", 7.6, DARK, "middle"))
    s += panel(536, 150, 170, 270)
    s += flag(610, 400, 1.0, "yu"); s += flag(660, 400, 0.8, "zhao")
    s.append(t(620, 418, "白旆央央", 7.6, DARK, "middle"))
    s += foot("图一 · 六月　戎车四牡，白旆央央", "六月栖栖，戎车既饬。")
    return "".join(s)


def f177b():
    return bfig("六月　文武吉甫", "武功之根，在孝友",
                [("栖栖", "六月遑遑；玁狁孔炽，我是用急", "急"),
                 ("大原", "车安马健；薄伐至于大原，吉甫为宪", "将"),
                 ("孝友", "燕喜受祉；炰鳖脍鲤，张仲孝友", "根")],
                "六月可出征，民不可久劳；文武吉甫，以孝友为根。", "一百七十七")


def f178a():
    s = head("采芑　采芑新田", "三千之车，威在显允", "一百七十八")
    s += panel(54, 150, 210, 270)
    s += plant(150, 396, 1.55, 5, False)
    s += p("M 80 380 L 220 380", 0.2, LIGHT); s += p("M 80 400 L 220 400", 0.2, LIGHT)
    s.append(t(150, 418, "于彼新田", 7.6, DARK, "middle"))
    s += panel(274, 150, 232, 270)
    s += ride(390, 366, 1.35)
    s.append(t(390, 418, "其车三千", 7.6, DARK, "middle"))
    s += panel(516, 150, 190, 270)
    s += falcon(604, 276, 1.75)
    s += flag(620, 400, 0.8, "zhao")
    s.append(t(610, 418, "飞隼 · 旗旐", 7.6, DARK, "middle"))
    s += foot("图一 · 采芑　采芑新田，车三千乘", "薄言采芑，于彼新田。")
    return "".join(s)


def f178b():
    return bfig("采芑　元老壮犹", "威不在车多，在显允",
                [("芑", "苦菜采于新田；师出于田，不废农", "出"),
                 ("钲鼓", "陈师鞠旅；伐鼓渊渊，振旅阗阗", "令"),
                 ("来威", "方叔元老，克壮其犹；蛮荆畏威而来", "威")],
                "芑可采，师不可暴；三千之车，威在显允。", "一百七十八")


def f179a():
    s = head("车攻　车攻马同", "田以讲武，不以娱乐", "一百七十九")
    s += panel(54, 150, 250, 270)
    s += ride(180, 360, 1.2)
    s.append(t(180, 418, "我车既攻", 7.6, DARK, "middle"))
    s += panel(320, 150, 200, 270)
    s += bow(384, 306, 1.35, DARK)
    for i in range(4):
        s.append(line(430, 300+i*10, 476, 300+i*10, 0.22, DARK))
        s.append(p(f"M 476 {300+i*10} L 468 {296+i*10} L 468 {304+i*10} Z", 0.18, DARK))
    s.append(t(390, 418, "决拾弓矢", 7.6, DARK, "middle"))
    s += panel(536, 150, 170, 270)
    s += deer(612, 336, 1.15)
    s.append(t(610, 418, "搏兽于敖", 7.6, DARK, "middle"))
    s += foot("图一 · 车攻　车攻马同，决拾弓矢", "我车既攻，我马既同。")
    return "".join(s)


def f179b():
    return bfig("车攻　大庖不盈", "田猎之善，在获而能节",
                [("会同", "赤芾金舄，会同有绎；田中有礼", "礼"),
                 ("射御", "两骖不猗，舍矢如破；御正而后中", "正"),
                 ("不盈", "萧萧马鸣，悠悠旆旌；大庖不盈，有闻无声", "节")],
                "车可攻，兽不可尽；大庖不盈，田礼乃成。", "一百七十九")


def f180a():
    s = head("吉日　吉日戊午", "田先敬，不先杀", "一百八十")
    s += panel(54, 150, 210, 270)
    s += sun(150, 252, 22)
    s.append(t(150, 418, "吉日维戊", 7.6, DARK, "middle"))
    s += panel(274, 150, 212, 270)
    s += deer(380, 336, 1.25)
    s.append(t(380, 418, "麀鹿麌麌", 7.6, DARK, "middle"))
    s += panel(496, 150, 210, 270)
    s += wine(596, 396, 1.3); s += bow(656, 336, 0.9, DARK)
    s.append(t(620, 418, "酌醴 · 张弓", 7.6, DARK, "middle"))
    s += foot("图一 · 吉日　吉日戊午，田车四牡", "吉日维戊，既伯既祷。")
    return "".join(s)


def f180b():
    return bfig("吉日　终以酌醴", "杀以奉上，宴以合众",
                [("伯祷", "吉日先祭马祖；不敬而田，是暴天物", "敬"),
                 ("群友", "中原祁有；或群或友，悉率以燕天子", "安"),
                 ("酌醴", "小豝大兕，取有大小；御宾酌醴，田乃成", "成")],
                "日可吉，杀不可纵；小豝大兕，终以酌醴。", "一百八十")


FIGS = [
    ("sj171a-jia-yu", f171a), ("sj171b-yan-xian", f171b),
    ("sj172a-nan-shan", f172a), ("sj172b-bang-jia", f172b),
    ("sj173a-liao-xiao", f173a), ("sj173b-ze-ji", f173b),
    ("sj174a-zhan-lu", f174a), ("sj174b-ling-yi", f174b),
    ("sj175a-tong-gong", f175a), ("sj175b-shang-gong", f175b),
    ("sj176a-jing-e", f176a), ("sj176b-yu-cai", f176b),
    ("sj177a-liu-yue", f177a), ("sj177b-ji-fu", f177b),
    ("sj178a-cai-qi", f178a), ("sj178b-fang-shu", f178b),
    ("sj179a-che-gong", f179a), ("sj179b-da-pao", f179b),
    ("sj180a-ji-ri", f180a), ("sj180b-zhuo-li", f180b),
]


def main():
    os.makedirs(OUT, exist_ok=True)
    for key, fn in FIGS:
        svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 540" '
               'width="760" height="540">\n' + fn() + "\n</svg>\n")
        path = os.path.join(OUT, key + ".svg")
        open(path, "w", encoding="utf-8").write(svg)
        print("wrote", path, len(svg))


if __name__ == "__main__":
    main()
