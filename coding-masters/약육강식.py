import sys
n = int(sys.stdin.readline())
eatten = [0]*(n+1)
for shark in map(int,sys.stdin.readline().split()):
    eatten[shark] = max(eatten[:shark]) + 1
print(max(eatten))