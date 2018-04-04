#!/usr/bin/env python3
# helper functions

from fractions import gcd

# loop until we get an integer
def get_int():
    while True:
        text = input()
        try:
            return int(text)
        except ValueError:
            print("Please enter an integer: ")

# gcd - the prime factors common to both numbers
# lcm - the "intersection" of the prime factors of both numbers
# consider:
#   x = abcde
#   y =    defg
# gcd =    de
# lcm = abcdefg
#
# then, xy = abc(de)(de)fg - we can see that the "extra" primes
# are actually the gcd. therefore:
def lcm(a, b):
    return a * b / gcd(a, b)


# https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm#Python

# solve ax = 1 mod n
def inverse_mod(a, n):
    g, x, _ = egcd(a, n)
    if g == 1:
        return x % n

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)
