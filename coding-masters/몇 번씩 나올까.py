n = int(input())
times = [0]*10
for digit in range(len(str(n))):
    share = n//(10**(digit+1))
    remain = n%(10**(digit+1))
    target = remain//(10**digit)
    unders = remain%(10**digit)

    for number in range(0,10):
        if number > target or number == 0:
            times[number] += share*(10**digit)
        elif number == target:
            times[number] += share*(10**digit) + unders + 1
        else:
            times[number] += (share+1)*10**digit
print(*times)