import sys
N,M = map(int,sys.stdin.readline().split())
robot1 = list(map(int,sys.stdin.readline().split()))
robot2 = list(map(int,sys.stdin.readline().split()))

from math import gcd
from itertools import repeat, chain
chain1 = chain(*repeat(robot1, M//gcd(N,M)))
chain2 = chain(*repeat(robot2, N//gcd(N,M)))
pairs = list(zip(chain1, chain2))

rpc = lambda h1,h2: h1<h2 if abs(h1-h2)==2 else h1>h2
winner = None
for h1,h2 in pairs:
    if rpc(h1,h2):
        winner = 1
    elif rpc(h2,h1):
        winner = 2
    elif winner:
        print(winner)
        break
else: print(0)