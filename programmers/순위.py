def preproc(n, data):
    some_betters = [[i] for i in range(n+1)]
    some_lowers = [[i] for i in range(n+1)]

    for (to, dest) in data:
        some_betters[to].append(dest)
        some_lowers[dest].append(to)

    return some_betters, some_lowers

def dijkstra(start, data):
    full = via = start

    while via:
        acq = set().union(*[data[b] for b in via])
        via = acq.difference(full)
        full += via

    return full

def solution(n, results):
    answer = 0
    some_betters, some_lowers = preproc(n, results)

    for better, lower in zip(some_betters, some_lowers):

        full_betters = dijkstra(better, some_betters)
        full_lowers = dijkstra(lower, some_lowers)
        known = set().union(full_betters, full_lowers)
        
        answer += 1 if len(known) == n else 0

    return answer



print(solution(7,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5],[7,4],[6,7]]))