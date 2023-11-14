import sys, math
n, k = map(int,sys.stdin.readline().split())
start = -math.inf
count = 0
for sinkholl in sorted(map(int,sys.stdin.readline().split())):
    if sinkholl-start >= k:
        start=sinkholl
        count+=1
print(count)