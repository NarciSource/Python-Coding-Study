def solution(s):
    from collections import defaultdict
    last = defaultdict(lambda: -1)
    answer = []
    for i, c in enumerate(s):
        answer.append(-1 if last[c]==-1 else i - last[c])
        last[c] = i
    return answer

print(solution("banana"))
print(solution("foobar"))