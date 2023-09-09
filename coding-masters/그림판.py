def getAreaColor(point):
    q = [point]
    acc = []
    while q:
        x, y = q.pop()
        dir = [(-1,0),(1,0),(0,-1),(0,1)]

        for dx,dy in dir:
            mx, my = x+dx, y+dy
            if 0<=mx<n and 0<=my<m and paint[mx][my] != 'X':
                acc.append(paint[mx][my])
                q.append((mx, my))
                paint[mx][my] = 'X'
    return acc

import sys
n,m = map(int,sys.stdin.readline().split())
paint = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
a,b = map(sum, zip(*[(p.count('A'), p.count('B')) for p in paint]))
for i in range(n):
    for j in range(m):
        if paint[i][j] != 'X':
            colors = getAreaColor((i,j))
            ac,bc = colors.count('A'), colors.count('B')
            if ac<=bc:
                a-=ac
            elif ac>bc:
                b-=bc
print(a,b)