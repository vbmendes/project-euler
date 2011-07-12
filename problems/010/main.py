#!/usr/bin/env python

import unittest

class ProjectEuler10TestCase(unittest.TestCase):

    def test_is_prime_2(self):
        self.assertEquals(is_prime(2), True)

    def test_is_prime_3(self):
        self.assertEquals(is_prime(3), True)

    def test_is_prime_4(self):
        self.assertEquals(is_prime(4), False)

    def test_is_prime_5(self):
        self.assertEquals(is_prime(5), True)

    def test_is_prime_6(self):
        self.assertEquals(is_prime(6), False)

    def test_sum_of_primes_below_10(self):
        self.assertEquals(sum_of_primes_below(10), 17)

    def test_sum_of_primes_below_10(self):
        self.assertEquals(sum_of_primes_below(2000000), 142913828922)
    
    def test_eratosthenes_sieve_for_10(self):
        expected = [False] * 10
        expected[1] = True
        expected[2] = True
        expected[3] = True
        expected[5] = True
        expected[7] = True
        
        self.assertEquals(eratosthenes_sieve(10), expected)

is_prime = lambda x: not any(not x%n for n in range(2,x))

def eratosthenes_sieve(max_limit):
    primes_list = [True] * max_limit
    primes_list[0] = False
    for i in range(2, max_limit):
        for j in range(i, max_limit/i + 1):
            multiple = i * j
            if multiple < max_limit:
                primes_list[multiple] = False
    return primes_list

def sum_of_primes_below(max_limit):
    sieve = eratosthenes_sieve(max_limit)
    return sum(i for i in range(2, max_limit) if sieve[i])

if __name__ == '__main__':
    unittest.main()
        