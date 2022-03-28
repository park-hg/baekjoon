import sys
sys.stdin = open('input.txt', 'r')
N, M, H = map(int, sys.stdin.readline().split())
edges = [[False]*(N+1) for _ in range(H+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    edges[a][b] = True

def get_last(h, n, edges):
    if h == H+1:
        return n
    if 0 <= n-1 < N+1 and edges[h][n-1]:
        return get_last(h+1, n-1, edges)
    if 0 <= n < N+1 and edges[h][n]:
        return get_last(h+1, n+1, edges)
    return get_last(h+1, n, edges)


ans = -1

def dfs(index, edges, depth):
    global ans
    if depth == 4:
        return
    cnt = 0
    for i in range(1, N+1):
        if i == get_last(0, i, edges):
            cnt += 1
        else:
            break
    if cnt == N:
        ans = depth
        return
    for h in range(index, H+1):
        for n in range(1, N):
            if not edges[h][n] and not edges[h][n+1]:
                edges[h][n] = True
                dfs(h, edges, depth+1)
                edges[h][n] = False

dfs(0, edges, 0)

print(ans)