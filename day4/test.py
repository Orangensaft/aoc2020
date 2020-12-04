from unittest import TestCase

from day4.solution import read_passports, is_valid, count_valid_passports, validate_field

PUZZLEINPUT = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

INVALID_PASSPORTS = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007"""

VALID_PASSPORTS = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""


class Test(TestCase):

    def setUp(self):
        self.passports = read_passports(PUZZLEINPUT)
        self.invalid = read_passports(INVALID_PASSPORTS)
        self.valid = read_passports(VALID_PASSPORTS)

    def test_read_passports_count(self):
        self.assertTrue(len(self.passports), 4)

    def test_first_passport_valid(self):
        self.assertTrue(is_valid(self.passports[0]))

    def test_second_passport_invalid(self):
        self.assertFalse(is_valid(self.passports[1]))

    def test_optional_field_missing(self):
        self.assertTrue(is_valid(self.passports[2], prints=True))

    def test_missing_too_much(self):
        self.assertFalse(is_valid(self.passports[3]))

    def test_number_of_valid_passports(self):
        self.assertEqual(2, count_valid_passports(self.passports))

    def test_byr_validation(self):
        self.assertTrue(validate_field("byr", "1920"))
        self.assertTrue(validate_field("byr", "2002"))
        self.assertFalse(validate_field("byr", "2003"))
        self.assertFalse(validate_field("byr", "1919"))
        self.assertFalse(validate_field("byr", "ASDF"))

    def test_iyr_validation(self):
        self.assertTrue(validate_field("iyr", "2010"))
        self.assertTrue(validate_field("iyr", "2020"))
        self.assertFalse(validate_field("iyr", "2009"))
        self.assertFalse(validate_field("iyr", "2021"))
        self.assertFalse(validate_field("iyr", "ASDF"))

    def test_eyr_validation(self):
        self.assertTrue(validate_field("eyr", "2020"))
        self.assertTrue(validate_field("eyr", "2030"))
        self.assertFalse(validate_field("eyr", "2019"))
        self.assertFalse(validate_field("eyr", "2031"))
        self.assertFalse(validate_field("eyr", "ASDF"))

    def test_hgt_validation(self):
        self.assertTrue(validate_field("hgt", "59in"))
        self.assertTrue(validate_field("hgt", "76in"))
        self.assertFalse(validate_field("hgt", "77in"))
        self.assertFalse(validate_field("hgt", "58in"))
        self.assertTrue(validate_field("hgt", "150cm"))
        self.assertTrue(validate_field("hgt", "193cm"))
        self.assertFalse(validate_field("hgt", "149cm"))
        self.assertFalse(validate_field("hgt", "194cm"))
        self.assertFalse(validate_field("hgt", "0.1cm"))

    def test_hcl_validation(self):
        self.assertTrue(validate_field("hcl", "#123123"))
        self.assertTrue(validate_field("hcl", "#ffffff"))
        self.assertTrue(validate_field("hcl", "#12ff12"))
        self.assertFalse(validate_field("hcl", "##"))
        self.assertFalse(validate_field("hcl", "123"))
        self.assertFalse(validate_field("hcl", "123123"))

    def test_ecl_validation(self):
        allowed = "amb blu brn gry grn hzl oth".split(" ")
        for a in allowed:
            self.assertTrue(validate_field("ecl", a))

        self.assertFalse(validate_field("ecl", "WAT"))

    def test_pid_validation(self):
        self.assertTrue(validate_field("pid", "000000001"))
        self.assertFalse(validate_field("pid", "0000000001"))
        self.assertFalse(validate_field("pid", "00a000001"))
        self.assertTrue(validate_field("pid", "000000000"))
        self.assertTrue(validate_field("pid", "005000000"))

    def test_all_invalids(self):
        for p in self.invalid:
            self.assertFalse(is_valid(p, part2=True, prints=True), f"Passport {p} passes validation!")

    def test_all_valids(self):
        for p in self.valid:
            self.assertTrue(is_valid(p, part2=True, prints=True), f"Passport {p} passes validation!")

    def test_count_valid(self):
        self.assertEqual(count_valid_passports(read_passports(PUZZLEINPUT), part2=True), 2)
