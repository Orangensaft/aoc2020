from day6.puzzleinput import PUZZLEINPUT

"""
Idea: convert answers of each person into a bitvector where bit n is 1 if the answer as given where
n=0 -> a
n=1 -> b
...
n=25 -> z

To find the answers that were given at least once bitwise or the vectors and count the 1s
To find the answers that were given from everyone bitwise and the vectors and count the 1s
"""


def find_solution_a():  # pragma: nocover
    return get_sum_of_answers(PUZZLEINPUT)


def find_solution_b():  # pragma: nocover
    return get_sum_by_everyone(PUZZLEINPUT)


def get_sum_of_answers(groups):
    groups = groups.split("\n\n")
    return sum(count_group_answers(g.split("\n")) for g in groups)


def get_sum_by_everyone(groups):
    groups = groups.split("\n\n")
    return sum( count_group_answers_all(g.split("\n")) for g in groups )


def get_char_value(c):
    return 2**(122-ord(c))


def get_bitvector(person):
    total = 0
    for c in person:
        total += get_char_value(c)
    return total


def get_group_answers_bitwise(group):
    answers = 0b0
    for p in group:
        answers |= get_bitvector(p)
    return answers


def count_group_answers(group):
    answers = get_group_answers_bitwise(group)
    return bin(answers).count("1")


def count_group_answers_all(group):
    answers = get_bitvector("abcdefghijklmnopqrstuvwxyz")
    for p in group:
        answers &= get_bitvector(p)
    return bin(answers).count("1")