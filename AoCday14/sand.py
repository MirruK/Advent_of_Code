from functools import reduce


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
        return [1 if self.state[row+1][col] != 0 else 0, 
                1 if self.state[row+1][col-1] != 0 else 0,
                1 if self.state[row+1][col+1] != 0 else 0]

    def upd_rec(self,pos):
        adj = self.get_adj()
        if pos == (False, False):
            return pos
        if pos[0]>self.lim:
            return (False, False)
        if all(adj) == "#":
            return pos
        else:
            if reduce(lambda x,y: (x[0] and x[1]) and (y[0] and y[1]), enumerate(zip(adj,[1,1,0])):
                return upd_rec((pos[0],pos[1]+1))
            elif reduce(lambda x,y: (x[0] and x[1]) and (y[0] and y[1]), enumerate(zip(adj,[0,0,0])):
 


            


#    def update(self):
#        adj_tiles = self.get_adj()
#        for i, adj in enumerate(adj_tiles):
#            if type(adj) == Grain:
                    



data = list(map(lambda x: x.removesuffix("\n"), open("./input.txt","r").readlines()))
state = []


def initialize(data):
    pass


def exec_frame(state):
    pass


print(data)

field = initialize(data)

