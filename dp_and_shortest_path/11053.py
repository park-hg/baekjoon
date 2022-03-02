import sys
sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp = [0]*N
dp[0] = 1
for i in range(N-1):
    m = 0
    for j in range(i+1):
        if A[i+1] > A[j]:
            m = max(dp[j], m)
    dp[i+1] = m+1

print(max(dp))