import sys, itertools, collections
times = collections.Counter(map(sum, itertools.product(range(1,7), repeat=3)))
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split())) + [-100]*(len(times)+3)

expected = list(sum(nums[t+k-1]*time for t, time in times.items())
                for k in range(1, n+1))
max_expected = max(expected)
print(max_expected)
print(*[i+1 for i, v in enumerate(expected) if v==max_expected])