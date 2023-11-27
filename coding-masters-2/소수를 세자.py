import sys
N = int(sys.stdin.readline())
remains = iter(sys.stdin.readline().split())
prime = [2]
try:
    r = next(remains)
    if r=='2': r = next(remains)
    num = 3
    while True:
        if all(map(lambda p: num%p!=0, prime)):
            prime.append(num)
            for v in str(num):
                if v == r:
                    r = next(remains)
        num+=2
except StopIteration:
    print(prime[-1])