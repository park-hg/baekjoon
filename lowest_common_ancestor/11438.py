import sys
import math
from collections import deque
sys.stdin = open('input.txt', 'r')
N = int(sys.stdin.readline())
logN = math.ceil(math.log2(N))
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

depth = [-1]*(N+1)
parent = [[0]*logN for _ in range(N+1)]
que = deque([1])
depth[1] = 0
while que:
    v = que.popleft()
    for w in graph[v]:
        if depth[w] == -1:
            depth[w] = depth[v]+1
            parent[w][0] = v
            que.append(w)

for j in range(logN-1):
    for i in range(1, N+1):
        parent[i][j+1] = parent[parent[i][j]][j]

M = int(sys.stdin.readline())
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    if depth[u] < depth[v]:
        u, v = v, u
    for i in range(logN-1, -1, -1):
        if depth[u] - depth[v] >= 1<<i:
            u = parent[u][i]
    if u != v:
        for j in range(logN-1, -1, -1):
            if parent[u][j] != 0 and parent[u][j] != parent[v][j]:
                u, v = parent[u][j], parent[v][j]
        u = parent[u][0]

    print(u)
