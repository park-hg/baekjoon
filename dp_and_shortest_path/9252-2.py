import sys
sys.stdin = open('input.txt', 'r')
A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()

dp = [['']*len(B) for _ in range(len(A))]

if A[0] == B[0]:
    dp[0][0] = A[0]

for i in range(len(A)-1):
    if len(dp[i][0]) > 0:
        dp[i+1][0] = dp[i][0]
    else:
        if A[i+1] == B[0]:
            dp[i+1][0] = B[0]

for i in range(len(B)-1):
    if len(dp[0][i]) > 0:
        dp[0][i+1] = dp[0][i]
    else:
        if B[i+1] == A[0]:
            dp[0][i+1] = A[0]

for i in range(len(A)-1):
    for j in range(len(B)-1):
        m = max(len(dp[i][j+1]), len(dp[i+1][j]), len(dp[i][j])+(A[i+1] == B[j+1]))
        if m == len(dp[i][j+1]):
            dp[i+1][j+1] = dp[i][j+1]
        elif m == len(dp[i+1][j]):
            dp[i+1][j+1] = dp[i+1][j]
        else:
            if A[i+1] == B[j+1]:
                dp[i+1][j+1] = dp[i][j] + A[i+1]
            else:
                dp[i+1][j+1] = dp[i][j]

print(len(dp[-1][-1]))
if len(dp[-1][-1]) > 0:
    print(dp[-1][-1])
