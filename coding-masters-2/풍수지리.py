import sys
N, M = map(int, sys.stdin.readline().split())
matrix = [sys.stdin.readline() for _ in range(N)]
blessings = []

from itertools import product
for (y1, x1, y2, x2) in product(range(N), range(M), repeat=2):
    if y2 >= y1 and x2 >= x1:
        uniques = set(matrix[a][b] for a in range(y1, y2+1) for b in range(x1, x2+1))
        if len(uniques) == 1:
            blessings.append((y2-y1+1)*(x2-x1+1))
print(max(blessings))