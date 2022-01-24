import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

gears = [deque(map(int, input().rstrip())) for _ in range(4)]
left = -2
right = 2

def start(idx, d):
    if idx-1 >= 0:
        move(-1, idx-1, (gears[idx][left]^gears[idx-1][right])*-d)
    if idx+1 <= 3:
        move(1, idx+1, (gears[idx][right]^gears[idx+1][left])*-d)

    gears[idx].rotate(d)

def move(pos_d, idx, d):
    this = gears[idx][right if pos_d==1 else left]
    compare = left if pos_d==1 else right
    gears[idx].rotate(d)
    if 0 <= idx+pos_d <= 3:
        move(pos_d, idx+pos_d, (this^gears[idx+pos_d][compare])*-d)

K = int(input())
for _ in range(K):
    idx, d = map(int, input().split())
    start(idx-1, d)

score = 0
for i, gear in enumerate(gears):
    if gear[0] == 1:
        score += 2**i

print(score)