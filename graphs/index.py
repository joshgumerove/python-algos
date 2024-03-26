class Graph():
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def add_edge(self, vertex, edge):
        self.gdict[vertex].append(edge)


custom_dict = {
    "a": ["b", "c"],
    "b": ["a", "d", "e"],
    "c": ["a", "e"],
    "d": ["b", "e", "f"],
    "e": ["b", "d", "f"],
    "f": ["d", "e"]
}

graph = Graph(custom_dict)
print(graph.gdict)

graph.add_edge("e", "c")
print(graph.gdict)
