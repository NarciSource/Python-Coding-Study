def solution(n, m, section):
    count = ranged = 0
    for s in section:
        if s >= ranged:
            ranged = s+m
            count += 1
    return count

print(solution(8,4,[2, 3, 6]))
print(solution(5,4,[1, 3]))
print(solution(4,1,[1, 2, 3, 4]))