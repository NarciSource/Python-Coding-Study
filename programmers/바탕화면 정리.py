def solution(wallpaper):
    files = [(y,x) for y, column in enumerate(wallpaper) for x, cell in enumerate(column) if cell=='#']
    ys, xs = zip(*files)
    return [min(ys), min(xs), max(ys)+1, max(xs)+1]


print(solution([".#...", "..#..", "...#."]))
print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]))
print(solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]))
print(solution(["..", "#."]))