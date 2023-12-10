import sys

n = int(sys.stdin.readline())
sheeps, wolves, parents = zip(*[(lambda t,a,p:(int(a) if t=='S' else 0,
                                               int(a) if t=='W' else 0,
                                               int(p))
                                )(*sys.stdin.readline().split()) for _ in range(n-1)])
sheeps, wolves, parents = [0,0]+list(sheeps), [0,0]+list(wolves), [0,0]+list(parents)

from collections import defaultdict
childrens = defaultdict(list)
for child, parent in enumerate(parents):
    childrens[parent].append(child)

def solution(start):
    stack = [start]
    for node in stack:                          # 리스트 뒤에 계속 추가해도 iterater 형태에서는 선입선출이 계속 진행됩니다.
        stack.extend(childrens[node])           # 그러므로 스택과 큐를 한 번에 쓸 수 있는 것이죠.

    for node in reversed(stack):
        sheeps[parents[node]] += max(sheeps[node]-wolves[node], 0)
    return sheeps[start]
print(solution(1))