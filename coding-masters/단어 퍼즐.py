import sys, itertools
words = sorted([sys.stdin.readline().rstrip() for _ in range(6)])
for rows in itertools.permutations(words, 3):
    columns = tuple(map(''.join,zip(*rows)))
    if sorted(rows+columns) == words:
        print(*rows, sep='\n')
        break