import sys
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

from collections import defaultdict
relationships = defaultdict(int)
for i in range(k):
    a,b,c = map(int,sys.stdin.readline().split())
    relationships[(b,c) if b<c else (c,b)] = 1 if a==1 else -1

def placeInSeat(students, pairs):
    if students:
        for idx in range(1,len(students)):
            student = students.pop(idx)
            placeInSeat(students[1:], pairs+[(students[0], student)])
            students.insert(idx, student)
    else:
        global max_atmosphere
        atmosphere = sum([relationships[pair] for pair in pairs])
        max_atmosphere = atmosphere if atmosphere > max_atmosphere else max_atmosphere
max_atmosphere=-n
placeInSeat(list(range(1,n*2+1)), [])
print(max_atmosphere)





"""
from collections import defaultdict

relationships = defaultdict(int)
for i in range(k):
    a,b,c = map(int,sys.stdin.readline().split())

    relationships[(b-1,c-1)] = 1 if a==1 else -1

print(relationships)
comb = list(combinations(range(n*2),2))
print(comb)
combs = [comb[i:i+n] for i in range(0,len(comb),n)]
print(combs)
for batch in combs:
    print("-"*5)
    print(batch)
    for b in batch:
        print(relationships[b])
    print(sum(map(relationships.get, batch)))"""