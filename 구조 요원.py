import sys
n = int(sys.stdin.readline())
x,y = map(int,sys.stdin.readline().split())

from math import sqrt, inf
min_time,min_time_pos = inf, None
for m in range(*((0,x+1) if 0<=x else (0,x-1,-1))):
    time=sqrt(m**2+n**2)+2*sqrt((m-x)**2+y**2)
    if time<min_time:
        min_time,min_time_pos = time, m
print(min_time_pos)