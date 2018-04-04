#!/usr/bin/env python3

import sys
from helper import *

msg = ""
n = 0
e = 0

if len(sys.argv) < (1 + 3):
    print("Please enter the message: ")
    msg = input()
    print("Please enter n: ")
    n = get_int()
    print("Please enter e: ")
    e = get_int()
else:
    msg = sys.argv[1]
    n = int(sys.argv[2])
    e = int(sys.argv[3])

for c in msg:
    m = ord(c)

    r = (m ** e) % n # c^e mod n
    print(r, end=" ")
print()

