import sys
n = int(sys.stdin.readline())
xs = list(map(int,sys.stdin.readline().split()))

flip = lambda enum: {value: idx for idx, value in enum}
orders = flip(enumerate(sorted(set(xs))))
print(*map(orders.get, xs))