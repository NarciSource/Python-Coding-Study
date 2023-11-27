import sys, collections
N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
def is_enabled():
    squares = collections.defaultdict(list)
    for i in range(N):
        for j in range(i+1,N):
            for oi, oj in squares[A[i]*A[j]]:
                if i!=oi and i!=oj and j!=oi and j!=oj:
                    return True
            else:
                squares[A[i]*A[j]].append((i,j))
    return False
print("YES" if is_enabled() else "NO")