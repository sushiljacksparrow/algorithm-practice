from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)


    def bfs(self, u):
        visited = [False]*(max(self.graph) + 1)

        queue = []
        queue.append(u)
        visited[u] = True

        while queue:
            temp = queue.pop(0)
            print temp
            for i in self.graph[temp]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True


    def dfs(self, u):
        visited = [False]*(max(self.graph) + 1)
        stack = []
        visited[u] = True
        stack.append(u)

        while stack:
            temp = stack.pop()
            print temp
            for i in self.graph[temp]:
                if not visited[i]:
                    stack.append(i)
                    visited[i] = True




if __name__=='__main__':
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    g.add_edge(2, 0)
    g.add_edge(0, 2)


    print 'bfs search'
    g.bfs(0)

    print 'dfs search'
    g.dfs(0)
