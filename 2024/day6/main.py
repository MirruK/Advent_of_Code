def get(space: list[list[str]], coord: tuple[int, int]) -> str | None:
    row, col = coord
    if row < 0 or col < 0:
        return None
    if row > len(space)-1 or col > len(space[0]) - 1:
        return None
    return space[row][col]


def traverse(dir: int, space: list[list[str]], current_pos) -> tuple[int, tuple[int, int]] | None:
    match dir:
        case 0:
            next_pos = (current_pos[0] - 1, current_pos[1])
            next_tile = get(space, next_pos)
            if next_tile is None:
                return None
            if next_tile == "#":
                return ((dir + 1) % 4, current_pos)
            return (dir, next_pos)
        case 1:
            next_pos = (current_pos[0], current_pos[1]+1)
            next_tile = get(space, next_pos)
            if next_tile is None:
                return None
            if next_tile == "#":
                return ((dir + 1) % 4, current_pos)
            return (dir, next_pos)
        case 2:
            next_pos = (current_pos[0] + 1, current_pos[1])
            next_tile = get(space, next_pos)
            if next_tile is None:
                return None
            if next_tile == "#":
                return ((dir + 1) % 4, current_pos)
            return (dir, next_pos)
        case 3:
            next_pos = (current_pos[0], current_pos[1] - 1)
            next_tile = get(space, next_pos)
            if next_tile is None:
                return None
            if next_tile == "#":
                return ((dir + 1) % 4, current_pos)

    return (dir, next_pos)


def find_start(space: list[list[str]]) -> tuple[int, int] | None:
    for i in range(len(space)):
        for j in range(len(space[i])):
            if space[i][j] == '^':
                return (i, j)


def walked_in_direction(markings: list[tuple[int, tuple[int, int], int]], direction_pos_order: tuple[int, tuple[int, int], int]) -> bool:
    direction, pos, order = direction_pos_order
    match direction:
        case 0: return len(list(filter(lambda x: x[0] == direction and x[1][0] <= pos[0] and x[1][1] == pos[1] and order >= x[2], markings))) > 0
        case 1: return len(list(filter(lambda x: x[0] == direction and x[1][1] >= pos[1] and x[1][0] == pos[0] and order >= x[2], markings))) > 0
        case 2: return len(list(filter(lambda x: x[0] == direction and x[1][0] >= pos[0] and x[1][1] == pos[1] and order >= x[2], markings))) > 0
        case 3: return len(list(filter(lambda x: x[0] == direction and x[1][1] <= pos[1] and x[1][0] == pos[0] and order >= x[2], markings))) > 0


with open(0) as f:
    lines = list(map(lambda x: x.removesuffix("\n"), f.readlines()))


# 0 - up, 1 - right, 2 - down, 3 - left
direction = 0
pos = find_start(lines)
markings = [pos]
turns = []
direction_pos_order = [(direction, pos, 0)]
# If head is None it is out of bounds
markings_count = 1
while (pos is not None):
    traverse_res = traverse(direction, lines, pos)
    if traverse_res is None:
        # We walked off the map
        break
    old_pos = pos
    direction, pos = traverse_res

    if old_pos != pos:
        markings.append(pos)
        direction_pos_order.append(
            (traverse_res[0], traverse_res[1], markings_count))
        markings_count += 1
    else:
        turns.append((*traverse_res, markings_count))


dupes = []
counted = []
for e in direction_pos_order:
    # count = direction_pos_order.count(
    #     e) + direction_pos_order.count(((e[0]+1) % 4, e[1]))
    if walked_in_direction(direction_pos_order, ((e[0]+1) % 4, e[1], e[2])):
        dupes.append(e)
dupes_set = []
for d in dupes:
    # if d not in map(lambda x: ((x[0]-1) % 4, x[1]), turns):
    dupes_set.append(d)
print(dupes_set)
print(len(dupes_set))
