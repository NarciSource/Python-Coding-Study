def solution(n, words):

    s = set()
    is_dup = lambda word: word in s or s.add(word)

    last_char = words[0][0]
    for idx, word in enumerate(words):
        if last_char == word[0] and not is_dup(word):
            last_char = word[-1]
        else:
            return [idx%n + 1, idx//n + 1]
    else:
        return [0, 0]