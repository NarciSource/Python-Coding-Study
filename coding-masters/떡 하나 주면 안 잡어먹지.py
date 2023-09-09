import sys, math, collections
n = int(sys.stdin.readline())
road = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
ddeok = [[math.inf]*n for _ in range(n)]
dir = [(-1,0),(0,-1),(1,0),(0,1)]

q = collections.deque([(0,0)])
ddeok[0][0]=road[0][0]
while q:
    x,y = q.popleft()
    if x!=n-1 or y!=n-1:
        for dx,dy in dir:
            mx,my = x+dx,y+dy
            if 0<=mx<n and 0<=my<n:
                if ddeok[mx][my] > road[mx][my] + ddeok[x][y]:
                    ddeok[mx][my] = road[mx][my] + ddeok[x][y]
                    q.append((mx,my))
print(ddeok[n-1][n-1])