# Pass input via stdin "cat input.txt | python main.py"

with open(0) as f:
    lines = f.readlines()


tuples = [(line.replace("   ", " ").split(" ")[0], line.replace("   ", " ").split(" ")[1].removesuffix("\n"))
          for line in lines]

first = list(map(lambda x: int(x[0]), tuples))
second = list(map(lambda x: int(x[1]), tuples))

histogram = {}
for n in second:
    histogram[n] = histogram.get(n, 0)+1

first = sorted(first)
second = sorted(second)

print(sum(map(lambda x: abs(x[0]-x[1]), zip(first, second))))
print(sum(map(lambda x: x*histogram.get(x, 0), first)))
