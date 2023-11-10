def solution(info, edges):
    from collections import defaultdict
    tree = defaultdict(list)    
    for parent, child in edges:
        tree[parent].append(child)

    visited = [False]*len(info)    
    max_sheep = 0
    def backtracking(horizon, sheep, wolf):
        if sheep > wolf:
            nonlocal max_sheep
            max_sheep = sheep if sheep > max_sheep else max_sheep

            for node in horizon:
                for child in tree[node]:
                    if not visited[child]:
                        visited[child] = True
                        backtracking(horizon+[child], sheep + 1-info[child], wolf + info[child])
                        visited[child] = False
    root = 0
    visited[root] = True
    backtracking([root], sheep=1, wolf=0)

    return max_sheep


print(solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
print(solution([0,1,0,1,1,0,1,0,0,1,0],[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))