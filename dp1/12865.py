import sys
sys.stdin = open('input.txt', 'r')
N, K = map(int, sys.stdin.readline().split())
w = []
v = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    w.append(a)
    v.append(b)

dp = [[0]*(K+1) for _ in range(N)]
for j in range(K+1):
    if j >= w[0]:
        dp[0][j] = v[0]
for i in range(N-1):
    for j in range(K+1):
        if j >= w[i+1]:
            dp[i+1][j] = max(dp[i][j], dp[i][j-w[i+1]]+v[i+1])
        else:
            dp[i+1][j] = dp[i][j]
print(dp)
