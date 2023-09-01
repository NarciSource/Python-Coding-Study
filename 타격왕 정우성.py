import sys
x,y=map(int,sys.stdin.readline().split())
s,e=0,1000000000
time=-1
while s<=e:
    t=(s+e)//2
    isUp = (100*(y+t))//(x+t) - (100*y)//x
    if isUp >= 1:
        e=t-1
        time=t
    else:
        s=t+1
print(time)