def formatdata():
    ls = []
    with open('./input.txt','r') as file:
        for line in file.readlines():
            ls.append([int(character) for character in line if character != "\n"])
    return ls

def check_left(pos,matrix):
    x = pos[0]
    y = pos[1]
    fromleft = matrix[x][0:y][::-1]
    return fromleft

def check_right(pos,matrix):
    x = pos[0] #row
    y = pos[1] #col
    rowlength = len(matrix[0])
    fromright = matrix[x][::-1][0:rowlength-y-1][::-1]
    return fromright

def check_up(pos, matrix):
    x = pos[0]
    y = pos[1]
    currcol = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if j == y:
                currcol.append(matrix[i][j])
    fromup = currcol[0:x][::-1]
    return fromup

def check_bottom(pos,matrix):
    x = pos[0]
    y = pos[1]
    rowlength = len(matrix[0])
    currcol = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if j == y:
                currcol.append(matrix[i][j])
    frombottom = currcol[::-1][0:rowlength-x-1][::-1]
    return frombottom

def score(height,view):
    if view == []:
        return 0
    if view[0] >= height:
        return 1
    count = 0
    for n in view:
        if n < height:
            count+=1
        else: return count +1
    return count

def mult(ls):
    total = 1
    for n in ls:
        total *= n
    return total

def tree_checker():
    matrix = formatdata()
    count = 0
    scores = []
    for row in range(0,len(matrix)):
        for col in range(0,len(matrix[0])):
            if row== 0 or col == 0 or row == len(matrix)-1 or col == len(matrix[0])-1:
                count+=1
            else:
                views = [check_left((row,col),matrix),check_right((row,col),matrix),check_up((row,col),matrix),check_bottom((row,col),matrix)]
                #print(views)
                count += any(list(map(lambda x: max(x) < matrix[row][col],views)))
                scores.append(mult(list(map(lambda x: score(matrix[row][col],x),views))))
    return count, max(scores)

print(tree_checker())