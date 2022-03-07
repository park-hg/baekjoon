import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
N, K = map(int, sys.stdin.readline().split())

visited = [0]*100001
que = deque([N])
dist = 0
cnt = 0
while que:
    sz = len(que)
    for _ in range(sz):
        x = que.popleft()
        visited[x] = True
        if x == K:
            cnt += 1
        for y in [x-1, x+1, 2*x]:
            if 0 <= y < 100001 and not visited[y]:
                que.append(y)
    if visited[K]:
        break
    dist += 1

print(dist)
print(cnt)
