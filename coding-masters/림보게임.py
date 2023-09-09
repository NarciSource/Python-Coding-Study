import sys
n = int(sys.stdin.readline())
for h in map(int,sys.stdin.readline().split()):
    if h <= 160:
        print('I',h)
        break
else: print('P')