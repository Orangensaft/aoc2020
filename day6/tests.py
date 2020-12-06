from unittest import TestCase

from day6.solution import get_bitvector, get_group_answers_bitwise, count_group_answers, count_group_answers_all, \
    get_sum_of_answers, get_sum_by_everyone


class TestsDay6(TestCase):
    def test_create_bitvector(self):
        person = "abcxyz"
        vector = get_bitvector(person)
        self.assertEqual(0b11100000000000000000000111, vector)

    def test_get_by_anyone(self):
        group = ["abcx", "abcy", "abcz"]
        by_anyone = get_group_answers_bitwise(group)
        self.assertEqual(0b11100000000000000000000111, by_anyone)

    def test_count_answers(self):
        group = ["abcx", "abcy", "abcz"]
        count = count_group_answers(group)
        self.assertEqual(6, count)

    def test_count_by_everyone(self):
        group = ["abcx", "abcy", "abcz"]
        count = count_group_answers_all(group)
        self.assertEqual(3, count)

    def test_sum_of_answers_OR(self):
        groups = """abc

a
b
c

ab
ac

a
a
a
a

b"""
        total = get_sum_of_answers(groups)
        self.assertEqual(11, total)

    def test_sum_of_answers_AND(self):
        groups = """abc

a
b
c

ab
ac

a
a
a
a

b"""
        total = get_sum_by_everyone(groups)
        self.assertEqual(6, total)