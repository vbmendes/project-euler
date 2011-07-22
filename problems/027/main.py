# coding: utf8

import math
import unittest


class QuadraticFormulaProducesPrimeTestCase(unittest.TestCase):

    def test_if_formula_produces_40_primes(self):
        for n in range(40):
            q = quadratic_formula(a=1, b=41, n=n)
            assert is_prime(q), 'quadratic for %s is %s and is not prime' % (s, q)

    def test_if_formula_produces_80_primes(self):
        for n in range(80):
            q = quadratic_formula(a=-79, b=1601, n=n)
            assert is_prime(q), 'quadratic for %s is %s and is not prime' % (s, q)

    def test_biggest_formula_that_produces_the_bigger_primes_sequence(self):
        a, b = get_coeficents_of_the_quadratic_formula_that_produces_the_bigger_primes_sequence()
        assert -59231 == a*b


def is_prime(n):
    return not any(n%d == 0 for d in range(2, int(math.sqrt(n)+1)))


def quadratic_formula(a, b, n):
    return n**2 + a*n + b

def is_prime_quadratic_formula(a, b, n):
    possible_prime = quadratic_formula(a, b, n)
    return possible_prime >= 0 and is_prime(possible_prime)

def get_coeficents_of_the_quadratic_formula_that_produces_the_bigger_primes_sequence():
    bigger_sequence = {
        'len': 0,
        'a': None,
        'b': None,
    }
    for a in xrange(-999, 1000):
        for b in xrange(-999, 1000):
            n = 0
            while is_prime_quadratic_formula(a, b, n):
                n += 1
            if n > bigger_sequence['len']:
                bigger_sequence = {
                    'len': n,
                    'a': a,
                    'b': b,
                }
    return bigger_sequence['a'], bigger_sequence['b']

