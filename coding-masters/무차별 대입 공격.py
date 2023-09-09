import sys
n,k = map(int,sys.stdin.readline().split())
alphabet = sorted(list(sys.stdin.readline().rstrip()))
from itertools import product
for password in product(*([alphabet]*k)):
    print(''.join(password))