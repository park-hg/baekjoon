import sys
import heapq

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
grid = [[0]*N for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

d = {}
for _ in range(N**2):
    l = list(map(int, input().split()))
    target, friends = l[0], l[1:]
    d[target] = friends
    heap = []
    for x in range(N):
        for y in range(N):
            if grid[x][y] == 0:
                num_f, num_b = 0, 0
                for i in range(4):
                    nx, ny = x+dx[i], y+dy[i]
                    if 0 <= nx < N and 0 <= ny < N:
                        if grid[nx][ny] in friends:
                            num_f -= 1
                        elif grid[nx][ny] == 0:
                            num_b -= 1
                heapq.heappush(heap, (num_f, num_b, x, y))

    _, _, xx, yy = heapq.heappop(heap)
    grid[xx][yy] = target

answer = 0
for x in range(N):
    for y in range(N):
        num = 0
        target = grid[x][y]
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if grid[nx][ny] in d[target]:
                    num += 1
        if num != 0:
            answer += 10**(num-1)
print(answer)