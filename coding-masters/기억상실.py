import sys
a, b, n = map(int,sys.stdin.readline().split())
print((n-b)//(a-b)+(1 if (n-b)%(a-b)!=0 else 0))