import sys

sys.stdin = open('input.txt', 'r')
N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

robots = list([False]*N)

cnt = 0
while True:
    cnt += 1
    A = [A.pop()]+A
    robots.pop()
    robots = [False] + robots
    robots[-1] = False
    for i in range(N-2, -1, -1):
        if robots[i]:
            if not robots[i+1] and A[i+1] > 0:
                robots[i+1] = True
                robots[i] = False
                A[i+1] -= 1
    robots[-1] = False

    if A[0] > 0:
        robots[0] = True
        A[0] -= 1

    zeros = 0
    for a in A:
        if a == 0:
            zeros += 1
    if zeros >= K:
        break

print(cnt)
