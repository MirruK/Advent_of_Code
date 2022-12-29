""" This is a solution that I came up with 
    using some help resources when I got stuck
    Credit goes largely to hyper-neutrino on youtube"""


def formatdata():
    # Store filesystem as a nested dictionary
    # Pwd is the current directory path
    pwd = root = {}
    # Here is some clever shit,
    # Use a stack to keep track of parent directories
    # Push to the stack when moving into a child
    # Pop the stack when reading a cd .. command
    stack = []
    # Open input file
    with open('./input.txt', 'r') as file:
        # line corresponds with one command from our input
        for line in file.readlines():
            # Remove the unnecessary newline character
            line = line.removesuffix('\n')
            # If the line is a command it starts with $
            if line[0] == '$':
                # We don't do anything for the $ ls commands
                if line[2] == 'l':
                    pass
                else:
                    # If it is a command but not ls it is a cd
                    # line[5:] corresponds with the filesize
                    dir = line[5:]
                    # If we cd to root we clear the stack
                    if dir == '/':
                        pwd = root
                        stack = []
                    # cd .. means move to parent
                    # new pwd is the dictionary 
                    # corresponding with the 
                    # parent dictionary
                    elif dir == '..':
                        pwd = stack.pop()
                    else: 
                        # This runs if it is not a command
                        # And it is not an ls command
                        # If dir is not in our dictionary
                        # we add it
                        if dir not in pwd:
                            # THis is to make sure
                            # There exist no uninitialized
                            # directories
                            pwd[dir] = {}
                        stack.append(pwd)
                        # Assign working dir to the dictionary
                        # corresponding with the path held in dir
                        pwd = pwd[dir]
            else:
                # line is here a non command so
                # x will be the size or "dir"
                x, y = line.split()
                # do a check if we are on a "dir" line
                # if so, initialize dictionary
                if x == "dir" and y not in pwd:
                    pwd[y] = {}
                # add the file and size to the current dictionary
                # files are therefore in the format {'path' : size}
                # 
                else: 
                    pwd[y] = int(x)

    return root


def sum_children(dir):
    """Takes a dir path and sums all children"""
    if type(dir) == int:
        return (dir,0)
    acc = 0
    tot = 0
    
    for child in dir.values():
        a, t = sum_children(child)
        acc += a
        tot += t
    if acc <= 100000:
        tot += acc
    return (acc,tot)


def size(dir):
    if type(dir) == int:
        return dir
    # mind... blown
    return sum(map(size, dir.values()))


def solve(target, dir):
    ans = float("inf")
    if size(dir) >= target:
        ans = size(dir)
    for child in dir.values():
        if type(child) == int:
            pass
        else:
            q = solve(target, child)
            ans = min(ans,q)
    return ans


root = formatdata()
print(sum_children(root)[1])
target = size(root) - 40_000_000
print(size(root))
print(target)
print(solve(target,root))
