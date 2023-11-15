import sys, math
n,k=map(int,sys.stdin.readline().split())
print(2*k-1 if k<=math.ceil(n/2) else 2*(k-math.ceil(n/2)))