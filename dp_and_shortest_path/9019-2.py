import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

def bfs(a, b):
    visited = [False]*10000
    que = deque([(a, '')])
    visited[a] = True
    while que:
        n, path = que.popleft()
        if n == b:
            return path
        d = (n*2)%10000
        if not visited[d]:
            que.append((d, path+'D'))
            visited[d] = True
        s = (n-1)%10000
        if not visited[s]:
            que.append((s, path+'S'))
            visited[s] = True
        temp = str(n).zfill(4)
        l = int(temp[1:]+temp[0])
        if not visited[l]:
            que.append((l, path+'L'))
            visited[l] = True
        r = int(temp[-1]+temp[:-1])
        if not visited[r]:
            que.append((r, path+'R'))
            visited[r] = True

T = int(sys.stdin.readline())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    path = bfs(A, B)
    print(path)