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

    def test_get_neighbors(self):
        area = WaitingArea(self.testarea)
        neighbors = area.getNeighbors(1,1)
        self.assertEqual(neighbors, {
            "L", ".", "L",
            "L",      "L",
            "L", ".", "L"})

    def test_get_neighbors_edge(self):
        area = WaitingArea(self.testarea)
        neighbors = area.getNeighbors(0,0)
        self.assertEqual(neighbors, {
            ".", "L", "L"
        })

