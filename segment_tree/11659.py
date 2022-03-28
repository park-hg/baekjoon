import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
dp = [0]*N
dp[0] = nums[0]
for i in range(N-1):
    dp[i+1] = dp[i] + nums[i+1]
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(dp[j-1]-dp[i-1]+nums[i-1])