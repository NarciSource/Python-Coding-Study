import sys
n,m = int(sys.stdin.readline()), int(sys.stdin.readline())

from collections import defaultdict
edges = defaultdict(list)

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    edges[a].append(b)
    edges[b].append(a)

moved = [1]
for cur in moved:
    for neighbor in edges[cur]:
        if neighbor not in moved:
            moved.append(neighbor)

print(len(moved)-1)
