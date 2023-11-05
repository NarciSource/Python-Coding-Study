def solution(a, b, n):
    bottle = 0
    while n//a>0:
        bottle += n//a*b
        n = n//a*b + n%a
    return bottle

print(solution(2,1,20))
print(solution(3,1,20))