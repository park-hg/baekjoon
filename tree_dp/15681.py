import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict
sys.stdin = open('input.txt', 'r')
N, R, Q = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [0]*(N+1)
visited = [False]*(N+1)
def dfs(v):
    dp[v] = 1
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:
            dfs(w)
            dp[v] += dp[w]
            
        

dfs(R)

for _ in range(Q):
    U = int(sys.stdin.readline())
    print(dp[U])