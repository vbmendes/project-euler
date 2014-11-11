#!/usr/bin/env python

import unittest

class ProjectEuller9TestCase(unittest.TestCase):

    def test_is_pythagorean_3_4_5_is_true(self):
        self.assertEquals(is_pythagorean(3, 4, 5), True)
    
    def test_is_pythagorean_2_4_5_is_false(self):
        self.assertEquals(is_pythagorean(2, 4, 5), False)
    
    def test_product_of_pythagorean_triples_sums_1000(self):
        self.assertEquals(product_of_pythagorean_triples_sums_1000(), 31875000)

def is_pythagorean(a, b, c):
    return a < b < c and a ** 2 + b ** 2 == c ** 2

def product_of_pythagorean_triples_sums_1000():
    for i in range(1000):
        for j in range(i):
            for k in range(j):
                if  i + j + k == 1000 and is_pythagorean(k, j, i):
                    return k * j * i

if __name__ == '__main__':
    unittest.main()
