import sys
N,M = map(int,sys.stdin.readline().split())

roots = [i for i in range(N+1)]
def find(v):
    while roots[v] != v:
        v = roots[v]
    return v

for _ in range(M):
    u,v = map(int,sys.stdin.readline().split())
    roots[find(v)] = find(u)
roots = [find(v) for v in roots]

from collections import Counter
id, times = Counter(roots).most_common(1)[0]
print(roots.index(id))