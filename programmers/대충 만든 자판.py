def solution(keymap, targets):
    from collections import defaultdict
    from math import inf
    short_key_times = defaultdict(lambda: inf)
    for keys in keymap:
        for i, key in reversed(list(enumerate(keys))):
            short_key_times[key] = i+1 if short_key_times[key]>i+1 else short_key_times[key]

    return [(lambda shortest: -1 if shortest==inf else shortest)
            (sum(short_key_times[t] for t in list(target))) for target in targets]

print(solution(["ABACD", "BCEFD"],["ABCD","AABB"]))
print(solution(["AA"],["B"]))