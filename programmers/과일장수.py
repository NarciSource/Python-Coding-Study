def solution(k, m, score):
    
    l = len(score)
    score.sort(reverse=True)
    
    sum = 0
    for i in range(m-1, l, m):
        sum += score[i]*m
        
    return sum