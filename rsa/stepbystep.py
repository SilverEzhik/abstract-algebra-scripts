#!/usr/bin/env python3

import sys
from helper import *

####

print_bold("Receiver:\n")
print_bold("1. Pick large primes p and q")

p = 149
q = 197

if len(sys.argv) >= (1 + 2):
    if is_prime(int(sys.argv[1])):
        p = int(sys.argv[1])
    else:
        print_yellow("First argument (p) is not a prime number!")
    if is_prime(int(sys.argv[2])):
        q = int(sys.argv[2])
    else:
        print_yellow("Second argument (q) is not a prime number!")

print("p =", str(p) + "; q =", q) #str(p) used to remove space



print_bold("2. Calculate n = pq")
n = p * q
print(p, "*", q, "=", n)



print_bold("3. Calculate m = lcm(p - 1, q - 1)");
m = int(lcm(p - 1, q - 1))
print("lcm(" + str(p) + " - 1, " + str(q) + " - 1) =", m)



print_bold("4. Find the public exponent e, which will be smaller than and relatively prime to m")

e = 2 ** 16 + 1
print("In common practice, the number", e, "is commonly chosen as the public exponent")

if e > m:
    e = 3
    print("However, since m is smaller than this number, a smaller e is needed. Choosing", str(e) + "...")

while m % e == 0:
    print(e, "divides m, so it cannot be used as the exponent")
    e = e + 2

print("The public exponent is e =", e)



print_bold("5. Find the public exponent d, such that (ed) mod m = 1")
print("(de) mod m = 1 implies mx = 1 + ed, which in turn implies xm - ed = 1")
print("The equation " + str(m) + "x - " + str(e) + "d = 1 can be solved using the Extended Euclidean algorithm")

# TODO: explain egcd in detail
d = inverse_mod(e, m)

print("d =", d)

print_bold("6. Publically announce n = " + str(n) + ", e = " + str(e))

print()

####

print_bold("Sender:\n")
print_bold("1. Convert the message to a list of digits (using UTF-8)")

message = "Hello, world!"

if len(sys.argv) >= (1 + 3):
    message = sys.argv[3]

print("The message is:")
print(message)

message_numbers = []

print("The message, converted to numbers:")
for c in message:
    message_numbers.append(ord(c))
    print(message_numbers[-1], end=' ')
print()

print_bold("2. Calculate r = (m^e) mod n for every m in the numbers list")


print("Encrypted message: ")
message_encrypted = []
for c in message_numbers:
    message_encrypted.append((c ** e) % n)
    print(message_encrypted[-1], end=' ')
print()

print_bold("3. Send the message")

print()

####

print_bold("Receiver:\n")

print_bold("1. For every r in the received list of numbers, calculate m = (r^d) mod n")

message_decrypted = []
for c in message_encrypted:
    message_decrypted.append((c ** d) % n)
    print(message_decrypted[-1], end=' ')
print()

print("Decrypted message:")
message_decrypted_char_list = []
for c in message_decrypted:
    message_decrypted_char_list.append(chr(c))

decrypted_string = ''.join(message_decrypted_char_list)
print(decrypted_string)

if decrypted_string != message:
    print_yellow("The decrypted string does not match the original message. One possible reason for this is if m^e for a certain symbol is larger than n - due to how Unicode works, this is more likely to happen when using non-Latin characters in the message. Try using larger prime numbers!")
