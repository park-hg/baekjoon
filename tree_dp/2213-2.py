"""
https://www.acmicpc.net/source/39854191
"""

from sys import stdin as s
from collections import deque

input = s.readline

n = int(input())
cost = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
deg = [len(graph[i]) for i in range(n + 1)]
leaves = deque()
for j in range(1, n + 1):
    if deg[j] == 1:
        leaves.append(j)
dp = [[0, 0] for _ in range(n + 1)]
while leaves:
    now = leaves.popleft()
    dp[now][1] = cost[now]
    for can_go in graph[now]:
        deg[can_go] -= 1
        if deg[can_go] == 1:
            leaves.append(can_go)
        dp[now][1] += dp[can_go][0]
        dp[now][0] += max(dp[can_go])
print(max(dp[now]))
visited = [False] * (n + 1)
ans = []


def trace(node, check):
    visited[node] = True
    if check:
        ans.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if check:
                trace(neighbor, 0)
            else:
                if dp[neighbor][0] > dp[neighbor][1]:
                    trace(neighbor, 0)
                else:
                    trace(neighbor, 1)


if dp[now][0] > dp[now][1]:
    trace(now, 0)
else:
    trace(now, 1)
ans.sort()
print(*ans)
