from functools import partial
from functools import cmp_to_key

with open(0) as f:
    lines = f.readlines()
    rules: list[str] = []
    i = 0
    while lines[i] != "\n":
        rules.append(lines[i])
        i += 1
    i += 1
    updates = list(
        map(lambda x: list(map(int, x.removesuffix("\n").split(","))), lines[i:]))
    rules = list(
        map(lambda x: tuple(map(int, x.removesuffix("\n").split("|"))), rules))


def define_rules(rules: list[tuple[int, int]]) -> dict[int, list[int]]:
    rule_dict = {}
    for rule in rules:
        rule_dict[rule[0]] = rule_dict.get(rule[0], []) + [rule[1]]

    return rule_dict


def check_validity(update: list[int], rules: dict[int, list[int]]) -> bool:
    v = []
    for idx, num in enumerate(update):
        for rule in rules.get(num, []):
            if rule not in update or (update.count(rule) and idx < update.index(rule)):
                v.append(True)
            else:
                v.append(False)
    return v


def comparator(rules: dict[int, list[int]], x: int, y: int):
    if y in rules.get(x, []):
        return 1
    return -1


def fix_update(update: list[int], keyfunc) -> list[int]:
    if len(update) < 2:
        return update
    return sorted(update, key=keyfunc)


def get_middle(ls: list):
    return ls[int(len(ls) / 2)]


# print(rules)
rules = define_rules(rules)
# print(updates)

valid_updates = []
invalid_updates = []
for update in updates:
    if all(check_validity(update, rules)):
        valid_updates.append(update)
    else:
        invalid_updates.append(update)


keyfunc = cmp_to_key(partial(comparator, rules))

print(f"Part 1: {sum(map(get_middle, valid_updates))}")
print(f"Part 2: {
      sum(map(get_middle, map(lambda x: fix_update(x, keyfunc), invalid_updates)))}")
