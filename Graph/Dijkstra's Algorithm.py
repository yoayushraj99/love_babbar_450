from typing import *
from collections import defaultdict
import heapq


def dijkstra(vec: List[List[int]], vertices: int, edges: int, source: int):
    adj = defaultdict(list)

    for i in range(edges):
        u = vec[i][0]
        v = vec[i][1]
        w = vec[i][2]

        adj[u].append((v, w))
        adj[v].append((u, w))

    n = vertices
    # set up "inf" distances
    dist = [2147483647 for _ in range(n)]
    # set up root distance
    dist[source] = 0
    # set up visited node list
    visited = [False for _ in range(n)]
    # set up priority queue
    pq = [(0, source)]
    # while there are nodes to process
    while len(pq) > 0:
        # get the root, discard current distance
        _, u = heapq.heappop(pq)
        # if the node is visited, skip
        if not visited[u]:
            # set the node to visited
            visited[u] = True
            # check the distance and node and distance
            for v, l in adj[u]:
                # if the current node's distance + distance to the node we're visiting
                # is less than the distance of the node we're visiting on file
                # replace that distance and push the node we're visiting into the priority queue
                if dist[u] + l < dist[v]:
                    dist[v] = dist[u] + l
                    heapq.heappush(pq, (dist[v], v))
    return dist
