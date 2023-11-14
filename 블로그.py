import sys
n,k= map(int,sys.stdin.readline().split())
visited = list(map(int,sys.stdin.readline().split()))
print(max([(sum(visited[i:i+k]),i+1) for i in range(n-k+1)])[1])