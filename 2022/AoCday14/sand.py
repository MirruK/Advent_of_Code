from collections import defaultdict
import os
import re
import numpy as np
from PIL import Image
import subprocess


class FrameNumber:
    def __init__(self,value) -> None:
        self.value = value
        self.digits = 4
    
    def __repr__(self):
        output = str(self.value)
        while(len(output)<self.digits):
            output = "0" + output
        return output

    def __add__(self, other):
        return self.value + other.value
    
    def add_int(self, inp):
        self.value += inp

class Grain:
    def __init__(self, state) -> None:
        # Settled True if finished falling
        self.state = state
        self.settled = False
        self.pos = (0, 500-350)
        self.lim = self.find_lim()
    
    def find_lim(self):
        for index,row in enumerate(self.state):
            if index<199 or any(row):
                pass
            else:
                return index

    def get_adj(self):
        row = self.pos[0]
        col = self.pos[1]
        return (1 if self.state[row+1][col-1] != 0 else 0, 
                1 if self.state[row+1][col] != 0 else 0,
                1 if self.state[row+1][col+1] != 0 else 0)

    def update(self):
        pos = self.pos
        adj = self.get_adj()
        relation = defaultdict(lambda: (pos[0]+1,pos[1]))
        relation.update({(1,1,0) : (pos[0]+1,pos[1]+1),
                         (0,1,1) : (pos[0]+1,pos[1]-1),
                         (0,1,0) : (pos[0]+1,pos[1]-1),
                         (1,1,1) : pos})
        while(adj != (1,1,1) and self.pos[0] < self.lim):
            adj = self.get_adj()
            relation = defaultdict(lambda: (self.pos[0]+1,self.pos[1]))
            relation.update({(1, 1, 0): (self.pos[0]+1, self.pos[1]+1),
                            (0, 1, 1): (self.pos[0]+1, self.pos[1]-1),
                            (0, 1, 0): (self.pos[0]+1, self.pos[1]-1),
                            (1,1,1) : self.pos})
            self.pos = relation[adj]
        if adj == (1,1,1):
            self.settled = True
        elif self.pos[0] < self.lim:
            self.settled = False

                    
def create_segment(state, segment):
    for n in range(1,len(segment)):
        prev = segment[n-1]
        curr = segment[n]
        diff = tuple(map(lambda x: int(x[1])-int(x[0]), zip(prev,curr)))
        vertical = True if diff.index(0) == 0 else False
        if vertical:
            negation = int((diff[1]/abs(diff[1])))
            for val in range(0,diff[1],negation):
                state[prev[1]+val][prev[0]] = 255
        else:
            negation = int((diff[0]/abs(diff[0])))
            for val in range(0,diff[0]+negation,negation):
                state[prev[1]][prev[0]+val] = 255
    return state


def simulate_grain(arr):
    active_grain = Grain(arr)
    active_grain.update()
    if active_grain.settled:
        arr[active_grain.pos[0]][active_grain.pos[1]] = 128
        return True
    else:
        print("Grain in abyss at:", active_grain.pos)
        return False
        

def initialize(data):
    segments = []
    state = np.array([[0] * 250 for _ in range(200)],np.uint8)
    for val in data:
        coords = re.findall("\d+,\d+", val)
        segments.append(list(map(lambda x: (int(x.split(",")[0])-350,int(x.split(",")[1])), coords)))
    for seg in segments:
        state = create_segment(state,seg)
    return state


data = list(map(lambda x: x.removesuffix("\n"), open("./input.txt","r").readlines()))
field = initialize(data)
cont = True
tot = 0
frame_counter = FrameNumber(0)
dir = './frames'
#for f in os.listdir(dir):
    #os.remove(os.path.join(dir, f))
while(cont):
    img = Image.fromarray(field,"L",)
    img_path = f"./frames/{frame_counter}-frame.bmp"
    img_path_tmp = f"./frames/{frame_counter}-frame_tmp.bmp"
    if not img_path_tmp in os.listdir(dir):
        img.save(img_path_tmp,bitmap_format="bmp")
        subprocess.call(f"ffmpeg -y -loglevel quiet -i {img_path_tmp} -vf scale=1000:-1 -sws_flags neighbor {img_path}",shell=True)
    frame_counter.add_int(1)
    cont = simulate_grain(field)
    
for i,n in enumerate(field):
    for j,val in enumerate(n):
        if val == 128:
            tot += 1

# ffmpeg command 
# The subprocess calls are the epitome of "this works on my pc" so beware
mkvid_cmd = "ffmpeg -framerate 24 -i \"./frames/%04d-frame.bmp\" -c:v libx264 -pix_fmt yuv420p visualization.mp4"
subprocess.call("rm ./frames/*_tmp.bmp", shell=True)
subprocess.call(mkvid_cmd, shell=True)
print("Total sand grains in grid:", tot)
