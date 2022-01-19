from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 'R':
            rx0, ry0 = i, j
        elif graph[i][j] == 'B':
            bx0, by0 = i, j

def bfs():
    que = deque([(rx0, ry0, bx0, by0)])
    visited = set((rx0, ry0, bx0, by0))
    cnt = 0
    while que:
        sz = len(que)
        for _ in range(sz):
            if cnt > 10:
                return -1
            rx, ry, bx, by = que.popleft()
            if graph[rx][ry] == 'O':
                return cnt
            for i in range(4):
                nrx, nry, r_mv = rx, ry, 0
                while 0 <= nrx+dx[i] < N and 0 <= nry+dy[i] < M and graph[nrx+dx[i]][nry+dy[i]] != '#':
                    nrx += dx[i]
                    nry += dy[i]
                    r_mv += 1
                    if graph[nrx][nry] == 'O':
                        break
                nbx, nby, b_mv = bx, by, 0
                while 0 <= nbx+dx[i] < N and 0 <= nby+dy[i] < M and graph[nbx+dx[i]][nby+dy[i]] != '#':
                    nbx += dx[i]
                    nby += dy[i]
                    b_mv += 1
                    if graph[nbx][nby] == 'O':
                        break
                if graph[nbx][nby] == 'O':
                    continue
                if (nrx, nry) == (nbx, nby):
                    if r_mv > b_mv:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if (nrx, nry, nbx, nby) not in visited:
                    visited.add((nrx, nry, nbx, nby))
                    que.append((nrx, nry, nbx, nby))
        cnt += 1
    return -1

print(bfs())
        