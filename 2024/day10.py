
class Node:
    
    def __init__(self, position, value):
        self.position = position
        self.value = value
        self.edges = set()

    def getval(self):
        return self.value
    
    def getpos(self):
        return self.position
    
    def getedges(self):
        return self.edges
    
    def add_descendants(self, grid, node_list):
        for diff in [(1,0), (-1,0), (0,1), (0,-1)]:
            new_coord = (self.position[0] + diff[0], self.position[1] + diff[1])
            if new_coord[0] >= len(grid) or new_coord[0] < 0:
                continue
            if new_coord[1] >= len(grid[0]) or new_coord[1] < 0:
                continue
            elif node_list[new_coord].getval() == self.getval() + 1:
                self.edges.add(node_list[new_coord])


class day10:
    def __init__(self, puzzle_input):
        self.grid = self.build_grid(puzzle_input)
        self.nodes_by_val = dict()
        self.nodes_by_pos = dict()
        self.init_graph(self.grid)
    

    def build_grid(self, puzzle_input):
        grid = []
        for line in puzzle_input.splitlines():
            grid.append(list(map(int,list(line))))
        return grid
    
    def get_grid(self):
        return self.grid
    
    def init_graph(self, grid):
        for i in range(10):
            self.nodes_by_val[i] = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                val = grid[i][j]
                pos = (i, j)
                new_node = Node(pos, val)
                self.nodes_by_val[val].add(new_node)
                self.nodes_by_pos[pos] = new_node

        for key, node in self.nodes_by_pos.items():
            node.add_descendants(self.grid, self.nodes_by_pos)
        return 0
    
    def run_bfs(self):
        score = 0
        for node in self.nodes_by_val[0]:
            score += self.bfs_helper(node)
        return score
    
    def bfs_helper(self, node):
        sum = 0
        if node.getval() == 9:
            return 1
        else:
            for subnode in node.getedges():
                sum += self.bfs_helper(subnode)
        return sum
    
    def run_bfs_pt1(self):
        score = 0
        for node in self.nodes_by_val[0]:
            nineset = set()
            score += len(self.bfs_helper(node, nineset))
        return score
    
    def bfs_helper_pt1(self, node, nineset):
        if node.getval() == 9:
            nineset.add(node.getpos())
            return nineset
        else:
            for subnode in node.getedges():
                nineset.update(self.bfs_helper(subnode, nineset))
        return nineset



if __name__ == "__main__":
    b = day10(test_input)
    print(b.grid)
    print(b.nodes_by_pos[0,0].getedges())
    for node in b.nodes_by_pos[0,0].getedges():
        print(node.getval())
        print(node.getpos())
    f = b.run_bfs()
    print(f)