# print("Prompt looks like it was written by an LLM")

test_input = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

class day8:
    
    def __init__(self, puzzle_input):
        self.grid = self.process_input(puzzle_input)
        self.rowlen = len(self.grid)
        self.collen = len(self.grid[0])
        self.antenna = self.process_grid()
        self.antenna_dists = self.process_all_antenna()
        # self.resonances = self.process_resonance()

    def process_input(self, input):
        input_lines = input.splitlines()
        grid = []
        for line in input_lines:
            grid.append(list(line))
        return grid

    def process_grid(self):
        antenna_list = dict()
        for i in range(self.rowlen):
            for j in range(self.collen):
                if self.grid[i][j] != '.':
                    if self.grid[i][j] not in antenna_list.keys():
                        antenna_list[self.grid[i][j]] = list()
                        antenna_list[self.grid[i][j]].append((i,j))
                    else: 
                        antenna_list[self.grid[i][j]].append((i,j))
        return antenna_list
    
    def process_single_antenna(self, coord):
        dist_dict = dict() 
        for i in range(self.rowlen):
            for j in range(self.collen):
                axis_0_dist = abs(i - coord[0])
                axis_1_dist = abs(j - coord[1])
                x = min(axis_0_dist, axis_1_dist)
                y = max(axis_0_dist, axis_1_dist)
                if (x,y) not in dist_dict.keys():
                    dist_dict[(x,y)] = []
                dist_dict[(x,y)].append( (i,j) )

        return dist_dict

    def process_antenna_class(self, antenna_key):
        antenna_class_dict = dict()
        for val in self.antenna[antenna_key]:
            antenna_class_dict[val] = self.process_single_antenna(val)
        return antenna_class_dict
    
    def process_all_antenna(self):
        all_antenna_dists = dict()
        for key in self.antenna.keys():
            all_antenna_dists[key] = self.process_antenna_class(key)

        return all_antenna_dists
            
    def process_single_resonance(self, key, ant1, ant2):
        resonant_subset = set()
        ant1_dists = self.antenna_dists[key][ant1]
        ant2_dists = self.antenna_dists[key][ant2]

        for key in ant1_dists.keys():
            doublekey = (key[0] * 2, key[1] * 2)
            if doublekey in ant2_dists.keys():
                for coord in ant1_dists[key]:
                    if coord in ant2_dists[doublekey]:
                        resonant_subset.add(coord)
    
        for key in ant2_dists.keys():
            doublekey = (key[0] * 2, key[1] * 2)
            if doublekey in ant1_dists.keys():
                for coord in ant2_dists[key]:
                    if coord in ant1_dists[doublekey]:
                        resonant_subset.add(coord)
        return resonant_subset

    def process_resonance(self, key):
        resonant_set = set()
        for i in range(len(self.antenna[key])):
            for j in range(1, len(self.antenna[key])):
                antenna_1 = self.antenna[key][i]
                antenna_2 = self.antenna[key][j]
                subset = self.process_single_resonance(key, antenna_1, antenna_2)
                resonant_set.update(subset)
        
        return resonant_set

        

            




        

if __name__ == "__main__":
    pt1 = day8(test_input)
    print(pt1.antenna)
    print(pt1.antenna_dists.keys())
    print(pt1.antenna_dists['0'].keys())
    print(pt1.antenna)
    print(pt1.process_resonance('0'))
    print(len(pt1.process_resonance('0')))


    