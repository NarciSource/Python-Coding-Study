import sys
n = int(sys.stdin.readline())
matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dr = [(-1,0),(0,-1),(1,0),(0,1)]
is_valid = lambda y,x: 0<=y<n and 0<=x<n

from math import inf
walks = [[inf]*n for _ in range(n)]
cheated_walks = [[inf]*n for _ in range(n)]

q = [(0,0)]
walks[0][0]=1
for y,x in q:
    for dy,dx in dr:
        my,mx=y+dy,x+dx

        if is_valid(my,mx):
            if matrix[my][mx]<=matrix[y][x]:
                if walks[my][mx] > walks[y][x]+1:
                    walks[my][mx] = walks[y][x]+1
                    q.append((my,mx))

                if cheated_walks[y][x]+1 < cheated_walks[my][mx]: 
                    cheated_walks[my][mx] = min(cheated_walks[y][x]+1, cheated_walks[my][mx])
                    q.append((my,mx))
            else:
                if walks[y][x]+1 < cheated_walks[my][mx]: 
                    cheated_walks[my][mx] = min(walks[y][x]+1, cheated_walks[my][mx])
                    q.append((my,mx))

last = [walks[n-1][n-1], cheated_walks[n-1][n-1]]
print(-1 if min(last)==inf else min(last))