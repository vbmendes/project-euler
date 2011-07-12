#!/usr/bin/env python

import unittest


class ProjectEuler20TestCase(unittest.TestCase):
    
    def test_factorial_of_10(self):
        self.assertEquals(factorial(10), 3628800)
    
    def test_sum_of_digits_in_factorial_of_10(self):
        self.assertEquals(sum_of_digits_in_factorial(10), 27)
        
    def test_sum_of_digits_in_factorial_of_100(self):
        self.assertEquals(sum_of_digits_in_factorial(100), 648)


def factorial(n):
    return reduce(lambda x, y: x*y,range(1, n+1))


def sum_of_digits_in_factorial(n):
    return sum(int(digit) for digit in str(factorial(n)))

if __name__ == '__main__':
    unittest.main()
