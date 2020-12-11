from unittest import TestCase

from day10.solution import find_chain, calc_differences, calc_solution_a, is_possible_chain, \
    find_possible_fits, count_solutions_memsafe


class TestDay10(TestCase):
    def setUp(self):
        self.EXAMPLE_ADAPTERS = """16
10
15
5
1
11
7
19
6
12
4"""
        self.EXAMPLE_ADAPTERS_2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

    def test_find_chain(self):

        chain = find_chain(self.EXAMPLE_ADAPTERS)
        self.assertEqual([0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22], chain)

    def test_calc_differences(self):
        diffs = calc_differences(self.EXAMPLE_ADAPTERS)
        self.assertEqual([1,3,1,1,1,3,1,1,3,1,3,3], diffs)

    def test_calc_solution(self):
        solution = calc_solution_a(self.EXAMPLE_ADAPTERS)
        self.assertEqual(7*5, solution)

    def test_calc_solution_2(self):
        solution = calc_solution_a(self.EXAMPLE_ADAPTERS_2)
        self.assertEqual(22*10, solution)

    def test_is_possible_chain(self):
        self.assertTrue(is_possible_chain([1,2,3,4,5]))
        self.assertFalse(is_possible_chain([1,3,5,8,12]))

    def test_count_possible_solutions(self):
        amount = count_solutions_memsafe(self.EXAMPLE_ADAPTERS)
        self.assertEqual(8, amount)

    def test_count_possible_solutions_2(self):
        amount = count_solutions_memsafe(self.EXAMPLE_ADAPTERS_2)
        self.assertEqual(19208, amount)


    def test_find_possible_fits(self):
        x = (1, 2, 3 , 4 , 5 , 6, 7)
        possible = find_possible_fits(3, x)
        for i in [4,5,6]:
            self.assertIn(i, possible)
        self.assertEqual(3, len(possible))