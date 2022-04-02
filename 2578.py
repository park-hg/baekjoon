import sys
sys.stdin = open('input.txt')

grid = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
check = []
for _ in range(5):
    check += list(map(int, sys.stdin.readline().split()))

def check_bingo(grid):
    cnt = 0
    for i in range(5):
        if sum(grid[i]) == -5:
           cnt += 1 

    for i in range(5):
        col_cnt = 0
        for j in range(5):
            col_cnt += grid[j][i]
        if col_cnt == -5:
            cnt += 1

    temp = 0
    for i in range(5):
        temp += grid[i][i]
    if temp == -5:
        cnt += 1
    temp = 0
    for i in range(5):
        temp += grid[i][4-i]
    if temp == -5:
        cnt += 1

    return cnt


for idx, num in enumerate(check):
    for i in range(5):
        for j in range(5):
            if grid[i][j] == num:
                grid[i][j] = -1

    if check_bingo(grid) >= 3:
        print(idx+1)
        break


