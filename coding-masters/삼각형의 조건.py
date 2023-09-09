import sys
a, b, c = map(int,sys.stdin.readline().split())
print('P' if a+b+c==180 and min(a,b,c)>0 else 'F')