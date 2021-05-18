from collections import defaultdict

class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighbours = {}

    def add_neighbour(self, neighbour, weight):
        self.neighbours[neighbour] = weight


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, key):
        vertex = Vertex(key)
        self.vertices[key] = vertex

    def add_edge(self, src, dest, weight):
        if self.vertices[src] == None:
            self.add_vertex(src)
        if self.vertices[dest] == None:
            self.add_vertex(dest)

        self.vertices[src].add_neighbour(dest, weight)

    def print_graph(self):
        for i in self.vertices:
            for j in self.vertices[i].neighbours:
                print i, ' --> ', j, ' --> ', self.vertices[i].neighbours[j]


if __name__=='__main__':
    g = Graph()
    for i in range(6):
        g.add_vertex(i)

    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 100)
    g.add_edge(1, 5, 20)
    g.add_edge(3, 5, 20)

    g.print_graph()
