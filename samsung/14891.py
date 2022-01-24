import sys
from copy import deepcopy
sys.stdin = open('input.txt', 'r')

gears = [list(sys.stdin.readline().rstrip()) for _ in range(4)]
K = int(sys.stdin.readline())

def turn_gear(gear, d):
    if d == -1:
        new_gear = gear[1:] + [gear[0]]
    elif d == 1:
        new_gear = [gear[-1]] + gear[:-1]
    return new_gear

def turn(gears, idx, d):
    new_gears = deepcopy(gears)
    turned = [False]*4
    target = gears[idx]
    new_target = turn_gear(target, d)
    new_gears[idx] = new_target
    turned[idx] = True

    if idx == 0:
        # 1
        if target[2] != gears[1][-2]:
            new_gears[1] = turn_gear(gears[1], -d)
            turned[1] = True
        # 2
        if turned[1]:
            if gears[1][2] != gears[2][-2]:
                new_gears[2] = turn_gear(gears[2], d)
                turned[2] = True
        # 3
        if turned[2]:
            if gears[2][2] != gears[3][-2]:
                new_gears[3] = turn_gear(gears[3], -d)
                turned[3] = True

    elif idx == 1:
        # 0, 2
        if target[-2] != gears[0][2]:
            new_gears[0] = turn_gear(gears[0], -d)
            turned[0] = True
        if target[2] != gears[2][-2]:
            new_gears[2] = turn_gear(gears[2], -d)
            turned[2] = True
        # 3
        if turned[2]:
            if gears[2][2] != gears[3][-2]:
                new_gears[3] = turn_gear(gears[3], d)
                turned[3] = True

    elif idx == 2:
        # 1, 3
        if target[-2] != gears[1][2]:
            new_gears[1] = turn_gear(gears[1], -d)
            turned[1] = True
        if target[2] != gears[3][-2]:
            new_gears[3] = turn_gear(gears[3], -d)
            turned[3] = True
        # 0
        if turned[1]:
            if gears[0][2] != gears[1][-2]:
                new_gears[0] = turn_gear(gears[0], d)
                turned[0] = True

    elif idx == 3:
        # 2
        if target[-2] != gears[2][2]:
            new_gears[2] = turn_gear(gears[2], -d)
            turned[2] = True
        # 1
        if turned[2]:
            if gears[1][2] != gears[2][-2]:
                new_gears[1] = turn_gear(gears[1], d)
                turned[1] = True
        # 0
        if turned[1]:
            if gears[0][2] != gears[1][-2]:
                new_gears[0] = turn_gear(gears[0], -d)
                turned[0] = True

    return new_gears
for _ in range(K):
    idx, d = map(int, sys.stdin.readline().split())
    gears = turn(gears, idx-1, d)

score = 0
for i, gear in enumerate(gears):
    if gear[0] == '1':
        score += 2**i

print(score)