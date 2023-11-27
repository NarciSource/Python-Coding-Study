n,m=map(int,input().split())
while (n>=2*m or m>=2*n) and not(m==0 or n==0):
    n %= 2*m
    m %= 2*n
print(n,m)