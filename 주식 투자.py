n,k=map(int,input().split())
move=[-100,100]
from itertools import product
print(list(map(sum,product(move,repeat=n))).count(k))