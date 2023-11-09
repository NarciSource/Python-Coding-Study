import sys
a,b,c,d=map(int,sys.stdin.readline().split())
w,x,y,z=map(int,sys.stdin.readline().split())
print(a*w-b*x-c*y-d*z,
      a*x+b*w+c*z-d*y,
      a*y+c*w-b*z+d*x,
      a*z+d*w+b*y-c*x)