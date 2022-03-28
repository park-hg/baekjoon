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

ans = 1e9
for comb in combinations(range(len(chiken)), M):
    total_dist = 0
    for i in range(len(home)):
        temp_dist = 1e9
        for j in comb:
            d = abs(home[i][0]-chiken[j][0]) + abs(home[i][1]-chiken[j][1])
            temp_dist = min(d, temp_dist)
        total_dist += temp_dist
    ans = min(ans, total_dist)

print(ans)