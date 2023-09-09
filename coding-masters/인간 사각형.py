import sys
n,m = map(int,sys.stdin.readline().split())
room = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

from collections import defaultdict 
cards_per_numbers = defaultdict(list)
for i in range(n):
    for j in range(m):
        cards_per_numbers[room[i][j]].append((i,j))

from itertools import combinations
print(max([(x2-x1+1)*(y2-y1+1)
        for (idx, cards) in cards_per_numbers.items() if len(cards)>=4
            for (x1,y1), (x2,y2) in combinations(cards,2) if x2-x1==y2-y1 and room[x1][y2]==room[x2][y1]==idx]))





#isSquare = lambda a,b,c,d: a[0]==b[0] and c[0]==d[0] and a[1]==c[1] and b[1]==d[1]
#size = lambda a,b,c,d: (c[0]-a[0]+1)*(b[1]-a[1]+1)

#from itertools import combinations
#print(max([size(*four_card) for cards in cards_per_numbers.values() if len(cards)>=4 for four_card in combinations(cards, 4) if isSquare(*four_card)]))



"""
from itertools import combinations
answer = []
for (idx, cards) in cards_per_numbers.items():
    if len(cards)>=4:
        for (x1,y1), (x2,y2) in combinations(cards, 2):
            if x2-x1 == y2-y1 and room[x1][y2] == room[x2][y1] == idx:
                answer.append((x2-x1+1)*(y2-y1+1))

"""