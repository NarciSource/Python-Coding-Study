def solution(park, routes):
    read_row = lambda lst,r: ''.join(map(lambda s:s[r],lst))
    ns,ms = len(park),len(park[0])

    def find_start():
        for i in range(ns):
            for j in range(ms):
                if park[i][j]=='S':
                    return i,j
    y,x = find_start()

    for route in routes:
        op, n = route.split()
        n = int(n)
        d = {'N':(-n, 0), 'S':(n,0), 'W':(0,-n), 'E':(0,n)}
        dy,dx = map(sum,zip((y,x),d[op]))

        if (op=='N' and 0<=dy<ns and 'X' not in read_row(park[dy:y+1],dx)) or\
            (op=='S' and 0<=dy<ns and 'X' not in read_row(park[y:dy+1],dx)) or\
            (op=='W' and 0<=dx<ms and 'X' not in park[dy][dx:x+1]) or\
            (op=='E' and 0<=dx<ms and 'X' not in park[dy][x:dx+1]):
                y,x = dy,dx

    return [y,x]

print(solution(["SOO","OOO","OOO"],["E 2","S 2","W 1"]))
print(solution(["SOO","OXX","OOO"],["E 2","S 2","W 1"]))
print(solution(["OSO","OOO","OXO","OOO"],["E 2","S 3","W 1"]))