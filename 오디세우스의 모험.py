import sys
n,m = map(int,sys.stdin.readline().split())
from collections import defaultdict 
edges = defaultdict(list)
for i in range(m):
    a,b,v = map(int,sys.stdin.readline().split())
    edges[a].append((b,v))
    edges[b].append((a,v))
start,end = map(int,sys.stdin.readline().split())

from math import inf
time = [0]*(n+1)
time[start] = inf
q = [start]
while q:
    node = q.pop()

    if node != end:
        for adj_node, t in edges[node]:
            if time[adj_node] < min(t, time[node]):
                time[adj_node] = min(t, time[node])
                q.append(adj_node)
print(time[end])