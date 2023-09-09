import sys
dessert=sys.stdin.readline().rstrip()
n=len(dessert)
i,j=0,n-1
diff_i,diff_j=0,0
parfait=0
while i<=j:
    if dessert[i]=='F' and diff_i<=diff_j:
        parfait+=diff_i
        diff_i=0
        i+=1
        continue    
    if dessert[j]=='F' and diff_j<=diff_i:
        parfait+=diff_j
        diff_j=0
        j-=1
        continue

    if not dessert[i]=='F':
        diff_i+=1
        i+=1
    if not dessert[j]=='F':
        diff_j+=1
        j-=1
print(parfait)