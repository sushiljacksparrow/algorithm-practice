class Node:
    def __init__(self, key):
        self.val = key
        self.next = None


class Graph:
    def __init__(self, v):
        self.V = v
        self.graph = [[0 for x in range(self.V)] for y in range(self.V)]

    def add_edge(self, src, dest, v):
        self.graph[src][dest] = v
        self.graph[dest][src] = v


    def find_min_edge(self, key, mstSet):
        res = 999999
        res_node = -1
        for i in range(self.V):
            if mstSet[i] == False and key[i] < res:
                res = key[i]
                res_node = i
        return res_node

    def print_mst(self, parent):
        for i in range(1, self.V):
            print parent[i], i, ' -- ', self.graph[i][parent[i]]

    def prims_mst(self):
        key = [999999]*self.V
        parent = [None]*self.V
        key[0] = 0
        parent[0] = -1
        mstSet = [False]*self.V

        for i in range(self.V):
            adj_nodes = self.graph[i]
            u = self.find_min_edge(key, mstSet)
            mstSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.print_mst(parent)

if __name__=='__main__':
    g = Graph(9)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 7, 8)
    g.add_edge(1, 7, 11)
    g.add_edge(1, 2, 8)
    g.add_edge(2, 3, 7)
    g.add_edge(3, 4, 9)
    g.add_edge(4, 5, 10)
    g.add_edge(5, 6, 2)
    g.add_edge(3, 5, 14)
    g.add_edge(2, 5, 4)
    g.add_edge(2, 8, 2)
    g.add_edge(6, 8, 6)
    g.add_edge(6, 7, 1)
    g.add_edge(8, 7, 7)

    g.prims_mst()
