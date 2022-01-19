import sys
from copy import deepcopy
sys.stdin = open('input.txt', 'r')

graph = []

for _ in range(4):
    a0, b0, a1, b1, a2, b2, a3, b3 = map(int, sys.stdin.readline().split())
    graph.append([[a0, b0-1], [a1, b1-1], [a2, b2-1], [a3, b3-1]])


dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]


def prey(graph, x, y):
    candidates = []
    d = graph[x][y][1]
    nx, ny = x, y
    while 0 <= nx+dx[d] < 4 and 0 <= ny+dy[d] < 4:
        nx, ny = nx+dx[d], ny+dy[d]
        if 1 <= graph[nx][ny][0] <= 16:
            candidates.append([nx, ny])
    return candidates


def find_fish(graph, index):
    for i in range(4):
        for j in range(4):
            if graph[i][j][0] == index:
                return i, j


def move_fish(graph, shark_x, shark_y):
    for i in range(1, 17):
        fish = find_fish(graph, i)
        if not fish:
            continue
        x, y = fish
        d = graph[x][y][1]
        for _ in range(8):
            nx, ny = x+dx[d], y+dy[d]
            if 0 <= nx < 4 and 0 <= ny < 4:
                if nx != shark_x or ny != shark_y:
                    graph[x][y][0], graph[nx][ny][0] = graph[nx][ny][0], graph[x][y][0]
                    graph[x][y][1], graph[nx][ny][1] = graph[nx][ny][1], d
                    break
            d = (d+1)%8


def backtrack(graph, x, y, score):
    global ans
    new_graph = deepcopy(graph)
    number = new_graph[x][y][0]
    new_graph[x][y][0] = -1
    ans = max(ans, score+number)
    move_fish(new_graph, x, y)
    candidates = prey(new_graph, x, y)
    for nx, ny in candidates:
        backtrack(new_graph, nx, ny, score+number)

ans = 0
backtrack(graph, 0, 0, 0)
print(ans)