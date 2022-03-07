import sys
sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
d = [[1e5+1]*n for _ in range(n)]
p = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if c < d[a-1][b-1]:
        d[a-1][b-1] = c
        p[a-1][b-1] = [a, b]

for i in range(n):
    d[i][i] = 0
    p[i][i] = [i]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if d[i][k]+d[k][j] < d[i][j]:
                d[i][j] = d[i][k]+d[k][j]
                p[i][j] = p[i][k][:-1] + p[k][j]
            
for d_list in d:
    lst = []
    for v in d_list:
        if v != 1e5+1:
            lst.append(v)
        else:
            lst.append(0)
    print(*lst)

for i in range(n):
    for j in range(n):
        if d[i][j] == 0 or d[i][j] == 1e5+1:
            print(0)
        else:
            print(len(p[i][j]), *p[i][j])
