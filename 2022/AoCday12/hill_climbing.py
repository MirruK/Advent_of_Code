from math import sqrt
from functools import partial

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

def move(pos,matrix,direction):
    #POS 1 = left, right
    #POS 0 = up, down
    height = len(matrix)
    width = len(matrix[0])
    #0: UP, 1: RIGHT, continue clockwise
    match direction:
        case 0:
            if pos[0] == 0:
                return (0,0)
                #raise IndexError("Slow down big fella'")
            return (pos[0]-1, pos[1])
        case 1:
            if pos[1] == width:
                return (0,0)
                #raise IndexError("Slow down big fella'")
            return (pos[0], pos[1]+1)
        case 2:
            if pos[0] == height:
                return (0,0)
                #raise IndexError("Slow down big fella'")
            return(pos[0]+1, pos[1])
        case 3:
            if pos[1] == 0:
                return (0,0)
                #raise IndexError("Slow down big fella'")
            return (pos[0], pos[1]-1)

def ascii_diff(curr_char,next_char):
    diff = ord(next_char) - ord(curr_char)
    return diff if diff == 1 or diff == 0 or diff == -1 else -2

def get_heights(pos,matrix):
    curr_row = pos[0]
    curr_col = pos[1]
    new = [move(pos,matrix,n) for n in range(4)]
    heights = list(map(lambda x: ascii_diff(matrix[curr_row][curr_col],
                                            matrix[x[0]][x[1]]), new))
    return [heights[n] for n in range(len(heights))]

def find_possible_directions(pos,matrix):
    """Returns an array with all the possible directions we can move"""
    return [ind for ind, n in enumerate(get_heights(pos,matrix)) if n != -2]

def dist(p1,p2):
    return sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)

def cost(pos, direction, matrix, end):
    moves = find_possible_directions(pos,matrix) 
    ls = [int(dist(move[pos,n],end)) for n in moves]
    best = ls.index(min[ls])



def greedy_search(start, matrix, iters):
    pos = start
    height, width = len(matrix), len(matrix[start[0]])
    for _ in range(iters):
        moves = get_heights(pos,matrix)
        heights = list(map(lambda x: x[1],moves))
        pos = move(pos,matrix,moves[ind][1])
    return pos

matrix = formatdata()
start, end = find_start_pos(matrix)
print(start, end)
matrix[start[0]][start[1]] = "a"
matrix[end[0]][end[1]] = "z"
print(matrix)
print(get_heights(end,matrix))
final = greedy_search(start,matrix,100)
print(f"Final location: {final}, height: {matrix[final[0]][final[1]]}")
