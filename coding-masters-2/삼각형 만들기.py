import sys
N = int(sys.stdin.readline())
bars = sorted(map(int,sys.stdin.readline().split()))
max_count = 0
for i in range(N):
    for j in range(i+2, N):
        if bars[i] + bars[i+1] > bars[j]:
            max_count = max(j-i+1, max_count)
        else:
            break
print(max_count)