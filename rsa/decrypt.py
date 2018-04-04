#!/usr/bin/env python3

import sys
from helper import *

n = 0
d = 0

if len(sys.argv) < (1 + 2):
    print("Please enter n: ")
    n = get_int()

    print("Please enter the private exponent (d): ")
    q = get_int()
else:
    n = int(sys.argv[1])
    d = int(sys.argv[2])

print("Please enter the encrypted message: ")
encrypted = input()

for c in encrypted.split():
    r = int(c)
    m = (r ** d) % n # c^e mod n
    print(chr(m), end="")
print()
