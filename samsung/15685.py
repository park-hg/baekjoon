import sys
sys.stdin = open('input.txt', 'r')
N = int(sys.stdin.readline())
grid = [[False]*101 for _ in range(101)]


dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def evolve(points):
    sz = len(points)
    a, b = points[-1]
    for i in range(sz-2, -1, -1):
        x, y = points[i]
        points.append([a+b-y, b-a+x])
        grid[a+b-y][b-a+x] = True
    return points

for _ in range(N):
    x, y, d, g = map(int, sys.stdin.readline().split())
    points = [[x, y], [x+dx[d], y+dy[d]]]
    grid[x][y] = True
    grid[x+dx[d]][y+dy[d]] = True
    for _ in range(g):
        points = evolve(points)

cnt = 0
for i in range(100):
    for j in range(100):
        if grid[i][j] and grid[i+1][j] and grid[i][j+1] and grid[i+1][j+1]:
            cnt += 1
print(cnt)

