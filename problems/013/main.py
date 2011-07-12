#!/usr/bin/env python

import unittest


class ProjectEuler16TestCase(unittest.TestCase):
    
    def setUp(self):
        with open('numbers', 'r') as f:
            self.numbers_iterator = (int(line) for line in f.readlines())
    
    def test_number_of_numbers(self):
        self.assertEquals(len(list(self.numbers_iterator)), 100)
    
    def test_sum_numbers(self):
        self.assertEquals(sum_numbers(self.numbers_iterator), 5537376230390876637302048746832985971773659831892672L)
    
    def test_first_ten_digits_of_a_number(self):
        self.assertEquals(first_digits_of(12345678901234, 10), 1234567890)

    def test_first_ten_digits_of_the_sum_of_the_numbers(self):
        self.assertEquals(first_digits_of(sum_numbers(self.numbers_iterator), 10), 5537376230)

def sum_numbers(numbers_iterator):
    return sum(numbers_iterator)

def first_digits_of(number, n_digits):
    return int(str(number)[:n_digits])

if __name__ == '__main__':
    unittest.main()
