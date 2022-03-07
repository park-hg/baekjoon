import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
N, K = map(int, sys.stdin.readline().split())
visited = [-1]*100001

def bfs():
    que = deque([(N, 0)])
    visited[N] = 0
    while que:
        x, dist = que.popleft()
        if x == K:
            return dist
        for y in [x-1, x+1, 2*x]:
            if 0 <= y < 100001 and visited[y] == -1:
                que.append((y, dist+1))
                visited[y] = x

dist = bfs()
path = [K]
cur = K

while cur != N:
    cur = visited[cur]
    path.append(cur)

print(dist)
print(*path[::-1])
