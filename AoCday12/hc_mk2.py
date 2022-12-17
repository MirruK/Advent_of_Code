from collections import deque
def formatdata():
    matrix = []
    with open("./input.txt") as file:
        for line in file.readlines():
            matrix.append(list(line.removesuffix("\n")))
    return matrix

def find_start_pos(matrix):
    start, end = (None,None), (None,None)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if start != (None,None) and end != (None,None):
                return start, end
            if matrix[i][j] == "S":
                start = (i,j)
            if matrix[i][j] == "E":
                end = (i,j)

def ascii_diff(curr_char,next_char):
    diff = ord(next_char) - ord(curr_char)
    return diff if diff == 1 or diff == 0 or diff < 0 else 1000

def move(pos,matrix,direction):
    #POS 1 = left, right
    #POS 0 = up, down
    height = len(matrix)
    width = len(matrix[0])
    #0: UP, 1: RIGHT, continue clockwise
    match direction:
        case 0:
            #if pos[0] == 0:
             #   return (0,0)
                #raise IndexError("Slow down big fella'")
            return (pos[0]-1, pos[1])
        case 1:
            #if pos[1] == width:
             #   return (0,0)
                #raise IndexError("Slow down big fella'")
            return (pos[0], pos[1]+1)
        case 2:
            #if pos[0] == height:
             #   return (0,0)
                #raise IndexError("Slow down big fella'")
            return(pos[0]+1, pos[1])
        case 3:
            #if pos[1] == 0:
            #    return (0,0)
                #raise IndexError("Slow down big fella'")
            return (pos[0], pos[1]-1)

def get_adjacent_heights(pos,matrix):
    if pos[1]-1 < 0:
        #print("at left edge, coords:", (pos[0],pos[1]))
        left = None
    else: left = ((pos[0],pos[1]-1), matrix[pos[0]][pos[1]-1])
    if pos[0]+1 >= len(matrix):
        #print("at bottom edge, coords:", (pos[0],pos[1]))
        down = None
    else: down = ((pos[0]+1,pos[1]), matrix[pos[0]+1][pos[1]])
    if pos[1]+1 >= len(matrix[pos[0]]):
        #print("at right edge, coords:", (pos[0],pos[1]))
        right = None
    else: right = ((pos[0],pos[1]+1), matrix[pos[0]][pos[1]+1])
    if pos[0]-1 < 0:
        #print("at top edge, coords:", (pos[0],pos[1]))
        up = None
    else: up = ((pos[0]-1,pos[1]), matrix[pos[0]-1][pos[1]])
    return [up,right,down,left]


def get_heights(pos,matrix):
    new = get_adjacent_heights(pos, matrix)
    new = list(filter(lambda x: x is not None, new))
    heights = list(map(lambda x: ascii_diff(matrix[pos[0]][pos[1]],
                                            x[1]), new))
    return heights

def find_possible_directions(pos,matrix):
    """Returns an array with all the possible directions we can move"""
    return [ind for ind, n in enumerate(get_heights(pos,matrix)) if n != 1000]

def get_coords(pos,matrix,directions):
    return [move(pos,matrix,n) for n in directions]

def add_valid_edge(matrix):
    edge_dict = {}
    visited = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            directions = find_possible_directions((i,j),matrix)
            coords = get_coords((i,j),matrix,directions)
            edge_dict.update({(i,j):coords})
            #for coord in coords:
            #    visited.append(coord)
    #print(len(visited), len(set(visited)))
    return edge_dict

def bfs(start,end,matrix,edge_dict):
    queue = deque([[start]])
    seen = set([start])
    while queue:
        #print(queue)
        path = queue.popleft()
        i,j = path[-1]
        if (i,j) == end:
            return path
        for coords in edge_dict[(i,j)]:
            if coords not in seen:
                i2 = coords[0]
                j2 = coords[1]
                if i2 < 0 or j2 < 0 or i2>=40 or j2>=92:
                    pass
                else:
                    queue.append(path+[(i2,j2)])
                    seen.add((i2,j2))

grid = formatdata()
start, end = find_start_pos(grid)
print(start,end)
grid[start[0]][start[1]] = 'a'
grid[end[0]][end[1]] = 'z'
#for i in range(len(grid)):
#    for j in range(len(grid[i])):
#        print(find_possible_directions((i,j),grid))
edge_dict = add_valid_edge(grid)
#print(len(edge_dict.items()))
path = bfs(start,end,grid,edge_dict)
print(path)
print(len(path))
