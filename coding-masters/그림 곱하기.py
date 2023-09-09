import sys
n,m = map(int,sys.stdin.readline().split())
paint = [list(sys.stdin.readline()) for _ in range(n)]

def getDivisor(n):
    divisors=[]
    for i in range(1, int(n**0.5+1)):
        if n%i==0:
            yield n//i
            if i*i!=n:
                divisors.append(i)
    for d in reversed(divisors):
        yield d

from math import gcd
for diviosr in getDivisor(gcd(n,m)):
    x,y = n//diviosr, m//diviosr

    for i in range(diviosr):
        for j in range(diviosr):
            if any(map(lambda ix: any(map(lambda iy: paint[ix][iy]!=paint[x*i+ix][y*j+iy], range(y))), range(x))):
                break
        else: continue
        break
    else:
        for i in range(x):
            print(''.join(paint[i][:y]))
        break