import queue
def create_graph(filename):
    orbit_graph = {}
    with open(filename) as raw:
        for line in raw:
            up, down = line.strip("\n").split(")")
            if up not in orbit_graph.keys():
                orbit_graph[up] = set()
            orbit_graph[up].add(down)
    return orbit_graph

def create_undirected_graph(filename):
    orbit_graph = {}
    with open(filename) as raw:
        for line in raw:
            up, down = line.strip("\n").split(")")
            if up not in orbit_graph.keys():
                orbit_graph[up] = set()
            if down not in orbit_graph.keys():
                orbit_graph[down] = set()
            orbit_graph[up].add(down)
            orbit_graph[down].add(up)
    return orbit_graph

def orbit_tree_recur(orbit_graph, value, tgt):
    downstream_value = value
    if tgt not in orbit_graph.keys():
        return value
    else:
        for new in orbit_graph[tgt]:
            downstream_value += orbit_tree_recur(orbit_graph, value + 1, new)
    return downstream_value

def bfs(uorbit_graph, start, goal):
    search = queue.Queue()
    visited = set()
    search.put((start,0))
    while not search.empty():
        next, dist = search.get()
        if next in visited:
            continue
        visited.add(next)
        if next == goal:
            return dist - 2 
        
        for adj in uorbit_graph[next]:
            if adj in visited:
                continue
            search.put((adj, dist+1))
    return -1

if __name__ == "__main__":
    graph = create_graph("day06.txt")
    n_orbits = orbit_tree_recur(graph, 0, 'COM')
    print(n_orbits)
    ugraph = create_undirected_graph("day06.txt")
    dist = bfs(ugraph, "YOU", "SAN")
    print(dist)


