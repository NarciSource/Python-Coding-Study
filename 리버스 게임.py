import sys
from collections import defaultdict
from itertools import chain
n = int(sys.stdin.readline())
matrix = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

columns, rows = [0]*n, [0]*n
for x in range(n):
    for y in range(n):
        if matrix[x][y]=='W':
            columns[x] += 1
            rows[y] += 1

def flip(x,y):
    if matrix[x][y]=='W':
        matrix[x][y]='B'
        rows[y]-=1
        columns[x]-=1
    else:
        matrix[x][y]='W'
        rows[y]+=1
        columns[x]+=1

check = defaultdict(bool)
min_white = n*n
def reverse():
    key = ''.join(chain(*matrix))

    if not check[key]:
        check[key]=True

        global min_white
        min_white = key.count('W') if key.count('W') < min_white else min_white

        for x in range(n):
            for y in range(n):
                if matrix[x][y]=='W':
                    if columns[x] >= n/2:
                        for c in range(n): flip(x,c)
                        reverse()
                        for c in range(n): flip(x,c)

                    if rows[y] >= n/2:
                        for r in range(n): flip(r,y)
                        reverse()
                        for r in range(n): flip(r,y)
reverse()
print(min_white)