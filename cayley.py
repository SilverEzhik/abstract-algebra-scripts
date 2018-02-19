#!/usr/bin/env python3
import sys

mod = int(sys.argv[1])

list = []

for a in sys.argv[2:]:
    row = []
    for b in sys.argv[2:]:
        row.append(int(a) * int(b) % mod)
    list.append(row)

def is_in_group(n):
    for a in sys.argv[2:]:
        if int(a) == n:
            return True
    return False

def print_table():
    for r in list:
        s = ""
        for v in r:
            if is_in_group(v) == False:
                s += "\033[1;31;40m" + str(v) + "\033[0m" + "\t" # color number red
            else:
                s += str(v) + "\t"
        print(s)

print_table()
