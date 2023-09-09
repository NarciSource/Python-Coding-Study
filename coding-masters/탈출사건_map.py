import sys
from itertools import *
from copy import deepcopy
n, m = map(int,sys.stdin.readline().split())
zoo = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
tigers = list(filter(lambda p: (lambda x,y: zoo[x][y]==2)(*p), product(range(n), range(m))))
fields = list(filter(lambda p: (lambda x,y: zoo[x][y]==0)(*p), product(range(n), range(m))))

def relaseTiger(zoo):
    zoo = deepcopy(zoo)
    stack = tigers[:]
    acc = []
    while stack:
        cor = stack.pop()
        dir = [(-1,0),(1,0),(0,-1),(0,1)]

        moved_cors = map(lambda c,d: tuple(map(sum,zip(c,d))), [cor]*4, dir)
        bounded_cors = filter(lambda p: (lambda x,y: 0<=x<n and 0<=y<m)(*p), moved_cors)
        valid_cors = filter(lambda p: (lambda x,y: zoo[x][y] == 0)(*p), bounded_cors)
        result_cors = list(valid_cors)

        for (x,y) in result_cors:
            zoo[x][y] = 4
        acc += result_cors
        stack += result_cors
    return acc
    
tiger_moved_len = []
for three in combinations(relaseTiger(zoo), 3):
    for (x,y) in three: zoo[x][y] = 1

    tiger_moved_len.append(len(relaseTiger(zoo)))

    for (x,y) in three: zoo[x][y] = 0

print(len(fields) - min(tiger_moved_len) -3)