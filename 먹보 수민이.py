import sys
n = int(sys.stdin.readline())
stores = [tuple(map(int,sys.stdin.readline().split())) for _ in range(n)]
l,p = map(int,sys.stdin.readline().split())
stores.append((l, 0))

fullness = [(0, p)]
pre = 0
for a,b in sorted(stores):
    if a>l: break
    energies,fullness = fullness[:], []
    diff = a-pre
    selectedMax = [0]*(n+2)
    for visits, energy in energies:
        if diff<=energy:
            if selectedMax[visits] < energy-diff:
                selectedMax[visits] = energy-diff
                fullness.append((visits, energy-diff))
            if selectedMax[visits+1] < energy-diff+b:
                selectedMax[visits+1] = energy-diff+b
                fullness.append((visits+1, energy-diff+b))
    pre = a
print(min(list(zip(*fullness))[0]) if fullness else -1)