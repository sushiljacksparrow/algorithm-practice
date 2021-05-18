class Graph:
    def __init__(self, v):
        self.V = v
        self.graph = []

    def add_edge(self, src, dest, weight):
        self.graph.append([src, dest, weight])

    def find(self, parent, v):
        if parent[v] == v:
            return v
        return self.find(parent, parent[v])

    def union(self, parent, u, v):
        x = self.find(parent, u)
        y = self.find(parent, v)

        if x > y:
            parent[x] = y
        else:
            parent[y] = x

    def kruskals(self):
        self.graph = sorted(self.graph, key=lambda item : item[2])

        result = []

        parent = {}
        for i in self.graph:
            parent[i[0]] = i[0]
            parent[i[1]] = i[1]

        i = 0
        for e in range(self.V-1):
            edge = self.graph[i]
            i += 1
            x = self.find(parent, edge[0])
            y = self.find(parent, edge[1])

            if x != y:
                result.append([edge])
                e += 1
                self.union(parent, edge[0], edge[1])

        for r in result:
            print r


if __name__=='__main__':
    g = Graph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)

    g.kruskals()
