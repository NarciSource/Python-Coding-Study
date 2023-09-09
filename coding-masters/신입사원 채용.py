import sys
n = int(sys.stdin.readline())
scores = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
roots = [ai for ai in range(n)]
def findRoot(v):
    while roots[v] != v:
        v = roots[v]
    return v
for ai, applicant in enumerate(scores):
    for oj, other in enumerate(scores):
        if (not ai == oj and
                other[0]==applicant[0] and other[1]==applicant[1] or
                not ((other[0]<=applicant[0] and other[1]<=applicant[1]) or
                     (other[0]>=applicant[0] and other[1]>=applicant[1]))):
            roots[findRoot(oj)] = findRoot(ai)
ranking = [1]*n
for ai, applicant in enumerate(scores):
    for oj, other in enumerate(scores):
        if (not ai == oj and
                not findRoot(ai) == findRoot(oj) and
                other[0]>=applicant[0] and other[1]>=applicant[1]):
            ranking[ai] += 1
print(*ranking)