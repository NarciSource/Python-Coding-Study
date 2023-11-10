def solution(n, computers):
    def findRoot(v):
        while group[v] != v:
            v = group[v]
        return v

    group = [i for i in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if computers[i][j] == 1:
                group[findRoot(j)] = findRoot(i)

    return len(set(map(findRoot, group)))

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))