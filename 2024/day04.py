class puzzle:
    def __init__(self, input) -> None:
        self.raw_input = input
        self.input = input.splitlines()
        self.n_rows = len(self.input)
        self.n_cols = len(self.input[0])
        self.total_count = 0
        self.total_a_count = 0

    def scan_x(self):
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                if self.input[i][j] == 'X':
                    self.total_count += self.check_xmas((i,j))
    
    def scan_a(self):
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                if self.input[i][j] == 'A':
                    self.total_a_count += self.check_x_mas((i,j))
    
    def check_xmas(self, origin):
        cnt = 0
        letter = ['M', 'A', 'S']
        for plus_row in (-1, 0, 1):
            for plus_col in (-1, 0, 1):
                if plus_row == plus_col == 0:
                    continue
                for i in range(1,4):
                    if origin[0] + plus_row * i < 0:
                        break
                    if origin[1] + plus_col * i < 0:
                        break
                    if origin[0] + plus_row * i >= self.n_rows:
                        break
                    if origin[1] + plus_col * i >= self.n_cols:
                        break
                    if self.input[origin[0] + plus_row * i][origin[1] + plus_col * i] != letter[i-1]:
                        break
                    if i == 3:
                        cnt +=1
        return cnt
    
    def check_x_mas(self, origin):
        if origin[0] < 1 or origin[1] < 1:
            return 0
        if origin[0] > self.n_rows - 2 or origin[1] > self.n_cols - 2:
            return 0
        ul = self.input[origin[0] - 1][origin[1] - 1]
        bl = self.input[origin[0] + 1][origin[1] - 1]
        ur = self.input[origin[0] - 1][origin[1] + 1]
        br = self.input[origin[0] + 1][origin[1] + 1]
        
        if not (ul + br == 'MS' or ul + br == 'SM'):
            return 0
        if not (bl + ur == 'MS' or bl + ur == 'SM'):
            return 0
        return 1
        

                    



if __name__ == "__main__":
    with open("day04_input.py", "r") as f:
        puzzle_input = f.read().strip("\n")

    chag = puzzle(puzzle_input)
    print(chag.input)
    print(chag.n_rows)
    print(chag.n_cols)
    chag.scan_x()
    print(f'wordsearch count is {chag.total_count}')
    chag.scan_a()
    print(f'x mas shape count is {chag.total_a_count}')
    print("Done")
