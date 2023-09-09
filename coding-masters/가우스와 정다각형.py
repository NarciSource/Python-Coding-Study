k=int(input())
for p in [3,5,17,257,65537]:
    if k%p==0: k//=p
print("YES" if k&(k-1)==0 else "NO")