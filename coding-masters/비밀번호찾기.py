import sys
str = sys.stdin.readline().split()
print(" ".join(str[:str.index('c')+1]))