
def solution(k, score):
    from heapq import heappop, heappush
    q, lowers = [], []
    for s in score:
        heappush(q,s)
        if len(q)>k: heappop(q)
        lowers.append(q[0])
    return lowers

print(solution(3,[10, 100, 20, 150, 1, 100, 200]))
print(solution(4,[0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))
