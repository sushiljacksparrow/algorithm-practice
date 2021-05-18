import sys

class Graph:
    def __init__(self, v):
        self.V = v
        self.graph = [[0] for x in range(self.V) for y in range(self.V)]

    def find_min(self, visited, dist):
        res = sys.maxint
        index = -1
        for i in range(self.V):
            if visited[i] == False and dist[i] < res:
                index = i
                res = dist[i]

        return index

    def dijkstras(self, src):
        dist = [sys.maxint]*self.V
        dist[src] = 0

        visited = [False]*self.V
        visited[src] = 0

        for i in range(self.V-1):
            u = self.find_min(visited, dist)
            visited[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and visited[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]


        for i in range(self.V):
            print i, ' --> ', dist[i]


    def dijkstras_queue(self, src):
        dist = [sys.maxint]*self.V
        dist[src] = 0

        queue = []
        queue.append(src)

        while queue:
            u = queue.pop(0)
            for v in range(self.V):
                if self.graph[u][v] > 0 and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
                    queue.append(v)

        for i in range(self.V):
            print i, ' --> ', dist[i]




if __name__=='__main__':
    g = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
            [4, 0, 8, 0, 0, 0, 0, 11, 0],
            [0, 8, 0, 7, 0, 4, 0, 0, 2],
            [0, 0, 7, 0, 9, 14, 0, 0, 0],
            [0, 0, 0, 9, 0, 10, 0, 0, 0],
            [0, 0, 4, 14, 10, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 1, 6],
            [8, 11, 0, 0, 0, 0, 1, 0, 7],
            [0, 0, 2, 0, 0, 0, 6, 7, 0]
            ];

    g.dijkstras(0);
    print 'queue based dijkstras'
    g.dijkstras_queue(0);
