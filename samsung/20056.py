import sys
sys.stdin = open('input.txt')

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
N, M, K = map(int, sys.stdin.readline().split())

info = {}
for _ in range(M):
    r, c, m, s, d = map(int, sys.stdin.readline().split())
    info[(r, c)] = [(m, s, d)]

def move(info):
    new_info = {}
    for r, c in info:
        for m, s, d in info[(r, c)]:
            nr, nc = (r+s*dx[d])%N, (c+s*dy[d])%N
            if (nr, nc) not in new_info:
                new_info[(nr, nc)] = [(m, s, d)]
            else:
                new_info[(nr, nc)].append((m, s, d))

    return new_info

def merge(info):
    new_info = {}
    for r, c in info:
        if len(info[(r, c)]) > 1:
            total_m = 0
            total_s = 0
            total_d = 0
            for m, s, d in info[(r, c)]:
                total_m += m
                total_s += s
                total_d += d%2

            total_m //= 5
            total_s //= len(info[(r, c)])
            if total_m > 0:
                if total_d == 0 or total_d == len(info[(r, c)]):
                    new_info[(r, c)] = [(total_m, total_s, 0), (total_m, total_s, 2), (total_m, total_s, 4), (total_m, total_s, 6),]
                else:
                    new_info[(r, c)] = [(total_m, total_s, 1), (total_m, total_s, 3), (total_m, total_s, 5), (total_m, total_s, 7),]
        else:
            new_info[(r, c)] = info[(r, c)][:]

    return new_info

for _ in range(K):
    info = move(info)
    info = merge(info)

ans = 0
for r, c in info:
    for m, _, _ in info[(r, c)]:
        ans += m

print(ans)
