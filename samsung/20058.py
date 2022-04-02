from copy import deepcopy
import sys
from collections import deque
sys.stdin = open('input.txt')
N, Q = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(2**N)]
L = list(map(int, sys.stdin.readline().split()))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def rotate(grid, l):
    new_grid = [[0]*(2**N) for _ in range(2**N)]
    for x in range(0, 2**N, 2**l):
        for y in range(0, 2**N, 2**l):
            for i in range(2**l):
                for j in range(2**l):
                    new_grid[x+i][y+j] = grid[x+2**l-1-j][y+i]
    
    return new_grid


def melt(grid):
    new_grid = deepcopy(grid)
    for x in range(2**N):
        for y in range(2**N):
            cnt = 0
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0 <= nx < 2**N and 0 <= ny < 2**N:
                    if grid[nx][ny] > 0:
                        cnt += 1
            if cnt < 3:
                if new_grid[x][y] > 0:
                    new_grid[x][y] -= 1

    return new_grid


def bfs(i, j, grid):
    
    que = deque([[i, j]])
    cnt = 0
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < 2**N and 0 <= ny < 2**N:
                if not visited[nx][ny] and grid[nx][ny] > 0:
                    visited[nx][ny] = True
                    cnt += 1
                    que.append([nx, ny])
    
    return cnt


for i in range(Q):
    grid = rotate(grid, L[i])
    grid = melt(grid)


ans = 0
total = 0
visited = [[False]*(2**N) for _ in range(2**N)]
for i in range(2**N):
    for j in range(2**N):
        total += grid[i][j]
        if not visited[i][j]:
            ans = max(ans, bfs(i, j, grid))

print(total)
print(ans)
