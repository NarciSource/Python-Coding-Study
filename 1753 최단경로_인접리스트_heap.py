import sys
from collections import defaultdict
V,E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
edges = defaultdict(list)
for _ in range(E):
    u,v,w = map(int, sys.stdin.readline().split())
    edges[u].append((w, v))

#dijkstra
from heapq import heappush, heappop
from math import inf
distance = [0]+[inf]*V
distance[K] = 0
heap = [(distance[K],K)]
while heap:                                             # O(E)
    w_via, via = heappop(heap)                          # O(logE)
    if w_via <= distance[via]:
        for w_dest, dest in edges[via]:
            if distance[dest] > w_via + w_dest:
                distance[dest] = w_via + w_dest
                heappush(heap, (w_via + w_dest, dest))  # O(logE)

print(*map(lambda d: "INF" if d==inf else d, distance[1:]), sep="\n")

# O(E)*(O(logE) + O(logE)) = O(ElogE) ~ O(ElogV)