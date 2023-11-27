import math,sys
trees = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
p = max(trees)+2
days = [0]+[math.inf]*p

history = set((1,1))
q = [((1,1), 0)]
for (a,b), day in q:
    days[b] = min(day, days[b])

    next_heights = [a+b, b-1, (a+b)//2]

    for c in filter(lambda c: 1<=c<p and (b,c) not in history, next_heights):
        q.append(((b,c), day+1))
        history.add((b,c))
print(*map(lambda tree: days[tree], trees),sep='\n')