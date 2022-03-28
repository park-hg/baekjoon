import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(N+1)
dp = [[0]*2 for _ in range(N+1)]
def dfs(v):
    dp[v][1] = 1
    visited[v] = 1
    for w in graph[v]:
        if not visited[w]:
            dfs(w)
            dp[v][0] += dp[w][1]
            dp[v][1] += min(dp[w][0], dp[w][1])

dfs(1)
print(min(dp[1][0], dp[1][1]))
