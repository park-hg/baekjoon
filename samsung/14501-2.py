import sys
sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
l = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]


memo = {}
# i~N 까지 일했을 때 최대이득
def solve(i):
    if i == N:
        return 0
    if i >= N:
        return -1e12
    if i in memo:
        return memo[i]

    memo[i] = max(solve(i+1), solve(i+l[i][0]) + l[i][1])
    return memo[i]

print(solve(0))
