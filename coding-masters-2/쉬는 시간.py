n = int(input())
a, b = 0, 1
for i in range(2,n):
    a, b = b, i*(a+b)%998244353
print(a if n==1 else b)