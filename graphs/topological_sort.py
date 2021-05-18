from collections import defaultdict


class Graph:
    def __init__(self, v):
        self.V = v
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort(self):
        visited = [False]*self.V
        res = []
        for i in range(self.V):
            if visited[i] == False:
                stack = []
                stack.append(i)
                visited[i] = True
                while stack:
                    t = stack.pop()
                    res.append(t)
                    for j in self.graph[t]:
                        if visited[j] == False:
                            stack.append(j)
                            visited[j] = True

        print res[::-1]



if __name__=='__main__':
    g = Graph(6)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)
    g.topological_sort()
