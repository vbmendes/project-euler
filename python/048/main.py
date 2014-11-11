# coding: utf8

import unittest

class ProjectEuler48TestCase(unittest.TestCase):

    def test_series_for_10(self):
        self.assertEquals(last_digits_in_series(10, 10), '0405071317')

    def test_series_for_1000(self):
        self.assertEquals(last_digits_in_series(1000, 10), '9110846700')


def series(n):
    return sum(i ** i for i in range(1, n+1))


def last_digits_in_series(n, digits):
    return str(series(n))[-digits:]
