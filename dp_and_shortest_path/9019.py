import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

def bfs(a, b):
    visited = [-1]*10000
    que = deque([a])
    visited[a] = 0
    while que:
        n = que.popleft()
        if n == b:
            break
        d = (n*2)%10000
        if visited[d] == -1:
            que.append(d)
            visited[d] = (n, 'D')
        s = (n-1)%10000
        if visited[s] == -1:
            que.append(s)
            visited[s] = (n, 'S')
        temp = str(n).zfill(4)
        l = int(temp[1:]+temp[0])
        if visited[l] == -1:
            que.append(l)
            visited[l] = (n, 'L')
        r = int(temp[-1]+temp[:-1])
        if visited[r] == -1:
            que.append(r)
            visited[r] = (n, 'R')
    
    path = []
    cur = b
    while cur != a:
        cur, op = visited[cur]
        path.append(op)
    
    return path[::-1]
    

T = int(sys.stdin.readline())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    path = bfs(A, B)
    print(''.join(path))