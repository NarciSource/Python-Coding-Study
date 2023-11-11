from math import factorial
def index_of(word):
    n = len(word)
    order = 0
    for i in range(n-1):
        sep = sum(1 for j in range(i+1, n) if word[j] < word[i])
        order += sep * factorial(n-i-1)
    return order

def get(word, n):
    result = []
    for i in range(len(word) - 1, 0, -1):
        index, n = divmod(n, factorial(i))
        result.append(word.pop(index))
    result.append(word[0])
    return result

import sys
N,K = map(int, sys.stdin.readline().split())
permutation = list(map(int, sys.stdin.readline().split()))
order = (index_of(permutation) + K) % factorial(N)
print(*get(sorted(permutation), order))