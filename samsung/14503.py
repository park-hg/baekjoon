import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt', 'r')
N, M = map(int, input().split())
r, c, d = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

grid = [list(map(int, input().split())) for _ in range(N)]

def move(x, y, cur_d, cleaned):
    flag = False
    for i in range(4):
        tx, ty = x+dx[i], y+dy[i]
        if grid[tx][ty] == 0:
            flag = True

    if flag:
        next_d = (cur_d+3)%4
        nx, ny = x+dx[next_d], y+dy[next_d]
        if grid[nx][ny] == 0:
            grid[nx][ny] = 2
            return move(nx, ny, next_d, cleaned+1)
        else:
            return move(x, y, next_d, cleaned)

    else:
        back_d = (cur_d+2)%4
        bx, by = x+dx[back_d], y+dy[back_d]
        if grid[bx][by] == 1:
            return cleaned
        else:
            return move(bx, by, cur_d, cleaned)

grid[r][c] = 2
ans = move(r, c, d, 1)
print(ans)
