import sys
sys.setrecursionlimit(10**6)

def isDivide(pivot, k, nums, links):
    def cut(node):
        left, right = links[node]
        current_num = nums[node]
        left_num, left_cutting = cut(left) if left!=-1 else (0,0)
        right_num, right_cutting = cut(right) if right!=-1 else (0,0)
        both_cutting = left_cutting + right_cutting

        return (current_num + left_num + right_num, both_cutting) if current_num + left_num + right_num <= pivot else\
                (current_num + min(left_num, right_num), both_cutting + 1) if current_num + min(left_num, right_num) <= pivot else\
                (current_num, both_cutting + 2)

    top = set(range(len(links))).difference([item for link in links for item in link]).pop()
    return (lambda _,cutting: cutting < k)(*cut(top))

def binarySearch(k, nums, links):
    start, end = max(nums), sum(nums)
    max_cutting = 0

    while start<=end:
        mid = (start+end)//2

        if isDivide(mid, k, nums, links):
            start, end = start, mid-1
            max_cutting = mid
        else:
            start, end = mid+1, end
    return max_cutting

solution = binarySearch

print(
    solution(1,
         	[6, 9, 7, 5],
        [[-1, -1], [-1, -1], [-1, 0], [2, 1]])
)
print(
    solution(3,
        [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1],
        [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]])
)