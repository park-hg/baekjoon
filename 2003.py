import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

l, r = 0, 0
s = 0
ans = 0

while r <= N:
    if s >= M:
        if s == M:
            ans += 1
        s -= A[l]
        l += 1
    else:
        if r == N:
            break
        s += A[r]
        r += 1

print(ans)