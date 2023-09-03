import sys
n = int(sys.stdin.readline())

blueprint = []
def dfs(start, target, changed):
    global blueprint
    q = [start]
    count = 0
    while q:
        x, y = q.pop()
        dir = [(-1,0),(1,0),(0,-1),(0,1)]

        for dx,dy in dir:
            mx, my = x+dx, y+dy
            if 0<=mx<10 and 0<=my<20 and blueprint[mx][my] == target:
                blueprint[mx][my] = changed
                count +=1
                q.append((mx, my))
    return count

for i in range(n):
    blueprint = [list(sys.stdin.readline()) for _ in range(10)]
    satisfied = 0

    count = 0
    for x in range(10):
        for y in range(20):
            if blueprint[x][y]=='.':
                dfs((x,y), '.', 'v')
                count +=1
    if count==1:
        satisfied += 1

    dfs((0,0), '#', 'w')

    count = 0
    check = True
    for x in range(10):
        for y in range(20):
            if blueprint[x][y]=='#':
                pillars=dfs((x,y), '#', 'v')

                if pillars>=6:
                    count+=1
    if count >= 1 and check:
        satisfied += 2

    print(satisfied)