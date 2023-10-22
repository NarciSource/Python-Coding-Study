import sys

n = int(sys.stdin.readline())
sheeps, wolves, parents = zip(*[(lambda t,a,p:(int(a) if t=='S' else 0,
                                               int(a) if t=='W' else 0,
                                               int(p))
                                )(*sys.stdin.readline().split()) for _ in range(n-1)])
sheeps, wolves, parents = [0,0]+list(sheeps), [0,0]+list(wolves), [0,0]+list(parents)

from collections import defaultdict
childrens = defaultdict(list)
for child, parent in enumerate(parents):
    childrens[parent].append(child)

def bfs(start):
    stack = [start]
    for node in stack:
        stack.extend(childrens[node])

    for node in reversed(stack):
        sheeps[parents[node]] += max(sheeps[node]-wolves[node], 0)
    return sheeps[start]
print(bfs(1))