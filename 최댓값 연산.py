import sys
x,y,z=sorted(map(int,sys.stdin.readline().split()))
print("possible" if y==z else "impossible")