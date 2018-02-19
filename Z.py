#!/usr/bin/env python3

from fractions import gcd
import sys

mod = int(sys.argv[1])

g = []

list = []

def op1(a, b):
    return (a * b) % mod

def op2(a, b):
    return (a + b) % mod


for a in range(0, mod):
    g.append(a)

op = op2

for a in g:
    row = []
    for b in g:
        row.append(op(a, b))
    list.append(row)

def is_in_group(n):
    if op == op2:
        return True
    for a in g:
        if int(a) == n:
            return True
    return False

def el_order(n):
    c = g[0]
    for i in range(1, 1000000):
        c = op(c, n)
        if c == g[0]: # identity
            return str(i)
    return "n"


def print_table():
    print("|Z(" + str(mod) + ")| = " + str(len(g)) + "\n")
    for r in list:
        s = ""
        for v in r:
            if is_in_group(v) == False:
                s += "\033[1;31;40m" + str(v) + "\033[0m" + "\t" # color number red
            else:
                s += str(v) + " (" + el_order(v) + ")" + "\t"
        print(s)

print_table()


