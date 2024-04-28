class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []

    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    def add_node(self, value):
        self.nodes.append(value)

    def print_solution(self, dist):
        print("Vertex Distance from Source")
        for key, value in dist.items():
            print(' ' + key, ' : ', value)

    def bellman_ford(self, src):
        dist = {i: float('Inf') for i in self.nodes}
        dist[src] = 0
        for _ in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != float('inf') and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        for s, d, we in self.graph:
            if dist[s] != float('Inf') and dist[s] + w < dist[d]:
                print("The graph contains a negative cycle")
                return

        self.print_solution(dist)
