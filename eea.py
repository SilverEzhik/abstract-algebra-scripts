#!/usr/bin/env python

import sys
import math

a = int(sys.argv[1])
b = int(sys.argv[2])

def res(a, s, b, t, gcd):
    print("as + bt = gcd(a, b)")
    print("a = " + str(a))
    print("b = " + str(b))
    print("s = " + str(s))
    print("t = " + str(t))
    print("gcd = " + str(gcd))

    print(str(a) + "*" + str(s) + " + " + str(b) + "*" + str(t) + " = " + str(gcd))

def gcde(a, b):
    s = 0
    ss = 1
    t = 1
    tt = 0
    r = b
    rr = a
    while r != 0:
        q = rr / r
        z = r
        r = rr - q * z
        rr = z

        z = s
        s = ss - q * z
        ss = z

        z = t
        t = tt - q * z
        tt = z
    res(a, ss, b, tt, rr)

gcde(a, b)
