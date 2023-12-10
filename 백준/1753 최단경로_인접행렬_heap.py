import sys
from math import inf
V,E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
board = [[0]+[inf]*V for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int, sys.stdin.readline().split())
    board[u][v]=w

#dijkstra
from heapq import heappush, heappop
from math import inf
distance = [0]+[inf]*V
distance[K] = 0
heap = [(distance[K],K)]
while heap:                                             # O(E)
    w_via, via = heappop(heap)                          # O(logE)
    if w_via <= distance[via]:
        for dest, w_dest in enumerate(board[via]):                       # O(V)
            if distance[dest] > distance[via] + w_dest:
                distance[dest] = distance[via] + w_dest
                heappush(heap, (w_via + w_dest, dest))  # O(logE)

print(*map(lambda d: "INF" if d==inf else d, distance[1:]), sep="\n")



# O(E)*(O(logE) + O(V)*O(logE)) = O(EVlogE) ~ O(V^2logE)
# 이런 시간복잡도가 나오니 아무도 이렇게 안 짜지...
# 이건 어거지로 인접행렬과 힙을 엇붙인겁니다.
# 간선을 찾기 위해 V번 검색하는 것에 간선탐색 E가 곱해지니 최악의 알고리즘이 탄생했습니다.
# 간선(E) > 정점(V) 입니다. 그러니 힙구조를 사용하는 것은 