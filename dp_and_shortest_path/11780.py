import sys
sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
d = [[1e5+1]*n for _ in range(n)]
p = [[-1]*n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if d[a-1][b-1] > c:
        d[a-1][b-1] = c
        p[a-1][b-1] = a-1
for i in range(n):
    d[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if d[i][k]+d[k][j] < d[i][j]:
                d[i][j] = d[i][k]+d[k][j]
                p[i][j] = p[k][j]

for i in range(n):
    for j in range(n):
        if d[i][j] == 1e5+1:
            d[i][j] = 0

for d_list in d:
    print(*d_list)

for i in range(n):
    for j in range(n):
        if d[i][j] == 0 or d[i][j] == 1e5+1:
            print(0)
        else:
            cur = j
            path = [cur+1]
            while cur != i:
                cur = p[i][cur]
                path.append(cur+1)
            print(len(path), *path[::-1])