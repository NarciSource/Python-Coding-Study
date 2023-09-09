n=int(input())
chk=[0,0]+[1]*(n-1)
primes=[]
from math import sqrt
for i in range(2,int(sqrt(n))+1):
    if chk[i]:
        primes.append(i)
        for j in range(i*2, n+1, i):
            chk[j]=0
print(sum(chk))