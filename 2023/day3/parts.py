import re


def check_adj(haystack: list[str], index: int, cols: int, num: int, gear_map: list[list[int]]) -> bool:
    adj = [1, -1, cols, cols+1, cols-1, -cols, -cols+1, -cols-1]
    valid_indices = [index+n for n in adj if (
        index + n < len(haystack)) and (index + n > 0)]
    found_true = False
    for i in valid_indices:
        cond = (not haystack[i].isdigit() and haystack[i] != ".")
        if cond:
            found_true = True
        if haystack[i] == "*":
            gear_map[i].append(num)
    return found_true


rows = 0
cols = 0
parts = []
nums = []

for line in open("input.txt"):
    line_list = list(line.strip())
    cols = len(line_list)
    rows += 1
    parts += line_list

parts_str = ''.join(parts)
nums = [n for n in re.split("[^0-9]", parts_str)
        if n.isdigit()]
valid_parts = []
skip_count = 0

gear_map: list[list[int]] = [[] for n in parts]

for num in nums:
    ind = parts_str.find(num, skip_count)
    skip_count += (ind-skip_count)
    for i in range(len(num)):
        if check_adj(parts, ind+i, cols, int(num), gear_map):
            valid_parts.append(int(num))
            skip_count += len(num)-1
            break

    skip_count += len(num)-1


gear_sum = 0
for ls in gear_map:
    if len(ls) == 2:
        gear_sum += (ls[0] * ls[1])

print(f"Part 1 valid parts sum -> {sum(valid_parts)}")
print(f"Part 2 gear ratio sum -> {gear_sum}")
