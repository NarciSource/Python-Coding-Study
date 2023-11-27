import sys
N,M = map(int, sys.stdin.readline().split())
cups = [i for i in range(N+1)]
for _ in range(M):
    A,B = map(int, sys.stdin.readline().split())
    cups[A],cups[B] = cups[B],cups[A]
K = int(sys.stdin.readline())
print(cups.index(K))