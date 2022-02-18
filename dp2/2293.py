import sys
sys.stdin = open('input.txt', 'r')
n, k = map(int, sys.stdin.readline().split())
w = [int(sys.stdin.readline()) for _ in range(n)]

dp = [0]*(k+1)
dp[0] = 1

for i in range(n):
    for j in range(1, k+1):
        if j >= w[i]:
            dp[j] = dp[j] + dp[j-w[i]]

print(dp[k])