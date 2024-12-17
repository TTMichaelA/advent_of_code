
test_input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

class day10:
    def __init__(self, puzzle_input):
        self.grid = self.build_grid(puzzle_input)

    def process_input(self, puzzle_input):
        grid = []
        for line in puzzle_input.splitlines():
            grid.append(list(map(int,list(line))))
        return grid
    


if __name__ == "__main__":
    b = day10(test_input)
    print(b.grid)