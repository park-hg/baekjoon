import sys
sys.stdin = open('input.txt', 'r')

M, N = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

dp = {}
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    if x == M-1 and y == N-1:
        return 1
    
    if (x, y) in dp:
        return dp[(x, y)]
    
    dp[(x, y)] = 0
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if grid[nx][ny] < grid[x][y]:
                dp[(x, y)] += dfs(nx, ny)

    return dp[(x, y)]

print(dfs(0, 0))