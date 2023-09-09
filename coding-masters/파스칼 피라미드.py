n=int(input())
elm=1
pyramid = []
for i in range(1,n+1):
    line = []
    for j in range(1,i):
        line.append(int(elm))

        elm *= i-j
        elm //= j
    line.append(int(elm))
    pyramid.append(line)

    elm *= n-i
    elm /= i

for i in range(n-1,-1,-1):
    print(*pyramid[i])