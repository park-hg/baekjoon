import sys
sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())

r, c = [], []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    r.append(a)
    c.append(b)

dp = [[1e9]*N for _ in range(N)]

for i in range(N):
    dp[i][i] = 0

for k in range(1, N):
    for i in range(N-k):
        for j in range(i, i+k):
            dp[i][i+k] = min(dp[i][i+k], dp[i][j]+dp[j+1][i+k]+r[i]*c[j]*c[i+k])

print(dp[0][-1])
