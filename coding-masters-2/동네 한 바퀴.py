import sys
from collections import defaultdict
n,m=map(int,sys.stdin.readline().split())
edges = defaultdict(list)
for _ in range(m):
    s,e=map(int,sys.stdin.readline().split())
    edges[s].append(e)

def is_circle():
    q = [1]
    for node in q:
        for neighbor in edges[node]:
            q.append(neighbor)
            if neighbor == 1:
                return True
    return False
print("YES" if is_circle() else "NO")