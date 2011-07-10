#!/usr/bin/env python

n = 600851475143
current = n
divisors = []
i = 2

is_divisor = lambda divisor, multiple: not multiple % divisor

while current >= i:
    if is_divisor(i, current):
        while current and is_divisor(i, current):
            current = current/i
        divisors.append(i)
    i += 1
print divisors[-1]
    
