import sys, math
n,k = map(int,sys.stdin.readline().split())
schedule = [0]+list(map(int,sys.stdin.readline().split()))
actors_last = [math.inf]+[None]*k
period = math.inf
for day in range(1,n+1):
    actors_last[schedule[day]] = day
    if all(actors_last):
        period = min(day-min(actors_last)+1, period)
print(period)