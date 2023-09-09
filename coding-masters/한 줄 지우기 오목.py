def isFiveWin(y,x, board):
    isWhite = lambda my,mx: 0<=x+mx<n and 0<=y+my<n and board[y+my][x+mx]=='W'
    _=0
    if all(map(lambda i: isWhite(_,-i), range(5))) or\
        all(map(lambda i: isWhite(_,1-i), range(5))) or\
        all(map(lambda i: isWhite(_,2-i), range(5))) or\
        all(map(lambda i: isWhite(_,3-i), range(5))) or\
        all(map(lambda i: isWhite(_,4-i), range(5))):
        return True
    if all(map(lambda i: isWhite(-i,_), range(5))) or\
        all(map(lambda i: isWhite(1-i,_), range(5))) or\
        all(map(lambda i: isWhite(2-i,_), range(5))) or\
        all(map(lambda i: isWhite(3-i,_), range(5))) or\
        all(map(lambda i: isWhite(4-i,_), range(5))):
        return True
    if all(map(lambda i: isWhite(-i,-i), range(5))) or\
        all(map(lambda i: isWhite(1-i,1-i), range(5))) or\
        all(map(lambda i: isWhite(2-i,2-i), range(5))) or\
        all(map(lambda i: isWhite(3-i,3-i), range(5))) or\
        all(map(lambda i: isWhite(4-i,4-i), range(5))):
        return True
    if all(map(lambda i: isWhite(-i,i), range(5))) or\
        all(map(lambda i: isWhite(1-i,i-1), range(5))) or\
        all(map(lambda i: isWhite(2-i,i-2), range(5))) or\
        all(map(lambda i: isWhite(3-i,i-3), range(5))) or\
        all(map(lambda i: isWhite(4-i,i-4), range(5))):
        return True

def putWhite(run, board):
    for x in range(n):
        for y in range(n):
            if board[x][y]=='.':
                backup, board[x][y] = board[x][y], 'W'
                run(x,y, board)
                board[x][y] = backup
wins = 0
def run(x,y, board):
    global wins
    wins+= 1 if isFiveWin(x,y, board) else 0

import sys
n = 10
board = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
for i in range(n):
    board_copy = [row[:] for row in board]
    for j in range(n): board_copy[i][j] = '.'
    putWhite(run, board_copy)

    board_copy = [row[:] for row in board]
    for j in range(n): board_copy[j][i] = '.'
    putWhite(run, board_copy)
print(wins)