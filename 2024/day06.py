test_input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""


class day06:

    def __init__(self, puzzle_input):
        self.grid = []
        for i in range(len(puzzle_input.splitlines())):
            gridline = []
            for j in range(len(puzzle_input.splitlines()[i])):
                gridline.append(puzzle_input.splitlines()[i][j])
            self.grid.append(gridline)
            self.dir = (-1, 0)
            self.dir_dict = {(-1,0):(0,1), (0,1):(1,0), (1,0):(0,-1), (0,-1):(-1,0) }
            self.rowlen = len(self.grid)
            self.collen = len(self.grid[0])
            self.potentials = set()
        
        self.exes = set()
        self.start, self.obstacles = self.process_input(self.grid)


    def process_input(self, puzzle_input):
        obstacles = set()
        start = None
        for i in range(len(puzzle_input)):
            for j in range(len(puzzle_input[i])):
                if puzzle_input[i][j] == '#':
                    obstacles.add((i,j))
                elif puzzle_input[i][j] == "^":
                    start = (i,j)
        return start, obstacles
    


    def traverse(self):
        curr = self.start
        dir = self.dir
        while True:
            self.exes.add(curr)
            next = (curr[0] + dir[0], curr[1] + dir[1])
            if next in self.obstacles:
                dir = self.dir_dict[dir]
                continue
            elif next[0] < 0 or next[0] >= self.rowlen:
                return 0
            elif next[1] < 0 or next[1] >= self.collen:
                return 0
            curr = next

    def loop_traverse(self, obstacle_copy):
        curr = self.start
        seen = set()
        dir = self.dir
        while True:
            seen.add((curr, dir))
            next = (curr[0] + dir[0], curr[1] + dir[1])
            if next in obstacle_copy:
                dir = self.dir_dict[dir]
                continue
            elif next[0] < 0 or next[0] >= self.rowlen:
                return False
            elif next[1] < 0 or next[1] >= self.collen:
                return False
            elif (next, dir) in seen:
                return True
            curr = next

    def traverse_all(self):
        for i in range(self.rowlen):
            for j in range(self.collen):
                if (i,j) in self.obstacles or self.start == (i,j):
                    continue
                else:
                    obstacle_set_copy = self.obstacles.copy()
                    obstacle_set_copy.add((i,j))
                    val = self.loop_traverse(obstacle_set_copy)
                    if val:
                        self.potentials.add((i,j))
            if i % 10 == 0:
                print(f"Brute forcing... {round(i / self.rowlen * 100,1)}% done")


    def get_exes_len(self):
        return len(self.exes)
    def get_pots_len(self):
        return len(self.potentials)



if __name__ == "__main__":
    instance = day06(true_input)
    instance.traverse()
    print(instance.get_exes_len())
    chog = instance.obstacles.copy()
    instance.loop_traverse(chog)

    instance.traverse_all()
    print(instance.get_pots_len())