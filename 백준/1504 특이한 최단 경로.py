import sys
from collections import defaultdict
N,E = map(int, sys.stdin.readline().split())
edges = defaultdict(list)
for _ in range(E):
    a,b,c = map(int, sys.stdin.readline().split())
    edges[a].append((c, b))
    edges[b].append((c, a))
v1,v2 = map(int, sys.stdin.readline().split())

from heapq import heappush, heappop
from math import inf
from functools import cache
@cache
def dijkstra(start):
    distances = [0]+[inf]*N
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

from itertools import starmap
distance = lambda to,dest: dijkstra(to)[dest]
route = lambda orders: sum(starmap(distance, zip(orders[:-1], orders[1:])))
min_route = min(route([1,v1,v2,N]), route([1,v2,v1,N]))
print(-1 if min_route==inf else min_route)