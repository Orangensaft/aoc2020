from unittest import TestCase

from day7.solution import parse_rule, parse_multiple_rules, count_bag_recursive, count_bags, count_subbags


class TestsDay7(TestCase):
    def test_read_rule(self):
        rule_str = "light red bags contain 1 bright white bag, 2 muted yellow bags."
        rule_down, rule_up = parse_rule(rule_str)

        #light red has to contain 1xbright white, 2xmuted yellow
        expected_down = {
            "light red" : [("bright white",1), ("muted yellow",2)]
        }

        # a bright white one could be in a light_red one
        # a muted yellow one could be twice in a light_red one
        expected_up = {
            "bright white" : ("light red",1),
            "muted yellow" : ("light red",2)
        }

        self.assertEqual(rule_down, expected_down)
        self.assertEqual(rule_up, expected_up)

    def test_single_rule(self):
        rule_str = "bright white bags contain 1 shiny gold bag."
        rule_down, rule_up = parse_rule(rule_str)

        # light red has to contain 1xbright white, 2xmuted yellow
        expected_down = {
            "bright white": [("shiny gold", 1)]
        }

        # a bright white one could be in a light_red one
        # a muted yellow one could be twice in a light_red one
        expected_up = {
            "shiny gold": ("bright white", 1),
        }

        self.assertEqual(expected_up, rule_up)
        self.assertEqual(expected_down, rule_down)

    def test_empty_rule(self):
        rule_str = "faded blue bags contain no other bags."
        rule_down, rule_up = parse_rule(rule_str)

        expected_down = {
            "faded blue": [(None, 0)]
        }

        expected_up = {
            None: ("faded blue", 0)
        }

        self.assertEqual(expected_up, rule_up)
        self.assertEqual(expected_down, rule_down)

    def test_parse_multiple(self):
        rules = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""
        up_rules, down_rules = parse_multiple_rules(rules)

        self.assertEqual(8,len(up_rules))
        self.assertEqual(9,len(down_rules))


    def test_count_contains(self):
        rules = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

        possible_bags = count_bags("shiny gold", rules)

        self.assertEqual(4, len(possible_bags))
        for i in ["light red", "dark orange", "bright white", "muted yellow"]:
            self.assertIn(i, possible_bags)

    def test_count_subbags(self):
        rules = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""

        subbags = count_subbags("shiny gold", rules)
        self.assertEqual(126, subbags)

    def test_count_subbags_part_a(self):
        rules = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""
        subbags = count_subbags("shiny gold", rules)
        self.assertEqual(32, subbags)