import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]


ans = 0
d = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
def backtrack(temp, x, y):
    global ans
    if y == M:
        x += 1
        y = 0

    if x == N:
        ans = max(ans, temp)
        return    

    for i in range(4):
        nx, ny = x+d[i][0], y+d[i][1]
        if 0 <= nx < N and 0 <= ny < M and not visited[x][y] and not visited[nx][y] and not visited[x][ny]:
            visited[x][y] = True
            visited[nx][y] = True
            visited[x][ny] = True
            backtrack(temp+2*A[x][y]+A[nx][y]+A[x][ny], x, y+1)
            visited[x][y] = False
            visited[nx][y] = False
            visited[x][ny] = False
    
    backtrack(temp, x, y+1)

backtrack(0, 0, 0)
print(ans)
    