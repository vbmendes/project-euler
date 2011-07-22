# coding: utf8

import unittest

class SumOfPowerOfDigitsTestCase(unittest.TestCase):

    def test_sum_of_4th_power_of_1634_digits(self):
        assert 1634 == sum_of_power_of_digits(1634, 4)
        assert is_equal_to_the_sum_of_the_power_of_its_digits(1634, 4)

    def test_sum_of_4th_power_of_8208_digits(self):
        assert 8208 == sum_of_power_of_digits(8208, 4)
        assert is_equal_to_the_sum_of_the_power_of_its_digits(8208, 4)

    def test_sum_of_4th_power_of_9474_digits(self):
        assert 9474 == sum_of_power_of_digits(9474, 4)
        assert is_equal_to_the_sum_of_the_power_of_its_digits(9474, 4)

    def test_sum_of_numbers_that_are_equal_to_the_4th_powers_of_its_digits(self):
        soma = sum_of_numbers_that_are_equal_to_the_powers_of_its_digits(4)
        assert 19316 == soma

    def test_sum_of_numbers_that_are_equal_to_the_5th_powers_of_its_digits(self):
        soma = sum_of_numbers_that_are_equal_to_the_powers_of_its_digits(5)
        assert 443839 == soma


def sum_of_power_of_digits(number, power):
    return sum(int(digit) ** power for digit in list(str(number)))


def is_equal_to_the_sum_of_the_power_of_its_digits(number, power):
    return number == sum_of_power_of_digits(number, power)


def sum_of_numbers_that_are_equal_to_the_powers_of_its_digits(power):
    sum = 0
    for number in range(2, 1000000):
        if is_equal_to_the_sum_of_the_power_of_its_digits(number, power):
            sum += number
    return sum
