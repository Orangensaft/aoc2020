from unittest import TestCase

from day5.solution import partition, find_row_id, find_coords, find_seat_id, get_highest_id, get_all_seat_ids, \
    get_missing_id


class TestsDay5(TestCase):

    def test_first_partition(self):
        lower, upper = 0, 127
        new_lower, new_upper = partition(lower, upper, "F")
        self.assertEqual(new_lower, 0)
        self.assertEqual(new_upper, 63)

    def test_second_partition(self):
        lower, upper = 0, 63
        new_lower, new_upper = partition(lower, upper, "B")
        self.assertEqual(new_lower, 32)
        self.assertEqual(new_upper, 63)

    def test_near_last_partition(self):
        lower, upper = 44, 47
        new_lower, new_upper = partition(lower, upper, "F")
        self.assertEqual(44, new_lower)
        self.assertEqual(45, new_upper)

    def test_last_partition(self):
        lower, upper = 44, 45
        new_lower, new_upper = partition(lower, upper, "F")
        self.assertEqual(44, new_lower)
        self.assertEqual(44, new_upper)

    def test_get_row_id(self):
        directions = "FBFBBFF"
        row_id = find_row_id(directions)
        self.assertEqual(44, row_id)

    def test_get_seat_first(self):
        l, u = 0, 7
        l, u = partition(l, u, "R")
        self.assertEqual(4, l)
        self.assertEqual(7, u)

    def test_get_seat_second(self):
        l, u = 4, 7
        l, u = partition(l, u, "L")
        self.assertEqual(4, l)
        self.assertEqual(5, u)

    def test_get_seat_id(self):
        directions = "RLR"
        seat = find_row_id(directions, find_row=False)
        self.assertEqual(5, seat)

    def test_get_coords(self):
        directions = "FBFBBFFRLR"
        row, seat = find_coords(directions)
        self.assertEqual(44, row)
        self.assertEqual(5, seat)

    def test_seat_id(self):
        directions = "FBFBBFFRLR"
        seat_id = find_seat_id(directions)
        self.assertEqual(357, seat_id)

    def test_other_directions(self):
        self.assertEqual(567, find_seat_id("BFFFBBFRRR"))
        self.assertEqual(119, find_seat_id("FFFBBBFRRR"))
        self.assertEqual(820, find_seat_id("BBFFBBFRLL"))

    def test_find_highest_id(self):
        passes = """BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL"""
        highest = get_highest_id(passes)
        self.assertEqual(820, highest)

    def test_get_all_passes(self):
        passes = """BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL"""
        ids = get_all_seat_ids(passes)
        self.assertEqual(567, ids[0])
        self.assertEqual(119, ids[1])
        self.assertEqual(820, ids[2])

    def test_get_find_missing_ids(self):
        ids = [1, 2, 3, 5]
        missing = get_missing_id(ids)
        self.assertEqual(4, missing)
