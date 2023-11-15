import sys,math,decimal
n,a,b=map(int,sys.stdin.readline().split())
print(n+ math.ceil(decimal.Decimal(str((n*b+n-1)))/(a-1)))