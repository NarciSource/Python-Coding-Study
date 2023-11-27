import sys
n,m = map(int,sys.stdin.readline().split())
board = [list(sys.stdin.readline()) for _ in range(n)]
start, end = (0,0), (n-1,m-1)

is_valid = lambda p: 0<=p[0]<n and 0<=p[1]<m
plus = lambda *args: tuple(map(sum,zip(*args)))
get = lambda p: board[p[0]][p[1]] if is_valid(p) else '#'

ds = [(-1,0), (0,-1), (1,0), (0,1)]
visited = set([start])
q = [(start,0)]
for p, count in q:
    if p!=end:
        for d in ds:
            moved, moved2 = plus(p,d), plus(p,d,d)

            if get(moved)=='.' and get(moved2)=='.':
                if moved2 not in visited:
                    q.append((moved2, count+1))
                    visited.add(moved2)
            elif get(moved)=='.':
                if moved not in visited:
                    q.append((moved, count+1))
                    visited.add(moved)
    else:
        print(count)
        break
else: print(-1)