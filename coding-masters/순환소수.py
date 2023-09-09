import sys
p,q = map(int,sys.stdin.readline().split())
remainders = [p]
decimals = []
while True:
    decimals.append((p*10)//q)
    p = (p*10)%q
    if p==0:
        d,r = decimals,[]
        break
    elif p in remainders:
        d,r = decimals[:remainders.index(p)], decimals[remainders.index(p):]
        break
    else:
        remainders.append(p)
d,r = map(lambda numbers: ''.join(map(str,numbers)), [d,r])
print(f'0.{d}{{{r}}}' if r else f'0.{d}')