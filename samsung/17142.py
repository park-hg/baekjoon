import sys
from itertools import combinations
from collections import deque

sys.stdin = open('input.txt', 'r')
N, M = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


virus_candidates = []
zeros = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == 2:
            virus_candidates.append([i, j])
        if grid[i][j] == 0:
            zeros.append((i, j))

def bfs(que, visited, zeros):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    while que:
        x, y, t = que.popleft()
        if grid[x][y] == 0:
            zeros.discard((x, y))
        if len(zeros) == 0:
            return t
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if grid[nx][ny] != 1:
                    visited[nx][ny] = True
                    que.append([nx, ny, t+1])

    return 1e9

ans = 1e9

for comb in combinations(virus_candidates, M):
    que = deque()
    visited = [[False]*N for _ in range(N)]
    for x, y in comb:
        que.append([x, y, 0])
        visited[x][y] = True
    ans = min(ans, bfs(que, visited, set(zeros)))

print(-1 if ans==1e9 else ans)