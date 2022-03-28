import sys
sys.setrecursionlimit(10**5)
sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
W = int(sys.stdin.readline())
events = [[-1, -1]]
for _ in range(W):
    a, b = map(int, sys.stdin.readline().split())
    events.append([a-1, b-1])


def dist(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)
    
memo = {}
def rec(i, j):
    if i == W or j == W:
        memo[(i, j)] = 0
        return 0

    if (i, j) in memo:
        return memo[(i, j)]

    next = max(i, j) + 1
    if i == 0:
        d1 = dist(0, 0, *events[next])
    else:
        d1 = dist(*events[i], *events[next])

    if j == 0:
        d2 = dist(N-1, N-1, *events[next])
    else:
        d2 = dist(*events[j], *events[next])

    memo[(i, j)] = min(d1 + rec(next, j), d2 + rec(i, next))
    return memo[(i, j)]

def path(i, j):
    if i == W or j == W:
        return

    next = max(i, j) + 1
    if i == 0:
        d1 = dist(0, 0, *events[next])
    else:
        d1 = dist(*events[i], *events[next])

    if j == 0:
        d2 = dist(N-1, N-1, *events[next])
    else:
        d2 = dist(*events[j], *events[next])

    if d1 + memo[(next, j)] < d2 + memo[(i, next)]:
        print(1)
        path(next, j)
    else:
        print(2)
        path(i, next)

rec(0, 0)
print(memo[(0, 0)])
path(0, 0)
