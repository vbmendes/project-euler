# coding: utf8

import unittest

class PalindromicInBaseTestCase(unittest.TestCase):

    def test_palindromic_585_base_10_is_true(self):
        self.assertTrue(is_palindromic(585, base=10))

    def test_palindromic_584_base_10_is_false(self):
        self.assertFalse(is_palindromic(584, base=10))

    def test_palindromic_585_base_2_is_true(self):
        self.assertTrue(is_palindromic(585, base=2))

    def test_sum_of_all_palindromic_base_2_and_10_until_one_million(self):
        self.assertEquals(872187, sum_of_palindrics(1000000, bases=(10, 2)))


def is_palindromic(number, base):
    if base == 10:
        number_str = str(number)
    if base == 2:
        number_str = ''
        while number:
            number_str += str(number % base)
            number /= base
    return number_str == number_str[::-1]

def sum_of_palindrics(limit, bases):
    for i in range(limit):
        return sum(
            number for number in range(limit) if all(is_palindromic(number, base) for base in bases)
        )