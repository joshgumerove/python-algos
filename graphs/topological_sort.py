from collections import defaultdict


class Graph():
    def __init__(self, numberOfVertices):
        self.graph = defaultdict(list)
        self.numberOfVertices = numberOfVertices

    def add_edge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def topological_sort_util(self, v, visited, stack):
        visited.append(v)

        for i in self.graph[v]:
            if i not in visited:
                self.topological_sort_util(i, visited, stack)

        stack.insert(0, v)

    def topological_sort(self):
        visited = []
        stack = []

        for k in list(self.graph):
            if k not in visited:
                self.topological_sort_util(k, visited, stack)
        print(stack)

    def print_graph(self):
        for vertex in self.graph:
            print(vertex, ":", self.graph[vertex])


custom_graph = Graph(8)
custom_graph.add_edge("A", "C")
custom_graph.add_edge("C", "E")
custom_graph.add_edge("E", "H")
custom_graph.add_edge("E", "F")
custom_graph.add_edge("F", "G")
custom_graph.add_edge("B", "D")
custom_graph.add_edge("B", "C")
custom_graph.add_edge("D", "F")

custom_graph.print_graph()
print("\n topological sort \n")
custom_graph.topological_sort()
