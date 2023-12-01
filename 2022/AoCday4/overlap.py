from functools import reduce

def formatdata():
    sections = []
    with open("./input.txt", "r") as file:
        for line in file.readlines():
            # Splits each line at the comma sign
            splitline = line.split(",")
            # Sections becomes a list of tuples containing two strings ("a-b", "c-d")
            sections.append((splitline[0],splitline[1]))
    return sections

def overlap(inp: tuple[range, range]):
    # Checks one of two range objects is contained within the other
    # Here two equal ranges satisfy the "contains" restriction 
    # This function looks messy, but it is O(1), so whatever.
    rangeA = inp[0]
    rangeB = inp[1]
    # If ranges are equal then obviously return true
    if rangeA == rangeB:
        return True
    # Checks if ranges are disjunct, if so obviously return false
    if rangeA[-1]<rangeB[0] or rangeA[0]>rangeB[-1]:
        return False
    # If the above condition is true then the following shows one is contained within the other
    if rangeA[0] == rangeB[0]:
        return True
    # Just checks which has a greater lowest value
    lower = rangeB
    other = rangeA
    if rangeA[0]<rangeB[0]:
        lower = rangeA
        other = rangeB
    # This final check compares the upper bounds
    if lower[-1]>=other[-1]:
        return True
    else: return False

def overlapatall(inp):
    #Same as above but it only checks if ranges are disjunct or not
    rangeA = inp[0]
    rangeB = inp[1]
    if rangeA[-1]<rangeB[0] or rangeA[0]>rangeB[-1]:
        return False
    else: return True

sections = formatdata()
def ranging(inp):
    # Convert the strings into range objects
    first_range = range(int(inp[0].split("-")[0]), int(inp[0].split("-")[1])+1)
    second_range = range(int(inp[1].split("-")[0]), int(inp[1].split("-")[1])+1)
    # Return a tuple of two ranges that correspond to the strings contained in the input tuple
    return (first_range,second_range)

# Make a list of (range, range), instead of a list of (str, str)
asranges = list(map(ranging, sections))
# We just add together the result of running the overlap function on all the values
# Add one to the total (True) if they do overlap, otherwise zero (False)
print("First answer:",reduce(lambda x,y: int(x)+int(y) ,map(overlap,asranges)))
print("Second answer:",reduce(lambda x,y: int(x)+int(y) ,map(overlapatall,asranges)))
    