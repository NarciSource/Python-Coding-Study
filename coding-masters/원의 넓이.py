import sys
r=int(sys.stdin.readline())
print(int(r*r*3.14) if r%10==0 else r*r*3.14)