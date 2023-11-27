def cut(matrix, y,x, cube):
    n,m = len(cube), len(cube[0])
    figure = []
    for dy,dx in product(range(n),range(m)):
        my,mx = y+dy,x+dx
        if 0<=mx<size and 0<=my<size:
            figure.append(matrix[my][mx]*int(cube[dy][dx]))
    return figure

def flip(axis, cube):
    return cube[::-1] if axis=='y' else [col[::-1] for col in cube]

def rotate90(cube):
    n,m = len(cube), len(cube[0])
    new_cube = [[0]*n for _ in range(m)]
    for y,x in product(range(n),range(m)):
        new_cube[x][n-y-1] = cube[y][x]
    return new_cube

import sys
from itertools import product
size = 10
cubes = [
    ['1000',
     '1111',
     '1000'],
    ['1000',
     '1111',
     '0100'],
    ['1000',
     '1111',
     '0010'],
    ['1000',
     '1111',
     '0001'],
    ['0100',
     '1111',
     '0100'],
    ['0100',
     '1111',
     '0010'],
    ['1000',
     '1110',
     '0011'],
    ['0100',
     '1110',
     '0011'],
    ['0010',
     '1110',
     '0011'],
    ['11100',
     '00111'],
    ['1100',
     '0110',
     '0011']]
matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(size)]

figures = []
for cube in cubes:
    for axis in ['y','x']:
        for _ in range(4):
            for y,x in product(range(size),repeat=2):
                figures.append(cut(matrix, y,x, cube))
            cube = rotate90(cube)
        cube = flip(axis,cube)
print(max(map(sum,figures)))