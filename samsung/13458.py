import sys
sys.stdin = open('input.txt', 'r')
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())

ans = 0
for a in A:
    ans += 1
    left = max(a-B, 0)
    if left > 0:
        if left%C != 0:
            ans += left//C + 1
        else:
            ans += left//C

print(ans)