n=int(input())
tiles=[1,2]+[None]*(n-2)
for i in range(2,n):
    tiles[i]=tiles[i-1]+tiles[i-2]
print(tiles[n-1])