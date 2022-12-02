def formatdata():
    strategyguide = []
    # A dictionary that maps the letters onto a respective value, makes the whole implementation easier
    choiceasnumber = {"A" : 1, "B": 2, "C" : 3, "X": 1, "Y": 2, "Z": 3}
    with open("./input.txt", "r") as file:
        for line in file.readlines():
            # We just apply the mapping dictionary on every pair of letters
            # So that they are now a tuple of two numbers
            strategyguide.append(tuple(map(lambda x: choiceasnumber[x], line.split())))
    return strategyguide

def scoreround(decisions):
    # Table that matches points you get for a win draw or loss
    # Matches them against what "opponent decision - my decision" would be
    wintable = {0 : 3, -2 : 0, 2 : 6, -1 : 6, 1 : 0}
    return decisions[1] + wintable[decisions[0]-decisions[1]] 

def choosecorrect(decisions):
    winningtable = {1 : 2, 2 : 3, 3 : 1}
    # Just the winningtable but with keys and values reversed
    losingtable = dict((key, value) for value, key in winningtable.items())
    # Tuples not mutable so gotta do this
    decisions = list(decisions)
    # This conditional sets our decision based on what the outcome should be
    # We then run the normal scoreround function on those decisions.
    if decisions[1] == 2:
        decisions[1] = decisions[0]
        return scoreround(decisions)
    elif decisions[1] == 1:
        decisions[1] = losingtable[decisions[0]]
        return scoreround(decisions)
    else: 
        decisions[1] = winningtable[decisions[0]]
        return scoreround(decisions)


instructions = formatdata()
print("Part one answer:", sum(map(scoreround,instructions)))
print("Part two answer:", sum(map(choosecorrect,instructions)))