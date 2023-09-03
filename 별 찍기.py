n=int(input())
star, empty = "*", " "
for i in range(n-1):
    star = [[star,  empty,  star],
            [empty, star,   empty],
            [star,  empty,  star]]
    empty = [[empty,empty,empty],[empty,empty,empty],[empty,empty,empty]]

fullstar = [['']*3**(n-1) for _ in range(3**(n-1))]
def draw(x,y,size, pixcels):
    if size==1:
        fullstar[x][y]=pixcels
    else:
        for i, columns in enumerate(pixcels):
            for j, pixcel in enumerate(columns):
                draw(x+(size//3)*i, y+(size//3)*j, size//3, pixcel)
draw(0,0,3**(n-1), star)

print(*[''.join(line) for line in fullstar],sep='\n')
