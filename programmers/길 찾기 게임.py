def solution(nodeinfo):
    indexed_nodeinfo = [[*node, idx] for idx, node in enumerate(nodeinfo)]
    sorted_nodeinfo = sorted(indexed_nodeinfo, key=lambda n: (-n[1], n[0]))

    from collections import defaultdict
    tree = defaultdict(list)
    for [x, y, idx] in sorted_nodeinfo:
        tree[y].append({'x': x, 'idx': idx + 1})
    tree = list(tree.values()) + [[]]


    from sys import setrecursionlimit
    setrecursionlimit(1000+3)
    def dfs(height, bound):
        nonlocal preorder, inorder, postorder

        if tree[height]:
            node = tree[height][0]
        
            if node['x'] < bound:
                tree[height] = tree[height][1:]

                preorder += [node['idx']]
                dfs(height + 1, node['x'])
                inorder += [node['idx']]
                dfs(height + 1, bound)
                postorder += [node['idx']]

    preorder, inorder, postorder = [], [], []
    from math import inf
    dfs(0, inf)
    return [preorder, postorder]

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))