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


true_input = """....................8.D.........Y...........c.....
....f.............D......O...........Y............
.......z..........7.N..........g..................
..........h...........9g.7....................Y...
.............8...............................c....
...9..8...............L........D....O.....l.......
..........f.9.......h.........................l...
...z...B..........................................
.................M.....C.....OR7.Y..g..........l..
........................M.......N.................
...............h..................TD....H.........
......z......M........C8.......N.......m.T........
......O.......................................A...
...........a...........h..........................
................B..................j..............
..............v..f..........g.....................
.......N..........s.M.........n..............Q....
...............s.........j.......................A
......................a......................T...b
........s....v......H..c..............j..i....m...
.......................a........2H.......m..V.....
................n.B..........o.....H......2.......
.....3.......s.B..............x......S..K.........
.3.G..................J................V...l.x..T.
....3.......................E..................V..
3..........................E..........V...i.......
...............v.......n.E...................2.i..
..F.........r.e......n....E...........A..Q.....K..
..z................................A....Q.........
.................................b..Q...d.Sw......
..G...0..e............v.......Z...j.....m...b.....
..y.............0.a.............................K.
.............Gp....Z.................4......S.....
....oJ....G........e.........Z............b.X.....
C........o.r........WL..1.......X........K.....d..
..................Z1.....r...............F........
............L.4................1.6..............tF
...y...............L......1............26.t.......
......e.k......y........I......x......d........t.R
.......0.........k...............d.........tWR..x.
..........q.....r......J..................F..P..w.
..........................5..........XwW..........
...........0....y.............J.............6p....
..q...k.......................I.....4........SR...
.........q..o.......P................W............
.............q.IP..............................p..
.....k...................w.............X.......f..
.............P...............4..................p.
.................I..........5.....................
.C.................................5...6.........."""

class day8:
    
    def __init__(self, puzzle_input):
        self.grid = self.process_input(puzzle_input)
        self.rowlen = len(self.grid)
        self.collen = len(self.grid[0])
        self.antenna = self.process_grid()
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

    def get_delta(self, ant1, ant2):
        x_delta = abs((ant1[0] - ant2[0]))
        y_delta = abs((ant1[1] - ant2[1]))
        return x_delta, y_delta
    
    def find_opposites(self, ant1, ant2):
        x_delta, y_delta = self.get_delta(ant1, ant2)

        min_x = min(ant1[0], ant2[0])
        max_x = max(ant1[0], ant2[0])
        min_y = min(ant1[1], ant2[1])
        max_y = max(ant1[1], ant2[1])

        new_xmin = min_x - x_delta
        new_xmax = max_x + x_delta
        new_ymin = min_y - y_delta
        new_ymax = max_y + y_delta

        if ant1[0] <= ant2[0]:
            if ant1[1] <= ant2[1]:
                return (new_xmin, new_ymin), (new_xmax, new_ymax)
            else:
                return (new_xmin, new_ymax), (new_xmax, new_ymin)
        else:
            if ant1[1] <= ant2[1]:
                return (new_xmin, new_ymin), (new_xmax, new_ymax)
            else:
                return (new_xmin, new_ymax), (new_xmax, new_ymin)


    def explore_resonances(self):
        resonance_set = set()
        for antenna_type, antenna_list in self.antenna.items():
            for i in range(len(antenna_list)):
                for j in range(i+1,len(antenna_list)):
                    ant1 = antenna_list[i]
                    ant2 = antenna_list[j]
                    r1, r2 = self.find_opposites(ant1, ant2)
                    add_r1 = True
                    add_r2 = True
                    if r1[0] >= len(self.grid) or r1[0] < 0:
                        add_r1 = False
                    if r1[1] >= len(self.grid[0]) or r1[0] < 0:
                        add_r1 = False
                    if r2[0] >= len(self.grid) or r2[0] < 0:
                        add_r2 = False
                    if r2[1] >= len(self.grid[0]) or r2[0] < 0:
                        add_r2 = False
                    
                    if add_r1:
                        resonance_set.add(r1)
                    if add_r2:
                        resonance_set.add(r2)
        return resonance_set
            
if __name__ == "__main__":
    pt1 = day8(true_input)
    # print(pt1.antenna)
    gz = pt1.explore_resonances()
    print(len(gz))
    # print(gz)
    
    