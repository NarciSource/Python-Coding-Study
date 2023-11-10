def solution(food):
    order = ''.join(str(i)*(f//2) for i, f in enumerate(food))
    return order+'0'+order[::-1]



print(solution([1, 3, 4, 6]))
print(solution([1, 7, 1, 2]))