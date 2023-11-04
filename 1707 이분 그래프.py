import sys
from collections import defaultdict
K = int(sys.stdin.readline())
for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())    
    edges = defaultdict(list)
    for _ in range(E):
        u, v = map(int, sys.stdin.readline().split())
        edges[u].append(v)
        edges[v].append(u)

    other_color = lambda c: 'black' if c=='red' else 'red'
    def is_bipartite():
        colors = [None]+[None]*V

        for pivot in range(V):
            if not colors[pivot]:
                q = [pivot]
                colors[pivot] = 'red'

                for node in q:
                    for neighbor in edges[node]:
                        if not colors[neighbor]:
                            colors[neighbor] = other_color(colors[node])
                            q.append(neighbor)

                        if colors[neighbor] == colors[node]:
                            return False
        else: return True

    print("YES" if is_bipartite() else "NO")