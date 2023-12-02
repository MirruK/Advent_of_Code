import sys
from itertools import zip_longest
from functools import reduce
from operator import mul


class Orbs():
    def __init__(self) -> None:
        self.r = self.g = self.b = self.id = 0

    def add_red(self, num):
        if not isinstance(self.r, tuple): self.r = (self.r, num)
        else: self.r = (*self.r, num)

    def add_green(self, num):
        if not isinstance(self.g, tuple): self.g = (self.g, num)
        else: self.g = (*self.g, num)

    def add_blue(self, num):
        if not isinstance(self.b, tuple): self.b = (self.b, num)
        else: self.b = (*self.b, num)

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
    
    def power_set(self):
        return reduce(mul, (map(lambda x: max(x) ,[self.r, self.g, self.b])), 1)


    
def main():
    games = []
    for line in sys.stdin.readlines():
        game = Orbs()
        splitted = line.split(" ") # => ["Game", "1:", "3", "blue,", "4", "red;", "1", "red"...]
        game.id = int(splitted[1].strip(":"))
        for i in range(2, len(splitted)-1):
            # Works off the assumption that a digit is always followed by its color name
            if splitted[i].isdigit():
                game.dispatcher(splitted[i+1].strip(",;\n"), int(splitted[i])) 
        games.append(game)
    # Filter out games that were impossible by the rules and then sum the valid games ids
    id_tot = sum(map(lambda x: x.id, filter(lambda x: x.validate(),games)))
    # Take the power set of each game and sum the values
    powers_sum = sum(map(lambda x: x.power_set(), games))
    print("Part 1 answer -> Total id: ", id_tot)
    print(f"Part 2 answer -> Power sets sum: {powers_sum}")


if __name__ == "__main__":
    print("NOTE: This program reads your file from STDIN")
    main()