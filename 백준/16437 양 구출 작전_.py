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

def solution(start):                            # 재귀를 쓰지 말고 풀이하자는 방식입니다.
    from collections import deque               # 재귀는 오버헤드가 큰 문제가 있기 때문입니다.
    queue = deque([start])
    stack = [start]
    while queue:                                # 스택(선입후출)과 큐(선입선출)의 작동 방식 차이를 이용하여
        node = queue.popleft()                  # DFS에서의 노드 접근 인덱스 순서를 추출하는 형태입니다.
        queue.extend(childrens[node])           # 큐는 dfs를 쫒아가는 형태입니다.
        stack.extend(childrens[node])           # 스택은 그 결과를 저장합니다.
                                                # 이 변환 형태는 중위 표기 -> 후위 표기에서 나오니 그 쪽으로 찾아보실 수 있습니다.
    for node in reversed(stack):
        sheeps[parents[node]] += max(sheeps[node]-wolves[node], 0)
    return sheeps[start]
print(solution(1))