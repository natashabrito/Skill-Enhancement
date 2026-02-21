# 3. The "Dynamic Network Vulnerability" (Tarjan's/Graphs)
# ○ Problem: Given a communication network represented as an undirected graph,
# identify all "Critical Links" (Bridges). A link is critical if its removal disconnects the
# network.
# ○ Complexity Requirement: Solve in O(V + E) using a single DFS pass.

from collections import defaultdict

class Graph:
    def __init__(self, n):
        self.n = n
        self.g = defaultdict(list)
        self.time = 0

    def add_edge(self, u, v):
        self.g[u].append(v)
        self.g[v].append(u)

    def dfs(self, u, parent, disc, low, res):

        disc[u] = low[u] = self.time
        self.time += 1

        for v in self.g[u]:

            if disc[v] == -1:   

                self.dfs(v, u, disc, low, res)

                low[u] = min(low[u], low[v])

                if low[v] > disc[u]:
                    res.append((u, v))

            elif v != parent:  # back edge
                low[u] = min(low[u], disc[v])

    def bridges(self):

        disc = [-1] * self.n
        low = [-1] * self.n
        res = []

        for i in range(self.n):
            if disc[i] == -1:
                self.dfs(i, -1, disc, low, res)

        return res
g = Graph(5)

edges = [(0,1),(1,2),(2,0),(1,3),(3,4)]

for u, v in edges:
    g.add_edge(u, v)

print(g.bridges())
