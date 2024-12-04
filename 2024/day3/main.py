multiplier = 1


def mul(a, b):
    global multiplier
    if multiplier == 0:
        return 0
    return a*b


def do():
    global multiplier
    multiplier = 1
    return 0


def dont():
    global multiplier
    multiplier = 0
    return 0


with open(0) as f:
    print(sum(map(lambda x: eval(x), f.readlines())))
