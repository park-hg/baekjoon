import sys
import heapq
sys.stdin = open('input.txt', 'r')
N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1

heap = []
for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

discovered = []
while heap:
    v = heapq.heappop(heap)
    discovered.append(v)
    for w in graph[v]:
        indegree[w] -= 1
        if indegree[w] == 0:
            heapq.heappush(heap, w)

print(*discovered)