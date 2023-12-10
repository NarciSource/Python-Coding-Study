import sys
from collections import defaultdict
N = int(sys.stdin.readline())
nested_defaultdict = lambda: defaultdict(nested_defaultdict)    # defaultdict은 값이 있는지 확인하는 조건을 자료구조 안에 감춥니다.
tree = nested_defaultdict()                                     # defaultdict을 무한히 겹칩니다.

for _ in range(N):
    _, *feeds = sys.stdin.readline().split()
    subtree = tree
    for feed in feeds:
        subtree = subtree[feed]                                 # 계층적으로 넣습니다.

def dfs(subtree, level):
    for key, val in sorted(subtree.items()):                    # 사전순으로 꺼냅니다.
        print("--"*level+key)
        dfs(val, level+1)
dfs(tree,0)