import sys
sys.stdin = open('input.txt', 'r')
N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

depth = [-1]*(N+1)
parent = [[0]*18 for _ in range(N+1)]
def dfs(v, d):
    depth[v] = d
    for w in graph[v]:
        if depth[w] == -1:
            parent[w][0] = v
            dfs(w, d+1)

dfs(1, 0)

for j in range(18-1):
    for i in range(1, N+1):
        parent[i][j+1] = parent[parent[i][j]][j]

M = int(sys.stdin.readline())
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    if depth[u] < depth[v]:
        u, v = v, u
    if depth[u] != depth[v]:
        for j in range(17, -1, -1):
            if depth[parent[u][j]] >= depth[v]:
                u = parent[u][j]
    if u != v:
        for j in range(17, -1, -1):
            if parent[u][j] != 0 and parent[u][j] != parent[v][j]:
                u, v = parent[u][j], parent[v][j]
        u = parent[u][0]

    print(u)
