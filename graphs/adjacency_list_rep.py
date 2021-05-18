class Node:
    def __init__(self, v):
        self.vertex = v
        self.next = None


class Graph:
    def __init__(self, v):
        self.V = v
        self.graph = [None]*self.V


    def add_edge(self, src, dest):
        dest_node = Node(dest)
        dest_node.next = self.graph[src]
        self.graph[src] = dest_node


        src_node = Node(src)
        src_node.next = self.graph[dest]
        self.graph[dest] = src_node


    def print_graph(self):
        for i in range(self.V):
            temp = self.graph[i]
            print 'adjacency list of node ', i
            while temp != None:
                print temp.vertex
                temp = temp.next
            print '\n'


if __name__=='__main__':
    graph = Graph(5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.print_graph()
