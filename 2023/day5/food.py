import re


class ConversionMap():
    def __iter__():
        """Yields ranges of numbers representing gaps or areas that map seeds"""
        pass


x = open(0)
nums = list(map(int, re.findall(r"\d+", x.readline().split(": ")[1])))
temp: list[str] = []

categorized = []
for line in x.readlines():
    if line.strip() == "":
        categorized.append(temp)
        temp = []
    else:
        temp.append(line.strip())
if len(temp) != 0:
    categorized.append(temp)

categorized = categorized[1:]
order_of_operations = []
label_to_values = {}
for lab_and_vals in categorized:
    label, values = lab_and_vals[0], lab_and_vals[1:]
    order_of_operations.append(label)
    label_to_values[label] = values


def is_outside(val: int, lower_bound: int, upper_bound: int) -> bool:
    return val < lower_bound or val > upper_bound


def is_outside_range(rang: tuple[int, int], lower_bound: int, upper_bound: int) -> bool:
    range_lower, range_upper = rang
    return (range_upper < lower_bound) or (range_lower > upper_bound)


def is_outside_range_revised(rang: tuple[int, int], mapper: dict[tuple[int, int], int]) -> bool:
    for key in mapper:
        lower = key[0]
        upper = key[1]
        if not is_outside_range(rang, lower, upper):
            return False
    return True


def conversionrange_to_tuple(conversion_range: str):
    return list(
        map(int, re.findall(r"\d+", conversion_range)))


def convert_seed(seed: int, conversion_range: list[str]):
    for conversion in conversion_range:
        output_range_start, input_range_start, range_extent = conversionrange_to_tuple(
            conversion)
        outside_range = is_outside(
            seed, input_range_start, input_range_start+range_extent-1)
        if not outside_range:
            return seed + (output_range_start - input_range_start)
    return seed


def range_is_valid(rang: tuple[int, int]) -> bool:
    return rang[0] <= rang[1]


def match_case(seed_range: tuple[int, int], converter_range: tuple[int, int]):
    # Returns 1 if seed_range upper part overlaps with converter_range
    # Returns 0 if seed_range is within or ontop of converter_range
    # Returns -1 if lower part within converter_range
    # returns 2 if seed_range overlaps and extends beyond converter_range
    l1 = seed_range[0]
    l2 = converter_range[0]
    h1 = seed_range[1]
    h2 = converter_range[1]
    if l1 < l2 and h1 < h2:
        return 1
    if l1 >= l2 and h1 <= h2:
        return 0
    if l1 > l2 and h1 > h2:
        return -1
    if l1 < l2 and h1 > h2:
        return 2


def find_conversion_factor(mapper: dict[tuple[int, int], int], seed_value: int) -> int:
    for key in mapper.keys():
        curr_range_start = key[0]
        curr_range_end = key[1]
        if seed_value >= curr_range_start and seed_value <= curr_range_end:
            return mapper[key]
    return 0


def map_seed_range(seed_range: tuple[int, int], mapper, conversions: list[str]) -> list[tuple[int, int]]:
    """
    Revised version: return new seed ranges that either get converted or not, no recursion needed
    Like convert_one_range but no unfinished seeds remain
    """
    """Takes one seed range and instructions for how to convert it
        Returns: A tuple containing a range of seeds that have been modified, 
        and the rest of the seeds to be processed further"""
    # 1. Is range a part of mapper keys at all?
    # Ex. mapper of ranges and gaps
    # ################..........######..###.............#############
    #  seed_range:          ######################
    # splits into           ----++++++--+++------- five ranges of seeds
    outside_range = is_outside_range_revised(
        seed_range, mapper)
    if not outside_range:
        offset = (output_range_start - input_range_start)
        l1 = seed_range[0]
        l2 = input_range_start
        h1 = seed_range[1]
        h2 = input_range_start + range_extent - 1
        match(match_case(seed_range, (l2,
                                      h2))):
            case 1:
                return ((l2 + offset, h1 + offset),
                        [(l1, l2-1),
                        (h2+1, h1)])
            case 0:
                return ((l1+offset, h1+offset),
                        [])
            case 1:
                return ((l1 + offset, h2 + offset),
                        [(l2, l1-1),
                        (h2+1, h1)])
            case 2:
                return ((l2 + offset, h2 + offset),
                        list(filter(range_is_valid, [(l1, l2-1), (h2+1, h1)])))
    return (None, [seed_range])
    return []
    # return seed_value + find_conversion_factor(mapper, seed_value)


