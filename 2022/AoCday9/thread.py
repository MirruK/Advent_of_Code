import math
def formatdata():
    instructions = []
    # Map strings to numbers, not really something you need to do for this
    direction_dict = {"L" : 4, "R" : 6, "U" : 8, "D" : 2}
    with open("./input.txt",'r') as file:
        for line in file.readlines():
            direction = line.split()[0]
            times = int(line.split()[1])
            instructions.append((direction_dict[direction], times))
    return instructions

def calc_vector(pos1,pos2):
    xhead,yhead = pos1
    xtail,ytail = pos2
    diff = (xhead-xtail,yhead-ytail)
    # If we got here that means we are a tail following a tail
    # That is moving diagonally, in that case follow it diagonally
    if abs(diff[0]) == abs(diff[1]):
        return (diff[0]/2,diff[1]/2)
    # Check in which direction the change is greater
    if abs(diff[0])>abs(diff[1]):
        bigger = 0
    else: bigger = 1
    # We want to not move ontop of the head but one behind it
    # Flipped sign just varies between positive and negative depending on direction
    flipped_sign = -1*(diff[bigger]/abs(diff[bigger]))
    modified_diff = (diff[0]+flipped_sign,diff[1]) if bigger == 0 else (diff[0],diff[1]+flipped_sign)
    return modified_diff


def follow(poshead,postail) -> tuple[int, int]:
    head_x, head_y = poshead
    tail_x, tail_y = postail
    if poshead == postail:
        return postail
    if math.sqrt((head_x-tail_x)**2+(head_y-tail_y)**2) < 2:
        return postail
    else:
        change = calc_vector(poshead,postail)
        #print(f"Head: {poshead}, Tail: {postail}, Change Vector: {change}")
        return (tail_x+change[0],tail_y+change[1])


def move_head(pos, direction) -> tuple[int, int]:
    head_x = pos[0]
    head_y = pos[1]
    # Python 3.10 go brrr
    match direction:
        case 2:
            return (head_x, head_y-1)
        case 4:
            return (head_x-1, head_y)
        case 6:
            return (head_x+1, head_y)
        case 8:
            return (head_x, head_y+1)

def simulate_multiple():
    visited = []
    instructions = formatdata()
    # Initialize head
    head_pos = (0,0)
    # Initialize list of 9 tails
    tails = [(0,0) for _ in range(9)]
    for inst in instructions:
        # Move as many units as is specified in the input
        for n in range(inst[1]):
            head_pos = move_head(head_pos, inst[0])
            # Only the first tail follows the head
            tails[0] = follow(head_pos,tails[0])
            # The rest of the tails follow the tail in front of it
            for n in range(1,len(tails)):
                tails[n] = follow(tails[n-1],tails[n])
            visited.append(tails[-1])
    # Conversion to set ensures we don't count duplicates
    return len(set(visited))

def simulate():
    visited = []
    instructions = formatdata()
    # Initialize head
    head_pos = (0,0)
    # Initialize list of 9 tails
    tail = (0,0)
    for inst in instructions:
        # Move as many units as is specified in the input
        for n in range(inst[1]):
            head_pos = move_head(head_pos, inst[0])
            # Tail follows the head
            tail = follow(head_pos,tail)
            visited.append(tail)
    # Conversion to set ensures we don't count duplicates
    return len(set(visited))

print("First Answer:",simulate())
print("Second Answer:",simulate_multiple())