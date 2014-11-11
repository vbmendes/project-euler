# coding: utf8

import unittest

class CircularNumbersTestCase(unittest.TestCase):

    def test_circulars_below_100(self):
        self.assertEquals(set([2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]),
            circular_numbers(below=100))

    def test_circulars_below_1000(self):
        self.assertTrue(197 in circular_numbers(below=1000))

    def test_n_circulars_below_100(self):
        self.assertEquals(13, len(circular_numbers(below=100)))

    def test_n_circulars_below_1000000(self):
        self.assertEquals(55, len(circular_numbers(below=1000000)))

def circular_numbers(below):
    numbers = set()
    primes_list = eratosthenes_sieve(below)
    for number, is_prime in enumerate(primes_list):
        if is_prime:
            if all(primes_list[int(str(number)[i:]+str(number)[:i])] for i in range(len(str(number)))):
                numbers.add(number)
    numbers.remove(1)
    return numbers

def eratosthenes_sieve(below):
    primes_list = [True] * below
    primes_list[0] = False
    for i in range(2, below):
        for j in range(i, below/i + 1):
            multiple = i * j
            if multiple < below:
                primes_list[multiple] = False
    return primes_list


  