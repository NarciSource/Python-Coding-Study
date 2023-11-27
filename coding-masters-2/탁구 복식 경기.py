from itertools import combinations
input()
skills = map(int,input().split())
print(min((lambda a,b,c,d:abs(a*d-b*c))(*sorted(comb)) for comb in combinations(skills,4)))