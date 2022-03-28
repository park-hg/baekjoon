from copy import deepcopy
import sys
from itertools import combinations
from collections import deque

sys.stdin = open('input.txt', 'r')
N, M = map(int, sys.stdin.readline().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, sys.stdin.readline().split())))

blanks = set()
viruses = set()
for i in range(N):
    for j in range(M):
        if grid[i][j] == 0:
            blanks.add((i, j))
        elif grid[i][j] == 2:
            viruses.add((i, j))

def bfs(viruses, grid):
    que = deque()
    for i, j in viruses:
        que.append([i, j])
    
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 0:
                grid[nx][ny] = 2
                que.append([nx, ny])

    zeros = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 0:
                zeros += 1
    
    return zeros

ans = 0
for comb in combinations(blanks, 3):
    new_grid = deepcopy(grid)
    for idx in comb:
        i, j = blanks[idx]
        new_grid[i][j] = 1
    zeros = bfs(viruses, new_grid)
    ans = max(ans, zeros)

print(ans)
    