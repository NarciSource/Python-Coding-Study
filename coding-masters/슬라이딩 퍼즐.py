import sys
puzzle = sys.stdin.readline().rstrip()
puzzle+= sys.stdin.readline().rstrip()

state = {puzzle:0}
from collections import deque
q = deque([puzzle])
while q:
    puzzle = q.popleft()

    if puzzle != '123X':
        x = puzzle.find('X')

        for m in [[1,2],[-1,2],[-2,1],[-1,-2]][x]:
            nxtPuzzle = puzzle.replace('X','_').replace(puzzle[x+m],'X').replace('_',puzzle[x+m])
            if nxtPuzzle not in state:
                state[nxtPuzzle] = state[puzzle]+1
                q.append(nxtPuzzle)
    else:
        print(state[puzzle])
        break
else:
    print(-1)