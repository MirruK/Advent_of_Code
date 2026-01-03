import re
# col=3, n = 0..3, m[n][col-n] => m[0][3] -> m[1][2] -> m[2][1] -> m[3][0]
# col=4, n = 0..4, m[0][4] m[1][3] m[2][2] m[3][1] m[4][0]
# mirrored:
# col= 0, n = 0..0: m[column_count-n][(column_count-col)+n)]
# col = 1, n=0..1: m[column_count-0][column_count-1] -> m[column_count-1][column_count]
# for col in range(0,column_count):
#   for n in range(0,col+1):
#       diagonal.append(m[n][col-n])


def get_cols(m: list[str]) -> list[str]:
    column_count = len(m[0])
    row_count = len(m)
    cols = []
    for i in range(0, column_count):
        col = []
        for j in range(0, row_count):
            col.append(m[j][i])
        cols.append(col)
    return cols


def get_diagonals(m: list[str]) -> list[str]:
    column_count = len(m[0])
    row_count = len(m)
    diagonals = []
    for i in range(0, column_count):
        diagonal1 = []
        diagonal2 = []
        diagonal3 = []
        diagonal4 = []
        for j in range(0, i+1):
            if i == column_count-1:
                diagonal1.append(m[j][i-j])
                diagonal3.append(m[j][column_count-1-i+j])
            else:
                diagonal1.append(m[j][i-j])
                diagonal2.append(m[row_count-1-j][column_count-1-i+j])
                diagonal3.append(m[j][column_count-1-i+j])
                diagonal4.append(m[row_count-1-i+j][j])
        diagonals.append(diagonal1)
        diagonals.append(diagonal2)
        diagonals.append(diagonal3)
        diagonals.append(diagonal4)

    return diagonals


with open(0) as f:
    lines = list(map(lambda x: x.removesuffix("\n"), f.readlines()))
    strs = list(map(lambda x: ''.join(x), get_diagonals(
        lines) + get_cols(lines))) + lines
    print(strs)
    counter = 0
    for n in range(0, len(strs)):
        counter += len(re.findall(r"(?=(XMAS|SAMX))", strs[n]))

print(counter)
