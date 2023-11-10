def isValid(round, a,b,g,s,w,t):
    numbers = [(round / ti + 1)//2 for ti in t]

    capacities = [ni * wi for (ni, wi) in zip(numbers, w)]

    golds = [min(ci, gi) for (gi, ci) in zip(g, capacities)]

    silvers = [min(ci, si) for (si, ci) in zip(s, capacities)]

    weights = [min(ci, gi + si) for (gi, si, ci) in zip(g, s, capacities)]

    return a <= sum(golds) and b <= sum(silvers) and a + b <= sum(weights)

def solution(a,b,g,s,w,t):
    start, end = 0, 4*10**14

    while start <= end:
        mid = (start + end)//2

        if (isValid(mid, a,b,g,s,w,t)):
            end = mid - 1
        else:
            start = mid + 1
    return start

        

print(solution(10,10,[100],[100],[7],[10]))
print(solution(90,500,[70,70,0],[0,0,500],[100,100,2],[4,8,1]))