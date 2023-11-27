import sys, math
n,k = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())
patties = [tuple(map(int,sys.stdin.readline().split())) for _ in range(m)]
q = int(sys.stdin.readline())

dp = [[0]+[math.inf]*n for _ in range(k+1)]
for bugger in range(1,k+1):
    for patty in range(1,n+1):
        dp[bugger][patty] = min(dp[bugger-1][max(patty-p,0)] + c for p,c in patties)

print(min(dp[k][patty] + q*(n-patty) for patty in range(1,n+1)))