import sys
n = int(sys.stdin.readline())
title1 = sys.stdin.readline().split()
title2 = sys.stdin.readline().split()

diff = sum(1 for w2,w3 in zip(title1, title2) if w2!=w3)
print(3 if diff==3 else 2 if diff==4 else 0)