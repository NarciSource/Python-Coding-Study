def solution(number, limit, power):
    divisors = [0]+[0]*number
    for i in range(1, number+1):
        for j in range(i, number+1, i):
            divisors[j] += 1
    return sum([power if d>limit else d for d in divisors])


print(solution(5,3,2))
print(solution(10,3,2))