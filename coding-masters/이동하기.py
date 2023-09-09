import sys
n = int(sys.stdin.readline())
x1,y1 = map(int,sys.stdin.readline().split())
x2,y2 = map(int,sys.stdin.readline().split())
count=0
def dfs(x,y, acc, moved):
    global count
    if not(x==x2 and y==y2):
        if moved<n and abs(x2-x)+abs(y2-y)<=n-moved:
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                mx,my = x+dx,y+dy
                if (mx,my) not in acc:
                    dfs(mx,my, acc+[(mx,my)], moved+1)
    elif moved==n:
        count+=1
dfs(x1,y1, [(x1,y1)], 0)
print(count)