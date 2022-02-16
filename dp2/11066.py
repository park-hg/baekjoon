import sys
sys.stdin = open('input.txt', 'r')

T = int(sys.stdin.readline())
for _ in range(T):
    K = int(sys.stdin.readline())
    C = list(map(int, sys.stdin.readline().split()))
    
    s = [0]*(K+1)
    s[1] = C[0]
    for i in range(1, K):
        s[i+1] = s[i] + C[i]
    dp = [[1e9]*K for _ in range(K)]
    for i in range(K):
        dp[i][i] = 0

    for k in range(1, K):
        for i in range(K-k):
            for j in range(i, i+k):
                dp[i][i+k] = min(dp[i][i+k], dp[i][j]+dp[j+1][i+k]+s[i+k+1]-s[i])
                
    print(dp[0][-1])
