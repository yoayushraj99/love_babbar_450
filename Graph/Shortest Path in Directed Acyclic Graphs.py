from collections import defaultdict


class Graph:
    def __init__(self):
        self.adj = defaultdict(list)

    def addEdge(self, u, v, weight):
        # Create a pair of vertex and weight
        p = [v, weight]
        self.adj[u].append(p)

    def printAdj(self):
        for index, item in enumerate(self.adj.values()):
            print(index, end="-> ")
            for j in item:
                print(f'({j[0]}, {j[1]}),', end=" ")
            print()

    def dfs(self, node, vis, topo):
        vis[node] = 1

        for neighbour in self.adj[node]:
            if not vis[neighbour[0]]:
                self.dfs(neighbour[0], vis, topo)
        topo.append(node)

    def getShortestPath(self, src, dist, topo):
        dist[src] = 0

        while topo:
            top = topo.pop()

            if dist[top] != float('inf'):
                for k in self.adj[top]:
                    if dist[top] + k[1] < dist[k[0]]:
                        dist[k[0]] = dist[top] + k[1]


g = Graph()
g.addEdge(0, 1, 5)
g.addEdge(0, 2, 3)
g.addEdge(1, 2, 2)
g.addEdge(1, 3, 6)
g.addEdge(2, 3, 7)
g.addEdge(2, 4, 4)
g.addEdge(2, 5, 2)
g.addEdge(3, 4, -1)
g.addEdge(4, 5, -2)

g.printAdj()

n = 6
# Topological Sort
visited = defaultdict(bool)
stack = []

for i in range(n):
    if not visited[i]:
        g.dfs(i, visited, stack)

distance = [float('inf')] * n
g.getShortestPath(1, distance, stack)
print("answer is:", distance[1:])
