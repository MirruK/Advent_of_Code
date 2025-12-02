from collections import defaultdict

def solve2(A: dict, goal: int):
    cache = {}
    # Use recursion to solve and then apply dynamic programming (memoize with cache dict)
    # Note: this is exactly the
    # how many ways to climb a staircase given you can take (1,2 or 3) steps-problem
    def go(curr: int):
        if curr == goal:
            return 1
        if curr > goal:
            return 0
        ls = list(filter(lambda x: x > 0, [
                A[curr+1],
                A[curr+2],
                A[curr+3]]))
        if curr in cache:
            return cache[curr]
        value = sum([go(n) for n in ls])
        cache[curr] = value
        return value
    return go(0)

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
c = solve2(a, goal)
print(b)
print(c)
    
