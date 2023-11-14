import sys
cate = list(map(int,sys.stdin.readline().strip()))
serial = list(map(int,sys.stdin.readline().strip()))
error = int(sys.stdin.readline())
classes = [(11,15),(21,22),(31,51),(81,86),(71,71)]

def get_error(c):
    a = sum(cate[0::2])+sum(serial[0::2])+c//10
    b = sum(cate[1::2])+sum(serial[1::2])+c%10
    r = (2*b+a)%10
    return (10-r)%10

print(*['O' if error in map(get_error,range(a,b+1)) else 'X' for a,b in classes],sep='')