def create_mapper_range_aggregate(ranges: list[str]):
    # Dict keys: tuple[start, end] => values: int (how much to add to seed if it falls in range)
    for r in ranges:
        map_to_start, map_from_start, range_size = conversionrange_to_tuple(r)


def convert_one_range(seed_range: tuple[int, int], conversion: str) -> tuple[tuple[int, int] | None, list[tuple[int, int]]]:
    """Takes one seed range and instructions for how to convert it
        Returns: A tuple containing a range of seeds that have been modified, 
        and the rest of the seeds to be processed further"""
    output_range_start, input_range_start, range_extent = conversionrange_to_tuple(
        conversion)
    outside_range = is_outside_range(
        seed_range, input_range_start, input_range_start+range_extent-1)
    if not outside_range:
        # black magic needed
        # Ex (54 60) ()
        offset = (output_range_start - input_range_start)
        l1 = seed_range[0]
        l2 = input_range_start
        h1 = seed_range[1]
        h2 = input_range_start + range_extent - 1
        match(match_case(seed_range, (l2,
                                      h2))):
            case 1:
                return ((l2 + offset, h1 + offset),
                        [(l1, l2-1),
                        (h2+1, h1)])
            case 0:
                return ((l1+offset, h1+offset),
                        [])
            case 1:
                return ((l1 + offset, h2 + offset),
                        [(l2, l1-1),
                        (h2+1, h1)])
            case 2:
                return ((l2 + offset, h2 + offset),
                        list(filter(range_is_valid, [(l1, l2-1), (h2+1, h1)])))
    return (None, [seed_range])


def convert_seed_range(seed_ranges: list[tuple[int, int]], conversion_range: list[str]) -> list[tuple[int, int]]:
    print(f"Unconverted seed ranges: {seed_ranges}")
    if len(seed_ranges) == 0 or len(conversion_range) == 0:
        return seed_ranges
    finished_seeds_ls = []
    unconverted_seeds_ls: list[tuple[int, int]] = []
    for seed_range in seed_ranges:
        finished_seeds, unconverted_seeds = convert_one_range(
            seed_range, conversion_range[0])
        if finished_seeds is not None:
            finished_seeds_ls.append(finished_seeds)
        unconverted_seeds_ls + unconverted_seeds
    print(f"Now converted seeds: {finished_seeds_ls}")

    # print(f"converting range {unconverted_seeds}")
    return finished_seeds_ls + convert_seed_range(unconverted_seeds_ls, conversion_range[1:])


seeds = nums
seed_ranges: list[tuple[int, int]] = []
for i, seed in enumerate(seeds):
    if i % 2 == 0:
        # print(seed+seeds[i+1]-1)
        seed_ranges.append((seed, seed+seeds[i+1]-1))
# print(seeds)
for key in order_of_operations:
    value = label_to_values[key]
    # print(value)
    seeds = list(map(lambda x: convert_seed(x, value), seeds))
    new_seed_ranges: list[tuple[int, int]] = []
    mapper = create_mapper_range_aggregate(value)
    for seed_range in seed_ranges:
        new_seed_ranges += convert_seed_range([seed_range], value)
        # new_seed_ranges += map_seed_range(seed_range, mapper, value)
    seed_ranges = new_seed_ranges
    print(seed_ranges)
    new_seed_ranges = []


# print(seed_ranges)
# print(list(map(lambda x: convert_seed_range(x, value), seed_ranges)))
# print(seeds)
print(f"Part 1 --> {min(seeds)}")
print(f"Part 2 --> {min(map(lambda tup: min(tup), seed_ranges))}")
