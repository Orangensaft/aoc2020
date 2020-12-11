import itertools

from day9.puzzleinput import PUZZLEINPUT


def is_sum_of_numbers(numbers, n):
    combinations = itertools.combinations(numbers, 2)
    for x,y in combinations:
        if x+y == n:
            return True


def find_disallowed_number(numbers:str, size=25):
    numbers = [int(i) for i in numbers.split("\n")]
    for i in range(size, len(numbers)):
        to_check = numbers[i]
        sublist = numbers[i-size:i]
        if not is_sum_of_numbers(sublist, to_check):
            return to_check


def find_contiguous_sum(numbers: str, n: int):
    numbers = [int(i) for i in numbers.split("\n")]
    for start_index in range(len(numbers)):
        max_size = len(numbers) - start_index
        for size in range(2,max_size+1):  # as end of range is excluded
            to_check = numbers[start_index:start_index+size]
            total = sum(to_check)
            if total == n:
                return to_check
            if total > n:
                break  # optimization: no need to keep adding lists as all members are positive


def break_encryption(numbers: str, preamble_size=25):
    disallowed = find_disallowed_number(numbers, preamble_size)
    contiguous = find_contiguous_sum(numbers, disallowed)
    return min(contiguous) + max(contiguous)


def find_solution_a():
    return find_disallowed_number(PUZZLEINPUT)

def find_solution_b():
    return break_encryption(PUZZLEINPUT)