import sys
n = int(sys.stdin.readline())
arr = [(sys.stdin.readline().split()) for _ in range(n)]
for (name,_) in sorted(arr, key=lambda x: int(x[1]), reverse=True)[:3]:
    print(name)