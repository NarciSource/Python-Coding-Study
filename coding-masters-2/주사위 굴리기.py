import sys
w,h= map(int,sys.stdin.readline().split())
x,y= map(int,sys.stdin.readline().split())
dice = list(map(int,sys.stdin.readline().split()))
n = int(sys.stdin.readline())
directions = list(map(int,sys.stdin.readline().split()))
east,south,west,north=1,2,3,4

def change(idxs):
    global dice
    dice = [dice[idx] for idx in idxs]

matrix = [[0]*w for _ in range(h)]
matrix[y][x]=dice[5]
for direction in directions:
    if direction==east:
        change([4,1,5,3,2,0])
        x+=1
    elif direction==south:
        change([0,4,2,5,3,1])
        y+=1
    elif direction==west:
        change([5,1,4,3,0,2])
        x-=1
    elif direction==north:
        change([0,5,2,4,1,3])
        y-=1
        
    x=min(max(0,x),w-1)
    y=min(max(0,y),h-1)
    matrix[y][x]=dice[5]

for col in matrix:
    print(*col)