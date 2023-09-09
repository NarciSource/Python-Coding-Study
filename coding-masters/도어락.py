import sys
sys.stdin.readline()
corner,side,center=4,4,1
for time in map(int,sys.stdin.readline().split()):
    if time==1: pass
    elif time==2: corner,side,center = 2*side+4*center, 2*corner+2*side+4*center, corner+side
    elif time==3: corner,side,center = 3*corner+2*side, 2*corner+side, 0
print((corner+side+center)%1000000007)