import sys
v,e = map(int,sys.stdin.readline().split())
edge = [list(map(int,sys.stdin.readline().split())) for _ in range(e)]

from collections import defaultdict 
table, room = defaultdict(list), defaultdict(int)
for (x, y) in edge:
    table[x].append(y)
    table[y].append(x)

def canAssignedRooms():
    other = lambda x: 2 if x==1 else 1
    stack = []

    while True:
        if stack:
            prisoner = stack.pop()
        else:
            prisoner = next(filter(lambda p: room[p]==0, range(1,v+1)), None)

            if prisoner:
                room[prisoner] = 1
            else:
                return True

        friends = table[prisoner]

        if any(map(lambda friend: room[friend]==room[prisoner], friends)):
            return False
        else:
            stack += list(filter(lambda p: room[p]==0, friends))
            
            for friend in friends:
                room[friend] = other(room[prisoner])
print(1 if canAssignedRooms() else 0)