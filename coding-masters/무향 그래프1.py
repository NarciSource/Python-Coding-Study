import sys
n,m = map(int,sys.stdin.readline().split())
matrix = [[0]*n for _ in range(n)]
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    matrix[a-1][b-1]=matrix[b-1][a-1]=1
for column in matrix:
    print(*column)