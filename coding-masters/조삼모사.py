import sys
n = int(input())
wants = sorted(map(int,sys.stdin.readline().split()))
maximum = int(input())
allocated = 0
for i, want in enumerate(wants):
    if want*(n-i) <= maximum - allocated:
        allocated += want
        ration = want
    else:
        ration = (maximum-allocated)//(n-i)
        break
print(ration)