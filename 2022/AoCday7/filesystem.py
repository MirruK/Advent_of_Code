import re

def formatdata():
    with open("./input.txt", "r") as file:
        return list(map(lambda x: x.removesuffix("\n"),file.readlines()))

def find_occurrences(path,pathtuples):
    return [i for i, x in enumerate(pathtuples) if x[0] == path]

instructions = formatdata()

pathtuples = [] 
original = []
currpath = ""
currsum = 0
for inst in instructions:
    parts = inst.split()
    if parts[0] == "$":
        if currsum > 0:
            original.append((currpath, currsum))
            if currsum <= 100000:
                pathtuples.append((currpath,currsum))
            currsum = 0
        if parts[1] == "ls":
            pass
        elif parts[1] == "cd" and parts[2] != "..":
            if parts[2] == "/":
                currpath = "/"
            elif currpath == "/":
                currpath += parts[2]
            else: currpath = "/".join((currpath, parts[2]))
        elif parts[1] == "cd" and parts[2] == "..":
            if len(currpath.split("/")) == 2:
                currpath = "/"
            else : currpath = "/".join(currpath.split("/")[:-1])
    elif parts[0] != "dir":
        currsum += int(parts[0])

def filter_outermost(pathtuples,original):
    invalid = []
    for path in pathtuples: 
        for other in original:
            if other[0].startswith(path[0]):
                if len(path[0])<len(other[0]):
                    print(f"{other[0]} is a child of {path[0]}, making it invalid")
                    invalid.append(path)
                    break
    return [path for path in pathtuples if path not in invalid]

def rec_find(pathtuples,original):
    add_to_total = 0
    checked = []
    for path in pathtuples:
        currsum = 0
        parent = "/".join(path[0].split("/")[:-1])
        for other in original:
            if other != path and parent not in checked:
                otherpath = other[0]
                if re.match(f"{parent}+.",otherpath) != None:
                    if path[1] + other[1] > 100000:
                        checked.append(other[0])
                        break
                    print(f"Adding paths of: {parent}, currently {path} and {other}")
                    add_to_total += other[1] + path[1]
        checked.append(parent)
    return add_to_total
    #loop over path in pathtuples
    #if path not already excluded from search,
    #use regex function with depth argument
    #starting at d=0 will find adjacent directories
    #Mark path as checked and add totals if they ever exceed 100000


for tupl in original:
    print(tupl)
total = 0
pathtuples = filter_outermost(pathtuples,original)
for tupl in pathtuples:
    total += tupl[1]
    print(tupl)
to_add = rec_find(pathtuples,original)
print("Total:",total)
print("Add this:",to_add)
print("Grand total:", total+to_add)
print(1252879)
