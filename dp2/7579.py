import sys
sys.stdin = open('input.txt', 'r')
N, M = map(int, sys.stdin.readline().split())
m = list(map(int, sys.stdin.readline().split()))
c = list(map(int, sys.stdin.readline().split()))

dp = [[0]*10001 for _ in range(N+1)]

for i in range(N):
    for j in range(10001):
        if j >= c[i]:
            dp[i+1][j] = max(dp[i][j], dp[i][j-c[i]]+m[i])
        else:
            dp[i+1][j] = dp[i][j]

ans = 0
for j in range(10001):
    if dp[-1][j] >= M:
        ans = j
        break

print(ans)
