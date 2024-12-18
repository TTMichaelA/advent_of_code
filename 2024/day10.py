
test_input = """5678543238765121087216787432128921016563210454323433
4169654119654037892107894549017430457654782369412812
3018767001843246543210787678186543368945691078908903
2189678914980158934345698187098901275632100165001894
3434589125678767891016521096167872984789321874112765
7823678034569876780123434545252766543215476903233456
6910167012423495679654321032341057630306985012945101
5401986543410584508765678211352348921437894123876298
4323877892543673210104569300235496530890123434565387
3210967871652598789213075410145687432765210123432456
0101454960701659654322186703456710101854321076501201
1012343459898741023763099812769823478923212987655652
4323012321101232212854210129876012569012503234234743
5011001410765540101940110238787112876503414105109892
6722340543894691001233221045698108976434565696589321
9821059652023782317874536789587012885325676787678780
9778968701110678498965945893496543494018989801210690
8769878889231589567767893672109824323561234892309541
1454399998342490430850104589678012012370348763458032
0141287107654321521943213212565503123987659654567123
1230236256565410101237870101419654598543210508948910
2340145348978321253210965432308765687696501417654323
3986501567899010344789876323219454766787432321078890
5677432450987432455670189410012349845696501434569701
0548901321976501964563208231987210036723109621435652
1239678100823457877854010145676210129814918730898543
4310369234710165756905423210122305610905825623567678
3423456765600874543814554761201456723876734514410569
2102109894321984562323669854398556894985232305320438
3076521003965433871234778034567647895894101476761023
4585412312870122930129872129867634456783230585872310
5694303456781211123123401256798521065656187694965432
6783201019892100054076540346543438980521090123456501
0340112387653456963981639457832523671439876101219602
1258903490144327870190128768901214512112725614308712
2569876589231016983278787434980108903003014525456893
1876767676546781074349896523076587654394523496327854
0945778789035690165234765014123496543487621087018969
1239869876124789234105676543287017012567634589829678
9018756765453210785411085010196528921298565676543549
8723605034301305696532398923483437430143476589762138
7634514125212154387783437654589016521052187679854023
6501323896521093210598568943078723632367098512763210
7432454787436789765677678732189654045458963403892001
8901343474345658894389589823476902102167872354301123
7623676543216743001210438214567813458054961065689054
5012389012109812123309321301054324569123452876548765
4589438729001901014578010102344567078212556989231076
3676567438782342145665430230133898167901665476102989
2109652145699654398765421321212101237810174345603478
1078743034328765219876323478903894376521089298714565
2167634145410898701101210569816765489432100107623434"""

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