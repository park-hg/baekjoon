#90min/60min
from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

N, M, K = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

def update(dice, direction, nx, ny):
    if direction == [0, 1]:
        new_dice = {
            'up':dice['left'],
            'down':dice['right'],
            'left':dice['down'],
            'right':dice['up'],
            'front':dice['front'],
            'behind':dice['behind']
        }
    elif direction == [0, -1]:
        new_dice = {
            'up':dice['right'],
            'down':dice['left'],
            'left':dice['up'],
            'right':dice['down'],
            'front':dice['front'],
            'behind':dice['behind']
        }
    elif direction == [1, 0]:
        new_dice = {
            'up':dice['behind'],
            'down':dice['front'],
            'left':dice['left'],
            'right':dice['right'],
            'front':dice['up'],
            'behind':dice['down']
        }
    elif direction == [-1, 0]:
        new_dice = {
            'up':dice['front'],
            'down':dice['behind'],
            'left':dice['left'],
            'right':dice['right'],
            'front':dice['down'],
            'behind':dice['up']
        }
    A, B = new_dice['down'], graph[nx][ny]
    if A > B:
        if direction == [0, 1]:
            new_direction = [1, 0]
        elif direction == [0, -1]:
            new_direction = [-1, 0]
        elif direction == [1, 0]:
            new_direction = [0, -1]
        elif direction == [-1, 0]:
            new_direction = [0, 1]
    elif A < B:
        if direction == [0, 1]:
            new_direction = [-1, 0]
        elif direction == [0, -1]:
            new_direction = [1, 0]
        elif direction == [1, 0]:
            new_direction = [0, 1]
        elif direction == [-1, 0]:
            new_direction = [0, -1]
    else:
        new_direction = direction[:]

    if nx == 0 and new_direction[0] == -1:
        new_direction[0] = 1
    if nx == N-1 and new_direction[0] == 1:
        new_direction[0] = -1
    if ny == 0 and new_direction[1] == -1:
        new_direction[1] = 1
    if ny == M-1 and new_direction[1] == 1:
        new_direction[1] = -1

    return new_dice, new_direction

def bfs(x0, y0):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    number = graph[x0][y0]
    que = deque([(x0, y0)])
    visited = [[False]*M for _ in range(N)]
    visited[x0][y0] = True
    cnt = 1
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == number:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    cnt += 1
                    que.append((nx, ny))
    return cnt*number

score = 0
x, y = 0, 0
direction = [0, 1]
dice = {
    'up':1,
    'down':6,
    'left':4,
    'right':3,
    'front':5,
    'behind':2
}
for _ in range(K):
    #print(x, y)
    nx, ny = x+direction[0], y+direction[1]
    dice, direction = update(dice, direction, nx, ny)
    score += bfs(nx, ny)
    x, y = nx, ny
print(score)