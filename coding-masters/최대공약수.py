import math
print(math.gcd(*map(int,input().split())))


import sys
n,m = sorted(map(int,sys.stdin.readline().split()))
while m%n!=0: n,m = m%n,n
print(n)