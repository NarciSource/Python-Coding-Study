import sys
n,m = map(int,sys.stdin.readline().split())
matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
acc = [[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        acc[i][j] = matrix[i-1][j-1] + acc[i-1][j] + acc[i][j-1] - acc[i-1][j-1]
count=0
for i in range(1,n+1):
    for j in range(1,m+1):
        for mi in range(i,n+1):
            area = acc[mi][j]-acc[mi][j-1]-acc[i-1][j]+acc[i-1][j-1]
            if area <= 10:
                for mj in range(j,m+1):
                    area = acc[mi][mj]-acc[mi][j-1]-acc[i-1][mj]+acc[i-1][j-1]
                    if area == 10:
                        count+= 1
                    if area >= 10:
                        break
            else:
                break
print(count)