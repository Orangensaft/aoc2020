import itertools
from .puzzleinput import PUZZLEINPUT


def find_summing_pair(count=2):
    for combination in itertools.combinations(PUZZLEINPUT.split("\n"),count):
        combination = [int(i) for i in combination]
        if sum(combination) == 2020:
            return combination


def find_solution_a():
    num1, num2 = find_summing_pair()
    return num1*num2


def find_solution_b():
    num1, num2, num3 = find_summing_pair(3)
    return num1*num2*num3

