import sys
from collections import deque
from copy import deepcopy

sys.stdin = open('input.txt', 'r')
field = []
while True:
    l = list(sys.stdin.readline().rstrip())
    if not l:
        break
    field.append(l)

m, n = len(field), len(field[0])

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(i, j):
    que = deque([[i, j]])
    visited = set()
    visited.add((i, j))
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                if field[nx][ny] == field[x][y]:
                    visited.add((nx, ny))
                    que.append([nx, ny])
    return visited


def down(field):
    new_field = deepcopy(field)
    for j in range(n):
        letter = []
        for k in range(m-1, -1, -1):
            if field[k][j] != '.':
                letter.append(field[k][j])
                new_field[k][j] = '.'
        for i in range(len(letter)):
            new_field[-1-i][j] = letter[i]
    return new_field


ans = 0
while True:
    flag = False
    for i in range(m):
        for j in range(n):
            if field[i][j] != '.':
                color = field[i][j]
                block = bfs(i, j)
                if len(block) >= 4:
                    flag = True
                    for a, b in block:
                        field[a][b] = '.'
    if not flag:
        break
    ans += 1
    field = down(field)
print(ans)
