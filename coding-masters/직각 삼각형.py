import sys
a,b,c = sorted(map(int,sys.stdin.readline().split()))
print("YES" if a*a+b*b==c*c else "NO")