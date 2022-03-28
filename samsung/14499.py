import sys
sys.stdin = open('input.txt', 'r')
N, M, x, y, K = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
moves = list(map(int, sys.stdin.readline().split()))
moves = [i-1 for i in moves]

dice = {
    'U':0,
    'D':0,
    'L':0,
    'R':0,
    'F':0,
    'B':0,
}

def roll_dice(dice, d):
    if d == 0:
        new_dice = {
            'U':dice['L'],
            'D':dice['R'],
            'L':dice['D'],
            'R':dice['U'],
            'F':dice['F'],
            'B':dice['B'],
        }
    elif d == 1:
        new_dice = {
            'U':dice['R'],
            'D':dice['L'],
            'L':dice['U'],
            'R':dice['D'],
            'F':dice['F'],
            'B':dice['B'],
        }
    elif d == 2:
        new_dice = {
            'U':dice['B'],
            'D':dice['F'],
            'L':dice['L'],
            'R':dice['R'],
            'F':dice['U'],
            'B':dice['D'],
        }
    elif d == 3:
        new_dice = {
            'U':dice['F'],
            'D':dice['B'],
            'L':dice['L'],
            'R':dice['R'],
            'F':dice['D'],
            'B':dice['U'],
        }

    return new_dice

def move_dice(x, y, moves, dice):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    for i in moves:
        nx, ny = x+dx[i], y+dy[i]
        new_dice = roll_dice(dice, i)
        if 0 <= nx < N and 0 <= ny < M:
            if grid[nx][ny] == 0:
                grid[nx][ny] = new_dice['D']
            else:
                new_dice['D'] = grid[nx][ny]
                grid[nx][ny] = 0
            print(new_dice['U'])

            x, y = nx, ny
            dice = new_dice

move_dice(x, y, moves, dice)