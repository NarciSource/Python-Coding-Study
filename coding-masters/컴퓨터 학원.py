x,o=1,2
for _ in range(int(input())-1):
    x,o = x+o, x*2+o
print((x+o)%796796)