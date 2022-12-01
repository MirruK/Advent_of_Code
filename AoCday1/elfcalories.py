from functools import reduce
def formatdata():
    current_elf_inventory = []
    foodinventories = []
    with open("./input.txt", "r") as file:
        for line in file.readlines():
            if line == "\n":
                foodinventories.append(current_elf_inventory)
                current_elf_inventory = []
            else: current_elf_inventory.append(int(line.removesuffix('\n')))
    return foodinventories

if __name__ == "__main__":
    calorielist = formatdata()
    elvestotalcalories = list(map(lambda z: reduce(lambda x,y : x+y, z), calorielist))
    firstans = max(elvestotalcalories)
    secondans = sum(sorted(elvestotalcalories)[-3:])
    print(f"Answer to first question: {firstans}\nAnswer to second question: {secondans}")
