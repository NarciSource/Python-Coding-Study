import sys
n,k = map(int,sys.stdin.readline().split())
scores = list(map(int,sys.stdin.readline().split()))
count_max = 0
final_cultine = None

for i in range(n):
    cutline = scores[i]
    passed = [False]*n
    for j in range(n):
        if scores[j] >= cutline:
            passed[j] = True
            if j-1>=0: passed[j-1] = True
            if j+1<n: passed[j+1] = True

    count = passed.count(True)
    if count_max< count <=k:
        count_max = count
        final_cultine = cutline
    elif count_max == count:
        final_cultine = cutline if final_cultine<cutline else final_cultine
print(final_cultine if final_cultine else min(scores)-1)