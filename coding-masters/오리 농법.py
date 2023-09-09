import sys
n = int(sys.stdin.readline())
field = [list(sys.stdin.readline().split()) for _ in range(n)]

from collections import defaultdict
isCropsRow, isCropsCol = defaultdict(bool), defaultdict(bool)
number_of_weed=0
weeds = []
for i in range(n):
    for j in range(n):
        if field[i][j]=='2':
            weeds.append((i,j))
            number_of_weed += 1
        elif field[i][j]=='1':
            isCropsRow[i] = True
            isCropsCol[j] = True

max_eaten = 0
def eatWeeds(duck, eaten):
    if duck < number_of_weed:
        x,y = weeds[duck]
        if field[x][y]=='2':
            if not isCropsRow[x]:
                weeds_of_col = [c for c in range(n) if field[x][c]=='2']

                for c in weeds_of_col: field[x][c]='0'
                eatWeeds(duck+1, eaten+len(weeds_of_col))
                for c in weeds_of_col: field[x][c]='2'

            if not isCropsCol[y]:
                weeds_of_row = [r for r in range(n) if field[r][y]=='2']

                for r in weeds_of_row: field[r][y]='0'
                eatWeeds(duck+1, eaten+len(weeds_of_row))
                for r in weeds_of_row: field[r][y]='2'
            
            eatWeeds(duck+1, eaten)
    else:
        global max_eaten
        max_eaten = eaten if eaten > max_eaten else max_eaten
eatWeeds(0,0)
print(number_of_weed-max_eaten)