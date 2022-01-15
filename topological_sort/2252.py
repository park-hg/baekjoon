import sys
from collections import defaultdict, deque

sys.stdin = open('input.txt', 'r')

N, M = map(int, sys.stdin.readline().split())

graph = {i:[] for i in range(N)}
indegree = [0]*N
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a-1].append(b-1)
    indegree[b-1] += 1

que = deque([])
ans = []


for i in range(N):
    if indegree[i] == 0:
        que.append(i)
while que:
    v = que.popleft()
    ans.append(v+1)
    for w in graph[v]:
        indegree[w] -= 1
        if indegree[w] == 0:
            que.append(w)
    del graph[v]

print(*ans)