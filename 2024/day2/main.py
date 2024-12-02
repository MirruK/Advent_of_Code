# Pass input via stdin "cat input.txt | python main.py"

def sign(x):
    if x == 0:
        return None
    return -1 if x < 0 else 1


def determine_validity(report: list[int]):
    prev_diff = 0
    for i in range(1, len(report)):
        diff = report[i] - report[i-1]
        if i == 1:
            if sign(diff) == 0 or diff > 3 or diff < -3:
                return False
            prev_diff = diff
            continue
        if sign(prev_diff) != sign(diff) or (diff > 3 or diff < -3) or sign(prev_diff) == 0:
            return False

    return True


def get_alternatives(report: list[int]):
    reports = []
    for i in range(0, len(report)):
        reports.append(report[:i]+report[1+i:])
    return reports


with open(0) as f:
    lines = f.readlines()
    reports = list(map(lambda x: list(
        map(lambda y: int(y.removesuffix("\n")), x.split(" "))), lines))


part1_count = 0
for r in reports:
    if determine_validity(r):
        part1_count += 1

new_reports = list(map(get_alternatives, reports))

count = 0
for rs in new_reports:
    if any(map(lambda x: determine_validity(x), rs)):
        count += 1


print(f"Part 1 answer: {part1_count}")
print(f"Part 2 answer: {count}")
