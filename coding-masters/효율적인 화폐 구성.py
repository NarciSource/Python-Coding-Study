import sys
n,m = map(int,sys.stdin.readline().split())
coins = sorted([int(sys.stdin.readline()) for _ in range(n)])
from math import inf
wallet = [0]+[inf]*m
for coin in coins:
    if coin <= m:
        wallet[coin] = 1
        for i in range(coin+1,m+1):
            wallet[i] = min(wallet[i-coin]+1, wallet[i])
    else: break
print(wallet[m] if wallet[m]!=inf else -1)