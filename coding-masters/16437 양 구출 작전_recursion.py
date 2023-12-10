import sys                                                                              # 최대 노드 개수만큼 재귀를 들어가야 할 수 있기 때문에
sys.setrecursionlimit(10**6) #123456                                                    # 재귀 허용 횟수를 늘려줘야합니다.
n = int(sys.stdin.readline())
sheeps, wolves, parents = zip(*[(lambda t,a,p:(int(a) if t=='S' else 0,                 # 각자 성격이 다른 입력은 변수를 구분해 주는 것이 좋습니다.
                                               int(a) if t=='W' else 0,
                                               int(p))
                                )(*sys.stdin.readline().split()) for _ in range(n-1)])
sheeps, wolves, parents = [0,0]+list(sheeps), [0,0]+list(wolves), [0,0]+list(parents)   # [0,0]은 바운드입니다.
                                                                                        # 인덱스가 1부터이므로 0 하나,
                                                                                        # 2번째 줄부터 시작이므로 0 하나 더
from collections import defaultdict
childrens = defaultdict(list)                                                           # 트리를 자료구조로 만드는 것입니다.
for child, parent in enumerate(parents):                                                # 각 노드의 자식노드를 리스트로 저장합니다.
    childrens[parent].append(child)                                                     # 인접 리스트 형태입니다.

def recursion(node):                                                                    # dfs 재귀를 이용해 푸는 방식
    sheeps[node] += sum(recursion(child) for child in childrens[node])                  # 각 노드에서 자식 노드의 살아남은 양을 가진 양에 더합니다.
    return max(sheeps[node]-wolves[node], 0)                                            # 현재 노드에서 늑대한테 잡아먹힌 양을 빼고 살아남은 양을 위로 보냅니다.
                                                                                        # max(,0)은 늑대>양일 경우, 배고픈 늑대가 올라가지 못하게 차단하는 것입니다.
print(recursion(1))