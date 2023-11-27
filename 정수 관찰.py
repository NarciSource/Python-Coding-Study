from itertools import combinations
from math import gcd
from functools import reduce

lcm = lambda numbers: reduce(lambda a,b: a*(b//gcd(a,b)), numbers)

def at_least(nums, alist):
    limit = 10**9
    total = 0

    for r in nums:
        for combination in combinations(alist, r):
            p = lcm(sorted(combination))
            count = (limit +1)//p
            total += count if r%2 else -count
    return total

import sys
n = int(sys.stdin.readline())
alist = list(map(int,sys.stdin.readline().split()))
print(at_least(range(1,n+1), alist))
# 1~2까지하면 테케 4, 6번 통과합니다.
# 테스트 프로그램이 틀린거죠


# 0: 2 [3 5] 466666667
# 1: 10 [2 4 6 8 10 12 14 16 18 20] 500000000
# 2: 14 [696 178 387 1001 1693 295 1794 1469 767 128 1811 973 1172 869] 27722294 <-
# 3: 2 [1001 1105] 1892226
# 4: 8 [197 718 1802 894 245 1136 487 1889] 15584368 <- 15584005
# 5: 1 [1001] 999001
# 6: 5 [20 1581 792 1728 1267] 52777346 <- 52765699