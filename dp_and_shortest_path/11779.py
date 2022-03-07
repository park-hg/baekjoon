import sys
import heapq
sys.stdin = open('input.txt', 'r')
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = {i:{} for i in range(n)}
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if b-1 in graph[a-1]:
        graph[a-1][b-1] = min(graph[a-1][b-1], c)
    else:
        graph[a-1][b-1] = c

s, e = map(int, sys.stdin.readline().split())
s, e = s-1, e-1

dist = [1e10]*n
dist[s] = 0
prev = [-1]*n
prev[s] = 0
heap = [(s, 0)]
while heap:
    v, cur_dist = heapq.heappop(heap)
    for w in graph[v]:
        if cur_dist > dist[w]:
            continue
        if cur_dist + graph[v][w] < dist[w]:
            dist[w] = cur_dist + graph[v][w]
            prev[w] = v
            heapq.heappush(heap, (w, dist[w]))

path = [e+1]
cur = e
while cur != s:
    cur = prev[cur]
    path.append(cur+1)

print(dist[e])
print(len(path))
print(*path[::-1])
