import re

from day4.puzzleinput import PUZZLEINPUT


def read_passports(puzzle_input: str):
    passports_raw = [line.replace("\n", " ") for line in puzzle_input.split("\n\n")]
    passports = []
    for entry in passports_raw:
        passport = {}
        pairs = [e.split(":") for e in entry.split(" ")]
        for key, value in pairs:
            passport[key] = value
        passports.append(passport)
    return passports


def is_valid(passport: dict, part2=False, prints=False):
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    optional = ["cid"]
    if prints:
        print("Checking "+str(passport))
    for fieldname in fields:
        if fieldname not in optional and fieldname not in passport:
            if prints:
                print(f"⚠ {fieldname} missing ⚠")
            return False
    if part2:
        # do part 2 validations
        for field, value in passport.items():
            if not validate_field(field, value):
                if prints:
                    print(f"{field} = {value} ❌")
                return False
            elif prints:
                print(f"{field} = {value} ✔")
    return True


def count_valid_passports(passports, part2=False):
    return [is_valid(p, part2) for p in passports].count(True)


def find_solution_a():  # pragma: nocover
    passports = read_passports(PUZZLEINPUT)
    return count_valid_passports(passports)


def is_int(x, length):
    if len(x) != length:
        return False
    try:
        int(x)
        return True
    except ValueError:
        return False


def validate_height(h: str):
    regexp = re.compile(r"(\d*)(cm|in)")
    match = regexp.fullmatch(h)
    if not match:
        return False
    height, unit = match.groups()
    if unit == "in":
        return 59 <= int(height) <= 76
    else:
        return 150 <= int(height) <= 193


VALIDATIONS = {
    "byr": lambda x: is_int(x, 4) and 1920 <= int(x) <= 2002,
    "iyr": lambda x: is_int(x, 4) and 2010 <= int(x) <= 2020,
    "eyr": lambda x: is_int(x, 4) and 2020 <= int(x) <= 2030,
    "hcl": lambda x: re.compile("^#([0-9a-f]{6})$").fullmatch(x) is not None,
    "hgt": validate_height,
    "ecl": lambda x: x in "amb blu brn gry grn hzl oth".split(" "),
    "pid": lambda x: is_int(x, 9),
    "cid": lambda x: True
}


def validate_field(fieldname, value):
    validator = VALIDATIONS.get(fieldname, lambda x: True)
    return validator(value)


def find_solution_b():  # pragma: nocover
    passports = read_passports(PUZZLEINPUT)
    return count_valid_passports(passports, True)
