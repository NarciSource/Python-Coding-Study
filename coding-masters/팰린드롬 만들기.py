import sys
n=int(sys.stdin.readline())
words=[sys.stdin.readline().split() for _ in range(n)]
from itertools import permutations, chain
for word in map(lambda p: ''.join(list(chain(*p))),permutations(words,n)):
    if all(map(lambda i: word[i]==word[-i-1], range(len(word)//2))):
        print("YES")
        break
else: print("NO")