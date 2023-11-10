def solution(x, y, n):
    from collections import deque
    times = [0]*(y+1)
    queue = deque([x])
    cases = [x]
    while queue and y not in cases:
        p = queue.popleft()
        cases = [p+n, p*2, p*3]
        for c in cases:
            if c <= y and not times[c]:
                times[c] = times[p] + 1
                queue.append(c)
    return times[y] if times[y] or x==y else -1

print(solution(10,40,5))
print(solution(10,40,30))
print(solution(2,5,4))
print(solution(2,2,4))