import sys
n, m = map(int,sys.stdin.readline().split())
zoo = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

tigers = [(x,y) for x in range(n) for y in range(m) if zoo[x][y]==2]
fields = [(x,y) for x in range(n) for y in range(m) if zoo[x][y]==0]


def relaseTiger(zoo):
    zoo = [zoo[i][:] for i in range(n)]
    q = tigers[:]
    acc = []
    while q:
        x, y = q.pop()
        dir = [(-1,0),(1,0),(0,-1),(0,1)]

        for dx,dy in dir:
            mx, my = x+dx, y+dy
            if 0<=mx<n and 0<=my<m and zoo[mx][my] == 0:
                zoo[mx][my] = 2
                acc.append((mx, my))
                q.append((mx, my))
    return acc

from itertools import *
tiger_moved_len = []
for three in combinations(relaseTiger(zoo), 3):
    for (x,y) in three: zoo[x][y] = 1
    tiger_moved_len.append(len(relaseTiger(zoo)))
    for (x,y) in three: zoo[x][y] = 0

print(len(fields) - min(tiger_moved_len) -3)