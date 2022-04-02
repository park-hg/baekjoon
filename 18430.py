import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

bumerangs = [
    [[0, 0], [1, 0], [0, -1]],
    [[0, 0], [1, 0], [0, 1]],
    [[0, 0], [-1, 0], [0, -1]],
    [[0, 0], [-1, 0], [0, 1]],
]


ans = 0
def backtrack(temp, depth):
    global ans

    if depth == N*M:
        ans = max(ans, temp)
        return

    i, j = depth//M, depth%M

    if not visited[i][j]:
        for bumerang in bumerangs:
            cur = 0
            cnt = 0
            for idx, (x, y) in enumerate(bumerang):
                if 0 <= x+i < N and 0 <= y+j < M and not visited[x+i][y+j]:
                    if idx == 0:
                        cur += 2*A[x+i][y+j]
                    else:
                        cur += A[x+i][y+j]
                    cnt += 1
                else:
                    break
            if cnt == 3:
                for x, y in bumerang:
                    visited[x+i][y+j] = True
                backtrack(temp+cur, depth+1)
                for x, y in bumerang:
                    visited[x+i][y+j] = False

    backtrack(temp, depth+1)



backtrack(0,0)
print(ans)
print(aa)
print(4*4*4*4*4*4*4*4*4)