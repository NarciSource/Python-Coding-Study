import sys
n = int(sys.stdin.readline())
members = [sys.stdin.readline().split() for _ in range(n)]
print(*map(' '.join,sorted(members, key=lambda x:int(x[0]))), sep='\n')