def formatdata():
    ls = []
    with open('./input.txt','r') as file:
        for line in file.readlines():
            ls.append([int(character) for character in line if character != "\n"])
    return ls

def check_left(pos,matrix):
    x = pos[0]
    y = pos[1]
    height = matrix[x][y]
    fromleft = matrix[x][0:y]
    if fromleft == []:
        return False
    return max(fromleft) < height 

def check_right(pos,matrix):
    x = pos[0] #row
    y = pos[1] #col
    rowlength = len(matrix[0])
    height = matrix[x][y]
    fromright = matrix[x][::-1][0:rowlength-y-1]
    return max(fromright) < height 

def check_up(pos, matrix):
    x = pos[0]
    y = pos[1]
    rowlength = len(matrix[0])
    height = matrix[x][y]
    currcol = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if j == y:
                currcol.append(matrix[i][j])
    fromup = currcol[0:x]
    return max(fromup) < height

def check_bottom(pos,matrix):
    x = pos[0]
    y = pos[1]
    rowlength = len(matrix[0])
    height = matrix[x][y]
    currcol = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if j == y:
                currcol.append(matrix[i][j])
    frombottom = currcol[::-1][0:rowlength-x-1]
    return max(frombottom) < height

def tree_checker():
    matrix = formatdata()
    count = 0
    print(len(matrix), len(matrix[0]))
    for row in range(0,len(matrix)):
        for col in range(0,len(matrix[0])):
            if row == 0 or col == 0 or row == len(matrix)-1 or col == len(matrix[0])-1:
                count += 1
            else:
                count += any([check_left((row,col),matrix),check_right((row,col),matrix),check_up((row,col),matrix),check_bottom((row,col),matrix)])
    return count

print(tree_checker())