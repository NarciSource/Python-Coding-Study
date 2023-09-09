import sys
n = sys.stdin.readline()
numbers = sorted(map(int,sys.stdin.readline().split()), reverse=True)
print(0 if sum(numbers)==0 else ''.join(map(str, numbers)) if sum(numbers[-2:])==0 and sum(numbers[0:-2])%3==0 else -1)