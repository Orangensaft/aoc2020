from .puzzleinput import PUZZLEINPUT

"""
 X ------->
Y
|    ..##.......
|    #...#...#..
|    .#....#..#.
V    ..#.#...#.#
    .#...##..#.
    ..#.##.....
    .#.#.#....#
    .#........#
    #.##...#...
    #...##....#
    .#..#...#.#

"""


class Toboggan:
    def __init__(self, pinput, delta_x, delta_y):
        self.field = pinput.split("\n")
        self.width = len(self.field[0])
        self.height = len(self.field)
        self.delta_x = delta_x
        self.delta_y = delta_y

    def get(self,x,y):
        return self.field[y][x%self.width]

    def calculate_path(self, starting=(0, 0)):
        x1,y1 = starting
        while y1 < self.height-1:
            x1, y1 = x1+self.delta_x, y1+self.delta_y
            yield x1, y1

    def get_route_stats(self, starting=(0, 0)):
        hit = 0
        dodged = 0
        for x,y in self.calculate_path(starting):
            if self.get(x,y) == "#":
                hit += 1
            else:
                dodged += 1
        return hit, dodged


def find_solution_a():
    t = Toboggan(PUZZLEINPUT,3,1)
    hit, _ = t.get_route_stats()
    return hit


def find_solution_b():
    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    total = 1
    for delta_x, delta_y in slopes:
        t = Toboggan(PUZZLEINPUT, delta_x, delta_y)
        hit, _ = t.get_route_stats()
        total *= hit
    return total