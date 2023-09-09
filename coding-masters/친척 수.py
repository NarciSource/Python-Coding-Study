import sys
n = int(sys.stdin.readline())
numbers = sorted([int(sys.stdin.readline()) for _ in range(n)])

answer = []
for i in range(1,numbers[-1]+1):
    if numbers[1] - numbers[0] < i and numbers[0] < i:
        break
    else:
        remain = numbers[0]%i
        if all(map(lambda n: n%i==remain, numbers)):
            answer.append(i)
print(*answer)