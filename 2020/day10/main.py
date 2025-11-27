from collections import defaultdict

def solve2(A: dict, goal: int):
    # For every step count number of ways to make 
    # TODO: Use recursion to solve and then apply dynamic programming
    pass

def solve(A: dict, goal: int):
    B = [0,0,0]
    curr = 0
    prev = 0
    while(True):
        ls = list(filter(lambda x: x > 0, [
        A[curr+1],
        A[curr+2],
        A[curr+3]]))
        next = min(ls)
        prev = curr
        curr = next
        B[next - prev - 1] += 1
        if (curr == goal):
            B[2] += 1
            return B

a = defaultdict(lambda: -1)

with open(0) as f:
    for l in f.readlines():
        v = int(l)
        a[v] = v

goal = max(a.keys())

b = solve(a, goal) 
print(b)
    
