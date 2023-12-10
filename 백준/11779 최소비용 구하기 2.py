import sys
from collections import defaultdict
N,M = int(sys.stdin.readline()), int(sys.stdin.readline())
edges = defaultdict(list)
for _ in range(M):
    to,dest,weight = map(int, sys.stdin.readline().split())
    edges[to].append((weight, dest))
A,B = map(int, sys.stdin.readline().split())

#dijkstra
from heapq import heappush, heappop
from math import inf
distance = [0]+[inf]*N
distance[A] = 0
parents = [v for v in range(N+1)]
heap = [(distance[A],A)]
while heap:
    w_via, via = heappop(heap)
    if w_via <= distance[via]:
        for w_dest, dest in edges[via]:
            if distance[dest] > w_via + w_dest:
                distance[dest] = w_via + w_dest
                parents[dest] = via
                heappush(heap, (w_via + w_dest, dest))

track = [B]
for t in track:
    if t!=A:
        track.append(parents[t])

print(distance[B])
print(len(track))
print(*reversed(track))