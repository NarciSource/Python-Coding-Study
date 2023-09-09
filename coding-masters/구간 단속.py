import sys
meter = int(sys.stdin.readline())
n = int(sys.stdin.readline())

start_log = {}
for _ in range(n):
    numbers, time = sys.stdin.readline().split()
    time = list(map(int, time.split(":")))
    start_log[numbers] = time[0]*3600 + time[1]*60 + time[2]
end_log = {}
for _ in range(n):
    numbers, time = sys.stdin.readline().split()
    time = list(map(int, time.split(":")))
    end_log[numbers] = time[0]*3600 + time[1]*60 + time[2]

for s,e in zip(sorted(start_log.items()), sorted(end_log.items())):
    print(s[0], int(meter/(e[1]-s[1])*3600))