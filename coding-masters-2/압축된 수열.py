import sys
N,M = map(int, sys.stdin.readline().split())
Ls = list(map(int, sys.stdin.readline().split()))

from math import log
for radix in range(10,63):
    if sum(map(lambda l: int(log(l, radix))+1, Ls)) + N - 1 <= M:
        print(radix)
        break
else: print(-1)