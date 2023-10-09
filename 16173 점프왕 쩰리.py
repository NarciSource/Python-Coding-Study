import sys
n = int(sys.stdin.readline())
board = {(y,x): v for y in range(n) for x, v in enumerate(map(int, sys.stdin.readline().split()))}
is_inbound = lambda y,x: y<n and x<n

start = (0,0)
moved = [start]
for cur in moved:
    jump = board[cur]

    if jump != -1:
        down = tuple(map(sum, zip(cur, (jump, 0))))
        right = tuple(map(sum, zip(cur, (0, jump))))

        if is_inbound(*down) and down not in moved:
            moved.append(down)
        if is_inbound(*right) and right not in moved:
            moved.append(right)
    else:
        print("HaruHaru")
        break
else:
    print("Hing")