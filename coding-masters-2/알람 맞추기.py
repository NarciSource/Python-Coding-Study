import sys
hh, mm = map(int,sys.stdin.readline().split(':'))
N = int(sys.stdin.readline())-1
mm += N*(N+1)//2
hh += mm//60
print(f'{hh%24:02d}:{mm%60:02d}')