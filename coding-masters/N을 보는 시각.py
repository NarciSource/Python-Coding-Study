n=int(input())
h= 12 if n==1 else 6 if n==2 else 3 if n==3 else 2
s=m= 15 if n<6 else 6
print(h*60*60 + 24*m*60 + 24*60*s - h*m*60 - h*60*s - 24*m*s + h*m*s)