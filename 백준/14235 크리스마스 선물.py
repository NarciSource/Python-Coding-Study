import sys
from heapq import heappush, heappop
n = int(sys.stdin.readline())
gifts = []
for _ in range(n):
    a, *values = map(int, sys.stdin.readline().split()) # unpacking 시 마지막 변수에 *을 붙이면 나머지를 리스트로 저장합니다.
    if not a == 0:
        for value in values:
            heappush(gifts, -value)                     # 최대힙의 선물에 넣어줍니다.
    else:
        print(-heappop(gifts) if len(gifts) else -1)    # 힙에서 최댓값을 꺼내줍니다. sp