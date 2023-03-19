from collections import deque, defaultdict


# Using BFS (T.C -> O(n), S.C -> O(n))

def isCyclicBFS(src, visited, adj):
    parent = defaultdict(int)

    parent[src] = -1
    visited[src] = 1
    q = deque()
    q.append(src)

    while q:
        front = q.popleft()

        for neighbour in adj[front]:
            if visited[neighbour] and neighbour != parent[front]:
                return True
            elif not visited[neighbour]:
                q.append(neighbour)
                visited[neighbour] = 1
                parent[neighbour] = front

    return False


def cycleDetection(edges, n, m):
    adjList = defaultdict(list)
    for i in range(m):
        u = edges[i][0]
        v = edges[i][1]

        adjList[u].append(v)
        adjList[v].append(u)

    # To handle disconnected components
    visited = defaultdict(bool)
    for i in range(n):
        if not visited[i]:
            ans = isCyclicBFS(i, visited, adjList)
            if ans == 1:
                return "Yes"

    return "No"


# Using DFS


def isCyclicDFS(node, parent, visited, adj):
    visited[node] = 1

    for neighbour in adj[node]:
        if not visited[neighbour]:
            cycleDetected = isCyclicDFS(neighbour, node, visited, adj)
            if cycleDetected:
                return True
        elif neighbour != parent:
            return True

    return False


def cycleDetection(edges, n, m):
    adjList = defaultdict(list)
    for i in range(m):
        u = edges[i][0]
        v = edges[i][1]

        adjList[u].append(v)
        adjList[v].append(u)

    # To handle disconnected components
    visited = defaultdict(bool)
    for i in range(n):
        if not visited[i]:
            ans = isCyclicDFS(i, -1, visited, adjList)
            if ans == 1:
                return "Yes"

    return "No"
