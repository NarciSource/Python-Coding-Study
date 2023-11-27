import sys
from collections import defaultdict
n,m,k = map(int,sys.stdin.readline().split())
weights = [{'weight': int(sys.stdin.readline()), 'activate': True} for _ in range(n)]
edges = defaultdict(list)
for _ in range(m):
    s,e=map(int,sys.stdin.readline().split())
    edges[s-1].append(e-1)
    edges[e-1].append(s-1)

cost = 0
for _ in range(n):
    top = max(weights, key=lambda w: w['weight'] if w['activate'] else 0)
    node = weights.index(top)
    tolearnce = top['weight'] - k

    for neighbor in edges[node]:
        if weights[neighbor]['activate'] and weights[neighbor]['weight'] < tolearnce:
            cost += tolearnce - weights[neighbor]['weight']

            weights[neighbor]['weight'] = tolearnce

    weights[node]['activate'] = False
print(cost)