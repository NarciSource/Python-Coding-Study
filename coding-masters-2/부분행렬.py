import sys
n,m,x = map(int,sys.stdin.readline().split())
matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

def is_exist_sub(x):
    from itertools import product
    for (y1, x1, y2, x2) in product(range(n), range(m), repeat=2):
        if y2 >= y1 and x2 >= x1:
            sumofsub = sum(matrix[a][b] for a in range(y1, y2+1) for b in range(x1, x2+1))
            if sumofsub == x:
                return True
    else: return False
print("YES" if is_exist_sub(x) else "NO")