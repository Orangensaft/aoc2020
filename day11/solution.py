from collections import Counter
from copy import deepcopy

from day11.puzzleinput import PUZZLEINPUT


class WaitingArea:
    def __init__(self, area: str):
        self.area: [[str]] = [list(row) for row in area.split("\n")]
        self.height = len(self.area)
        self.width = len(self.area[0])

    def get(self,x,y) -> str:
        if x < 0 or y < 0:
            return ""
        if x >= self.width or y >= self.height:
            return ""
        return self.area[y][x]

    def getNeighbors(self,x,y) -> [str]:
        out = []
        for n_x in [-1,0,1]:
            for n_y in [-1,0,1]:
                if n_x==n_y==0:
                    continue  # skip (0,0) as the field itself is no neighbor
                n = self.get(x+n_x, y+n_y)
                if n != "":
                    out.append(n)
        return sorted(out)

    def getNeighborCounts(self, x, y) -> Counter:
        ret = Counter(self.getNeighbors(x,y))
        if ret.get("L") is None:
            ret["L"] = 0
        if ret.get(".") is None:
            ret["."] = 0
        if ret.get("L") is None:
            ret["#"] = 0
        return ret

    @staticmethod
    def simulate_single(content:str, occupied:int):
        if content == "L":
            # empty seat
            if occupied == 0:
                return "#"  # fill seat

        if content == ".":
            return "."

        if content == "#":
            if occupied >= 4:  # too crowded
                return "L"

        return content  # default case

    def step(self) -> bool:
        new = deepcopy(self.area)
        for x in range(self.width):
            for y in range(self.height):
                cell = self.get(x,y)
                occupied = self.getNeighborCounts(x,y)["#"]
                new[y][x] = self.simulate_single(cell, occupied )
        stable = self.field_to_str(new) == self.field_to_str(self.area)
        self.area = new
        return stable

    def stabilize(self):
        steps = 0
        while not self.step():
            steps += 1
        return steps

    @staticmethod
    def field_to_str(field):
        return "\n".join(["".join(row) for row in field])

    def __str__(self):
        return self.field_to_str(self.area)

    def countSeats(self):
        return str(self).count("#")

def find_solution_a():
    area = WaitingArea(PUZZLEINPUT)
    area.stabilize()
    return area.countSeats()

def find_solution_b():
    return 0