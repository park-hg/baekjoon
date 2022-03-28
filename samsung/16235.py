import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
N, M, K = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

trees = [[deque() for _ in range(N)] for _ in range(N)]
grid = [[5]*N for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, sys.stdin.readline().split())
    trees[x-1][y-1].append(z)


def year():

    for x in range(N):
        for y in range(N):
            if trees[x][y]:
                new_tree = deque()
                temp = 0
                for t in trees[x][y]:
                    if t <= grid[x][y]:
                        grid[x][y] -= t
                        new_tree.append(t+1)
                    else:
                        temp += t//2
                trees[x][y] = new_tree
                grid[x][y] += temp

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    for x in range(N):
        for y in range(N):
            for t in trees[x][y]:
                if t%5 == 0:
                    for i in range(8):
                        nx, ny = x+dx[i], y+dy[i]
                        if 0 <= nx < N and 0 <= ny < N:
                            trees[nx][ny].appendleft(1)

    for i in range(N):
        for j in range(N):
            grid[i][j] += A[i][j]


for _ in range(K):
    year()

ans = 0
for i in range(N):
    for j in range(N):
        ans += len(trees[i][j])

print(ans)