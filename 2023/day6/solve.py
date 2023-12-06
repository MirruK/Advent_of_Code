from cmath import sqrt
from math import prod
import re
from functools import reduce

def solve_quadratic(a: int, b: int, c: int) -> tuple[complex, complex]:
    # calculate the discriminant
    d = (b**2) - (4*a*c)
    # find two solutions
    sol1 = (-b-sqrt(d))/(2*a)
    sol2 = (-b+sqrt(d))/(2*a)
    return (sol1, sol2) if sol1.real < sol2.real else (sol2, sol1)

def get_rows():
    return list(map(str.strip, open(0).readlines()))

def parse_input(rows: list[str]) -> list[tuple[int, int]]:
    times, distances = list(map(lambda row: tuple(map(int, re.findall(r"\d+", row))), rows))
    return list(zip(times, distances))
    
def parse_input_pt2(rows: list[str]) -> tuple[int, int]:
    temp_pt2 = list(map(lambda row: re.findall(r"\d+", row), rows))
    return tuple(map(lambda x: reduce(lambda acc, curr: acc + curr, x, ""), temp_pt2))


#     x * (52 - x)   = 426
# => -x² + 52x - 426 = 0
# => where x is the time you hold the button
# => and 52 is the time of the game
# => and 426 the distance
solutions = []
rows = get_rows()
times_and_distances = parse_input(rows)

# Part 1
for (time, max_distance) in times_and_distances:
    lower, upper = map(lambda z: z.real, solve_quadratic(-1,time, -max_distance-1))
    lower, upper = [int(lower+1) if lower != int(lower) else int(lower), int(upper)]
    solutions.append((upper+1) - lower)


# Part 2
(time_pt2, dist_pt2) = map(int,parse_input_pt2(rows))
# Get real components of roots to quadratic equation
lower_pt2, upper_pt2 = map(lambda z: z.real, solve_quadratic(-1,time_pt2, -dist_pt2-1))
# Round the lower float up and the upper float down because only integers are accounted for in this game
lower_pt2, upper_pt2 = [int(lower_pt2+1) if lower_pt2 != int(lower_pt2) else int(lower_pt2), int(upper_pt2)]
# Solution is how many numbers lie within the range, that is, how many total ways to win
solution_pt2 = ((upper_pt2+1) - lower_pt2)

print(f"Part 1 -> {prod(solutions)}")
print(f"Part 2 -> {solution_pt2}")
