import sys
start = {'SUN':0, 'MON':1, 'TUE':2, 'WED':3, 'THU':4, 'FRI':5, 'SAT':6}.get(sys.stdin.readline().strip())
n = int(sys.stdin.readline())
holidays = [tuple(map(int,sys.stdin.readline().split())) for _ in range(n)]

number_colors = [{'red':0, 'blue':0, 'black':0} for _ in range(10)]
months=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dayofweek = lambda month, day: (sum(months[:month-1]) + day)%7
colorofweek = lambda week: 'red' if week==0 else 'blue' if week==6 else 'black'

for month in range(1, 13):
    for day in range(1, months[month-1]+1):
        color = colorofweek(dayofweek(month, day+start-1))

        if day//10 !=0:
            number_colors[day//10][color] += 1
        number_colors[day%10][color] += 1

for month, day in holidays:
    color = colorofweek(dayofweek(month, day+start-1))
    
    if day//10 !=0:
        number_colors[day//10][color] -= 1
    number_colors[day%10][color] -= 1
    
    if day//10 !=0:
        number_colors[day//10]['red'] += 1
    number_colors[day%10]['red'] += 1

for red, blue, black in map(lambda nc: nc.values(), number_colors):
    print(red, blue, black)