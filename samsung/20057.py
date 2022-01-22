import sys
sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

total = 0
for i in range(N):
    for j in range(N):
        total += grid[i][j]

[x, y] = [N//2, N//2]

d = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def sand(x, y, i):
    spread = {
        tuple(sum(j) for j in zip(d[(i+3)%4], d[(i+3)%4])):0.02,
        tuple(sum(j) for j in zip(d[i], d[(i+3)%4])):0.1,
        d[(i+3)%4]:0.07,
        tuple(sum(j) for j in zip(d[(i+2)%4], d[(i+3)%4])):0.01,
        tuple(sum(j) for j in zip(d[i], d[i])):0.05,
        tuple(sum(j) for j in zip(d[i],d[(i+1)%4])):0.1,
        d[(i+1)%4]:0.07,
        tuple(sum(j) for j in zip(d[(i+1)%4], d[(i+2)%4])):0.01,
        tuple(sum(j) for j in zip(d[(i+1)%4], d[(i+1)%4])):0.02,      
    }

    t = grid[x][y]
    left = t
    grid[x][y] = 0

    for k, v in spread.items():
        nx, ny = x+k[0], y+k[1]
        if 0 <= nx < N and 0 <= ny < N:
           grid[nx][ny] += int(t*v)
        left -= int(t*v)
    nx, ny = x+d[i][0], y+d[i][1]

    if 0 <= nx < N and 0 <= ny < N:
        grid[x+d[i][0]][y+d[i][1]] += left

def solve(x, y):
    step = 0
    for length in range(1, N+1):
        for _ in range(2):
            i = step%4
            for _ in range(length):
                x += d[i][0]
                y += d[i][1]
                sand(x, y, i)
                if x == 0 and y == 0:
                    return
            step += 1

solve(x, y)
for i in range(N):
    for j in range(N):
        total -= grid[i][j]

print(total)