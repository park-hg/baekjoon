from copy import deepcopy
import sys
from itertools import combinations
sys.stdin = open('input.txt', 'r')
N, M = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cctv_idx = []
cctvs = {}
for i in range(N):
    for j in range(M):
        if 1 <= grid[i][j] < 6:
            cctv_idx.append((i, j))
            cctvs[(i, j)] = grid[i][j]

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

cctv_direction = {}
for i in range(1, 6):
    if i == 2:
        cctv_direction[i] = [((1, 0), (-1, 0)), ((0, 1), (0, -1))]
    elif i == 3:
        cctv_direction[i] = [((-1, 0), (0, 1)), ((0, 1), (1, 0)),((1, 0), (0, -1)),((0, -1), (-1, 0))]
    elif i == 1:
        cctv_direction[i] = list(combinations(d, i))
    else:
        cctv_direction[i] = list(combinations(d, i-1))

ans = N*M
def count_zeros(grid, index):
    global ans

    if index == len(cctv_idx):
        zeros = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 0:
                    zeros += 1
        ans = min(zeros, ans)
        return
    
    x, y = cctv_idx[index]

    directions = cctv_direction[cctvs[(x, y)]]
    new_grid = deepcopy(grid)
    for ds in directions:
        for d in ds:
            nx, ny = x, y
            while 0 <= nx + d[0] < N and 0 <= ny + d[1] < M:
                nx += d[0]
                ny += d[1]
                if new_grid[nx][ny] == 6:
                    break
                elif new_grid[nx][ny] == 0:
                    new_grid[nx][ny] = '#'
        count_zeros(new_grid, index+1)
        new_grid = deepcopy(grid)

count_zeros(grid, 0)
print(ans)
