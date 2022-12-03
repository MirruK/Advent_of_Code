def formatdata():
    bagcontents = []
    with open("./input.txt", "r") as file:
        for line in file.readlines():
            #Make a list of bags that are divided into two compartments
            bagcontents.append((line[0:int(len(line)/2)],line[int(len(line)/2):len(line)].removesuffix("\n")))
    return bagcontents

def aspriority(character: str):
    # Helper function that returns the corresponding priority of the character
    if character.isupper():
        return ord(character)-38
    elif character.islower():
        return ord(character) - 96
    else: return 0

def findtotalpriority(bags):
    # Slow implementation, could be done faster
    # by finding matching characters by counting instead of comparison
    prioritysum = 0
    for bag in bags:
        for i in range(len(bag[0])):
            if bag[0][i] in bag[1]:
                print(f"Matched character: {bag[0][i]}")
                prioritysum += aspriority(bag[0][i])
                break
    return prioritysum

def findgrouppriorities(bags):
    # Again slow, but gets the job done.
    prioritysum = 0
    # Here I have to concatenate the strings
    # so that one bag is just one string of characters
    bags = list(map(''.join,bags))
    # Loop over all bags, stepping in groups of 3
    for i in range(0,len(bags),3):
        for j in range(len(bags[i])):
            # See if current character exists somewhere in both other bags
            # If this is true we have found our badge so we go to the next three bags
            if bags[i][j] in bags[i+1] and bags[i][j] in bags[i+2]:
                prioritysum += aspriority(bags[i][j])
                break
    return prioritysum

bags = formatdata()
print("First answer:", findtotalpriority(bags))
print("Second answer:", findgrouppriorities(bags))