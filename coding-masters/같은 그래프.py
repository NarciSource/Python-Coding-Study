import sys
n1,m1 = map(int,sys.stdin.readline().split())
edges1 = [list(map(int,sys.stdin.readline().split())) for _ in range(m1)]
n2,m2 = map(int,sys.stdin.readline().split())
edges2 = [list(map(int,sys.stdin.readline().split())) for _ in range(m1)]

if n1==n2:
    matrix1 = [[0]*n1 for _ in range(n1)]
    for u,v in edges1: matrix1[u-1][v-1]=matrix1[v-1][u-1]=1
    matrix2 = [[0]*n2 for _ in range(n2)]
    for u,v in edges2: matrix2[u-1][v-1]=matrix2[v-1][u-1]=1

    from itertools import permutations, combinations
    basic = tuple(range(n1))
    for nodes in permutations(basic):
        for edge1, edge2 in zip(combinations(basic,2), combinations(nodes,2)):
            if matrix1[edge1[0]][edge1[1]] != matrix2[edge2[0]][edge2[1]]:
                break
        else:
            print("YES")
            break
    else: print("NO")
else: print("NO")