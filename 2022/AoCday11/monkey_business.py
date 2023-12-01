from math import lcm

class Monkey():
    def __init__(self,specs):
        self.inspections = 0
        self.id = int(specs[0].split()[1][0])
        #could be 19 if whitespace included
        self.items: list = list(map(int,specs[1][16:].split(",")))
        self.operation: str = specs[2].split()[3:]
        self.test_divide_by: int = int(specs[3].split()[3])
        self.test_true: int = int(specs[4].split()[5])
        self.test_false: int = int(specs[5].split()[5])
    
    def test_item(self,item):
        return True if item % self.test_divide_by == 0 else False
    
    def throw_to(self, item):
        return self.test_true if self.test_item(item) == True else self.test_false

    def find_equivalent(self,num):
        factors = [2,3,5,7,11,13,17,19]
        #newnum = 1
        #isdivisible = list(filter(lambda x: int(num/3) % x == 0,factors))
        #for n in range(len(factors)):
            #if isdivisible[n] == True:
                #newnum *= factors[n]
        #print("Number",num, "is divisible by:",isdivisible, "Smallest number:",lcm(*isdivisible))
        return num % lcm(*factors)
        #return lcm(*isdivisible) 

    def update_worry_level(self,item):
        opcodes = {"+" : lambda x, y: x+y, "*" : lambda x,y: x*y}
        #return item + int(self.operation[2]) if self.operation[2] != "old" else item
        if self.operation[2] != "old":
            return opcodes[self.operation[1]](item,int(self.operation[2])) 
        else: return item*item

    def update_worry_level_large(self,item):
        opcodes = {"+" : lambda x, y: x+y, "*" : lambda x,y: x*y}
        if self.operation[2] != "old":
            result = opcodes[self.operation[1]](item,int(self.operation[2]))
        else: result = item*item
        return self.find_equivalent(result)

    def play_round(self,monkeys):
        #For every item
        for i in range(len(self.items)-1,-1,-1):
            # inpect (increment inspect)
            self.inspections += 1
            # update worry lvl by operation
            #self.items[i] = self.update_worry_level(self.items[i])
            self.items[i] = self.update_worry_level_large(self.items[i])
            # update worry lvl by int(worry_lvl / 3)
            #print("On item num:", i+1,"out of",len(self.items))
            #self.items[i] = int(self.items[i] / 3)
            # determine who to and throw_to
            monkey_to_throw_to = self.throw_to(self.items[i])
            # remove item from list and give it to other monkey from monkeys list
            monkeys[monkey_to_throw_to].items.append(self.items[i])
            self.items.pop()
            # repeat until all items thrown



def create_monkeys():
    buffer = []
    monkey_specs = []
    monkeys = []
    with open("./input.txt", 'r') as file:
        for line in file.readlines():
            if line == "\n":
                monkey_specs.append(buffer) 
                buffer = []
            else:
                buffer.append(line.removesuffix('\n'))
    if len(buffer) > 0:
        monkey_specs.append(buffer)
    for specs in monkey_specs:
        monkeys.append(Monkey(specs)) 
    return monkeys

monkes = create_monkeys()
list_of_inspections = []
for n in range(10000):
    for i in range(len(monkes)):
        monkes[i].play_round(monkes)
for monke in monkes:
    print(f"Monke id: {monke.id}, Monke items: {monke.items}, Monke inspection count: {monke.inspections}")

inspections = sorted(list(map(lambda x: x.inspections,monkes)))
print(inspections, inspections[-1]*inspections[-2])
