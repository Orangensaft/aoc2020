from collections import defaultdict

from day7.puzzleinput import PUZZLEINPUT


def find_solution_a():  # pragma: nocover
    return len(count_bags("shiny gold", PUZZLEINPUT))


def find_solution_b():  # pragma: nocover
    return count_subbags("shiny gold", PUZZLEINPUT)

def parse_rule(rule_str):
    "light red bags contain 1 bright white bag, 2 muted yellow bags."
    rules_up = {}
    rules = []
    rule_str = rule_str.replace(" bags","").replace(" bag","").replace(".","")
    source_color, rest = rule_str.split(" contain ")
    if rest == "no other":
        rules.append((None, 0))
        rules_up[None] = (source_color, 0)
    else:
        contains = rest.split(", ")
        for content in contains:
            num, target = content.split(" ",1)
            rules.append((target, int(num)))
            rules_up[target] = (source_color, int(num))
    rules_down = {source_color : rules}

    return rules_down, rules_up


def parse_multiple_rules(rules):
    up_rules = defaultdict(list)
    down_rules = {}
    for rule in rules.split("\n"):
        down, up = parse_rule(rule)
        down_rules.update(down)
        for key, value in up.items():
            up_rules[key].append(value)
    return up_rules, down_rules


def count_bags(start, rules: str):
    up_rules, _ = parse_multiple_rules(rules)
    return count_bag_recursive(start, up_rules)


def count_bag_recursive(target_color, rules:dict):
    #get direct neighbors
    colors = set([c[0] for c in rules[target_color]])  # [color1, color2, ...]
    others = set()

    #for each neighbor
    for color in colors:
        r = count_bag_recursive(color, rules)  # recursion
        others = others.union(r)

    return colors.union(others)  # set of all colors


def count_subbags(target_color, rules: str):
    _, down_rules = parse_multiple_rules(rules)
    return count_subbags_recursive(target_color, down_rules)


def count_subbags_recursive(target, rules):
    count = 0

    #get direct ones
    direct = rules[target]
    if direct[0][0] is None:  # contains nothing
        return 0

    for color, amount in direct:
        # this bag contains n bags of that color + the bags contained in it
        count += amount + (amount * count_subbags_recursive(color,rules))

    return count
