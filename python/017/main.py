# coding: utf8

import unittest

class TextualNumberTestCase(unittest.TestCase):

    def test_textual_one(self):
        self.assertEquals(textual_number(1), 'one')

    def test_textual_two(self):
        self.assertEquals(textual_number(2), 'two')

    def test_textual_ten(self):
        self.assertEquals(textual_number(10), 'ten')

    def test_textual_twenty(self):
        self.assertEquals(textual_number(20), 'twenty')

    def test_textual_twenty_nine(self):
        self.assertEquals(textual_number(29), 'twenty-nine')

    def test_textual_one_hundred(self):
        self.assertEquals(textual_number(100), 'one hundred')

    def test_textual_one_hundred_and_twenty_nine(self):
        self.assertEquals(textual_number(129), 'one hundred and twenty-nine')

    def test_textual_one_hundred_and_twenty_nine(self):
        self.assertEquals(textual_number(1000), 'one thousand')

    def test_len_of_numbers_until_five(self):
        self.assertEquals(len_of_numbers(until=5), 19)

    def test_len_of_numbers_until_five(self):
        self.assertEquals(len_of_numbers(until=1000), 21124)


def len_of_numbers(until):
    return sum(
        len(textual_number(n).replace(' ','').replace('-',''))
        for n in range(1, until+1)
    )


def textual_number(n):
    mapping = [
        None,
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine',
        'ten',
        'eleven',
        'twelve',
        'thirteen',
        'fourteen',
        'fifteen',
        'sixteen',
        'seventeen',
        'eighteen',
        'nineteen',
    ]
    mapping_tenths = [
        None,
        None,
        'twenty',
        'thirty',
        'forty',
        'fifty',
        'sixty',
        'seventy',
        'eighty',
        'ninety',
    ]
    if n < 20:
        resp = mapping[n]
    elif n < 100:
        resp = mapping_tenths[n/10]
        if n%10:
            resp = '%s-%s' % (resp, mapping[n%10])
    elif n < 1000:
        resp = '%s hundred' % mapping[n/100]
        if n%100:
            resp = '%s and %s' % (resp, textual_number(n%100))
    else:
        resp = 'one thousand'
    return resp