import sys
board=['01010101','10101010','01010101','10101010','01010101','10101010','01010101','10101010']
mole=[sys.stdin.readline() for _ in range(8)]
print(sum([1 for j in range(8) for i in range(8) if board[i][j]=='0' and mole[i][j]=='F']))