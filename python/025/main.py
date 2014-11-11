#!/usr/bin/env python

import unittest

class ProjectEuler25TestCase(unittest.TestCase):

    def test_len_n_1000(self):
        self.assertEquals(len_n(1000), 4)

    def test_fibonnaci_iterator(self):
        fibonacci_iterator = fibonacci()
        self.assertEquals(next(fibonacci_iterator), 1)
        self.assertEquals(next(fibonacci_iterator), 1)
        self.assertEquals(next(fibonacci_iterator), 2)
        self.assertEquals(next(fibonacci_iterator), 3)
        self.assertEquals(next(fibonacci_iterator), 5)
        self.assertEquals(next(fibonacci_iterator), 8)
        self.assertEquals(next(fibonacci_iterator), 13)
        self.assertEquals(next(fibonacci_iterator), 21)

    def test_first_fibonacci_with_2_digits(self):
        self.assertEquals(first_fibonacci_with_digits(2), 7)

    def test_first_fibonacci_with_1000_digits(self):
        self.assertEquals(first_fibonacci_with_digits(1000), 4782)


def len_n(n):
    return len(str(n))

def fibonacci():
    current = 1
    previous = 0
    while True:
        yield current
        current, previous = current + previous, current


def first_fibonacci_with_digits(n_digits):
    current_n_digits = 0
    fibonacci_iterator = fibonacci()
    i = 0
    while current_n_digits < n_digits:
        i += 1
        fib_n = next(fibonacci_iterator)
        current_n_digits = len_n(fib_n)
    return i