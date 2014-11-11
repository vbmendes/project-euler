# coding: utf8

import unittest


class IsDivisorTestCase(unittest.TestCase):

    def test_2_is_divisor_of_10(self):
        self.assertTrue(is_divisor(2, 10))


class SumOfDivisorsTestCase(unittest.TestCase):

    def test_sum_of_divisors_of_10_should_be_7(self):
        self.assertEquals(8, get_sum_of_divisors(10))

    def test_sum_of_divisors_of_12_should_be_16(self):
        self.assertEquals(16, get_sum_of_divisors(12))


class AbundantNumberTestCase(unittest.TestCase):

    def test_10_is_not_abundant(self):
        self.assertFalse(is_abundant(10))

    def test_12_is_abundant(self):
        self.assertTrue(is_abundant(12))

    def _test_get_all_abundant_numbers(self):
        self.assertEquals(6965, len(get_all_abundant_numbers()))


class SumOfAbundantNumberTestCase(unittest.TestCase):

    def test_get_all_numbers_that_cant_be_written_as_sum_of_two_abundant_numbers(self):
        self.assertEquals(0, get_sum_of_numbers_that_cant_be_written_as_sum_of_two_abundant_numbers())

is_divisor = lambda divisor, multiple: not multiple % divisor


def get_sum_of_divisors(number):
    sum_of_divisors = 1
    for i in range(2, number/2 + 1):
        if is_divisor(i, number):
            sum_of_divisors += i
    return sum_of_divisors


def is_abundant(number):
    return get_sum_of_divisors(number) > number


def _define_if_numbers_is_abundant_or_not():
    numbers = [False]*(28123+1)
    for i in range(12, 28123):
        if is_abundant(i):
            numbers[i] = True
    return numbers

def get_all_abundant_numbers(numbers=None):
    numbers = numbers or _define_if_numbers_is_abundant_or_not()
    return filter(lambda i: numbers[i], (i for i in range(len(numbers))))

def get_sum_of_numbers_that_cant_be_written_as_sum_of_two_abundant_numbers():
    abundant_numbers = get_all_abundant_numbers()
    numbers = range(0, 28123)
    for i, a1 in enumerate(abundant_numbers):
        for a2 in abundant_numbers[i:]:
            if a1 + a2 < 28123:
                numbers[a1 + a2] = 0
    return sum(numbers)
