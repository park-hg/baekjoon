import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

visited = [[False]*M for _ in range(N)]
ans = 0
def dfs(step, x, y, sum):
    global ans
    visited[x][y] = True
    if step == 3:
        ans = max(ans, sum)
        return
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            dfs(step+1, nx, ny, sum+grid[nx][ny])
            visited[nx][ny] = False

def get_h(x, y):
    values = []
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            values.append(grid[nx][ny])
    if len(values) >= 3:
        values.sort(reverse=True)
        return sum(values[:3])+grid[x][y]
    return 0

for i in range(N):
    for j in range(M):
        dfs(0, i, j, grid[i][j])
        visited[i][j] = False
        print(visited)
        ans = max(ans, get_h(i, j))

print(ans)