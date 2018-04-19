#!/usr/bin/env python3
# helper functions

from fractions import gcd

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def print_bold(i):
    print_color(i, color.BOLD)

def print_yellow(i):
    print_color(i, color.YELLOW)

def print_color(i, c):
    print(c, end='')
    print(i)
    print(color.END, end='')


# loop until we get an integer
def get_int():
    while True:
        text = input()
        try:
            return int(text)
        except ValueError:
            print("Please enter an integer: ")

def get_prime():
    while True:
        i = get_int()
        if is_prime(i):
            return i
        else:
            print("Please enter a prime number: ")

def is_prime(a):
    if a < 0 or (a > 2 and a % 2 == 0) or a == 1:
        return False
    if a == 2:
        return True
    return all(a % i for i in range(3, int(a ** 0.5) + 1, 2))


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
