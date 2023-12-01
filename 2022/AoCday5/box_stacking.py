from copy import deepcopy

def formatdata():
    instructions = []
    with open("./instructions.txt", "r") as file:
        for line in file.readlines():
            # The relevant data is on each line at every other word
            splitline = list(map(int,line.split()[1::2]))
            instructions.append(splitline)
    stacks = [[] for n in range(9)]
    with open("./stacks.txt", "r") as file:
        for line in file.readlines()[-2::-1]:
            # The relevant data is on every line, every fourth character (incl. blankspace)
            for n in range(len(stacks)):
                if line[n*4+1] != " ":
                    stacks[n].append(line[n*4+1])
    return instructions, stacks

def applyinstruction(inst, stack):
    # Function crime committed, impurity detected
    for n in range(inst[0]):
        stack[inst[2]-1].append(stack[inst[1]-1].pop())

def applyreverse(inst, stack):
    howmany = inst[0]
    towhere = inst[2]-1
    fromwhere = inst[1]-1
    temp = []
    temp = stack[fromwhere][len(stack[fromwhere])-howmany:]
    for n in range(len(temp)):
        stack[towhere].append(temp[n])
        stack[fromwhere].pop()
     
instructions1, stacks1 = formatdata()
stacks2 = deepcopy(stacks1)

for inst in instructions1:   
    applyinstruction(inst, stacks1)
for inst in instructions1:   
    applyreverse(inst, stacks2)

print("First answer: ")
for n in stacks1:
    print(n[-1], end="")
print("\nSecond answer: ")
for n in stacks2:
    print(n[-1],end="")