import sys
n,m = map(int,sys.stdin.readline().split())
start,end = 1,2
edges = [set() for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    edges[a].add(b)
    edges[b].add(a)

rounds = 0
visited = set([])
while True:
    marked = set([start])
    queue = [(start, [])]
    for node,path in queue:
        if node not in visited:
            if node != end:
                neighbors = [neighbor for neighbor in edges[node] if neighbor not in marked and neighbor not in visited]
                queue += [(neighbor, path+[neighbor]) for neighbor in neighbors]
                marked.update(neighbors)
            else:
                rounds +=1
                visited.update(path[:-1])
                break
    else: break
print(rounds)