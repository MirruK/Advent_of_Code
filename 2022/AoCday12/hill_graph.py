class Graph:
    """Class that represents a graph structure
    Where verteces are stored as tuples
    One vertex represents a coordinate in a 2d grid
    """

    def __init__(self, matrix) -> None:
        self.starts = []
        self.verteces = {}
        self.matrix = matrix
        self.start = (None, None)
        self.end = (None, None)

    def add_edge(self, v1, v2) -> None:
        """Adds a directed edge from v1 to v2 to the graph"""
        # print("added edge from", v1, "to", v2)
        self.verteces.update({v1: v2})

    def BFS(self):
        """performs breadth-first-search on the graph
        returns the shortest distance from start to end
        """
        s = self.start
        e = self.end
        seen = []
        queue = [[s]]

        while queue:
            path = queue.pop()
            node = path[-1]
            if node not in seen:
                # print(node)
                neighbours = self.verteces[node]
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                    if neighbour == e:
                        # print("Path:", new_path)
                        print("Length of path:", len(new_path))
                        return
                seen.append(node)

    def dijkstra(self):
        start = self.start
        end = self.end
        visited = dict.fromkeys(self.verteces.keys(), False)
        dist = dict.fromkeys(self.verteces.keys(), 9000000000)
        pred = dict.fromkeys(self.verteces.keys(), -1)
        dist[start] = 0
        visited[start] = True
        queue = [start]
        while queue:
            u = queue.pop(0)
            for edge in self.verteces[u]:
                if not visited[edge]:
                    visited[edge] = True
                    dist[edge] = dist[u] + 1
                    pred[edge] = u
                    queue.append(edge)
                    if edge == end:
                        return True, dist, pred
        
        return False, dist, pred

    def find_start_pos(self):
        start, end = (None, None), (None, None)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == "a":
                    self.starts.append((i,j))
                if start != (None, None) and end != (None, None):
                    self.start = start
                    self.end = end
                if self.matrix[i][j] == "S":
                    start = (i, j)
                    self.matrix[i][j] = "a"
                if self.matrix[i][j] == "E":
                    end = (i, j)
                    self.matrix[i][j] = "z"

    def ascii_diff(self, curr_char, next_char):
        diff = ord(next_char) - ord(curr_char)
        return diff if diff == 1 or diff == 0 or diff < 0 else 1000

    def move(self, pos, direction):
        match direction:
            case 0:
                # UP
                return (pos[0] - 1, pos[1])
            case 1:
                # LEFT
                return (pos[0], pos[1] + 1)
            case 2:
                # DOWN
                return (pos[0] + 1, pos[1])
            case 3:
                # RIGHT
                return (pos[0], pos[1] - 1)

    def get_height(self, pos):
        if pos[0] < 0 or pos[0] > len(self.matrix) - 1:
            return False
        if pos[1] < 0 or pos[1] > len(self.matrix[pos[0]]) - 1:
            return False

        return self.matrix[pos[0]][pos[1]]

    def move_possible(self, pos, next):
        curr_height = self.get_height(pos)
        next_height = self.get_height(next)
        if next_height is False:
            return False
        diff = self.ascii_diff(curr_height, next_height)
        if diff > 1:
            # print("cant move from", pos,"in direction", direction)
            return False
        else:
            return True

    def initialize_graph(self) -> None:
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                ls = []
                for n in range(4):
                    next_pos = self.move((i, j), n)
                    if self.move_possible((i, j), next_pos):
                        ls.append(next_pos)
                self.add_edge((i, j), ls)


def formatdata():
    matrix = []
    with open("./input.txt") as file:
        for line in file.readlines():
            matrix.append(list(line.removesuffix("\n")))
    return matrix


grid = formatdata()
mygraph = Graph(grid)
mygraph.find_start_pos()
mygraph.initialize_graph()
print(mygraph.start, mygraph.end)
lens = []
print(mygraph.starts)
for n in range(len(mygraph.starts)):
    mygraph.start = mygraph.starts[n]
    result, dist, pred = mygraph.dijkstra()
    if result:
        lens.append(dist[mygraph.end])

print(min(lens))
 
