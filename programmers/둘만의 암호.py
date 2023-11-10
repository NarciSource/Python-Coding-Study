def solution(s, skip, index):
    filtered = sorted(set("abcdefghijklmnopqrstuvwxyz").difference(skip))
    return ''.join(map(lambda c: filtered[(filtered.index(c)+index)%len(filtered)], s))




print(solution("aukks","wbqd",5))
print(solution("a","cb",1))