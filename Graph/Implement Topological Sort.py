from collections import defaultdict


def topoSort(node, visited, adj, stack):
    visited[node] = 1

    for neighbour in adj[node]:
        if not visited[neighbour]:
            topoSort(neighbour, visited, adj, stack)
    stack.append(node)


def topologicalSort(adj, v, e):
    # Write your code here
    adjList = defaultdict(list)
    for i in range(e):
        x = adj[i][0]
        y = adj[i][1]

        adjList[x].append(y)

    stack = []
    visited = defaultdict(bool)

    for i in range(v):
        if not visited[i]:
            topoSort(i, visited, adjList, stack)

    if stack:
        return stack[::-1]
