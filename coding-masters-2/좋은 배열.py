import sys
N = int(sys.stdin.readline())
minmax = [[] for _ in range(N+1)]
for idx,a in enumerate(map(int,sys.stdin.readline().split())):
    minmax[a].append(idx)
    
print(minmax)
def is_good_array(minmax):
    for idx,(a,b) in enumerate(minmax):
        for c,d in minmax[idx+1:]:
            if c<b<d:
                return "NO"
    return "YES"
print(is_good_array(sorted(minmax[1:])))