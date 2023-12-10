import sys
from collections import defaultdict
n,m = map(int, sys.stdin.readline().split())
bridges = defaultdict(list)
for _ in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    bridges[a].append((c, b))
    bridges[b].append((c, a))
start, end = map(int, sys.stdin.readline().split())

from heapq import heappush, heappop
from math import inf
distance = [0]+[0]*n
distance[start] = inf
heap = [(-inf, start)]
while True:
    w_node, node = (lambda x,y:(-x,y))(*heappop(heap))
    if node != end:
        for w_dest, dest in bridges[node]:
            w_dest = min(w_node, w_dest)
            if distance[dest] < w_dest:
                distance[dest] = w_dest
                heappush(heap, (-w_dest, dest))
    else: break

print(distance[end])