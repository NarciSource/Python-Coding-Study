import sys
k,n = map(int,sys.stdin.readline().split())
lancables = [int(sys.stdin.readline()) for _ in range(k)]

low,high = 1,max(lancables)
while low<=high:
    mid = (low+high)//2

    maked = sum(lancable//mid for lancable in lancables)
    if maked < n:
        high = mid-1
    else:
        low = mid+1
print(high)