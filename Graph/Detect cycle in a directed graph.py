from collections import defaultdict


# Using DFS

def checkCycleDFS(node, visited, dfsVisited, adj):
    visited[node] = 1
    dfsVisited[node] = 1

    for neighbour in adj[node]:
        if not visited[neighbour]:
            cycleDetected = checkCycleDFS(neighbour, visited, dfsVisited, adj)
            if cycleDetected:
                return True
        elif dfsVisited[neighbour]:
            return True

    dfsVisited[node] = 0
    return False


def detectCycleInDirectedGraph(n, edges):
    # Write your code here
    adj = defaultdict(list)
    for i in range(len(edges)):
        u = edges[i][0]
        v = edges[i][1]

        adj[u].append(v)

    visited = defaultdict(bool)
    dfsVisited = defaultdict(bool)

    for i in range(n):
        if not visited[i]:
            cycleDetected = checkCycleDFS(i, visited, dfsVisited, adj)
            if cycleDetected:
                return True

    return False
