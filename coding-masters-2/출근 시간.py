import sys
from collections import defaultdict
n,m,k=map(int,sys.stdin.readline().split())
edges = defaultdict(list)
for _ in range(m):
    u,v,w = map(int,sys.stdin.readline().split())
    edges[u].append((w,v))

from heapq import heappush, heappop
from math import inf
def dijkstra(start):
    distances = [0]+[inf]*n
    distances[start] = 0
    heap = [(distances[start],start)]
    while heap:
        w_via, via = heappop(heap)
        if w_via <= distances[via]:
            for w_dest, dest in edges[via]:
                if distances[dest] > w_via + w_dest:
                    distances[dest] = w_via + w_dest
                    heappush(heap, (w_via + w_dest, dest))
    return distances
print(dijkstra(1)[k]+dijkstra(k)[n])