from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
K = int(input())

grid = [[0]*N for _ in range(N)]
grid[0][0] = 0
for _ in range(K):
    r, c = map(int, input().split())
    grid[r-1][c-1] = 1

# right-based
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
L = int(input())
mv_list = {}
for _ in range(L):
    x, c = input().rstrip().split()
    mv_list[int(x)] = 1 if c == 'D' else -1

ans = 0
i = 0
snake = deque([[0, 0]])
while True:
    ans += 1
    head = snake[-1]
    nx, ny = head[0]+d[i][0], head[1]+d[i][1]
    if 0 > nx or nx >= N or 0 > ny or ny >= N:
        break
    if [nx, ny] in snake:
        break
    if grid[nx][ny] == 1:
        snake.append([nx, ny])
        grid[nx][ny] = 0
    elif grid[nx][ny] == 0:
        if snake:
            snake.popleft()
        snake.append([nx, ny])
    if ans in mv_list:
        i = (i+mv_list[ans])%4
print(ans)