import sys
n = int(sys.stdin.readline())
print('A' if n >= 200 else 'B' if n >= 180 else 'C' if n >= 150 else 'D')