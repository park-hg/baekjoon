import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline())
w = [0] + list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(n+1)]
while True:
    line = sys.stdin.readline()
    if not line:
        break
    a, b = map(int, line.split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[0]*2 for _ in range(n+1)]
visited = [False]*(n+1)
def dfs(i):
    visited[i] = True
    dp[i][1] = w[i]
    for j in graph[i]:
        if not visited[j]:
            dfs(j)
            dp[i][0] += max(dp[j][0], dp[j][1])
            dp[i][1] += dp[j][0]

dfs(1)
print(max(dp[1][0], dp[1][1]))

visited = [False]*(n+1)
discovered = []
def path(i):
    visited[i] = True
    if dp[i][1] > dp[i][0]:
        discovered.append(i)
        for j in graph[i]:
            if not visited[j]:
                visited[j] = True
                for k in graph[j]:
                    if not visited[k]:
                        path(k)
    else:
        for j in graph[i]:
            if not visited[j]:
                path(j)
            
path(1)
print(*sorted(discovered))