import sys
#n,m = map(int,sys.stdin.readline().split())
#wood = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
n,m = 3, 3
wood = [[32, 83, 75], [24, 96, 56], [71, 88, 12]]
shapes = [(-1,0),(0,0),(-1,-1)], [(0,0),(0,-1),(-1,0)], [(0,-1),(0,0),(-1,-1)], [(-1,-1),(0,-1),(-1,0)]
visited = [[False]*m for _ in range(n)]

isInner = lambda p:(lambda x,y: 0 <= x < n and 0 <= y < m)(*p)
isVisited = lambda p:(lambda x,y: visited[x][y])(*p)
getValue = lambda p:(lambda x,y: wood[x][y])(*p)
calc = lambda ps: sum(map(getValue, ps)) + getValue(ps[0])
next = lambda p:(lambda x,y: None if y==m-1 and x==n-1 else (x+1,0) if y==m-1 else (x,y+1))(*p)

def setVisited(ps, b):
    for (x,y) in ps:
        visited[x][y] = b

def dfs(point, strength):
    if point:
        strength_bundle = []
        nxt = next(point)

        if not isVisited(point):
            boomerangs = map(lambda shape: list(map(lambda s,p: tuple(map(sum,zip(s,p))), shape,[point]*3)), shapes)
            valid_boomerangs = filter(lambda boomerang: all(map(isInner, boomerang)), boomerangs)
            enabled_boomerangs = filter(lambda boomerang: not any(map(isVisited, boomerang)), valid_boomerangs)

            for boomerang in list(enabled_boomerangs):
                setVisited(boomerang, True)
                strength_bundle += [dfs(nxt, strength + calc(boomerang))]
                setVisited(boomerang, False)

        strength_bundle += [dfs(nxt, strength)]
    else:
        strength_bundle = [strength]

    return max(strength_bundle)


print(dfs((0,0),0))