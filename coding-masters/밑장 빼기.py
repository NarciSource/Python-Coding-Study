import sys
n=int(sys.stdin.readline())
cards=list(map(int,sys.stdin.readline().split()))
j,k=0,n-1
for i in range(1,n+1):
    if cards[j] == i: j+=1
    elif cards[k] == i: k-=1
    else:
        print("NO")
        break
else:
    print("YES")
