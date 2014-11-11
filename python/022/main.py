# coding: utf8

import unittest

class NameScoreTestCase(unittest.TestCase):

    def test_c_alphabetical_char_value(self):
        self.assertEquals(alphabetical_char_value('c'), 3)

    def test_o_alphabetical_char_value(self):
        self.assertEquals(alphabetical_char_value('o'), 15)

    def test_colin_alphabetical_value(self):
        self.assertEquals(alphabetical_value('COLIN'), 53)

    def test_file_score(self):
        with open('names.txt', 'r') as f:
            self.assertEquals(calculate_score(f.read()), 871198282)


def alphabetical_char_value(char):
    return ord(char) - 96


def alphabetical_value(name):
    return sum(alphabetical_char_value(c) for c in name.lower())


def calculate_name_score(i, name):
    return alphabetical_value(name) * (i+1)


def calculate_score(data):
    names = sorted([name.strip('"') for name in data.strip().split(",")])
    return sum(calculate_name_score(i, name) for i, name in enumerate(names))
