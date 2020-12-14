from unittest import TestCase

from day11.solution import WaitingArea


class TestDay11(TestCase):
    def setUp(self):
        self.testarea = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

    def test_load_area(self):
        area = WaitingArea(self.testarea)
        self.assertEqual(10, area.width)
        self.assertEqual(10, area.height)
        self.assertEqual(".", area.get(1,0))
        self.assertEqual("L", area.get(1,1))

    def test_none_on_nonexisting(self):
        area = WaitingArea(self.testarea)
        self.assertEqual("",area.get(0,-1))
        self.assertEqual("",area.get(-1,0))
        self.assertEqual("",area.get(-1,-1))
        self.assertEqual("",area.get(0,10))
        self.assertEqual("",area.get(10,0))
        self.assertEqual("",area.get(10,10))
        self.assertIsNotNone(area.get(0,0))
        self.assertIsNotNone(area.get(9,9))

    def test_get_neighbors(self):
        area = WaitingArea(self.testarea)
        neighbors = area.getNeighbors(1,1)
        self.assertEqual(neighbors, sorted([
            "L", ".", "L",
            "L",      "L",
            "L", ".", "L"]))

    def test_get_neighbors_edge(self):
        area = WaitingArea(self.testarea)
        neighbors = area.getNeighbors(0,0)
        self.assertEqual(neighbors, sorted([
            ".", "L", "L"
        ]))

    def test_get_neighbor_count(self):
        area = WaitingArea(self.testarea)
        neighbors = area.getNeighborCounts(1,1)
        self.assertEqual(6, neighbors["L"])
        self.assertEqual(2, neighbors["."])

    def test_get_neighbor_edge(self):
        area = WaitingArea(self.testarea)
        neighbors = area.getNeighborCounts(0,0)
        self.assertEqual(2, neighbors["L"])
        self.assertEqual(1, neighbors["."])

    def test_rule_fill_seat(self):
        area = WaitingArea(self.testarea)
        occupied = 0
        new = area.simulate_single("L",occupied)
        # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
        self.assertEqual("#", new , "Empty seat was not filled")

    def test_rule_leave_seat(self):
        area = WaitingArea(self.testarea)
        occupied = 4
        new = area.simulate_single("#", occupied)
        self.assertEqual("L", new, "Seat was not freed")

    def test_getting_neighbors(self):
        area = WaitingArea("""#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##""")
        neighbors = area.getNeighbors(2,9)  # should be 3 # and 2 .
        self.assertEqual(3, neighbors.count("#"))
        self.assertEqual(2, neighbors.count("."))

    def test_singlestep(self):
        target = """#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##"""
        area = WaitingArea(self.testarea)
        is_stable = area.step()
        self.assertEqual(target, str(area))
        self.assertFalse(is_stable)
        is_stable = area.step()
        self.assertEqual("""#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##""", str(area))
        self.assertFalse(is_stable)
        area.step()
        area.step()
        area.step()
        is_stable = area.step()
        self.assertTrue(is_stable)

        is_stable = area.step()  # should still be stable
        self.assertTrue(is_stable)

    def test_stabilize(self):
        area = WaitingArea(self.testarea)
        steps = area.stabilize()
        self.assertEqual(5, steps)

    def test_count_stable_seats(self):
        area = WaitingArea(self.testarea)
        area.stabilize()
        seats = area.countSeats()
        self.assertEqual(37, seats)