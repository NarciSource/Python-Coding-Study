n,k=input().split()
d=int(k)-int(n)
up=d//3 if d%3==0 else d//3+1
down=up*3-d
print(up+down)