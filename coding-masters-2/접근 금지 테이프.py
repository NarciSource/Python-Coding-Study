import sys
n,m=map(int,sys.stdin.readline().split())
polygon=list(map(int,sys.stdin.readline().split()))
polygon=[tuple(polygon[i:i+2]) for i in range(0,n*2,2)]
points=list(map(int,sys.stdin.readline().split()))
points=[tuple(points[i:i+2]) for i in range(0,m*2,2)]

def is_inside(point):
    crosses = 0
    for p1,p2 in zip(polygon[1:]+[polygon[0]],polygon):
        if (p1[0] > point[0]) != (p2[0] > point[0]):
            at_x = (p2[1]-p1[1])*(point[0]-p1[0])/(p2[0]-p1[0])+p1[1]

            if point[1] < at_x:
                crosses += 1
    return crosses%2==1
print("YES" if all(map(is_inside, points)) else "NO")