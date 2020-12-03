from .puzzleinput import PUZZLEINPUT


class DatabaseEntry:
    def __init__(self, line: str):
        policy, password = line.split(": ")
        counts ,self.policy_letter = policy.split(" ")
        min_amount, max_amount = counts.split("-")
        self.min_amount = int(min_amount)
        self.max_amount = int(max_amount)
        self.password = password

    def is_valid(self):
        return self.min_amount <= self.password.count(self.policy_letter) <= self.max_amount


class DatabaseEntryNew(DatabaseEntry):
    def is_valid(self):
        pos1 = self.password[self.min_amount - 1]  # 1-indexed
        pos2 = self.password[self.max_amount - 1]
        pos1_valid = pos1 == self.policy_letter
        pos2_valid = pos2 == self.policy_letter
        return pos1_valid != pos2_valid  # xor


def preprocess_input(part2=False):
    """
    Convert puzzle input to class representations

    :param part2: If true, the policy from part 2 will be used
    :return: Number of valid entries
    """
    lines = PUZZLEINPUT.split("\n")
    EntryClass = DatabaseEntryNew if part2 else DatabaseEntry
    entries = [EntryClass(line) for line in lines]
    return entries


def find_solution_a():
    entries = preprocess_input()
    return [e.is_valid() for e in entries].count(True)


def find_solution_b():
    entries = preprocess_input(part2=True)
    return [e.is_valid() for e in entries].count(True)
