import sys
n = int(input())
movies = [tuple(map(int,sys.stdin.readline().split())) for _ in range(n)]

isLow = lambda p1,p2: p1[0]<p2[0] and p1[1]<p2[1] and p1[2]<p2[2]
tree = {i: [j for j in range(n) if isLow(movies[i],movies[j])] for i in range(n)}
tree = filter(lambda el: el[1], tree.items())
tree = {k: v for k, v in sorted(tree, key=lambda item: len(item[1]))}

drop_enable = [2]*n
under_nodes = [1]*n
for node, parents in tree.items():
    for parent in parents:
        if under_nodes[node] > 0:
            dropped = min(drop_enable[parent], under_nodes[node])
            drop_enable[parent] -= dropped
            under_nodes[node] -= dropped
        else: break
    else:
        under_nodes[parent] += under_nodes[node]
        under_nodes[node] = 0
print(sum(under_nodes))