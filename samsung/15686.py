import sys
from itertools import combinations
sys.stdin = open('input.txt', 'r')
N, M = map(int, sys.stdin.readline().split())
city = []
for _ in range(N):
    city.append(list(map(int, sys.stdin.readline().split())))

home = []
chiken = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append([i, j])
        elif city[i][j] == 2:
            chiken.append([i, j])

M = min(M, len(chiken))
dist = [[-1]*len(chiken) for _ in range(len(home))]

for i in range(len(home)):
    for j in range(len(chiken)):
        dist[i][j] = abs(home[i][0]-chiken[j][0]) + abs(home[i][1]-chiken[j][1])

def dist_sum(num):
    d = 1e9
    for comb in combinations(range(len(chiken)), num):
        sum_d = [1e9]*len(home)
        for j in comb:
            for i in range(len(home)):
                sum_d[i] = min(sum_d[i], dist[i][j])
        d = min(d, sum(sum_d))
    
    return d

ans = 1e9
for num in range(1, M+1):
    ans = min(ans, dist_sum(num))

print(ans)