from functools import reduce
from collections import defaultdict
from re import findall


class Grain():

    def __init__(self, state) -> None:
        # Settled True if finished falling
        self.state = state
        self.settled = False
        self.pos = (0, 500)
        self.lim = self.find_lim()

    def __repr__(self) -> str:
        return "o" if self.settled else "+"
    
    def find_lim(self):
        for index,row in enumerate(self.state):
            if any(row):
                pass
            else:
                return index

    def get_adj(self):
        row = self.pos[0]
        col = self.pos[1]
        return (1 if self.state[row+1][col] != 0 else 0, 
                1 if self.state[row+1][col-1] != 0 else 0,
                1 if self.state[row+1][col+1] != 0 else 0)

    def update(self):
        pos = self.pos
        adj = self.get_adj()
        relation = defaultdict(lambda: [pos[0]+1,pos[1]])
        relation.update({(1,1,0) : (pos[0]+1,pos[1]+1),
                         (0,1,1) : (pos[0]+1,pos[1]-1),
                         (0,1,0) : (pos[0]+1,pos[1]-1)})

        while(adj != (1,1,1) and self.pos[0] < self.lim):
            self.pos = relation[adj]
            adj = self.get_adj()


#    def update(self):
#        adj_tiles = self.get_adj()
#        for i, adj in enumerate(adj_tiles):
#            if type(adj) == Grain:
                    



data = list(map(lambda x: x.removesuffix("\n"), open("./input.txt","r").readlines()))
state = []


def initialize(data):
    state = [[0] * 1000 for n in range(10)]
    for val in data:
        coords = findall("[0-9+,0-9]+ [0-9+,0-9]+", val)
        coords[0] = eval("(" + coords[0] + ")")
        coords[1] = eval("(" + coords[1] + ")")

def exec_frame(state):
    pass


print(data)

field = initialize(data)

