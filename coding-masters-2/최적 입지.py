import sys, math
n = int(sys.stdin.readline())
viliage = [sys.stdin.readline() for _ in range(n)]
houses = [(row,col) for row, cols in enumerate(viliage) for col, val in enumerate(cols) if val=='H']

cul_rows = [sum(abs(i-x) for y,x in houses) for i in range(n)]
cul_cols = [sum(abs(i-y) for y,x in houses) for i in range(n)]

min_distance = math.inf
for y in range(n):
    for x in range(n):
        distance = cul_rows[x] + cul_cols[y]
        if distance < min_distance:
            min_distance = distance
            min_y,min_x = y,x
print(min_y+1,min_x+1)