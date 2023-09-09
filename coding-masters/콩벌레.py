import sys
matrix = [list(sys.stdin.readline().rstrip()) for _ in range(10)]
x,y = (lambda: [(i,j) for i in range(10) for j in range(10) if matrix[i][j]=='2'])()[0]
matrix[x][y]='0'
move=[(-1,0),(0,-1)]
sw=0
mx,my=move[sw]
while True:
    nx,ny=x+mx,y+my    
    if 0<=nx<10 and 0<=ny<10:
        if matrix[nx][ny]=='0':
            x,y=nx,ny
        elif matrix[nx][ny] == '1':
            matrix[nx][ny] = '4'
            sw^=1
            mx,my=move[sw]
        elif matrix[nx][ny] == '4':
            print("no")
            break
    else:
        print("yes")
        break