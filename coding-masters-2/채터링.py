import sys
N,K = map(int, sys.stdin.readline().split())
print(''.join([c*K for c in sys.stdin.readline().strip()]))