import sys
k,n = map(int,sys.stdin.readline().split())
mx = n if n>k else k
from collections import deque
q = deque([k])
times = [0]*(mx+2)
cases = [k]
while q and n not in cases:
    p = q.popleft()
    cases = [p-1,p+3,p*2]

    for c in cases:
        if 0<=c<=mx+1 and not times[c]:
            times[c] = times[p]+1
            q.append(c)
print(times[n])