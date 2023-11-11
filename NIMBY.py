import sys
N,K= map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
print(A[max([(sum(map(lambda a: abs(a-pivot) if K>=abs(a-pivot) else -abs(a-pivot), A)), i) for i, pivot in enumerate(A)], key=lambda x:(x[0],-x[1]))[1]])