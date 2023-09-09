import sys
n,m=int(sys.stdin.readline()),5
cells=[list(sys.stdin.readline()) for _ in range(m)]
ds = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
adjcells = lambda x,y: [(x+dx,y+dy) for dx,dy in ds if 0<=x+dx<m and 0<=y+dy<m and cells[x+dx][y+dy]=='1']

for i in range(n):
    live=[]
    for x in range(m):
        for y in range(m):
            if ((cells[x][y]=='1' and 2<=len(adjcells(x,y))<=3) or
                    (cells[x][y]=='0' and len(adjcells(x,y))==3)):
                live.append((x,y))
    cells=[['0']*m for _ in range(m)]
    for x,y in live: cells[x][y]='1'

for i in range(m):
    print(''.join(cells[i]))