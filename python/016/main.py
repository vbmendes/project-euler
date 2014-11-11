#!/usr/bin/env python

import unittest


class ProjectEuler16TestCase(unittest.TestCase):
    
    def test_sum_of_digits_in_2_pow_15(self):
        self.assertEquals(sum_of_digits_in_pow(2, 15), 26)

    def test_sum_of_digits_in_2_pow_1000(self):
        self.assertEquals(sum_of_digits_in_pow(2, 1000), 1366)


def sum_of_digits_in_pow(n, pow):
    return sum(int(digit) for digit in str(n ** pow))

if __name__ == '__main__':
    unittest.main()
