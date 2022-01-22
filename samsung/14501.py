import sys
sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
l = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

def check(bit):
    candidate = []
    pay = 0
    for i in range(N):
        if 1 << i & bit:
            candidate.append(i)
    app = [False]*N
    for idx in candidate:
        t, p = l[idx]
        if app[idx] or idx+t > N:
            return 0
        pay += p
        for i in range(t):
            app[i+idx] = True
    return pay

ans = 0
for bit in range(1 << (N+1)):
    ans = max(ans, check(bit))
print(ans)