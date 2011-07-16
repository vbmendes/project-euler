# coding: utf8

import unittest

class MondaysTestCase(unittest.TestCase):

    def test_first_weekday_in_twentieth_century(self):
        self.assertEquals(first_weekday_in_twentieth_century(), 1)

    def test_mondays_in_first_year(self):
        self.assertEquals(count_mondays(1), 2)

    def test_mondays_in_first_year(self):
        self.assertEquals(count_mondays(99), 2)


def first_weekday_in_twentieth_century():
    return (0 + 365) % 7

def count_mondays(years):
    current_year = 0
    current_weekday = (0 + 365)%7
    mondays = 0
    while current_year < years:
        months_len = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (current_year + 1901) % 4 == 0:
            months_len[1] = 29
        for len in months_len:
            current_weekday = (current_weekday + len)%7
            if current_weekday == 0:
                mondays += 1
        current_year += 1
    return mondays
