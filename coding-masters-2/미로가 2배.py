import sys
h1,w1=map(int,sys.stdin.readline().split())
maze1=[list(sys.stdin.readline()) for _ in range(h1)]
s1=[(row,cols.index('S')) for row,cols in enumerate(maze1) if 'S' in cols][0]
h2,w2=map(int,sys.stdin.readline().split())
maze2=[list(sys.stdin.readline()) for _ in range(h2)]
s2=[(row,cols.index('S')) for row,cols in enumerate(maze2) if 'S' in cols][0]

def bfs():
    ds = [(-1,0), (0,-1), (1,0), (0,1)]
    q = [(s1,s2,0)]
    visited = set((s1,s2))

    for (p1y,p1x), (p2y,p2x),count in q:
        for my, mx in ds:
            m1y = p1y+my if 0<=p1y+my<h1 and maze1[p1y+my][p1x]!='#' else p1y
            m1x = p1x+mx if 0<=p1x+mx<w1 and maze1[p1y][p1x+mx]!='#' else p1x
            m2y = p2y+my if 0<=p2y+my<h2 and maze2[p2y+my][p2x]!='#' else p2y
            m2x = p2x+mx if 0<=p2x+mx<w2 and maze2[p2y][p2x+mx]!='#' else p2x
            v1 = maze1[m1y][m1x]
            v2 = maze2[m2y][m2x]

            if ((m1y,m1x),(m2y,m2x)) not in visited:
                q.append(((m1y,m1x),(m2y,m2x),count+1))
                visited.add(((m1y,m1x),(m2y,m2x)))
                
            if (v1,v2)==('E','E'):
                return count+1
    else: return -1
print(bfs())