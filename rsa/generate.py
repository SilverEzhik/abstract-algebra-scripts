#!/usr/bin/env python3

import sys
from helper import *

p = 0
q = 0

if len(sys.argv) < (1 + 2):
    print("Please enter the first prime number (p): ")
    p = get_int()

    print("Please enter the first prime number (q): ")
    q = get_int()
else:
    p = int(sys.argv[1])
    q = int(sys.argv[2])

n = p * q

m = int(lcm(p - 1, q - 1))

# Public exponent

# While in the original algorithm, the exponent is chosen
# with a method such as the Extended Euclidean Algorithm,
# in practice, most implementations appear to use 65537 as
# the default exponent. Since it's prime, gcd would be 1.

e = 2 ** 16 + 1 # this exponent is called r in the Gallian book

# this exponent is supposed to be smaller than m, so switch to
# a small prime if m is small
if e > m:
    e = 3
    while m % e == 0:
        e = e + 2

# Private exponent
d = inverse_mod(e, m) # called s in the Gallian book

print("Private: ")
print("d = " + str(d))
print("\nPublic: ")
# publically announce numbers
print("n = " + str(n))
print("e = " + str(e))
