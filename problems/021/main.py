# coding: utf8

import math
import unittest

class ProjectEuler19TestCase(unittest.TestCase):

    def test_sum_of_divisors_of_220(self):
        self.assertEquals(sum_of_divisors(220), 284)

    def test_sum_of_divisors_of_284(self):
        self.assertEquals(sum_of_divisors(284), 220)

    def test_is_amicable_220_and_284(self):
        self.assertTrue(is_amicable(284, 220))

    def test_sum_of_amicables_until_300(self):
        self.assertEquals(sum_of_amicables(until=300), 504)

    def test_sum_of_amicables_until_1000(self):
        self.assertEquals(sum_of_amicables(until=10000), 31626)


def sum_of_divisors(n):
    sum = 1
    for i in range(2, n/2+1):
        if not n % i:
            sum += i
    return sum

def is_amicable(n1, n2):
    return sum_of_divisors(n1) == n2 and sum_of_divisors(n2) == n1

def sum_of_amicables(until):
    sums_of_divisors = [0] * (until+1)
    for i in range(1, until+1):
        sums_of_divisors[i] = sum_of_divisors(i)
    amicables = set()
    for i in range(1, until+1):
        try:
            possible_i = sums_of_divisors[sums_of_divisors[i]]
        except IndexError:
            pass
        else:
            if i == possible_i and i != sums_of_divisors[i]:
                amicables.add(i)
                amicables.add(sums_of_divisors[i])
    return sum(amicables)