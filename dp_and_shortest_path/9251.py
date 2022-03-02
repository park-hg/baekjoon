import sys
sys.stdin = open('input.txt', 'r')
A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()

dp = [[0]*len(B) for _ in range(len(A))]

if A[0] == B[0]:
    dp[0][0] = 1

for i in range(len(A)-1):
    if dp[i][0] > 0:
        dp[i+1][0] = dp[i][0]
    else:
        if A[i+1] == B[0]:
            dp[i+1][0] = 1

for i in range(len(B)-1):
    if dp[0][i] > 0:
        dp[0][i+1] = dp[0][i]
    else:
        if A[0] == B[i+1]:
            dp[0][i+1] = 1

for i in range(len(A)-1):
    for j in range(len(B)-1):
        dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j], dp[i][j]+(A[i+1] == B[j+1]))

print(dp[-1][-1])