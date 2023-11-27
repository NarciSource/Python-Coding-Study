import sys
n = int(sys.stdin.readline())
profit = list(map(int, sys.stdin.readline().split()))
for i in range(1,n):
    profit[i] += max(profit[i-1], 0)
print(max(profit))