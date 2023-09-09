import sys
n = int(input())
data = [list(map(int,sys.stdin.readline().split())) for _ in range(1,n+1)]
print(min([(sum(abs(di-dj)*aj for (dj, aj) in data),i+1) for i, (di,ai) in enumerate(data)])[1])