import sys
n=5
matrix=[list(sys.stdin.readline()) for _ in range(n)]

block = []
for i in range(n):
    for j in range(n):
        if matrix[i][j]=='#':
            block.append((i,j))

if len(block) == 4:
    (ay,ax),(by,bx),(cy,cx),(dy,dx) = block
    if (ax==bx==cx==dx and ay+3==by+2==cy+1==dy) or\
        (ay==by==cy==dy and ax+3==bx+2==cx+1==dx) or\
        (ax+1==bx==cx+1==dx and ay+1==by+1==cy==dy) or\
        (ax+2==dx+2==bx+1==cx and ay+1==dy==by+1==cy+1) or\
        (ax+1==bx+1==cx+1==dx and ay+2==by+1==cy==dy) or\
        (ax==dx==bx+2==cx+1 and ay+1==by==cy==dy) or\
        (ax+1==bx==cx==dx and ay+2==by+2==cy+1==dy) or\
        (ax+2==bx+1==cx+1==dx and ay+1==by+1==cy==dy) or\
        (ax==cx==bx+1==dx+1 and ay+2==by+1==cy+1==dy) or\
        (ax+1==bx==dx==cx-1 and ay==by==cy==dy-1) or\
        (ax==cx==dx==bx+1 and ay+1==by==cy==dy-1) or\
        (ax==cx==bx+1==dx-1 and ay+1==by==cy==dy) or\
        (ax==bx==cx-1==dx and ay+1==by==cy==dy-1):
        print("YES")
    else: print("NO")
else: print("NO")