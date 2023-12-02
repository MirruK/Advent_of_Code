import sys
from itertools import zip_longest
from functools import reduce
from operator import mul


class Orbs():
    def __init__(self, r = 0, g = 0, b = 0) -> None:
        self.r = (r) if r != 0 else ()
        self.r_tot = r
        self.g = (g) if g != 0 else ()
        self.g_tot = g
        self.b = (b) if b != 0 else ()
        self.b_tot = b
        self.id = 0

    def add_red(self, num):
        self.r = (*self.r, num)
        self.r_tot += num

    def add_green(self, num):
        self.g = (*self.g, num)
        self.g_tot += num

    def add_blue(self, num):
        self.b = (*self.b, num)
        self.b_tot += num

    def dispatcher(self, color, num):
        match color:
            case "red":
               self.add_red(num) 
            case "green":
               self.add_green(num) 
            case "blue":
               self.add_blue(num) 
    
    def validate(self) -> bool:
        validate_tuple = lambda tup: tup[0] <= 12 and tup[1] <= 13 and tup[2] <= 14
        return all(map(validate_tuple, zip_longest(self.r, self.g, self.b, fillvalue=0)))
    
    def __str__(self) -> str:
        return f"Orbs:  [r: {self.r}, g: {self.g}, b: {self.b}]"
    
    def power_set(self):
        return reduce(mul, (map(lambda x: max(x) ,[self.r, self.g, self.b])), 1)


    
def main():
    games = []
    for line in sys.stdin.readlines():
        line = line.rstrip()
        game = Orbs()
        splitted = line.split(" ") # => ["Game", "1:", "3", "blue,", "4", "red;", "1", "red"...]
        game_id = int(splitted[1].strip(":"))
        game.id = game_id
        for i in range(2, len(splitted)-1):
            if splitted[i].isdigit():
                game.dispatcher(splitted[i+1].strip(",;"), int(splitted[i])) 
        games.append(game)
    id_tot = 0
    powers = []
    for g in games:
        powers.append(g.power_set())
        if g.validate():
            id_tot += g.id
    print("Part 1 answer -> Total id: ", id_tot)
    print(f"Part 2 answer -> Power sets sum: {sum(powers)}")


if __name__ == "__main__":
    print("NOTE: This program reads your file from STDIN")
    main()