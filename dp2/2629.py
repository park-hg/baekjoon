import sys
sys.stdin = open('input.txt', 'r')
n = int(sys.stdin.readline())
w = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
v = list(map(int, sys.stdin.readline().split()))

dp = [[0]*(40001) for _ in range(n+1)]
dp[0][0] = 1

for i in range(n):
    for j in range(40001):
        if j+w[i] > 40000:
            dp[i+1][j] = dp[i][j]|dp[i][abs(j-w[i])]
        else:
            dp[i+1][j] = dp[i][j]|dp[i][j+w[i]]|dp[i][abs(j-w[i])]

for value in v:
    print('Y' if dp[-1][value] == 1 else 'N')