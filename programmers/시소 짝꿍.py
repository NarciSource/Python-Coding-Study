def solution(weights):    
    from collections import Counter
    from itertools import product

    cw = Counter(weights)
    return  sum(count*(count-1)//2 for count in cw.values())+\
            sum(count*cw[weight*ratio] for (weight, count), ratio in product(cw.items(), [1/2, 2/3, 3/4]) if weight*ratio in cw)

print(solution([100,180,360,100,270]))