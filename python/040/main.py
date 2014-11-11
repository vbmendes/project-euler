# coding: utf8

import unittest

class NFractionalDigitTestCase(unittest.TestCase):

    def test_1_fractional_digit(self):
        self.assertEquals(1, fractional_digit(1))

    def test_10_fractional_digit(self):
        self.assertEquals(1, fractional_digit(10))

    def test_12_fractional_digit(self):
        self.assertEquals(1, fractional_digit(12))

    def test_100_fractional_digit(self):
        self.assertEquals(5, fractional_digit(100))

    def test_1000_fractional_digit(self):
        self.assertEquals(3, fractional_digit(1000))

    def test_10000_fractional_digit(self):
        self.assertEquals(7, fractional_digit(10000))

    def test_100000_fractional_digit(self):
        self.assertEquals(2, fractional_digit(100000))

    def test_1000000_fractional_digit(self):
        self.assertEquals(1, fractional_digit(1000000))

    def test_product_of_fractionals(self):
        self.assertEquals(210, product_of_fractionals([1, 10, 100, 1000, 10000, 100000, 1000000]))

def fractional_digit(n):
    f_len = 0
    i = 0
    while f_len < n:
        i += 1
        f_len += len(str(i))
    return int(str(i)[n - f_len - 1])

def product_of_fractionals(args):
    ret = 1
    for n in args:
        ret *= fractional_digit(n)
    return ret