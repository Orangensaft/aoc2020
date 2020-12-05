from day5.puzleinput import PUZZLEINPUT


def partition(lower, upper, direction):
    old_width = (upper-lower+1)  # Number of seats
    if direction in "FL":
        new_lower = lower
        new_upper = lower + old_width // 2 - 1
    else:
        new_lower = upper - old_width // 2 + 1
        new_upper = upper
    return new_lower, new_upper  # if last seat is reached, both are equal


def find_row_id(directions: str, find_row=True):
    if find_row:
        l, u = 0, 127
    else:
        l, u = 0, 7
    for direction in directions:
        l, u = partition(l, u, direction)
    return l


def find_coords(directions: str):
    row_directions = directions[:7]
    seat_directions = directions[7:]
    return find_row_id(row_directions), find_row_id(seat_directions, False)


def find_seat_id(directions: str):
    coords = find_coords(directions)
    return coords[0] * 8 + coords[1]


def get_highest_id(passes):
    return max(get_all_seat_ids(passes))


def get_all_seat_ids(passes):
    ids = [find_seat_id(p) for p in passes.split("\n")]
    return ids


def get_missing_id(ids):
    ids = sorted(ids)
    for i in range(len(ids)-1):
        cur = ids[i]
        n = ids[i+1]
        if cur+2 == n:
            return cur+1  # the next one is 2 away, meaning a "hole" of 1


def find_solution_a():  # pragma: nocover
    return get_highest_id(PUZZLEINPUT)


def find_solution_b():  # pragma: nocover
    ids = get_all_seat_ids(PUZZLEINPUT)
    missing = get_missing_id(ids)
    return missing
