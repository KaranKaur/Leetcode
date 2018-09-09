"""

Find if there is a path between two vertices in a directed graph

"""

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edges(self, u,v):
        self.graph[u].append(v)

    def is_reachable(self, s, d):
        visited = [False]*self.V # all vertices unmarked
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:

            n = queue.pop(0) # popping operation takes O(N) time
            if n == d:
                return True
            else:
                for i in self.graph[n]:
                    if visited[i] == False:
                        queue.append(i)
                        visited[i] = True

        return False


g = Graph(4) # telling that graph has 4 vertices
g.add_edges(0, 1)
g.add_edges(0, 2)
g.add_edges(1, 2)
g.add_edges(2, 0)
g.add_edges(2, 3)
g.add_edges(3, 3)

u =1; v = 3

if g.is_reachable(u, v):
    print("There is a path from %d to %d" % (u, v))
else:
    print("There is no path from %d to %d" % (u, v))

u = 3; v = 1
if g.is_reachable(u, v):
    print("There is a path from %d to %d" % (u, v))
else:
    print("There is no path from %d to %d" % (u, v))



