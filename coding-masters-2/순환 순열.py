from functools import reduce
mod = 1000000007
factorial = lambda n: reduce(lambda x,y: x*y%mod, range(1,n+1))
n = int(input())
print((factorial(n) - 2**(n-1))%mod)

"""
from itertools import permutations
n = int(input())
count=0
for permu in permutations(range(n),n):
    for i in range(1,n-1):
        if max(permu[:i]) > permu[i] and permu[i]< max(permu[i+1:]):
            count+=1
            break
print(len(list(permutations(range(n),n))))
print(count)
"""