import sys
from collections import defaultdict
V,E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
edges = defaultdict(list)       # 인접 리스트는 간선으로 표현하는 자료구조입니다.
                                # 정점에서 이어지는 간선으로 리스트묶음을 구성합니다.
                                # 인접 리스트가 공간복잡도 O(E)와 시간복잡도가 작습니다.
for _ in range(E):
    u,v,w = map(int, sys.stdin.readline().split())
    edges[u].append((w, v))

#dijkstra
from math import inf
distance = [0]+[inf]*V
distance[K] = 0
q = [(distance[K],K)]           # 일반 리스트
#heap = [(distance[K],K)]
while q:                        # O(E)
#while heap:
    w_via, via = min(q)         # min은 매번 O(E)
    #w_via, via = heappop(heap) # heappop은 매번 O(logE)
                                # heappop 이란건 최소값을 뽑아줍니다.
                                # 다만 반복시 저렴한 비용이 듭니다. min 반복이 필요할 때 쓰면 됩니다.
    q.remove((w_via, via))      # O(E) ,체크로 피할 수도 있습니다. 시간복잡도에는 영향X
    if w_via <= distance[via]:
        for w_dest, dest in edges[via]:
            if distance[dest] > w_via + w_dest:
                distance[dest] = w_via + w_dest
                q.append((w_via + w_dest, dest))        # 뒤에 삽입 O(1)
                #heappush(heap, (w_via + w_dest, dest)) # heap트리에 삽입 O(logE)

print(*map(lambda d: "INF" if d==inf else d, distance[1:]), sep="\n")


# min사용 O(E)*(O(E) + O(E) + O(1)) = O(E^2) ~ O(EV)
# heapq사용 O(E)*(O(logE) + O(logE)) = O(ElogE) ~ O(ElogV)