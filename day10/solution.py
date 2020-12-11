from functools import lru_cache


def find_chain(adapters: str):
    adapters = map(int, adapters.split("\n"))
    chain = sorted(adapters)
    # add wall and device
    chain.insert(0, 0)
    chain.append(max(chain)+3)
    return chain


def calc_differences(adapters: str):
    chain = find_chain(adapters)
    diffs = []
    for i in range(len(chain)-1):
        diffs.append( chain[i+1] - chain[i])
    return diffs


def calc_solution_a(adapters: str):
    diffs = calc_differences(adapters)
    return diffs.count(1) * diffs.count(3)


def is_possible_chain(chain: [int]):
    for i in range(len(chain)-1):
        if chain[i+1] - chain[i] >3:
            return False
    return True


def count_solutions_memsafe(adapters: str):
    adapters = find_chain(adapters)
    adapters.pop(0) # remove the wall plug
    lastelem = max(adapters)
    solutions = find_solutions_memsafe(0, tuple(adapters), lastelem)
    return solutions

@lru_cache
def find_possible_fits(current: int, adapters: [int]):
    possible = []
    for r in adapters:
        if 0 < r - current <= 3:
            possible.append(r)
    return possible

@lru_cache
def find_solutions_memsafe(cur: int, adapters: [int], target: int):
    if cur == target:
        # this is a solution
        return 1

    possible_next = find_possible_fits(cur, adapters)
    if len(possible_next) == 0:
        # For the current adapters selected, there are no remaining solutions left
        return 0

    total = 0
    for a in possible_next:
        results = find_solutions_memsafe(a, adapters, target)

        total += results

    return total


def find_solution_a():  # pragma: nocover
    from .puzzleinput import PUZZLEINPUT
    return calc_solution_a(PUZZLEINPUT)


def find_solution_b():  # pragma: nocover
    from .puzzleinput import PUZZLEINPUT
    return count_solutions_memsafe(PUZZLEINPUT)