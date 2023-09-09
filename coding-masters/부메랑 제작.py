import sys
#n,m = map(int,sys.stdin.readline().split())
#wood = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
n,m = 3, 3
wood = [[32, 83, 75], [24, 96, 56], [71, 88, 12]]
shapes = [(-1,0),(0,0),(-1,-1)], [(0,0),(0,-1),(-1,0)], [(0,-1),(0,0),(-1,-1)], [(-1,-1),(0,-1),(-1,0)]
visited = [[False]*m for _ in range(n)]


def dfs(point, strength):
    if point:
        strength_bundle = []
        px,py = point
        nxt = None if py==m-1 and px==n-1 else (px+1,0) if py==m-1 else (px,py+1)

        if not visited[px][py]:
            for shape in shapes:
                boomerang = [(sx+px,sy+py) for (sx,sy) in shape]
                (ax,ay),(bx,by),(cx,cy) = boomerang
                if 0<=ax<n and 0<=ay<m and 0<=bx<n and 0<=by<m and 0<=cx<n and 0<=cy<m \
                and not visited[ax][ay] and not visited[bx][by] and not visited[cx][cy]:
                    for (x,y) in boomerang: visited[x][y] = True
                    strength_bundle += [dfs(nxt, strength + wood[ax][ay]*2+wood[bx][by]+wood[cx][cy])]
                    for (x,y) in boomerang: visited[x][y] = False

        strength_bundle += [dfs(nxt, strength)]
    else:
        strength_bundle = [strength]
    return max(strength_bundle)


print(dfs((0,0),0))