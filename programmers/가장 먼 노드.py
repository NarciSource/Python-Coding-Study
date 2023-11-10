def preproc(n, edge):
    d = [[] for _ in range(n+1)]
    for a, b in edge:
        d[a].append(b)
        d[b].append(a)
    return d

def dijkstra(n, d):
    dist = [math.inf]*(n+1)
    dist[1] = 0

    import queue
    q = queue.Queue()
    q.put(1)

    while not q.empty():
        i = q.get()
        for j in d[i]:
            if dist[j] > dist[i] + 1:
                dist[j] = dist[i] + 1
                q.put(j)
    return dist

import math
def solution(n, edge):
    d = preproc(n, edge)
    dist = dijkstra(n, d)

    answer = dist.count(max(filter(lambda d: not math.isinf(d), dist)))
    
    return answer