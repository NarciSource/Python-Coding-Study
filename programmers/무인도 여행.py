def find_root_in(group):
    def find_root(v):
        while group[v] != v:
            v = group[v]
        return v
    return find_root

def solution(maps):
    maps = list(map(list, maps))
    n,m = len(maps), len(maps[0])

    from itertools import product
    group = {p: p for p in product(range(n), range(m))}
    find_root = find_root_in(group)

    for r,c in product(range(n), range(m)):
        if maps[r][c] != 'X':
            if 0<=r-1 and maps[r-1][c] != 'X':
                group[find_root((r-1,c))] = (r,c)
            if 0<=c-1 and maps[r][c-1] != 'X':
                group[find_root((r,c-1))] = (r,c)

    from collections import defaultdict
    foods = defaultdict(int)
    for r,c in group:
        if maps[r][c] != 'X':
            foods[find_root((r,c))] += int(maps[r][c])

    return sorted(foods.values()) if len(foods) else [-1]


print(solution(["X591X","X1X5X","X231X", "1XXX1"]))
print(solution(["XXX","XXX","XXX"]))