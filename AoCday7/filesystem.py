def formatdata():
    with open("./input.txt", "r") as file:
        return list(map(lambda x: x.removesuffix("\n"),file.readlines()))

def isparent(parentpath,childpath):
    return True if parentpath in childpath else False

def getparent(path : str):
    return "/".join(path.split("/")[:-1])


def isadjacent(path1, path2):
    if path1 == path2:
        return False
    return True if getparent(path1) == getparent(path2) else False

def find_directorystack(path,pathtuples):
    #return [x for i,x in enumerate(pathtuples) if x==isparent(x[0],path)]
    return list(filter(lambda x: isparent(x[0],path),pathtuples)) + list(filter(lambda x: isadjacent(x[0],path),pathtuples))

def string_diff(str1: str,str2: str):
    if len(str1) > len(str2):
        return str1.replace(str2, '')
    else: return str2.replace(str1, '') 

#def find_size(dir):
    #if size(dir):
        #pass

def find_occurrences(path,pathtuples):
    return [i for i, x in enumerate(pathtuples) if x[0] == path]

def sum_duplicates(currentpath,pathtuples):
    path = currentpath[0]
    #original = list with the duplicates
    #pathtuples = the one we want to check
    indeces = find_occurrences(path,pathtuples)
    if len(indeces) > 1:
        print("found thief")
        newelem = (path, pathtuples[indeces[0]][1] + pathtuples[indeces[1]][1])
        return newelem
    else: return currentpath

 

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


# for ind in range(len(pathtuples)):
#     print(pathtuples[ind])
#     pathtuples[ind] = sum_duplicates(pathtuples[ind],original)
# total = sum(map(lambda x: x[1],pathtuples))


# print(total)
# for ind in range(len(pathtuples)):
#     thissum = 0
#     ls = find_directorystack(pathtuples[ind][0],pathtuples)
#     print("Current stack:", ls)
#     if len(ls) > 1:
#         thissum = sum(map(lambda x: x[1],ls))
#         print("Sum of stack:", thissum)
#     if thissum <= 100000:
#         total += thissum 

print(total)