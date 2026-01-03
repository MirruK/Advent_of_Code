import re


def match_columns(cols: list[str]) -> bool:
    fst, snd, thrd = cols
    fst_diag = fst[0] + snd[1] + thrd[2]
    snd_diag = fst[2] + snd[1] + thrd[0]

    m1 = re.fullmatch(r"MAS|SAM", fst_diag) is not None
    m2 = re.fullmatch(r"MAS|SAM", snd_diag) is not None
    return m1 and m2


def get_column(ls: list[list[str]], col: int, row: int) -> str | None:
    if row+2 > len(ls)-1 or col > len(ls[0])-1:
        return None
    return ls[row][col] + ls[row+1][col] + ls[row+2][col]


def get_search_kernel(ls: list[list[str]], top_left_coord: tuple[int, int]) -> list[str] | None:
    row, col = top_left_coord
    kernel = [get_column(ls, col, row), get_column(
        ls, col+1, row), get_column(ls, col+2, row)]
    if not all(kernel):
        return None
    return kernel


def find_Xs(ls):
    counter = 0
    for i in range(0, len(ls)-2):
        for j in range(0, len(ls[0])-2):
            kernel = get_search_kernel(ls, (i, j))
            if match_columns(kernel):
                counter += 1
    return counter


with open(0) as f:
    lines = list(map(lambda x: x.removesuffix("\n"), f.readlines()))

print(find_Xs(lines))
