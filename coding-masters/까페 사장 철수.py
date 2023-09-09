import sys
n,m = map(int,sys.stdin.readline().split())
toSecond = lambda hh,mm,ss: hh*3600+mm*60+ss
times = sorted([list(map(lambda s: toSecond(*map(int,s.split(':'))), sys.stdin.readline().split())) for _ in range(m)])
import heapq
heap = [0]
count = 0
for entry, exit in times:
    last = heap[0] if len(heap) > 0 else 0

    if len(heap)<n:
        heapq.heappush(heap, exit)
        count+=1
    elif entry >= last:
        heapq.heappop(heap)
        heapq.heappush(heap, exit)
        count+=1
    else: pass
print(count)