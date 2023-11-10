def dijkstra(n, start, data):
    graph = [[] for _ in range(n+1)]
    for (to, dest, cost) in data:
        graph[to].append((dest, cost))
        graph[dest].append((to, cost))

    import math
    dist = [math.inf]*(n+1)
    dist[start] = 0
    q = []

    import heapq
    heapq.heappush(q, (dist[start], start))

    while q:
        via_cost, via_idx = heapq.heappop(q)

        if via_cost <= dist[via_idx]:
            for (dest, known_cost) in graph[via_idx]:
                cost = via_cost + known_cost

                if dist[dest] > cost:
                    dist[dest] = cost
                    heapq.heappush(q, (cost, dest))
    return dist

def solution(n, s, a, b, fares):
    return min(map(sum, zip(*map(lambda x: dijkstra(n, x, fares), [s, a, b]))))

print(solution(6,4,6,2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7,3,4,1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6,4,5,6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))