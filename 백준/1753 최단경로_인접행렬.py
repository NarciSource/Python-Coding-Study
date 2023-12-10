import sys
V,E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
from math import inf
board = [[inf]*(V+1) for _ in range(V+1)]   # 인접 행렬은 정점으로 표현하는 자료구조입니다.
                                            # 정점X정점으로 이차원배열을 구성합니다.
                                            # 공간복잡도 O(V^2)와 시간복잡도가 큽니다. 다만 구현이 쉽습니다.
for _ in range(E):
    u,v,w = map(int, sys.stdin.readline().split())
    board[u][v]=w

#dijkstra
distance = [0]+board[K][1:]
distance[K] = 0
visited = set([K])                              # 아 요방식은 check 안 쓰고는 안되네요
for _ in range(1,V+1):                          # O(V)
    via, w_via = min(filter(lambda x: x[0] not in visited, enumerate(distance)), key=lambda x:x[1]) # O(V)
    visited.add(via)

    for dest, w_dest in enumerate(board[via]):  # O(V)
        if distance[dest] > distance[via] + w_dest:
            distance[dest] = distance[via] + w_dest

print(*map(lambda d: "INF" if d==inf else d, distance[1:]), sep="\n")

# O(V)*(O(V) + O(V)) = O(V^2)