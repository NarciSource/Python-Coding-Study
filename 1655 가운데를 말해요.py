import sys
N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]

from heapq import heappush, heappop                 # 양편으로 최소힙과 최대힙 둡니다
from math import inf                                # 짝,홀을 맞추기 위해 한쪽에 bound(inf)를 넣습니다.
smaller, bigger = [], [inf]                         # smaller는 중앙에서 작은 값들이며 최대힙으로 구성됩니다.
                                                    # bigger는 중앙에서 큰 값들이며 최소힙으로 구성됩니다.
for num in nums:
                                                    # 양편의 개수를 맞추려고 적은 쪽 힙으로 일단 넣어줍니다.
    if len(smaller) < len(bigger):                  # 잘못된 힙에 넣었다면 아래에서 잡아줄 수 있습니다. 
        heappush(smaller, -num)                     # 파이썬의 heapq는 디폴트가 최소힙입니다.
    else:                                           # 음수로 바꿔 넣으면 의미상 최소힙을 최대힙처럼 사용할 수 있습니다.
        heappush(bigger, num)
                                                    # heap 구조에서 0번째 인덱스는 가장 작은 값입니다.
                                                    # 다만, 다른 인덱스의 값들은 순서가 없고 오로지 0번째만 의미가 있습니다.
    biggest_of_smaller = -smaller[0]                # 음수로 바꿔서 구성된 최대힙이므로 꺼낼 때 다시 원복해줍니다.
    smallest_of_bigger = bigger[0]                  # smaller 중에서 가장 큰 값, bigger 중에서 가장 작은 값을 찾아줍니다.

    if biggest_of_smaller > smallest_of_bigger:     # 올바르다면 smaller 중에서 가장 큰 값도 bigger 중에서 가장 작은 값보다는 작아야합니다.
        heappop(smaller)                            # 올바르지 않다면 잘못된 힙에 넣어준 것이므로 양 끝값을 swap합니다.
        heappush(smaller, -smallest_of_bigger)
        heappop(bigger)
        heappush(bigger, biggest_of_smaller)

    print(-smaller[0])                              # bigger에는 inf 하나가 들어가 있으므로 두 힙의 중간값은 smaller에 있습니다.