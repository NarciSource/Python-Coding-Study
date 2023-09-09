import sys
a,b = map(int,sys.stdin.readline().split())
cur,nxt = 0,1
i = ffibsum = 0
while i<b:
    cur, nxt = nxt, cur + nxt
    for _ in range(cur):
        i += 1            
        if a<=i<=b:
            ffibsum += cur
print(ffibsum)