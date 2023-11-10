from itertools import *

def is_prime(num):
    if num < 2 or num%2 == 0:
        return False
    else:
        for i in range(3, int(num**0.5)+1, 2):
            if num%i == 0:
                return False
    return True

def solutions(nums):
    odd = list(filter(lambda v: v%2==1, nums))
    even = list(filter(lambda v: v%2==0, nums))

    count_prime = lambda numbers: len(list(filter(None, map(is_prime, numbers))))

    #case1: 3-odd
    o3 = combinations(odd, 3)
    o3_sums = sum(o3)
    o3_prime_counts = count_prime(o3_sums)

    #case2: 1-odd and 2-even
    e2 = combinations(even, 2)
    e2_sums = map(sum, e2)
    e2o1 = product(e2_sums, odd)
    e2o1_sums = map(sum, e2o1)
    e2o1_prime_counts = count_prime(e2o1_sums)

    return o3_prime_counts + e2o1_prime_counts



