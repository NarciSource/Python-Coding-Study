import sys
n=int(sys.stdin.readline())
for i in range(1,n+1):
    coins = list(map(int,sys.stdin.readline().split()))
    for j in range(i):
        up = collected_coins[j] if j<i-1 else 0
        upleft = collected_coins[j-1] if j-1>=0 else 0
        coins[j] = coins[j] + (up if up>upleft else upleft)
    collected_coins = coins
print(max(collected_coins))