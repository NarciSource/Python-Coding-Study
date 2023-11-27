hiddenmap = list(input())
minmap = []
maxmap = []
switch = {'g':'o','o':'g'}.get
how_many_islands = lambda m: sum(1 for pre, p in zip(m, m[1:]) if pre=='o' and p=='g')

for p in hiddenmap:
    p_when_min = p_when_min if p=='x' else p
    p_when_max = switch(p_when_max) if p=='x' else p

    minmap.append(p_when_min)
    maxmap.append(p_when_max)

print(how_many_islands(minmap))
print(how_many_islands(maxmap))