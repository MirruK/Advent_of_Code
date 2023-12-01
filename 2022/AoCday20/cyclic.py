from copy import deepcopy
from collections import defaultdict

def formatdata():
    data = []
    with open('./input.txt','r') as file:
        for line in file.readlines():
            data.append(int(line.removesuffix('\n')))
    return data

def swap(ls,ind,end):
    # if ls[ind] or ls[end] in duplicates
    #duplicates[ls[ind]] == end and vice versa
    ls[ind], ls[end] = ls[end], ls[ind]
    return ls

# def shift_circularly(ls,start,iterations):
#     #Wohoo this works because the list can be shifted without problems
#     #This does not handle the edge-cases in the same way as aoc website
#     i=0
#     if iterations == 0:
#         return ls
#     if iterations > 0:
#         for n in range(start, start+iterations):
#             i = n % len(ls)
#             nexti = (n+1) % len(ls)
#             ls = swap(ls,i,nexti)
#     if iterations < 0:
#         for n in range(start, start+iterations, -1):
#             i = n % len(ls)
#             nexti = (n-1) % len(ls)
#             ls = swap(ls,i,nexti)
#     return ls

# all this bs and the offset of the circular list doesn't even matter...
def shift_circularly(ls,start,iterations):
    i = 0
    if iterations == 0:
        return ls
    if iterations > 0:
        edge_offset = 0
        for n in range(start,start+iterations):
            n += edge_offset
            i = n % len(ls)
            nexti = (n+1) % len(ls)
            #print(f"current i: {i}, next i {nexti}")
            if nexti == 0:
                #print("ran edge case")
                ls.insert(0,ls.pop())#
                #print(ls)
            elif nexti == len(ls)-1:
                ls.insert(0,ls.pop(len(ls)-2))
                edge_offset += 1
            else:
                #print("swapping", i, "and", nexti)
                #print(ls)
                ls = swap(ls,i,nexti)
    if iterations < 0:
        edge_offset = 0
        for n in range(start,start+iterations,-1):
            #print("Edge offset:",edge_offset)
            n = n-edge_offset
            i = n % len(ls)
            nexti = (n-1) % len(ls)
            #print(f"current i: {i}, next i {nexti}")
            #nexti = (len(ls)-(abs(n)+1%(len(ls)-1)))
            if nexti == len(ls)-1:
                #print("ran edge in negative branch")
                ls.insert(len(ls)-2,ls.pop(0))
                edge_offset += 1
                #print(ls)
            elif nexti == 0:
                ls.append(ls.pop(1))
                edge_offset += 1
            else:
                #print("swapping", i, "and", nexti)
                ls = swap(ls,i,nexti)
    return ls

def find_occurrences(data,val):
    return [ind for ind,value in enumerate(data) if value == val]

def list_duplicates(data):
    checked = []
    duplicates = defaultdict(lambda: [1])
    for val in data:
        if val in checked:
            duplicates[val].append(len(duplicates[val])+1)
        checked.append(val)
    return duplicates

#data = formatdata()
#newdata = deepcopy(data)
#data = [1,2,-3,3,-2,0,4]
data = [1,2,1,1,0,1]
newdata = deepcopy(data)
duplicates = list_duplicates(data)

print(newdata)

for val in data:
    #print(data)
    #print(newdata)
    if duplicates[val] == [1]:
        ind = newdata.index(val)
    else:
        which_inst = duplicates[val].pop(0)-1
        print("Grabbing", which_inst, "instace of var:",val)
        ind = find_occurrences(newdata,val)[which_inst]
        
    #print(ind,val)
    newdata = shift_circularly(newdata,ind,val)

#print(newdata)
#data = construct_list(newdata,len(data))
print(newdata)
zero = newdata.index(0)
thousandth=newdata[(1000+zero)%len(newdata)]
two_thousandth = newdata[(2000+zero)%len(newdata)]
three_thousandth = newdata[(3000+zero)%len(newdata)]
# for n in range(zero,zero+3000):
#     i = n % len(data)
#     if n == zero+1000:
#         thousandth = data[i]
#     if n == zero+2000:
#         two_thousandth = data[i]
#     if n == zero+3000:
#         print("yee")
#         three_thousandth = data[i]

print(thousandth,two_thousandth,three_thousandth)
print(thousandth+two_thousandth+three_thousandth)
