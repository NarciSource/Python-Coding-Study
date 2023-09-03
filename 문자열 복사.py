import sys
s1 = list(sys.stdin.readline().strip())
s2 = list(sys.stdin.readline().strip())

def compressed(s):
    pivot = s[0]
    count = 0
    for w in s:
        if w==pivot:
            count+=1
        else:
            yield (pivot, count)
            pivot=w
            count=1
    else: yield (pivot, count)

from math import log2, ceil
copies = [log2(m/n) for (w1, n), (w2, m) in zip(compressed(s1), compressed(s2))]
if len(copies)==3 and copies[1]<copies[0] and copies[1]<copies[2]:
    print(ceil(copies[0])+ceil(copies[2])-int(copies[1]))
else:
    print(max(map(ceil,copies)))


"""
def findHills(horizon):
    for i in range(len(horizon)):
        if (horizon[i-1] if i-1>=0 else 0)<horizon[i] and horizon[i]>=(horizon[i+1] if i+1<len(horizon) else 0):
            yield horizon[i]
print(sum(findHills(copies)))"""