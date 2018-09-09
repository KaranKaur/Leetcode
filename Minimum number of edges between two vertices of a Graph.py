"""

You are given a undirected graph G(V, E) with N vertices and M edges.
We need to find the minimum number of edges between a given pair of vertices (u, v).

"""

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edges(self, u, v):
        self.graph[u].append(v)


    def min_count_edges(self, s, d):
        visited = [False]* self.V
        distance = [0] * self.V

        queue = []

        queue.append(s)
        visited[s] = True

        while queue:
            n = queue.pop(0)
            if n == d:
                return distance[d]
            else:
                for i in self.graph[n]:
                    if visited[i] == False:
                        queue.append(i)
                        visited[i] = True
                        distance[i] = distance[n] + 1

g = Graph(9) # telling that graph has 9 vertices
g.add_edges(0, 1)
g.add_edges(0, 7)
g.add_edges(1, 7)
g.add_edges(1, 2)
g.add_edges(2, 3)
g.add_edges(2, 5)
g.add_edges(2, 8)
g.add_edges(3, 4)
g.add_edges(3, 5)
g.add_edges(4, 5)
g.add_edges(5, 6)
g.add_edges(6, 7)
g.add_edges(7, 8)

u =0; v = 5

print(g.min_count_edges(u, v))

