def solution(begin, target, words):
    checked = {key: False for key in words}
    from collections import deque
    queue = deque([(begin, 0)])
    while queue:
        trans, count = queue.popleft()
        if trans != target:
            for word in words:
                if not checked[word]:
                    if sum([w1!=w2 for w1, w2 in zip(word, trans)])==1:
                        queue.append((word, count+1))
                        checked[word]=True
        else: return count
    else: return 0

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit","cog",["hot", "dot", "dog", "lot", "log"]))