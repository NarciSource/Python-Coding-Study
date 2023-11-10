def solution(name, yearning, photo):
    values = {n:y for n,y in zip(name, yearning)}
    return [sum(values[name] for name in p if name in values) for p in photo]

print(solution(["may", "kein", "kain", "radi"],[5, 10, 1, 3],[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))
print(solution(["kali", "mari", "don"],[11, 1, 55],[["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]))
print(solution(["may", "kein", "kain", "radi"],[5, 10, 1, 3],[["may"],["kein", "deny", "may"], ["kon", "coni"]]))