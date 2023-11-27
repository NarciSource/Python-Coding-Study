import sys
n,m = map(int,sys.stdin.readline().split())
k = sys.stdin.readline()
records = list(map(int,sys.stdin.readline().split()))

groups = [*((0, m*i+1) for i in range(n)), *(range(i*m+1,(i+1)*m+1) for i in range(n))]
for a,b in zip(records[:-1], records[1:]):
    if not any(a in group and b in group for group in groups):
        print("NO")
        break
else: print("YES")