import sys
n,m = map(int,sys.stdin.readline().split())
edges = sorted([list(map(int,sys.stdin.readline().split())) for _ in range(m)], key=lambda e:e[2])

roots = [i for i in range(n+1)]
def whatRoot(v):
    while roots[v] != v:
        v = roots[v]
    return v

mst = visited = 0
for (a,b,c) in edges:
    if visited == n-1:
        break
    elif whatRoot(a) != whatRoot(b):
        if a<b:
            roots[whatRoot(b)] = whatRoot(a)
        else:
            roots[whatRoot(a)] = whatRoot(b)
        mst += c
        visited += 1
print(mst)