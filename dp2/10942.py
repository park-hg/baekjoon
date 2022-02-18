import sys
sys.stdin = open('input.txt', 'r')
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

dp = [[-1]*N for _ in range(N)]
for i in range(N):
    dp[i][i] = 1
    if i < N-1:
        dp[i][i+1] = int(nums[i] == nums[i+1])
for k in range(2, N):
    for i in range(N-k):
        dp[i][i+k] = dp[i+1][i+k-1]*(nums[i] == nums[i+k])

for _ in range(M):
    S, E = map(int, sys.stdin.readline().split())
    print(dp[S-1][E-1])
