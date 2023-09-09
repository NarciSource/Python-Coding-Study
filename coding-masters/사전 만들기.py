import sys
n=int(input())
for word in sorted(set([sys.stdin.readline().rstrip() for _ in range(n)]), key=lambda word:(len(word),word)):
    print(word)