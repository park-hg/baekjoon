import sys

N, M = map(int, sys.stdin.readline().split())
A = []
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

clouds = set([(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)])

def move_clouds(clouds, di, s):
    next_clouds = set()
    for x, y in clouds:
        nx = (x+s*dx[di])%N
        ny = (y+s*dy[di])%N
        next_clouds.add((nx, ny))

    return next_clouds

def rain(clouds):
    for x, y in clouds:
        A[x][y] += 1

    return clouds

def copy_water(rain_spot):
    for x, y in rain_spot:
        for i in range(4):
            diag_x = x+dx[2*i+1]
            diag_y = y+dy[2*i+1]
            if 0 <= diag_x < N and 0 <= diag_y < N:
                A[x][y] += (A[diag_x][diag_y] != 0)

    return

def make_clouds(rain_spot):
    clouds = set()
    for i in range(N):
        for j in range(N):
            if A[i][j] >= 2 and (i, j) not in rain_spot:
                clouds.add((i, j))
                A[i][j] -= 2
                
    return clouds

for _ in range(M):
    di, s = map(int, sys.stdin.readline().split())
    di -= 1
    clouds = move_clouds(clouds, di, s)
    rain_spot = rain(clouds)
    copy_water(rain_spot)
    clouds = make_clouds(rain_spot)

ans = 0
for i in range(N):
    for j in range(N):
        ans += A[i][j]

print(ans)