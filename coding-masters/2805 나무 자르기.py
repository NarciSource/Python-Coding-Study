import sys, collections, math
n,m = map(int,sys.stdin.readline().split())
heights = collections.Counter(map(int,sys.stdin.readline().split()))
heights = sorted(heights.items(), reverse=True)+[(0,1)]

setting = heights[0][0]
wood = 0
trees = 0
for height, num in heights:
    remain = m - wood
    remain_each = math.ceil(remain/trees) if trees else remain
    gap = setting - height

    cutted = min(remain_each, gap)
    wood += cutted*trees
    setting -= cutted

    if wood < m:
        trees += num
    else:
        print(setting)
        break

# O(log(n)) + O(n) = O(n)