import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt', 'r')
N = int(sys.stdin.readline())
nums = [0] + list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[0]*2 for _ in range(N+1)]
visited = [False]*(N+1)
def dfs(v):
    visited[v] = True
    dp[v][1] = nums[v]
    for w in graph[v]:
        if not visited[w]:
            dfs(w)
            dp[v][1] += dp[w][0]
            dp[v][0] += max(dp[w][0], dp[w][1])

dfs(1)
print(max(dp[1][0], dp[1][1]))
