import sys
n,m = map(int,sys.stdin.readline().split())
enter, rotate = 1, 0
eaten = []
for candy in map(int,sys.stdin.readline().split()):
    (x, y) = (enter, candy) if enter<candy else (candy, enter)
    left = y - x - len([candy for candy in eaten if x<=candy<y])
    right = (x+n - y)%n - len([candy for candy in eaten if candy<x or y<=candy])

    eaten.append(candy)
    rotate+=min(left, right)
    enter = candy
print(rotate)