# coding: utf8

import unittest

class ProjectEuler15TestCase(unittest.TestCase):

    def test_factorial_0(self):
        self.assertEquals(factorial(0), 1)

    def test_factorial_1(self):
        self.assertEquals(factorial(1), 1)

    def test_factorial_2(self):
        self.assertEquals(factorial(2), 2)

    def test_factorial_3(self):
        self.assertEquals(factorial(3), 6)

    def test_factorial_4(self):
        self.assertEquals(factorial(4), 24)

    def test_combination_4_2(self):
        self.assertEquals(combination(4, 2), 6)

    def test_permutation_with_repetition_for_2(self):
        self.assertEquals(n_permutations_with_repetition(2,2), 6)

    def test_permutation_with_repetition_for_20(self):
        self.assertEquals(n_permutations_with_repetition(20,20), 137846528820L)


def factorial(n):
    if n < 1:
        return 1
    return reduce(lambda x, y: x*y, xrange(1, n+1))

def combination(m, p):
    return factorial(m)/(factorial(m - p)*factorial(p))

def n_permutations_with_repetition(*repetitions):
    n_slots = sum(repetitions)
    n_permutations = 1
    for rep in repetitions:
        n_permutations *= combination(n_slots, rep)
        n_slots -= rep
    return n_permutations
