from math import factorial
p,n=map(int,input().split())

trailing_zero = 0
fact = factorial(n)
while fact>=1:
    fact, remain = divmod(fact, p)
    if remain==0:
        trailing_zero+=1
    else:
        break
print(trailing_zero)




"""
trailing_zero = 0
divisor_set = set()
for divisor in range(1, int(p**0.5)+1):
    if p%divisor == 0:
        divisor_set |= {p//divisor}
print(divisor_set)
print(n//p*(len(divisor_set))+len(list(filter(lambda d: d<=n%p, divisor_set))))
"""