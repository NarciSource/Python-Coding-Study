from itertools import combinations
solution = lambda number: len(list(filter(lambda x: not x, map(sum, combinations(number, 3)))))

print(solution([-2, 3, 0, 2, -5]))
print(solution([-3, -2, -1, 0, 1, 2, 3]))
print(solution([-1, 1, -1, 1]))