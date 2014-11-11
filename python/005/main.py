#!/usr/bin/env python

current = 20

is_divisor = lambda divisor, multiple: not multiple % divisor
is_prime = lambda x: not any(not x%n for n in range(2,x))
primos = [n for n in xrange(2,21) if is_prime(n)]

prime_powers = dict((n, 0) for n in primos)

for i in range(2, 21):
    n_prime_powers = dict((n, 0) for n in primos)
    current = i
    j = 0
    while len(primos) > j and current >= primos[j]:
        primo = primos[j]
        if is_divisor(primo, current):
            while current and is_divisor(primo, current):
                current = current/primo
                n_prime_powers[primo] += 1
        j += 1
    for primo, power in n_prime_powers.items():
        if prime_powers[primo] < power:
            prime_powers[primo] = power

print reduce(lambda x, y: x * y, (x[0] ** x[1] for x in prime_powers.items()))