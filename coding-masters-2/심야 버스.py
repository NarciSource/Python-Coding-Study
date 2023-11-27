import sys
N = int(sys.stdin.readline())
matrix = [sys.stdin.readline().split() for _ in range(N)]
for j in range(N):
    for i in range(N):
        for k in range(N):
            matrix[i][k] = '1' if matrix[i][k]=='1' or matrix[i][j]==matrix[j][k]=='1' else '0'
print(*[' '.join(line) for line in matrix], sep='\n')