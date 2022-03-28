import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
N, L, R = map(int, sys.stdin.readline().split())
A = []
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(i, j, discovered=[]):
    cnt, total = 1, A[i][j]
    que = deque([[i, j]])
    visited[i][j] = True
    discovered.append([i, j])
    while que:
        x, y = que.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(A[x][y] - A[nx][ny]) <= R:
                    que.append([nx, ny])
                    cnt += 1
                    total += A[nx][ny]
                    visited[nx][ny] = True
                    discovered.append([nx, ny])
    
    return cnt, total, discovered

ans = 0


while True:
    visited = [[False]*N for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                cnt, total, discovered = bfs(i, j, [])
                if cnt > 1:
                    for x, y in discovered:
                        if A[x][y] != total//cnt:
                            flag += abs(A[x][y]-total//cnt)
                            A[x][y] = total//cnt
    if flag == 0:
        break
    ans += 1

print(ans)
