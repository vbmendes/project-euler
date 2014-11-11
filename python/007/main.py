#!/usr/bin/env python

import unittest

class ProjectEuller7TestCase(unittest.TestCase):

    def test_is_prime_2(self):
        self.assertEquals(is_prime(2), True)
    
    def test_is_prime_3(self):
        self.assertEquals(is_prime(3), True)
    
    def test_is_prime_4(self):
        self.assertEquals(is_prime(4), False)
    
    def test_is_prime_5(self):
        self.assertEquals(is_prime(5), True)
    
    def test_is_prime_6(self):
        self.assertEquals(is_prime(6), False)

    def test_6_prime(self):
        self.assertEquals(get_prime(6), 13)
    
    def test_10001_prime(self):
        self.assertEquals(get_prime(10001), None)

is_prime = lambda x: not any(not x%n for n in range(2,x))

def get_prime(index):
    i = 0
    current = 1
    while(i < index):
        current += 1
        if is_prime(current):
            i += 1
    return current

if __name__ == '__main__':
    unittest.main()
