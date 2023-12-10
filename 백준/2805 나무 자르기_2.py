import sys, collections
n,m = map(int,sys.stdin.readline().split())
heights = collections.Counter(map(int,sys.stdin.readline().split()))
low,high = 0,max(heights)

while low<=high:            # 이분 탐색
    mid = (low+high)//2

    if sum(max(height-mid, 0)*num for height, num in heights.items()) >= m:
        low = mid+1
    else:
        high = mid-1
print(high)

# O(log2(1,000,000,000)) * O(n) = O(29*n)