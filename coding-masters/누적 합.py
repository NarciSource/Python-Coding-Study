import sys
n=int(input())
m=n-1
while m&(m-1): m=m&(m-1) 
m=1 if m==0 else m<<1

arr = list(map(int,sys.stdin.readline().split()))+[0]*(m-n)
tree = []
while m:
    m=m>>1
    tree.append(arr)
    arr = [arr[2*i]+arr[2*i+1] for i in range(m)]
for t in reversed(tree):
    print(*t)