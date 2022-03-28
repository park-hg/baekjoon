import sys
sys.stdin = open('input.txt', 'r')
m = int(sys.stdin.readline())
f = list(map(int, sys.stdin.readline().split()))
Q = int(sys.stdin.readline())
next = [[0]*19 for _ in range(m+1)]
for i in range(m):
    next[i+1][0] = f[i]
for j in range(19-1):
    for i in range(m+1):
        next[i][j+1] = next[next[i][j]][j]

for _ in range(Q):
    n, x = map(int, sys.stdin.readline().split())
    for i in range(19):
        if n & 1<<i:
            n -= 1<<i
            x = next[x][i]
    print(x)

