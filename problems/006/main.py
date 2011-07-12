#!/usr/bin/env python

import unittest

class ProjectEuller6TestCase(unittest.TestCase):
    
    def test_sum_of_squares_until_ten_is_385(self):
        self.assertEquals(sum_of_squares(until=10), 385)
    
    def test_square_of_sum_until_ten_is_3025(self):
        self.assertEquals(square_of_sum(until=10), 3025)
    
    def test_difference_between_square_of_sum_and_sum_of_squares_untion_ten_is_2640(self):
        self.assertEquals(diff_between_square_of_sum_and_sum_of_squares(until=10), 2640)
    
    def test_difference_between_square_of_sum_and_sum_of_squares_untion_ten_is_unknown(self):
        self.assertEquals(diff_between_square_of_sum_and_sum_of_squares(until=100), 25164150)

def sum_of_squares(until):
    return sum(n ** 2 for n in xrange(1, until+1))

def square_of_sum(until):
    return sum(xrange(1, until+1)) ** 2

def diff_between_square_of_sum_and_sum_of_squares(until):
    return square_of_sum(until) - sum_of_squares(until)

if __name__ == '__main__':
    unittest.main()
        