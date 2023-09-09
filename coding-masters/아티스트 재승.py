import sys
paint = sys.stdin.readline().rstrip()
n,m = map(int,sys.stdin.readline().split())
canvas = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

dir = [(-1,0),(1,0),(0,-1),(0,1)]
def draw(x,y, paint):
    if len(paint):
        enabled = False
        ink = canvas[x][y]
        canvas[x][y]='X'
        for dx,dy in dir:
            mx,my = x+dx,y+dy
            if 0<=mx<n and 0<=my<m and canvas[mx][my]==paint[0]:
                enabled = draw(mx,my, paint[1:])
                if enabled: break
        canvas[x][y]=ink

        if enabled: return True
    else:
        return True

count = 0
if len(paint) == len([ink for columns in canvas for ink in columns if ink!='.']):
    for x in range(n):
        for y in range(m):
            if canvas[x][y] == paint[0]:
                if draw(x,y, paint[1:]):
                    count+=1
print(count)