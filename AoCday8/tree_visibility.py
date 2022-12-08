
def isvisible(pos,grid) -> bool:
    flat_list = [item for sublist in grid for item in sublist]
    tree_height = grid[pos[0]][pos[1]]
    tree_x = pos[0]
    tree_y = pos[1]
    left, right, up, down = False, False, False, False
    fromleft = grid[tree_y][0:tree_x+1]
    fromright = grid[tree_y][-1:tree_x:-1]
    print(tree_x, tree_y)
    fromup = flat_list[tree_x:tree_x+len(grid[0])*tree_y+1:len(grid[0])]
    fromdown = flat_list[-(len(grid[0])-tree_x):tree_x+len(grid[0])*tree_y:-len(grid[0])]
    if max(fromleft)< tree_height-1:
        left = True
    if max(fromright) < tree_height-1:
        right = True
    if max(fromup) < tree_height-1:
        up = True
    if max(fromdown) < tree_height-1:
        down = True
    if any([right,left,up,down]) == True:
        return True
    else: return False

def formatdata():
    ls = []
    with open('./input.txt','r') as file:
        for line in file.readlines():
            ls.append([int(character) for character in line if character != "\n"])
    return ls
grid = formatdata()
total = 0
for row,rowval in enumerate(grid):
    for col, colval in enumerate(rowval):
        if row == 0 or row == len(grid) or col == 0 or col == len(rowval):
            total +=1
        elif isvisible((row,col),grid):
            total += 1
print(total)