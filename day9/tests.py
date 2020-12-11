from unittest import TestCase

from day9.solution import is_sum_of_numbers, find_disallowed_number, find_contiguous_sum, break_encryption

"""
preamble: 25 nums
num[n]: num[x] + num[y] ; x,y < n ; x != y
only check the previous 25 numbers
"""

class TestDay9(TestCase):
    def test_is_sum_of_numbers(self):
        numbers = [i+1 for i in range(25)]
        self.assertTrue(is_sum_of_numbers(numbers, 49))
        self.assertFalse(is_sum_of_numbers(numbers, 1))
        self.assertTrue(is_sum_of_numbers(numbers, 26))
        self.assertFalse(is_sum_of_numbers(numbers, 50))

    def test_find_disallowed_number(self):
        numbers = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""
        disallowed = find_disallowed_number(numbers, size=5)
        self.assertEqual(127, disallowed)

    def test_find_contiguous_sum(self):
        numbers = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""
        s = find_contiguous_sum(numbers, 127)
        for i in [15, 25, 47, 40]:
            self.assertIn(i, s)

    def test_break_encryption(self):
        numbers = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""
        key = break_encryption(numbers, 5)
        self.assertEqual(62, key)
