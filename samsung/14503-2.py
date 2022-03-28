import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

grid = [list(map(int, input().split())) for _ in range(N)]

ans = 0
def move(x, y, cur_d):
    global ans
    if grid[x][y] == 0:
        grid[x][y] = 2
        ans += 1

    for _ in range(4):
        next_d = (cur_d+3)%4
        nx, ny = x+dx[next_d], y+dy[next_d]
        #if 0 <= nx < N and 0 <= ny < N:
        if grid[nx][ny] == 0:
            move(nx, ny, next_d)
            return
        cur_d = next_d

    back_d = (cur_d+2)%4
    bx, by = x+dx[back_d], y+dy[back_d]
    if grid[bx][by] == 1:
        return
    move(bx, by, cur_d)


move(r, c, d)
print(ans)
