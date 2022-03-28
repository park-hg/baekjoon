from copy import deepcopy
import sys
sys.stdin = open('input.txt', 'r')
R, C, T = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
cleaner = []
for i in range(R):
    for j in range(C):
        if A[i][j] == -1:
            cleaner.append([i, j])

def spread(grid):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    new_grid = [[0]*C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if grid[x][y] > 0:
                s = grid[x][y] // 5
                cnt = 0
                for i in range(4):
                    nx, ny = x+dx[i], y+dy[i]
                    if 0 <= nx < R and 0 <= ny < C:
                        if grid[nx][ny] != -1:
                            cnt += 1
                            new_grid[nx][ny] += s
                new_grid[x][y] += grid[x][y] - s*cnt
    x0, y0 = cleaner[0]
    x1, y1 = cleaner[1]
    new_grid[x0][y0] = -1
    new_grid[x1][y1] = -1
    return new_grid

def rotate(grid, cleaner):
    x0, _ = cleaner[0]
    for i in range(x0-2, -1, -1):
        grid[i+1][0] = grid[i][0]
    for j in range(C-1):
        grid[0][j] = grid[0][j+1]
    for i in range(x0):
        grid[i][C-1] = grid[i+1][C-1]
    for j in range(C-2, -1, -1):
        grid[x0][j+1] = grid[x0][j]
    grid[x0][1] = 0

    x1, _ = cleaner[1]
    for i in range(x1+1, R-1):
        grid[i][0] = grid[i+1][0]
    for j in range(C-1):
        grid[R-1][j] = grid[R-1][j+1]
    for i in range(R-2, x1-1, -1):
        grid[i+1][C-1] = grid[i][C-1]
    for j in range(C-2, -1, -1):
        grid[x1][j+1] = grid[x1][j]
    grid[x1][1] = 0

    return grid

for _ in range(T):
    A = spread(A)
    A = rotate(A, cleaner)

ans = 0
for i in range(R):
    for j in range(C):
        if A[i][j] != -1:
            ans += A[i][j]


print(ans)