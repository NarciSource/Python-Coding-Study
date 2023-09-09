import sys
p,q = sys.stdin.readline().split()
n = int(sys.stdin.readline())
from decimal import *
getcontext().prec = n
getcontext().rounding=ROUND_HALF_UP
print(f"{Decimal(p)/Decimal(q):.{n}f}")