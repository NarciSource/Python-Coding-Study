def solution(s):

    counts = 0
    for bracket in s:
        counts += 1 if bracket == "(" else -1
        if counts < 0:
            break
    return counts == 0
    
print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))
