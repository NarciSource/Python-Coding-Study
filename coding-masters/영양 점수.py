import sys
n = int(sys.stdin.readline())
scores = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

from itertools import *
comb = list(combinations([*range(n)],n//2))

import math
result = math.inf
for i in range(len(comb)//2):
    def sumScores(group):
        score_sum = 0
        for a in group:
            for b in group:
                score_sum += scores[a][b]
        return score_sum

    dish1 = comb[i]
    dish2 = comb[-1-i]
    
    diff = abs(sumScores(dish1) - sumScores(dish2))
    result = diff if result > diff else result
    if result ==0: break
print(result)
