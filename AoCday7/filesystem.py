import re

class ElfFileSystem():

    def __init__(self, instructions):
        self.instructions = instructions
        self.parent_directory = None
        self.root = ElfDirectory('', None)
        self.filesystem = [self.root]
        self.current_directory = self.root
        
    def new_directory(self,name):
        self.filesystem.append(ElfDirectory(name,self.current_directory))
    
    def new_file(self,name,size):
        self.current_directory.content.append(ElfFile(name,size,self.pwd()))

    def cd(self, arg):
        if arg == '..':
            self.current_directory = self.parent_directory
            self.parent_directory = self.current_directory.parent_dir
        else:
            self.current_directory = arg

    def pwd(self):
        origin = self.current_directory
        full_path = '/'
        while(self.parent_directory != None):
            full_path = '/'.join([self.parent_directory.name, full_path])
            self.cd('..')
        self.current_directory = origin
        self.parent_directory = origin.parent_dir
        return full_path 
    
    def construct_fs(self, instructions):
        for inst in instructions:
            if inst[0] == '$':
                self.runcommand(inst.split()[1], inst.split()[2])


class ElfDirectory():

    def __init__(self, name, parent) -> None:
        self.parent_dir = parent
        self.name = name
        self.content = [] 


class ElfFile():

    def __init__(self,name, size, path_to_file) -> None:
        self.name = name
        self.size = size
        self.path_to_file = path_to_file


def formatdata():
    with open("./input.txt", "r") as file:
        return list(map(lambda x: x.removesuffix("\n"),file.readlines()))

instructions = formatdata()

pathtuples = [] 


currpath = ''
currsum = 0
for inst in instructions:
    if inst == "$ ls":
        pass
    else:
        if inst == '$ cd ..':
            currpath = currpath.split("/")
            print(currpath)
            currpath.pop()
            print(currpath)
            currpath = "/".join(currpath)
        elif inst.split()[1] == 'cd':
            pathtuples.append((currpath,currsum))
            currsum = 0
            currpath = '/'.join([inst[5:], currpath])
        elif inst.split()[0] != "dir":
            currsum += int(inst.split()[0])

print(pathtuples)

fs = ElfFileSystem([])
fs.new_file("MyFile","1024")
fs.new_directory("dir1")