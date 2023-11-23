import sys
n,k = map(int, sys.stdin.readline().split())
houses = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
distance = lambda p1,p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
start = (1,1)
from itertools import permutations
print(min(sum(distance(a,b) for a,b in zip([(start)]+list(locations), list(locations)+[start]))
          for locations in permutations(houses, k)))