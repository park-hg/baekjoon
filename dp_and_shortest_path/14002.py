import sys
sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp = [0]*N
dp[0] = [A[0]]
for i in range(N-1):
    m = []
    for j in range(i+1):
        if A[i+1] > A[j]:
            if len(dp[j]) > len(m):
                m = dp[j]
    dp[i+1] = m + [A[i+1]]

ans = []
for i in range(N):
    if len(dp[i]) > len(ans):
        ans = dp[i]
print(len(ans))
print(*ans)