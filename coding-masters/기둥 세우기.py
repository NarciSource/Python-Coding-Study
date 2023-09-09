import sys, math
n,m = map(int,sys.stdin.readline().split())
status = [list(sys.stdin.readline().split()) for _ in range(n)]

from collections import defaultdict
isPillarsRow, isPillarsCol = defaultdict(bool), defaultdict(bool)
opening = []
for x in range(n):
    for y in range(m):
        if status[x][y]=='0':
            isPillarsRow[x],isPillarsCol[y] = True,True
        elif status[x][y]=='1':
            opening.append((x,y))

min_pillars=math.inf
def buildPalace(idx, pillars, built):
    if built < n+m:
        if idx < len(opening):
            x,y=opening[idx]
            isPR,isPC = isPillarsRow[x],isPillarsCol[y]

            if not isPR or not isPC:
                isPillarsRow[x],isPillarsCol[y] = True,True
                buildPalace(idx+1, pillars+1, built+(isPR^1)+(isPC^1))
                isPillarsRow[x],isPillarsCol[y] = isPR,isPC

            buildPalace(idx+1, pillars, built)
    else:
        global min_pillars
        min_pillars = pillars if pillars < min_pillars else min_pillars

buildPalace(0,0,len(isPillarsCol)+len(isPillarsRow))
print(min_pillars)