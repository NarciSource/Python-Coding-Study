N = int(input())

index = 0
while N%5==0:
    N //= 5
    index +=1
N *= 2**(index*2)

index2 = 0
while N%3==0:
    N //= 3
    index2 += 1
N *= 2**index2

from math import log2
index3 = log2(N)
print(int(index+index2+index3) if index3%1==0 else -1)